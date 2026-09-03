from datetime import datetime
import json
import os
from pathlib import Path
import tempfile
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup
import httpx
from scholarly import scholarly


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID", "CxKy4lEAAAAJ")
PROFILE_URL = "https://scholar.google.com.hk/citations"


def parse_count(value: str) -> int:
    digits = "".join(character for character in value if character.isdigit())
    return int(digits) if digits else 0


def fetch_public_profile() -> dict:
    response = httpx.get(
        PROFILE_URL,
        params={"user": SCHOLAR_ID, "hl": "en", "pagesize": 100},
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 Chrome/131.0 Safari/537.36"
            )
        },
        follow_redirects=True,
        timeout=30,
    )
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    name_element = soup.select_one("#gsc_prf_in")
    metric_rows = soup.select("#gsc_rsb_st tr")
    if name_element is None or len(metric_rows) < 2:
        raise ValueError("Google Scholar public profile was blocked or incomplete")

    metrics = [
        element.get_text(" ", strip=True)
        for element in metric_rows[1].select(".gsc_rsb_std")
    ]
    if not metrics:
        raise ValueError("Google Scholar returned no citation metrics")

    publications = {}
    for row in soup.select(".gsc_a_tr"):
        title_element = row.select_one(".gsc_a_at")
        if title_element is None:
            continue
        query = parse_qs(urlparse(title_element.get("href", "")).query)
        publication_id = query.get("citation_for_view", [""])[0]
        if not publication_id:
            continue

        description = row.select(".gs_gray")
        citation_element = row.select_one(".gsc_a_c a")
        year_element = row.select_one(".gsc_a_y")
        publication = {
            "author_pub_id": publication_id,
            "bib": {
                "title": title_element.get_text(" ", strip=True),
                "author": description[0].get_text(" ", strip=True)
                if description
                else "",
                "citation": description[1].get_text(" ", strip=True)
                if len(description) > 1
                else "",
                "pub_year": year_element.get_text(" ", strip=True)
                if year_element
                else "",
            },
            "num_citations": parse_count(
                citation_element.get_text(" ", strip=True)
                if citation_element
                else ""
            ),
        }
        publications[publication_id] = publication

    return {
        "scholar_id": SCHOLAR_ID,
        "name": name_element.get_text(" ", strip=True),
        "citedby": parse_count(metrics[0]),
        "publications": publications,
    }


def fetch_with_scholarly() -> dict:
    author = scholarly.search_author_id(SCHOLAR_ID)
    scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
    author = json.loads(json.dumps(author, ensure_ascii=False))
    author["citedby"] = sum(
        publication.get("num_citations", 0)
        for publication in author["publications"]
    )
    author["publications"] = {
        publication["author_pub_id"]: publication
        for publication in author["publications"]
    }
    return author


def validate_author(author: dict) -> None:
    publications = author.get("publications")
    citedby = author.get("citedby")
    if not isinstance(publications, dict) or not publications:
        raise ValueError("Google Scholar returned no publications")
    if type(citedby) is not int or citedby < 0:
        raise ValueError("Invalid total citation count")

    publication_total = sum(
        publication.get("num_citations", 0) for publication in publications.values()
    )
    if citedby < publication_total:
        raise ValueError(
            "Total citation count is lower than the sum of publication citations"
        )

    for publication_id, publication in publications.items():
        citation_count = publication.get("num_citations", 0)
        if not publication_id or type(citation_count) is not int or citation_count < 0:
            raise ValueError(f"Invalid publication record: {publication_id}")


def without_timestamp(data: dict) -> dict:
    comparable = dict(data)
    comparable.pop("updated", None)
    return comparable


def write_json_atomically(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=path.parent,
        prefix=f".{path.name}.",
        delete=False,
    )
    temporary_path = Path(handle.name)
    try:
        with handle:
            json.dump(data, handle, ensure_ascii=False)
        os.replace(temporary_path, path)
    finally:
        temporary_path.unlink(missing_ok=True)


try:
    author = fetch_public_profile()
    validate_author(author)
    print("Fetched citation data from the public Google Scholar profile.")
except Exception as public_profile_error:
    print(f"Public profile fetch failed: {public_profile_error}")
    author = fetch_with_scholarly()
    print("Fetched citation data with scholarly.")

validate_author(author)
author["updated"] = datetime.now().astimezone().isoformat()

stats_path = RESULTS / "gs_data.json"
previous = None
if stats_path.exists():
    try:
        previous = json.loads(stats_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("Existing Scholar data is invalid; replacing it.")

if previous is not None and without_timestamp(previous) == without_timestamp(author):
    print(f"No Google Scholar data changes for {SCHOLAR_ID}.")
else:
    write_json_atomically(stats_path, author)
    print(json.dumps(author, ensure_ascii=False))

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": str(author["citedby"]),
}
write_json_atomically(RESULTS / "gs_data_shieldsio.json", shieldio_data)
