# For You Skills demo

[中文项目说明](../../README.zh-CN.md) · [English project overview](../../README.md) · [English transcript](#english-transcript)

这段 78 秒演示呈现两次实际使用的结果。先回答“今天已经发过一篇，还能发吗？”，再把作者的 Article 曝光观察改成一篇导读 Post。画面来自问答结果、审稿结果和浏览器中的源码截图，经过摘录、排版与剪辑。视频全程中文、无音轨。

The 78-second video replays two actual runs, covering a posting-frequency question and an introductory Post based on an Article-reach observation. It combines excerpts from the outputs with a browser screenshot of the source code. All on-screen text is Simplified Chinese, with an English transcript below.

[![78 秒演示，从发帖频率问题查到源码，再审查 Article 导读](preview-zh.gif)](for-you-skills-demo-zh.mp4)

[打开 1080p 视频 / Open MP4](for-you-skills-demo-zh.mp4) · [下载 MP4 / Download](for-you-skills-demo-zh.mp4?raw=1) · [中文字幕 / Chinese subtitles](captions.zh-CN.srt)

另有一段 [实际安装与问答日志录屏 / Live installation and Q&A](live/README.md)，记录新的 Work 执行过程，可与本页的 78 秒结果剪辑分别查看。

## 提问、回答与依据

**第一例问发帖频率。** 今天已经发过一篇，有另一主题的新内容，是否现在发？回答先给内容安排建议，再读 `author_pool_counts` 和倍率函数。使用演示所选的公开默认参数时，同作者在这次计算中按分数排第一、第二、第三的候选，倍率依次为 `1`、`0.625`、`0.4375`。哪些帖子进入这次候选、实际启用哪些参数和账号曝光表现，需要各自的证据。[计数与倍率函数](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L183-L237) · [公开默认参数](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/vm-ranker/params.rs#L169-L197)

**第二例审查 Article 导读。** 作者报告一篇 Article 发布一周后曝光超过 3K，其他 Post 最多几百。审稿保留这组观察，交付完整导读、实际长度测量、格式建议和首图方案，并提出需要补充的统计时间、指标定义和推广记录。[完整提问、回答与代码摘录](run-record.zh-CN.md) · [逐项审稿记录](review-ledger.json)

原始运行日期为 **2026-11-04**，知识库研究截止于 **2026-10-29**。源码固定在 `5ed796374ea48ee26058aab66ab10c266bea2bef`，实际开关和参数的取值范围见完整记录。视频中的 `0.9`、`0.8`、`0.7` 用于示意算术，3K 来自作者报告的个人观察。完整记录保留当次执行的访问结果与核验范围。

## English transcript

| Time | What the video shows |
| --- | --- |
| 0:00–0:06 | A creator asks whether a second post on the same day loses about 40% of its reach. |
| 0:06–0:15 | The answer recommends publishing if the new post answers another question and is ready. That recommendation concerns the content and its timing. |
| 0:15–0:26 | The code sorts candidates by score and counts posts by the same author within that call. Each call starts a new count. The input contains no daily publication counter or four-hour reset timer. |
| 0:26–0:39 | With author diversity enabled and the selected published defaults, the second candidate from the same author receives a multiplier of `0.625`. An illustrative calculation shows how this affects a score. It supplies no measurement of impressions. |
| 0:39–0:47 | Timely material can be published when ready. Finding an account's best frequency requires account observations, and the next post's reach remains uncertain. |
| 0:47–0:57 | The author reports an Article with more than 3K impressions after a week and other Posts with hundreds. The reviewer keeps the observation and identifies the missing evidence for attributing the difference to format. |
| 0:57–1:07 | The review provides a complete introductory Post, a measured length, a format recommendation and a first-image plan. The format recommendation follows the reader's needs. |
| 1:07–1:18 | Install `x-assistant` and ask naturally about posting decisions, source code or a draft. |

The demo records results produced on **2026-11-04** using the research cutoff and code revision stated above. The run record contains the complete Chinese prompts and answers, code excerpts and review evidence. The reported Article impressions are the author's observation, and the numerical scoring example is illustrative arithmetic.

## Demo files

| File | Contents |
| --- | --- |
| [for-you-skills-demo-zh.mp4](for-you-skills-demo-zh.mp4) | Full 78-second video, 1920 × 1080, H.264, 24 fps, silent |
| [preview-zh.gif](preview-zh.gif) | Full 78-second preview, 1120 × 630, 2 fps |
| [captions.zh-CN.srt](captions.zh-CN.srt) | Chinese subtitles |
| [for-you-skills-cover-zh.png](for-you-skills-cover-zh.png) | Chinese cover |
| [for-you-skills-cover-en.png](for-you-skills-cover-en.png) | English cover |
| [for-you-skills-qa-card-zh.png](for-you-skills-qa-card-zh.png) | Posting-frequency Q&A card in Chinese |
| [promo-copy.zh-CN.md](promo-copy.zh-CN.md) | Chinese launch copy and image descriptions |
| [promo-copy.en.md](promo-copy.en.md) | English launch copy |
| [run-record.zh-CN.md](run-record.zh-CN.md) | Archived prompts, full answers, source excerpts and verification records |
| [review-ledger.json](review-ledger.json) | Topic screening, format evidence and review outcomes |

Original materials follow the repository's [license](../../LICENSE). Quoted code retains its source attribution and license as described in [NOTICE.md](../../NOTICE.md).
