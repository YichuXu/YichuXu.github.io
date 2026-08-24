# Yichu Xu (徐一楚)

This repository contains the source code for my academic homepage: [yichuxu.github.io](https://yichuxu.github.io/).

The website is built with Jekyll and uses the visual system and data-driven components from [zzaiyan/zzaiyan.github.io](https://github.com/zzaiyan/zzaiyan.github.io), adapted with my own profile, research, news, publications, honors, collaborators, and academic service.

## Features

- Data-driven publication, news, and honors sections under `_data/`
- English/Chinese language switcher
- Light/dark theme switcher
- Responsive publication cards
- Multi-format citation display and download
- Google Scholar citation badge and statistics

## Content management

- Personal and social information: `_config.yml`
- Homepage introduction, collaboration, and service: `_pages/about.md`
- Publications: `_data/pubs.json` and `_data/references.json`
- News: `_data/news.json`
- Honors: `_data/honors.json`
- Navigation: `_data/navigation.yml`

After editing publication references, regenerate citation output with:

```bash
npm ci
npm run citations:build
```

## Local preview

Install the Ruby dependencies, then run:

```bash
bundle install
bundle exec jekyll serve
```

The site is available locally at `http://127.0.0.1:4000`.

## Acknowledgements

The site is based on [zzaiyan/zzaiyan.github.io](https://github.com/zzaiyan/zzaiyan.github.io), AcadHomepage, Minimal Mistakes, and Academic Pages. See [LICENSE](LICENSE) for licensing information.
