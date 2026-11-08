# For You Skills — X.com / Twitter 算法分析与发帖技能

[English](README.md) | **简体中文**

**“上午已经发了一条，下午这条要不要留到明天？”**

这就是你可以直接问 **For You Skills** 的运营问题，手里不用先有稿子。发帖频率怎么定？图片和外链在推荐里怎么处理？长文发 Post 还是 Article？它会查随技能安装的研究资料，把建议、适用条件和对应的 X.com / Twitter 推荐源码放在一起。手里有草稿，可以请它改；有帖子和后台数据，也可以请它一起查曝光变化的原因。

**8 个技能 · 578 个原始知识条目 + 14 项更新核查 · 保留 49 个待解问题**

**v1.3.0：已核对算法代码至 2026-11-08。** [这次改了什么，用人话说明](docs/research-update.zh-CN.md) · [算法更新记录](ALGORITHM_CHANGELOG.md) · [版本记录](CHANGELOG.md)

[阅读完整研究文档](https://blog.go5.si/posts/zh/x-algorithm-teardown/) · [关注作者，了解最新进展](https://x.com/alexlee20122022)

装一个总入口就能使用下面七项功能，之后用自己的话问就行。

```bash
npx skills add alexliyu7352/for-you-skills --skill x-assistant
```

> 我上午已经在 X.com 发了一篇，下午有另一主题的新内容，今天能发吗？请给出建议，对照推荐源码解释依据，并说明还有哪些不能确定。

**建议动作：** 新帖已经准备好，对读者有用，又有时效，今天就发。这是内容安排上的建议；代码没有规定一个最佳发布时间。

**代码能确定的：** `author_pool_counts` 把这次考虑推荐给某位读者的帖子按分数排序，再为每位作者从零计数。每次调用都重新计数。启用作者多样性、并采用 VM Ranker 排序服务的公开默认参数时，倍率是 `0.75 × 0.5^k + 0.25`，其中 `k` 就是这个计数：你分数最高的候选乘 `1`，第二名乘 `0.625`，第三名乘 `0.4375`。下午的新帖也可能排第一。**这次计算中排第二的候选，不一定是你今天发的第二篇。** [计数与倍率源码](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L183-L237) · [默认参数](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/vm-ranker/params.rs#L169-L197)

**还不能确定的：** `0.625` 是分数倍率，不能换算成“曝光剩 62.5%”。这个函数推不出每日发帖上限或“四小时恢复期”，也不能确定线上某次请求的候选、参数和你账号的最佳发布间隔。不同主题可以给读者新价值，但不能绕过按作者 ID 计数的规则。这套计数逻辑已在 `3b6919f` 再次核对，仍然如此；实际线上配置并未全部核验。[完整原始回答与算例](docs/demo/run-record.zh-CN.md#原始运营问答输出)

已验证 **Claude Code、Codex、Gemini CLI、Cursor、GitHub Copilot、OpenCode** 的安装。你用中文提问，它就用中文回答。[其他安装方式](#安装) · [验证报告](docs/validation/results.md)

## 查看安装与问答执行证据

[查看安装日志与核验记录](docs/demo/live/README.md)：在新项目目录安装技能，查知识库，读取原始代码，再由 **ChatGPT Work** 给出本次回答。保留完整执行日志与源码核验记录；原独立录屏已从 Git 中移除。[完整回答和源码链接](docs/demo/live/answer.zh-CN.md)。安装后的 31 个文件已与仓库逐位元组比对，差异为零。

## 78 秒看两次实际使用

**0:15**，打开源码，看“第二条”究竟指哪条帖子。**0:47**，换成作者报告的一组观察。一篇 Article 发了一周，曝光超过 3,000，其他 Post 最多几百。看它怎么把这段经历改成导读，也看它指出还需要哪些数据来研究差距的原因。

[![在 YouTube 看中文演示：从第二条帖子的曝光问题查到推荐源码，再审一篇 Article 导读](docs/demo/for-you-skills-cover-zh.png)](https://youtu.be/TQfDplGaFXY?si=mNGTutX1lj7Py08r)

[在 YouTube 看中文版](https://youtu.be/TQfDplGaFXY?si=mNGTutX1lj7Py08r) · [Watch in English](https://youtu.be/QSL0kNQvs_E?si=VXDbXhogFb7bq7ip) · [演示说明](docs/demo/README.md) · [查看完整提问、回答和源码](docs/demo/run-record.zh-CN.md) · [单看问答对照图](docs/demo/for-you-skills-qa-card-zh.png)

中英文影片均为两次实际问答结果的无声剪辑，英文版翻译并重新排版了原始结果。影片统一放在 YouTube；[演示素材](docs/demo/README.md#demo-files)保留中英文字幕、静态封面、发布文案与原始证据。

## 从 Article 曝光问题，到一篇可用的导读

第二例来自作者的实际观察：**“我的一篇 Article 发了一周，每天还有新曝光，总曝光超过 3K；其他 Post 最多也就几百。这是什么原因？”** 这次要求是把问题改成一篇导读 Post，面向正在选择长 Post 和 Article 的创作者。

审稿保留了原观察，交付完整稿件，开头改成：

> 我的一篇 Article 发了一周，每天还有新曝光，总曝光超过 3K（3000）；其他 Post 最多也就几百。这是为什么？长文就该改发 Article 吗？

| 审查项 | 这次实际交付 |
| --- | --- |
| 完整稿与长度 | 一篇 546 个 Unicode 码点的中文稿，去首尾空白，计入链接和段落换行。这是文本测量，不等于 X 的加权字数，也不代表已确认账号发布权限。 |
| 发布形式 | 这份材料用单条较长的导读 Post；有多节材料、图表和反复查阅的需要，再考虑 Article。这是编辑判断。 |
| 首图 | 一张待制作的信息卡：“Post：一个问题，几段讲清”／“Article：多节内容、图表、反复查阅”；页脚保留个人观察及其限制。这次交付的是配图方案。 |
| 依据与下一步 | 保留原数字，核对指标定义、发布时间、截数时间、主题与推广情况。统一比较发布后七天，Article 和介绍它的 Post 分开记录。仅凭这组观察，还不能认定差距由格式造成。 |

[查看完整稿件和审稿意见](docs/demo/run-record.zh-CN.md#完整审稿输出) · [查看逐项依据记录](docs/demo/review-ledger.json)。原始输出保留了算法判断的源码链接和未取得的证据，读者可以继续核查。

## 查过代码，建议会有什么不同？

| 你关心的问题 | 分析实际查到了什么 | 对发帖有什么用 |
| --- | --- | --- |
| **“多图帖子，第一张到底该放什么？”** | V8.2 的一条媒体选择路径，遇到**第一张有可用内容的图片就返回**。只放在第四张图里的结果，不会随这次选择一起送过去。[源码](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer_v82.py#L285-L314) | 把最有用、有依据的结果及关键条件放进首图，正文也说清主要发现。这个依据限定在该处理路径内，不保证换首图就涨曝光。 |
| **“长 Post 必须控制在 4,000 字符以内？”** | V8.2 的一条文本处理路径，会把正文截到 **4,000 字符**。它说明的是特定处理流程的边界，不是平台统一的发文上限。[源码](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer_v82.py#L33-L50) | 实测稿件长度，检查核心发现落在什么位置。有必要的论证可以保留；选发布形式前，先解释这个边界究竟影响哪一步。 |

技能把适用条件和结论一起保存，并区分代码事实、官方说明、本地观察、写作判断和待解问题。**每条有依据的建议，都能继续往下查。**

## 把稿子交进来，拿到能直接用的修改

发布前审查会遍历研究中的全部主题，再逐项检查与你这篇内容有关的规则。你应该拿到：

- **能直接替换的开头。** 引用你实际写的前几行，判断是否说清读者为什么要继续看，以及正文是否兑现了这个承诺；需要修改时给出成稿。
- **实际测量的长度。** 统计提供的文本，说明计数单位，检查重要内容的位置。
- **针对这篇稿子的配图方案。** 说明是否值得配图、首图应该表达什么、后面每张图补充什么。没有提交图片，也会给出具体建议。
- **有理由的发布形式选择。** 根据内容和目标，判断适合长 Post、Article 还是 Thread。
- **其余适用的发布检查。** 外链、阅读收益、视频条件、hashtag、可见性标签、重复内容、互动和更正安排，都按实际情况检查，附上依据和缺失信息。
- **有明确结果的读者审查。** 支持独立上下文时，由没有参与写作的读者拿到完整审查标准，从头检查指代、术语和推理步骤；不支持时明确标为自审。默认最多进行三次读者审查，缺少事实或仍有问题就如实列出。只有发布计划时继续审查计划，不编造正文；只提供节选时，结论也只覆盖节选。这一段是编辑判断，与算法证据分开报告。

已经发过的内容，可以提供帖子链接、账号链接、截图或导出记录。有相应能力时，技能通过已授权的浏览器或 Chrome MCP 查看实际内容，记录真正看到了什么，再给修改建议。曝光诊断会区分观察结果与可能原因，并说明下一步看什么数据才能分辨。

## 配图建议，可以接着做成图

直接说：**“按这次审稿的方案配图，以后这个系列保持同样风格。”** 助手会把稿件、来源和图片顺序交给 `x-create-visuals`，你不用重新解释一遍内容。

它会先检查当前环境有哪些工具；如果能直接生成图片，就明确告诉你。你可以选自己的图片、真实截图、AI 生图或混合使用。首次使用时，只询问缺少的图片来源、生图方式和风格偏好。以后可以沿用、仅这次修改，或另存为新系列。**临时换风格，不会覆盖默认设置。**

偏好保存在私有的用户配置文件里，独立于技能安装目录和公开仓库。默认、账号、系列可以分别设置，还能导出、导入 JSON，在不同 Agent 或设备之间迁移。同一系统账号下重新安装可读取原来的文件；不同主机需要主动迁移。如果环境不能长期保存，助手会说明，并提供导出方式。

涉及真实证据时，截图和代码面板使用原始材料，精确图表根据核实过的数据绘制，适合插画的部分才交给 AI。交付前检查文字、数字、裁切和图片顺序。如果没有可用的制作工具，就明确交付配图方案和提示词。实际生图能力取决于你的 Agent 和所选服务；技能不附带服务凭证，也不承诺“配图就涨曝光”。

## 一个总入口，七项具体工作

不用背命令。**`x-assistant` 根据你的问题选择技能**，连续追问时沿用已有上下文，最后给出一份合并后的回答。也可以单独安装或指定某个技能。

| 技能 | 负责什么 |
| --- | --- |
| [`x-assistant`](skills/x-assistant/SKILL.md) | 总入口，处理自然语言问题、复合任务和后续追问 |
| [`x-explain`](skills/x-explain/SKILL.md) | 解答 X.com / Twitter 算法、权重、发帖频率、阅读信号、媒体和外链问题 |
| [`x-myth-check`](skills/x-myth-check/SKILL.md) | 逐条核查算法传言与攻略，给出原始出处 |
| [`x-format-advisor`](skills/x-format-advisor/SKILL.md) | 为具体内容选择长 Post、Article 或 Thread |
| [`x-publish-checklist`](skills/x-publish-checklist/SKILL.md) | 发布前审查草稿，给出可执行的修改 |
| [`x-review-posts`](skills/x-review-posts/SKILL.md) | 查看已发布内容或截图，提出改进建议 |
| [`x-reach-diagnosis`](skills/x-reach-diagnosis/SKILL.md) | 排查曝光表现，确定下一项值得做的核查 |
| [`x-create-visuals`](skills/x-create-visuals/SKILL.md) | 制作配图，保存、复用或迁移你的视觉风格 |

可以这样问：

> 我的 Article 发了一周，浏览超过 3K，每天还在涨。其他 Post 只有几百。这说明了什么？下一篇应该怎么发？

> 检查这篇 X.com / Twitter 算法攻略。每条说法都列出依据、是否读错了，以及代码没能证明什么。

> 给这篇帖子做两张图。沿用 weekly-code 系列的风格，但只在这次换一套配色。

> 保留 Article 形式。这次只重写导读 Post：直接告诉读者能确定什么、不能确定什么，以及建议怎么做。

自动识别技能的效果取决于所用 Agent 和模型。如果没有自动调用，先让它读取 `x-assistant/SKILL.md` 即可。总入口内置了七项工作的完整流程，只安装入口也能使用。

## 研究成果随技能一起安装

完整报告被蒸馏为 **578 个英文条目，其中包括 49 个待解问题**，覆盖 **668 个实质性原文单元、100 组参考来源和 396 个不同的原始 URL**。中文分析原文也一并保留，方便追溯。另有 **14 项截至 2026-11-08 的更新核查**；检索受影响的旧条目时，会同时返回新结论及其源码依据。

每个条目都保存结论、适用条件、实操含义、核查步骤、信息不足时如何回答、结论边界及原始引用。相关出处包括源文件、代码行、常量、公式和变更记录。

**连哪些问题还没有答案，也一起做进了技能。** 源码公开，不代表某个账号曝光变化的原因就已经确定。技能保留这个区别，同时给出下一步值得做的检查。

每个技能都带有自己需要的知识资料，可以离线检索。核实最新变化或查看账号时，再使用 Agent 已有的工具。无需强制购买数据服务、申请 X.com / Twitter API Key，或安装指定的 MCP 服务。参见[知识库说明](knowledge/README.md)与[完整中文研究原文](provenance/research-report.zh-CN.md)。

## 深入阅读与后续更新

想进一步了解这些建议是怎么得出的，可以阅读我们的原始研究文档，其中展开了代码分析、公式、具体案例和结论的适用范围：

- [完整中文研究文档](https://blog.go5.si/posts/zh/x-algorithm-teardown/)
- [Full research in English](https://blog.go5.si/posts/x-algorithm-teardown/)

本项目会根据 [X.com / Twitter 算法仓库主线](https://github.com/xai-org/x-algorithm)的变化，持续更新研究内容和技能，并标明分析对应的代码版本与研究日期，方便追溯依据。想了解新的发现、研究进展和技能更新，可以关注作者 [@alexlee20122022](https://x.com/alexlee20122022)。

仓库每周检查一次算法主线，也支持手动检查；有新提交时会列出待核对的差异。检查不会自动改写结论或发布技能。已安装的技能仍需更新，才会取得新资料。

## 安装

上方命令使用 [Skills CLI](https://github.com/vercel-labs/skills)，需要 **Node.js 22.20 或更新版本**。按提示选择 Agent，默认安装到当前项目；加上 `-g` 可安装到用户级目录。

想让八个技能分别出现在列表里，可以用 `--skill '*'` 安装全套。如果只想安装到 Claude Code 和 Codex，再用 `-a` 指定这两个 Agent。

```bash
npx skills add alexliyu7352/for-you-skills --skill '*' -a claude-code codex
```

只安装总入口或某个独立技能：

```bash
npx skills add alexliyu7352/for-you-skills --skill x-assistant -a gemini-cli
npx skills add alexliyu7352/for-you-skills --skill x-publish-checklist -a opencode
```

也可以把完整的 `skills/<技能名>/` 目录复制到 Agent 的技能目录，保留其中的引用资料和脚本。辅助脚本使用 **Python 3.9+**，只依赖标准库；没有 Python 时，Agent 仍可直接读取知识文件。浏览器访问能力由宿主环境提供。[兼容性说明](docs/compatibility.md)

## 已经验证到哪一步

[验证说明](docs/validation/results.md)列出可复现的知识完整性检查、生成文件一致性检查、**81 项自动测试**和 Linux／Windows CI 配置。某次提交是否通过，以链接中的 Actions 结果为准。

已检查六种目标 Agent 的安装。公开演示保留[安装与问答执行证据](docs/demo/live/README.md)和[完整审稿案例](docs/demo/run-record.zh-CN.md)。安装成功不代表每个客户端的模型行为都已验证；六种外部 CLI 各自的模型运行、实时访问 X.com 采集，以及曝光提升实验，**尚未实测**。

## 研究范围

原始报告截止于 **2026-10-29**，基准版本 `5ed7963`、对照版本 `606b254`。本次补充核查日期为 **2026-11-08**，从 `606b254` 检查到 `3b6919f`，共 7 次提交。原报告保留原样，新结论和适用条件另行记录。代码里存在某项功能，不等于已经向所有用户开放；公开默认参数也不等于每次线上请求的实际配置。

技能不计算平台未公开的“曝光分”，也不保证推荐量。公开浏览数、首页曝光、Article 页面计数与独立读者数各自保留原有含义。技能负责审查和建议；发布、编辑、删除或互动操作，需要另行提出请求，并遵循宿主的授权规则。

<details>
<summary><strong>维护与验证</strong></summary>

维护源文件位于 `workflows/`、`shared/`、`knowledge/`、`routing.json`、`metadata/` 和 `tools/`。`skills/` 是生成后的可安装目录。工作流源文件中的链接按安装后的目录编写，在 GitHub 的 `workflows/` 下直接点击可能返回 404；阅读时请从[工作流索引](workflows/README.md)进入对应的生成版本，其中的链接可以正常访问。修改源文件后运行：

```bash
python3 tools/build.py
python3 tools/validate.py
python3 tools/build.py --check
python3 -m unittest discover -s tests -v
```

每个技能携带独立的引用和脚本，维护时共用一套源文件。参见[知识维护说明](knowledge/README.md)、[版本记录](CHANGELOG.md)和[来源说明](NOTICE.md)。

</details>

## 许可证

原创技能指令、英文整理内容及辅助代码采用 [MIT 许可证](LICENSE)。第三方材料保留原有许可证和署名要求，详见 [NOTICE.md](NOTICE.md)。
