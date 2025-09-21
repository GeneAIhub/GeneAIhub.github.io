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



We are PhD student in Mechanical Engineering at Universiti Malaya and publish 5+ papers with 
<a href='https://scholar.google.com/citations?user=DmN2rEYAAAAJ'>
<img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FGeneAIhub%2FGeneAIhub.github.io%2Fgoogle-scholar-stats%2Fgs_data_shieldsio.json&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations">
</a>, under supervision of <highlight> <a href="https://umexpert.um.edu.my/alexongzc" target="_blank">Associate Professor Ong Zhi Chao</a></highlight>,<highlight> <a href="https://umexpert.um.edu.my/khooshinyee" target="_blank">Dr. Khoo Shin Yee</a></highlight>, and <highlight> <a href="https://umexpert.um.edu.my/siowpeiyi" target="_blank">Dr. Siow Pei Yi</a></highlight>.
We are member of the <highlight> <a href="https://umengshm.com/asvr/" target="_blank">Advanced Shock and Vibration Research (ASVR) Group</a></highlight>, based in the <a href="https://engine.um.edu.my/department-of-mechanical-engineering" target="_blank">Department of Mechanical Engineering, Faculty of Engineering, Universiti Malaya</a>. 

My research interest includes: 
- Nonlinear time series analysis
- Entropy feature extraction
- Generative model for data augmentation
- Data imbalance, data scarcity, lack of labeled samples
- Few-shot learning


[//]: # (# 💻 Work Experiences)

[//]: # (- *2024.09 - Now*&ensp;Postdoctoral researcher in School of Information Science and Technology, University of Science and Technology of China, Hefei, China.)


# 🎓 Educations 
- *2023.03 - Expected 2026*&ensp;Ph.D. in Mechanical Engineering at Universiti Malaya, Kuala Lumpur, Malaysia. <a href="https://engine.um.edu.my/about-mechanical-engineering"><img class="svg" src="/images/UM.png" width="16pt"></a> 
- *2019.09 - 2022.06*&ensp;M.Sc. in School of Mechanical Science and Engineering of Northeast Petroleum university, Daqing, China. <a href="https://jxkxygcxy.nepu.edu.cn/"><img class="svg" src="/images/NEPU.png" width="16pt"></a> 

[//]: # (- *2012.09 - 2016.06*&ensp;B.Sc. in School of Electrical Engineering and Automation, Hefei University of Technology, Hefei, China. <a href="https://en.hfut.edu.cn/"><img class="svg" src="/images/hfut.png" width="16pt"></a> )


# 📝 Publications 

<h3 align="center">2025</h3>
<div style="border-bottom: 1px solid #000; margin: 0px 0;"></div>

<div class='paper-box'>
    <div class='paper-box-image' style="text-align:center;">
        <img src='images/MDSEN.png' alt="sym" style="max-width:80%; height:auto; margin:auto; vertical-align:middle">
    </div>
    <div class='paper-box-text'>
        <a href="https://www.sciencedirect.com/science/article/pii/S0952197625023164">
            <papertitle> Multi-scale distance similarity entropy: A novel complexity measurement for gearbox fault diagnosis </papertitle>
        </a>
        <br>
        <strong>Tao Wang</strong>, Shin Yee Khoo, Zhi Chao Ong, Pei Yi Siow, <strong>Teng Wang</strong>.
        <br>
        <em>  Engineering Applications of Artificial Intelligence</em>, 2025 (TOP) <a href="https://github.com/GeneAIhub/GeneAIhub">[code]</a>
        <p></p>
        <p>We propose a novel method called Multi-scale Distance Similarity Entropy (MDSE), 
            which integrates distance similarity entropy with a multi-scale coarse-graining process to capture nonlinear variations in gearbox vibration signals while effectively suppressing noise. 
            We validate its effectiveness on two gearbox datasets, where it achieves over 97% diagnostic accuracy and shows strong robustness and efficiency for real-time fault detection in complex industrial environments.
        </p>
</div>
</div>

<h3 align="center">2025</h3>
<div style="border-bottom: 1px solid #000; margin: 0px 0;"></div>

<div class='paper-box'>
    <div class='paper-box-image' style="text-align:center;">
        <img src='images/DSEN.png' alt="sym" style="max-width:80%; height:auto; margin:auto; vertical-align:middle">
    </div>
    <div class='paper-box-text'>
        <a href="https://www.sciencedirect.com/science/article/pii/S0951832024007142">
            <papertitle> Distance similarity entropy: A sensitive nonlinear feature extraction method for rolling bearing fault diagnosis </papertitle>
        </a>
        <br>
        <strong>Tao Wang</strong>, Shin Yee Khoo, Zhi Chao Ong, Pei Yi Siow, <strong>Teng Wang</strong>.
        <br>
        <em>  Reliability Engineering & System Safety</em>, 2025 (TOP) <a href="https://github.com/GeneAIhub/GeneAIhub">[code]</a>
        <p></p>
        <p>We propose an entropy-based method, DSEN, for bearing fault diagnosis. It captures subtle local variations through element-wise distance and Gaussian similarity,
          and estimates similarity distributions to achieve accurate complexity measurement, thereby enhancing diagnostic accuracy and reliability.
        </p>
</div>
</div>


<h3 align="center">2025</h3>
<div style="border-bottom: 1px solid #000; margin: 0px 0;"></div>

<div class='paper-box'>
    <div class='paper-box-image' style="text-align:center;">
        <img src='images/EnSeqInfo.jpg' alt="sym" style="max-width:80%; height:auto; margin:auto; vertical-align:middle">
    </div>
    <div class='paper-box-text'>
        <a href="https://www.sciencedirect.com/science/article/pii/S0952197625007602">
            <papertitle> An enhanced generative adversarial network for longer vibration time data generation under variable operating conditions for imbalanced bearing fault diagnosis </papertitle>
        </a>
        <br>
        <strong>Teng Wang</strong>, Zhi Chao Ong, Shin Yee Khoo, Pei Yi Siow, <strong>Tao Wang</strong>.
        <br>
        <em> Engineering Applications of Artificial Intelligence</em>, 2025 (TOP) <a href="https://github.com/GeneAIhub/GeneAIhub">[code]</a>
        <p></p>
        <p>We propose an enhanced generative adversarial network for generating longer vibration time data to improve imbalanced bearing fault diagnosis under variable operating conditions.</p>
    </div>
</div>


<div class='paper-box'>
    <div class='paper-box-image' style="text-align:center;">
        <img src='images/SeqInfo.jpg' alt="sym" style="max-width:80%; height:auto; margin:auto; vertical-align:middle">
    </div>
    <div class='paper-box-text'>
        <a href="https://www.sciencedirect.com/science/article/pii/S0263224124022292#f0005">
            <papertitle> SeqInfo-SAWGAN-GP: Adaptive feature extraction from vibration time data under variable operating conditions for imbalanced bearing fault diagnosis </papertitle>
        </a>
        <br>
        <strong>Teng Wang</strong>, Zhi Chao Ong, Shin Yee Khoo, Pei Yi Siow <strong>Tao Wang</strong>.
        <br>
        <em> Measurement</em>, 2025 <a href="https://github.com/GeneAIhub/GeneAIhub">[code]</a>
        <p></p>
        <p>We propose SeqInfo-SAWGAN-GP, a generative model conditioned on sequence information, to enhance the diversity of synthetic time-series data under varying operating conditions and address the scarcity of fault data.</p>
    </div>
</div>

# 🏅 Honors and Awards
- *2025.03*&ensp;Awarded Top 10% SCI Journal Publication Incentive, Faculty of Engineering
- *2024.12*&ensp;Awarded Top 10% SCI Journal Publication Incentive, Faculty of Engineering
- *2024.12*&ensp;Awarded Top 10% SCI Journal Publication Incentive, Faculty of Engineering
- *2020.12*&ensp;Third Prize, 21st Huawei Cup China Postgraduate Mathematical Contest in Modeling (CPMCM) — Wang Tao (Team Leader)


# 💪🏸 Things I Enjoy
- **Fitness**  
  Regular strength training and wellness activities.
  
- **Badminton**  
  Passionate about competitive badminton. Honors include:  
  - 🥇 Champion, Postgraduate Team Tournament, Northeast Petroleum University (2021)  
  - 🥈 Runner-up, Team Tournament, Northeast Petroleum University (2022)  
  - 🥈 Runner-up, CCB Malaysia 2nd Badminton Tournament (2024)  
  - 🏆 Champion, Universiti Malaya International Students Men’s Doubles (2024)


# 💬 News
- *Now* &ensp;&ensp;&ensp;&ensp;![Visitors](https://api.visitorbadge.io/api/visitors?path=https://GeneAIhub.github.io/&label=visitors&countColor=%232ccce4&style=plastic)


  



  
