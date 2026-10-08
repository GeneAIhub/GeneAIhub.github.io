---
layout: page
title: 中文简历
permalink: /zh-cn/
author_profile: true
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

我是 **Teng Wang**，获**马来亚大学（Universiti Malaya）机械工程博士学位**。我的研究主要围绕机械设备状态监测与智能故障诊断展开，重点关注深度学习在时间序列分析中的应用，以及生成模型在故障数据增强中的应用，致力于解决变工况、类别不平衡和故障样本稀缺条件下的诊断问题。

已发表 SCI 期刊论文 5 篇以上，论文及引用情况可查看我的
<a href="https://scholar.google.com/citations?user=DmN2rEYAAAAJ" target="_blank" rel="noopener noreferrer">Google Scholar 主页 <img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations" alt="Google Scholar 引用次数"></a>。

博士期间由 <a href="https://umexpert.um.edu.my/alexongzc" target="_blank" rel="noopener noreferrer">Ong Zhi Chao 教授</a>、<a href="https://umexpert.um.edu.my/khooshinyee" target="_blank" rel="noopener noreferrer">Khoo Shin Yee 博士</a>和 <a href="https://umexpert.um.edu.my/siowpeiyi" target="_blank" rel="noopener noreferrer">Siow Pei Yi 博士</a>指导。我是先进冲击与振动研究组（Advanced Shock and Vibration Research，ASVR）成员，该研究组隶属于<a href="https://engine.um.edu.my/department-of-mechanical-engineering" target="_blank" rel="noopener noreferrer">马来亚大学工程学院机械工程系</a>。

研究兴趣包括：

- 机械设备状态监测与智能故障诊断
- 用于时间序列数据增强的生成模型
- 不平衡、稀缺及弱标注数据条件下的学习方法
- 小样本学习
- 非线性时间序列分析与基于熵的特征提取

# 🎓 教育经历

- *2023.03 – 2026.05*&ensp;**博士，机械工程**，马来亚大学，马来西亚吉隆坡。<a href="https://engine.um.edu.my/about-mechanical-engineering"><img class="svg" src="/images/UM.png" width="16pt" alt="马来亚大学校徽"></a>
- *2019.09 – 2022.06*&ensp;**硕士**，东北石油大学机械科学与工程学院，中国大庆。<a href="https://jxkxygcxy.nepu.edu.cn/"><img class="svg" src="/images/NEPU.png" width="16pt" alt="东北石油大学校徽"></a>

# 📝 学术论文

<h3 align="center">代表性论文</h3>
<div style="border-bottom: 1px solid #000; margin: 0;"></div>

<div class="paper-box">
    <div class="paper-box-image" style="text-align:center;">
        <img src="/images/EnSeqInfo.jpg" alt="增强生成对抗网络用于长振动时间序列生成" style="max-width:80%; height:auto; margin:auto; vertical-align:middle;">
    </div>
    <div class="paper-box-text">
        <a href="https://www.sciencedirect.com/science/article/pii/S0952197625007602">
            <papertitle>An enhanced generative adversarial network for longer vibration time data generation under variable operating conditions for imbalanced bearing fault diagnosis</papertitle>
        </a>
        <br>
        <strong>Teng Wang</strong>, Zhi Chao Ong*, Shin Yee Khoo, Pei Yi Siow, Tao Wang.
        <br>
        <em>Engineering Applications of Artificial Intelligence</em>, 2025（TOP） <a href="https://github.com/GeneAIhub/GeneAIhub">[代码]</a>
        <p>提出增强生成对抗网络，用于生成变工况下更长的振动时间序列，改善故障类别不平衡条件下的轴承故障诊断性能。</p>
    </div>
</div>

<div class="paper-box">
    <div class="paper-box-image" style="text-align:center;">
        <img src="/images/SeqInfo.jpg" alt="SeqInfo-SAWGAN-GP 模型示意图" style="max-width:80%; height:auto; margin:auto; vertical-align:middle;">
    </div>
    <div class="paper-box-text">
        <a href="https://www.sciencedirect.com/science/article/pii/S0263224124022292">
            <papertitle>SeqInfo-SAWGAN-GP: Adaptive feature extraction from vibration time data under variable operating conditions for imbalanced bearing fault diagnosis</papertitle>
        </a>
        <br>
        <strong>Teng Wang</strong>, Zhi Chao Ong*, Shin Yee Khoo, Pei Yi Siow, Tao Wang.
        <br>
        <em>Measurement</em>, 2025 <a href="https://github.com/GeneAIhub/GeneAIhub">[代码]</a>
        <p>提出以序列信息为条件的生成模型 SeqInfo-SAWGAN-GP，提高变工况下合成振动时间序列的多样性，缓解故障数据稀缺与类别不平衡问题。</p>
    </div>
</div>

<div class="paper-box">
    <div class="paper-box-image" style="text-align:center;">
        <img src="/images/DHMDSEn.jpg" alt="双层级多尺度距离相似熵方法示意图" style="max-width:80%; height:auto; margin:auto; vertical-align:middle;">
    </div>
    <div class="paper-box-text">
        <a href="https://www.sciencedirect.com/science/article/pii/S0888327026010137">
            <papertitle>Dual-hierarchical multi-scale distance similarity entropy as a novel nonlinear measure for wind turbine gearbox intelligent fault diagnosis</papertitle>
        </a>
        <br>
        Tao Wang, Shin Yee Khoo*, Zhi Chao Ong, Pei Yi Siow, <strong>Teng Wang</strong>.
        <br>
        <em>Mechanical Systems and Signal Processing</em>, 2026
        <p>提出双层级多尺度距离相似熵（DHMDSEn），将互补的相移层级分解与多尺度距离相似熵相结合，提高振动信号的信息利用率与复杂度表征能力。在实验室风电齿轮箱和实际工业数据集上，平均诊断准确率分别达到 91.22% 和 99.98%，优于所比较的层级熵方法。</p>
    </div>
</div>

<div class="paper-box">
    <div class="paper-box-image" style="text-align:center;">
        <img src="/images/MDSEN.jpg" alt="多尺度距离相似熵方法示意图" style="max-width:80%; height:auto; margin:auto; vertical-align:middle;">
    </div>
    <div class="paper-box-text">
        <a href="https://www.sciencedirect.com/science/article/pii/S0952197625023164">
            <papertitle>Multi-scale distance similarity entropy: A novel complexity measurement for gearbox fault diagnosis</papertitle>
        </a>
        <br>
        Tao Wang, Shin Yee Khoo*, Zhi Chao Ong, Pei Yi Siow, <strong>Teng Wang</strong>.
        <br>
        <em>Engineering Applications of Artificial Intelligence</em>, 2025（TOP） <a href="https://github.com/lattetaotao/Multi-scale-distance-similarity-entropy">[代码]</a>
        <p>提出多尺度距离相似熵（MDSE），将距离相似熵与多尺度粗粒化过程结合，在抑制噪声的同时捕捉齿轮箱振动信号的非线性变化。在两个齿轮箱数据集上，诊断准确率均超过 97%，并表现出良好的鲁棒性与计算效率。</p>
    </div>
</div>

<div class="paper-box">
    <div class="paper-box-image" style="text-align:center;">
        <img src="/images/DSEN.png" alt="距离相似熵方法示意图" style="max-width:80%; height:auto; margin:auto; vertical-align:middle;">
    </div>
    <div class="paper-box-text">
        <a href="https://www.sciencedirect.com/science/article/pii/S0951832024007142">
            <papertitle>Distance similarity entropy: A sensitive nonlinear feature extraction method for rolling bearing fault diagnosis</papertitle>
        </a>
        <br>
        Tao Wang, Shin Yee Khoo*, Zhi Chao Ong, Pei Yi Siow, <strong>Teng Wang</strong>.
        <br>
        <em>Reliability Engineering &amp; System Safety</em>, 2025（TOP） <a href="https://github.com/GeneAIhub/GeneAIhub">[代码]</a>
        <p>提出用于滚动轴承故障诊断的距离相似熵（DSEN），通过逐元素距离与高斯相似度捕捉信号的细微局部变化，并通过估计相似度分布表征信号复杂度，提高故障诊断的准确性与可靠性。</p>
    </div>
</div>

# 🏅 荣誉与奖励

- *2025.03*&ensp;马来亚大学工程学院 Top 10% SCI 期刊论文发表奖励。
- *2024.12*&ensp;马来亚大学工程学院 Top 10% SCI 期刊论文发表奖励。

# 💪🏸 兴趣爱好

- **健身**：坚持力量训练，注重健康与体能管理。
- **羽毛球**：热爱羽毛球运动，积极参加校内外比赛，曾获：
  - 🥇 2021 年东北石油大学研究生羽毛球团体赛冠军
  - 🥈 2022 年东北石油大学羽毛球团体赛亚军
  - 🥈 2024 年马来西亚 CCB 第二届羽毛球赛亚军
  - 🏆 2024 年马来亚大学国际学生羽毛球男双冠军

# 💬 访问统计

![访问量](https://api.visitorbadge.io/api/visitors?path=https://GeneAIhub.github.io/&label=visitors&countColor=%232ccce4&style=plastic)
