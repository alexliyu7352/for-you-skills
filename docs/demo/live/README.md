# Installation and Q&A: a real Work run

[项目中文说明](../../../README.zh-CN.md) · [English overview](../../../README.md) · [78 秒结果演示](../README.md)

**[观看安装与问答实录 / Watch the recording](install-and-qa.mp4)** · [下载 / Download MP4](install-and-qa.mp4?raw=1) · [完整回答及原始源码链接](answer.zh-CN.md)

录制于 **2026-11-06（America/Los_Angeles）**。时长约 **3 分 49 秒**，816 × 484，无音轨。内容包括：在新项目目录安装 `x-assistant`、按自然语言问题查知识库、在线读取固定版本源码，以及本次生成的回答。终端里显示的是 **ChatGPT Work 的实际执行日志**；工具输出在运行过程中更新，回答完成后整段显示，没有模拟逐字输入。

This records a real ChatGPT Work run: a fresh project installation, evidence lookup, source retrieval and a newly generated answer. The terminal is a live log viewer, **not a Codex or Claude Code client interface**. Some tool output is condensed and source URLs are abbreviated on screen; the complete answer and original URLs are retained alongside the recording.

## What was actually executed

```bash
npx --yes skills@1.7.6 add alexliyu7352/for-you-skills --skill x-assistant -a codex -y
```

- 安装前，该项目目录没有 `x-assistant`。安装退出码为 `0`，目标为 `.agents/skills/x-assistant`。
- 安装后的 **31 个文件**与项目提交 `27ea82bf1c6caa4459f483fd7aacfb362b9189be` 中的技能逐位元组比对，差异为零。
- 当前 Work 会话读取新安装的 `SKILL.md`、路由表与 `x-explain` 工作流，然后实际执行随包附带的 `knowledge.py`。
- 读取条目 `K01-006`、`K01-032`、`K01-033` 和待解问题 `Q02`；另检查了发帖频率主题目录及 `K01-005`。
- 在线读取固定提交 `5ed796374ea48ee26058aab66ab10c266bea2bef` 的计数函数、VM Ranker 默认参数与 Home Mixer 本地开关；重新计算 `1`、`0.625`、`0.4375`。
- 本次回答明确区分内容建议、代码计数范围、分数倍率和未核验的线上设置。

The clean boundary is the **project installation directory**. The answer was produced by the existing authenticated ChatGPT Work session using the installed skill's documented fallback procedure. This does not claim a fresh OS, a fresh model context, automatic skill discovery, or a successful external Codex CLI model call. The external CLI could not initialize in the execution environment; the desktop CLI was not signed in. No credentials were moved between those environments.

## Video chapters

| Approximate time | What to inspect |
| --- | --- |
| 0:00 | Natural-language question and recording method |
| 0:15–0:45 | Actual Skills CLI installation and success output |
| 1:10 | Installed workflow and knowledge entry lookup |
| 1:35–2:10 | Original code and service-specific switch |
| 2:35 | Default parameters and arithmetic |
| 3:00 | Newly generated recommendation and explanation |
| 3:35 | Remaining uncertainty and source locations |

The recording includes pauses while tools and the assistant work. Its MP4 container did not close cleanly when capture stopped. Complete encoded frames were recovered, remuxed at the capture rate and exported at 6 fps; the incomplete tail was discarded. The final file was decoded in full without errors, and sampled frames confirm that installation, lookup, code, answer and limitations are all present. No answer or screen content was inserted after recording.

## Evidence

| File | What it establishes |
| --- | --- |
| [installation.json](installation.json) | Actual command, timing, exit code and initially empty skill directory |
| [installed-byte-check.json](installed-byte-check.json) | 31 installed files match the referenced repository revision |
| [execution-log.txt](execution-log.txt) | Terminal log, with ANSI control codes removed |
| [knowledge-search.json](knowledge-search.json) | Actual lookup results |
| [knowledge-claims.json](knowledge-claims.json) | Full retrieved claims and original links |
| [knowledge-count-scope.json](knowledge-count-scope.json) | Per-call count scope |
| [unknown-Q02.json](unknown-Q02.json) | Limits of interpreting defaults as live configuration |
| [source-checks.json](source-checks.json) | Source URLs and hashes of downloaded original bytes |
| [answer.zh-CN.md](answer.zh-CN.md) | Complete newly generated answer and source links |
| [run-metadata.json](run-metadata.json) | Input, execution method and scope |

No live X account was changed and no reach improvement was measured. This run verifies the demonstrated install and evidence-backed workflow; it does not certify every host or production configuration. The earlier [78-second video](../README.md) remains a separate, edited presentation of the November 4 results.
