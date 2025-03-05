---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Welcome to my academic homepage. I am Yunlong Lin, a Master student at Xiamen University (XMU) @[SmartDSP](https://xmu-smartdsp.github.io/) advised by [Prof. Xinghao Ding](https://scholar.google.com.hk/citations?user=k5hVBfMAAAAJ&hl=zh-CN). My primary research interests include computational photography, multimodal learning for understanding, reasoning and skill learning.

- <span style="color: #FFB6C1">**Multimodal learning**</span>: Vision and language, Visual reasoning, Generalist models
- <span style="color: #008B8B">**Inverse Problems**</span>: Real-world degradation restoration, Generative priors  
- <span style="color: #87CEEB">**AI Agents**</span>: Planning and Decision-Making, Reinforcement learning


# 🔥 News
- Three papers accepted by CVPR'25!
- Four papers accepted by AAAI'25 (2 oral)!
- One paper accepted by ECCV'24!
- Two paper accepted by TGRS'25!
- Two paper accepted by TCSVT'24!
- Two paper accepted by TGRS'24!
- Three papers accepted by ACMMM'23 (1 oral)!

# 📝 Publications
<!-- <p style='text-align: justify;'> My current research focuses on three main areas: <strong>(I)</strong> Addressing the challenges of real-world image restoration and enhancement by identifying and overcoming the limitations of existing learning-based methods. <strong>(II)</strong> Exploring vision problems related to photography, with the goal of producing images of superior visual quality. <strong>(III)</strong> Providing support for the art creation industry and digital asset generation through advancements in AIGC (Artificial Intelligence Generated Content) technology.
</p> -->

<!-- ------------------------------------ -->

<!-- Paper 1 -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2025</div><img src='images/papers/jarvisir.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**JarvisIR: Elevating Autonomous Driving Perception with Intelligent Image Restoration**]()

**Yunlong Lin\***, ZiXu Lin\*, Haoyu Chen\*, Panwang Pan\*, Chenxin Li, Sixiang Chen, Kairun Wen, YEYING JIN, Wenbo Li, Xinghao Ding

[PDF]() | [Project]()
</div>
</div>

<!-- Paper 1 -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2025</div><img src='images/papers/aglldiff.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**AGLLDiff: Guiding Diffusion Models Towards Unsupervised Training-free Real-world Low-light Image Enhancement**](https://arxiv.org/pdf/2407.14900)

**Yunlong Lin\***, Tian Ye\*, Sixiang Chen\*, Zhenqi Fu, Yingying Wang, Wenhao Chai, Zhaohu Xing, Lei Zhu, Xinghao Ding

[PDF](https://arxiv.org/pdf/2407.14900) | [Project](https://aglldiff.github.io)
</div>
</div>

<!-- ------------------------------------ -->
<!-- Paper 2 -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2025</div><img src='images/papers/dplut.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**Unsupervised Low-light Image Enhancement with Lookup Tables and Diffusion Priors**](https://arxiv.org/pdf/2409.18899)

**Yunlong Lin\***, Zhenqi Fu\*, Kairun Wen, Tian Ye, Sixiang Chen, Ge Meng, Yingying Wang, Yue Huang, Xiaotong Tu, Xinghao Ding

[PDF](https://arxiv.org/pdf/2409.18899) | [Project](https://dplut.github.io/)
</div>
</div>


<!-- # 📝 Other Publications  -->
<ul>
  <!-- Paper 1 -->
  <li>
    <strong>Sp3ctralMamba: Physics-Driven Joint State Space Model for Hyperspectral Image Reconstruction. AAAI 2025 Oral.</strong>
    <div style="display: inline">
        <a href=""> [paper]</a>
        <a href=""> [code]</a>
    </div>
    <div><i>Ge Meng, Jingyan Tu, Jingjia Huang, <strong>Yunlong Lin</strong>, Yingying Wang, Xiaotong Tu, Yue Huang, Xinghao Ding</i></div>
  </li>

  <!-- ------------------------------------ -->

  <!-- Paper 1 -->
  <li>
    <strong>Accelerated Diffusion via High-Low Frequency Decomposition for Pan-sharpening. AAAI 2025 Oral.</strong>
    <div style="display: inline">
        <a href=""> [paper]</a>
        <a href=""> [code]</a>
    </div>
    <div><i>Ge Meng, Jingjia Huang, Jingyan Tu, Yingying Wang, <strong>Yunlong Lin</strong>, Xiaotong Tu, Yue Huang, Xinghao Ding</i></div>
  </li>

  <!-- ------------------------------------ -->


  <!-- Paper 1 -->
  <li>
    <strong>Teaching Tailored to Talent: Adverse Weather Restoration via Prompt Pool and Depth-Anything Constraint. ECCV 2024.</strong>
    <div style="display: inline">
        <a href=""> [paper]</a>
        <a href=""> [code]</a>
    </div>
    <div><i>Sixiang Chen, Tian Ye, Kai Zhang, Zhaohu Xing, <strong>Yunlong Lin</strong>, Lei Zhu</i></div>
  </li>

  <!-- ------------------------------------ -->
  <!-- Paper 2 -->
  <li>
    <strong>Fusion2Void: Unsupervised Multi-focus Image Fusion Based on Image Inpainting. TCSVT 2024.</strong>
    <div style="display: inline">
        <a href=""> [paper]</a>
        <a href=""> [code]</a>
    </div>
    <div><i>Huangxing Lin, <strong>Yunlong Lin</strong>, Jingyuan Xia, Linyu Fan, Feifei Li, Yingying Wang, Xinghao Ding</i></div>
  </li>

  <!-- ------------------------------------ -->
  <!-- Paper 3 -->
  <li>
    <strong>Frequency decoupled domain-irrelevant feature learning for Pan-sharpening. TCSVT 2024.</strong>
    <div style="display: inline">
        <a href="https://ieeexplore.ieee.org/abstract/document/10718360"> [paper]</a>
        <a href=""> [code]</a>
    </div>
    <div><i>Jie Zhang, Ke Cao, Keyu Yan, <strong>Yunlong Lin</strong>, Xuanhua He, Yingying Wang, Rui Li, Chengjun Xie, Jun Zhang, Man Zhou</i></div>
  </li>

  <!-- ------------------------------------ -->
  <!-- Paper 4 -->
  <li>
    <strong>Cross-Modality Interaction Network for Pan-sharpening. TGRS 2024.</strong>
    <div style="display: inline">
        <a href=""> [paper]</a>
        <a href=""> [code]</a>
    </div>
    <div><i>Yingying Wang, Xuanhua He, Yuhang Dong, <strong>Yunlong Lin</strong>, Yue Huang, Xinghao Ding</i></div>
  </li>

  <!-- ------------------------------------ -->
  <!-- Paper 5 -->
  <li>
    <strong>Domain-irrelevant Feature Learning for Generalizable Pan-sharpening. ACMMM 2023.</strong>
    <div style="display: inline">
        <a href=""> [paper]</a>
        <a href=""> [code]</a>
    </div>
    <div><i><strong>Yunlong Lin</strong>, Zhenqi Fu, Ge Meng, Yingying Wang, Yuhang Dong, Linyu Fan, Hedeng Yu, Xinghao Ding</i></div>
  </li>

  <!-- ------------------------------------ -->
  <!-- Paper 6 -->
  <li>
    <strong>Learning High-frequency Feature Enhancement and Alignment for Pan-sharpening. ACMMM 2023 Oral.</strong>
    <div style="display: inline">
        <a href=""> [paper]</a>
        <a href=""> [code]</a>
    </div>
    <div><i>Yingying Wang, <strong>Yunlong Lin</strong>, Ge Meng, Zhenqi Fu, Yuhang Dong, Linyu Fan, Hedeng Yu, Xinghao Ding, Yue Huang</i></div>
  </li>

  <!-- ------------------------------------ -->
  <!-- Paper 7 -->
  <li>
    <strong>CPLFormer: Cross-scale Prototype Learning Transformer for Image Snow Removal. ACMMM 2023.</strong>
    <div style="display: inline">
        <a href=""> [paper]</a>
        <a href=""> [code]</a>
    </div>
    <div><i>Sixiang Chen, Tian Ye, Yun Liu, Jinbin Bai, Haoyu Chen, <strong>Yunlong Lin</strong>, Jun Shi, Erkang Chen</i></div>
  </li>
</ul>


# 🎖 Honors and Awards
- National Scholarship in Xiamen University, 2024
- Outstanding Graduate in Jimei University, 2023
- Second Price of Mathematical Contest In Modeling, 2021
- First Price of Mathorcup Mathematical Contest in Modeling, 2021
- First Price of Mathorcup Mathematical Contest in Modeling, 2022

# 📖 Educations
- Sep'2023-Jul'2026: Master Student, Xiamen University
- Sep'2019-Jul'2023: B.Eng (Telecommunication Engineering), Jimei University, Xiamen

# 💬 Academic Service
- Conference Reviewer: ACMMM‘24/25, NeurIPS’24/25, ICLR‘25, CVPR’25, ICCV‘25, ICML 2025.



<script type="text/javascript" id="clustrmaps" src="//clustrmaps.com/map_v2.js?d=jacK9ggqHSefN4z3yvCMPbr34roVzQhT1qc6eb2yeTA&cl=ffffff&w=a"></script>