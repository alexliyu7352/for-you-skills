# For You Skills — X.com / Twitter 算法分析与发帖技能

[English](README.md) | **简体中文**

**让你的 AI 发帖助手，拿源码说话。**

For You Skills 把对 **X.com / Twitter 开源推荐算法的完整分析**，做成了一套可以直接安装的 Agent Skills。给它一篇草稿、一组截图，或者一句流传的“算法秘诀”，它会告诉你具体怎么改、依据在哪里、哪些问题还不能下结论。

长文发 Post、Article 还是 Thread？首图该放什么？为什么 Article 发了一周还有新增浏览？你可以顺着回答，找到对应的代码、常量和适用条件。

**8 个技能 · 578 个知识条目 · 396 个原始来源链接 · 保留 49 个待解问题**

[阅读完整研究文档](https://blog.go5.si/posts/zh/x-algorithm-teardown/) · [关注作者，了解最新进展](https://x.com/alexlee20122022)

```bash
npx skills add alexliyu7352/for-you-skills --skill '*'
```

装好后，直接说：

> 帮我审这篇准备发到 X.com / Twitter 的稿子。告诉我哪里要改，应该发 Article 还是长 Post，第一张图该放什么。说明哪些建议有代码依据。

已验证 **Claude Code、Codex、Gemini CLI、Cursor、GitHub Copilot、OpenCode** 的安装。技能和知识库用英文编写，回答跟随你的语言。[安装说明](#安装) · [验证报告](docs/validation/results.md)

## 查过代码，建议会有什么不同？

一个数字可以是真的，用它推出来的发帖建议却可能是错的。下面三个例子，都来自技能内置的研究：

| 你关心的问题 | 分析实际查到了什么 | 对发帖有什么用 |
| --- | --- | --- |
| **“每天第二篇，曝光就只剩六成？”** | 作者多样性计算中的 `0.625`，对应的是**同一次评分中，同一作者按分数排序的第二个候选**。这段函数没有统计每天发了几篇。[源码](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L183-L237) | 根据下一篇是否提供新问题、新证据或新进展安排发布。具体间隔应作为待测试的方案；这个系数推不出统一的每日上限或“四小时重置”。 |
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
- **一次陌生读者冷读。** 由没有参与写作的读者从头读一遍，逐处报出卡住的地方——指代不清、术语没解释、机制到后果之间缺了步骤——改完再读，直到通过。这一段是编辑判断，与算法证据分开报告。

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

完整报告被蒸馏为 **578 个英文条目，其中包括 49 个待解问题**，覆盖 **668 个实质性原文单元、100 组参考来源和 396 个不同的原始 URL**。中文分析原文也一并保留，方便追溯。

每个条目都保存结论、适用条件、实操含义、核查步骤、信息不足时如何回答、结论边界及原始引用。相关出处包括源文件、代码行、常量、公式和变更记录。

**连哪些问题还没有答案，也一起做进了技能。** 源码公开，不代表某个账号曝光变化的原因就已经确定。技能保留这个区别，同时给出下一步值得做的检查。

每个技能都带有自己需要的知识资料，可以离线检索。核实最新变化或查看账号时，再使用 Agent 已有的工具。无需强制购买数据服务、申请 X.com / Twitter API Key，或安装指定的 MCP 服务。参见[知识库说明](knowledge/README.md)与[完整中文研究原文](provenance/research-report.zh-CN.md)。

## 深入阅读与后续更新

想进一步了解这些建议是怎么得出的，可以阅读我们的原始研究文档，其中展开了代码分析、公式、具体案例和结论的适用范围：

- [完整中文研究文档](https://blog.go5.si/posts/zh/x-algorithm-teardown/)
- [Full research in English](https://blog.go5.si/posts/x-algorithm-teardown/)

本项目会根据 [X.com / Twitter 算法仓库主线](https://github.com/xai-org/x-algorithm)的变化，持续更新研究内容和技能，并标明分析对应的代码版本与研究日期，方便追溯依据。想了解新的发现、研究进展和技能更新，可以关注作者 [@alexlee20122022](https://x.com/alexlee20122022)。

下方的研究截止日期对应当前内置知识库；安装技能并不意味着会自动拉取算法仓库之后的变更。

## 安装

上方命令使用 [Skills CLI](https://github.com/vercel-labs/skills)，需要 **Node.js 22.20 或更新版本**。按提示选择 Agent，默认安装到当前项目；加上 `-g` 可安装到用户级目录。

指定安装到某些 Agent：

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

全库独立审查逐条检查了 **578 条知识**、八个技能和完整安装包，发现了原先 43 项测试未覆盖的 **22 项问题**。修复记录逐项列出更正、回归测试或源码核查，以及独立验收结果。

[验证记录](docs/validation/results.md)分别记录自动测试、实际 Agent 任务、单技能离线执行、六种目标的安装和 Linux／Windows CI。具体数量与版本结果以该记录为准，避免把历史检查当成新版已经验证。

任务案例覆盖多语言问答、复合请求、连续追问、稿件审查和提供的已发帖子记录。六种外部 CLI 各自的模型运行、实时访问 X.com 采集，以及曝光提升实验，**尚未实测**。[完整验证记录与修复项](docs/validation/results.md)

## 研究范围

研究截止于 **2026-10-29**。基准版本为 `5ed796374ea48ee26058aab66ab10c266bea2bef`，对照版本为 `606b254b45be798bfaecfa8c23f5a9c51bc8000c`。它们是公开代码快照；涉及当前产品功能或线上部署的问题，需要结合能够取得的最新一手来源核实。

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
