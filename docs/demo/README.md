# For You Skills demo

[中文项目说明](../../README.zh-CN.md) · [English project overview](../../README.md) · [English transcript](#english-transcript)

这段 78 秒演示呈现两次实际使用的结果：回答“今天已经发过一篇，还能发吗？”，再把作者的 Article 曝光观察改成一篇导读 Post。中英文版本均为无声剪辑，影片托管在 YouTube。

The 78-second demo replays two actual runs: a posting-frequency question and an introductory Post based on an Article-reach observation. Both language versions are silent and hosted on YouTube. The English edition translates and re-typesets the archived results; it is not a separately rerun English agent session.

| 中文版 | English |
| --- | --- |
| [![观看中文演示](for-you-skills-cover-zh.png)](https://youtu.be/TQfDplGaFXY?si=mNGTutX1lj7Py08r) | [![Watch the English demo](for-you-skills-cover-en.png)](https://youtu.be/QSL0kNQvs_E?si=VXDbXhogFb7bq7ip) |
| [在 YouTube 观看](https://youtu.be/TQfDplGaFXY?si=mNGTutX1lj7Py08r) · [中文字幕](captions.zh-CN.srt) | [Watch on YouTube](https://youtu.be/QSL0kNQvs_E?si=VXDbXhogFb7bq7ip) · [English subtitles](captions.en.srt) |

中文片的源码画面来自原浏览器截图；英文片使用保留行号的原始代码摘录。The Chinese edition uses the original browser source screenshot; the English edition typesets selected original code lines with their line numbers.

仓库保留字幕、静态封面、文案和执行证据，视频与 GIF 预览已从 Git 历史中移除。[历史清理说明 / History cleanup](media-hosting.md)。另见[安装与问答执行证据 / Installation and Q&A evidence](live/README.md)；原 3:49 安装录屏已移除，该记录与上面的演示片是两次不同执行。

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

The English localization was prepared on **2026-11-07**. The original draft length measurement and reader-review results apply to the Chinese draft, not its English translation. The demo records results produced on **2026-11-04** using the research cutoff and code revision stated above. The run record contains the complete Chinese prompts and answers, code excerpts and review evidence. The reported Article impressions are the author's observation, and the numerical scoring example is illustrative arithmetic.

## Demo files

| File | Contents |
| --- | --- |
| [captions.zh-CN.srt](captions.zh-CN.srt) | Chinese subtitles |
| [captions.en.srt](captions.en.srt) | English subtitles |
| [for-you-skills-cover-zh.png](for-you-skills-cover-zh.png) | Chinese cover |
| [for-you-skills-cover-en.png](for-you-skills-cover-en.png) | English cover |
| [for-you-skills-qa-card-zh.png](for-you-skills-qa-card-zh.png) | Posting-frequency Q&A card in Chinese |
| [promo-copy.zh-CN.md](promo-copy.zh-CN.md) | Chinese launch copy and image descriptions |
| [promo-copy.en.md](promo-copy.en.md) | English launch copy |
| [run-record.zh-CN.md](run-record.zh-CN.md) | Archived prompts, full answers, source excerpts and verification records |
| [review-ledger.json](review-ledger.json) | Topic screening, format evidence and review outcomes |

Original materials follow the repository's [license](../../LICENSE). Quoted code retains its source attribution and license as described in [NOTICE.md](../../NOTICE.md).
