# Full workflow and product review

Reviewed commit: `9193233924df388727296c4e76948db919ac32eb` · Date: 2026-11-01 · Reviewer: `full_review_workflows`.

No confirmed actionable defect was found in the assigned workflow, routing, shared-guide, metadata or README scope. This is a full-file review, not a diff review. The conclusions below come from current reads and fresh helper/workflow executions. They do **not** establish automatic invocation in six external model clients, live X collection, actual image generation or durable preference saving.

## Method and evidence boundary

Read all 24 assigned canonical files in full: eight workflows, routing.json, four shared guides, eight metadata files, both READMEs and compatibility. Screened the 578 rule catalog titles across topics 00–06, then read 43 task-relevant full claims and 18 related unknown entries. The knowledge reviewers own whole-corpus semantic verification; this review does not certify every source claim.

The representative answers below were actually composed by this reviewer while following the workflows and running their bundled helpers. They are not expected-answer prose masquerading as execution. No separate model was launched, no subagent was used, and no native skill invocation call was fabricated. The selected route is reviewer-executed behavior, not a measured guarantee of host/model automatic selection.

The supplied OCR draft and fictional saved-post records were reused as **inputs**, with current helper output recomputed. Their exact text, SHA-256, normalized observation inputs and complete helper JSON outputs are retained in [coverage/workflows.json](coverage/workflows.json). The published records explicitly identify themselves as fictional; none of their X URLs was opened. No image pixels were supplied, and the workspace contained no PNG/JPEG/WebP/GIF fixture to inspect. A described image is therefore never reported as visually inspected here.

Only the two requested review files were written. No image generation, paid provider, login, account mutation or real preference write occurred. The style test used an in-memory fixture and a read of an absent private test path; it did not touch the user's actual preferences.

## Findings

**Confirmed findings: none.** There is no severity/file:line/repro/fix item because no actionable defect survived reproduction in this scope. This should not be read as a claim that unexecuted capabilities passed.

Specific failure hypotheses checked and rejected:

| Hypothesis | Source locations | Observed result |
| --- | --- | --- |
| A specialist routes back forever | workflows/x-assistant.md:12–18; each specialist:8 | Explicit selection, `routed_by`, standalone execution and retained working state provide stop conditions. W01/W04/W08 completed without re-entering completed collection. No native multi-client loop test was run. |
| Router fallback Markdown links break because workflows are nested | workflows/x-assistant.md:14; routing.json:11–54 | Inspected all 13 relative links in generated router fallback workflows. They are rewritten to `../knowledge-guide.md`, `../browsing.md`, etc.; all exist relative to their containing file. The canonical source text alone would have suggested a defect, but generated distribution disproved it. |
| A review-only task creates images or asks repeated style questions | workflows/x-publish-checklist.md:18; shared/visual-workflow.md:25–38 | W04 supplied a concrete image offer and brief, without generation or style setup. W07 accepted the explicitly supplied series/temporary palette without another question. |
| Unknown observations become zero, exact counts, or additional posts | shared/observations.md:13–28 | Current helper retained rounded 3.2K, unknown bookmarks, blocked body, unknown video milliseconds and URL-less records. Sparse pinned A retained likes=21 and complete Article coverage; it did not become a fifth unique post. |
| Temporary palette changes overwrite long-term style | shared/visual-workflow.md:38; tools/visual_preferences.py:130–139 | Actual `selection()` returned `temporary_override=true` with purple/white palette and left the entire supplied store unchanged. The no-save path was tested; durable saving was not. |
| Installation claims imply native model behavior has been tested | README.md:128–130; README.zh-CN.md:128–130; docs/compatibility.md:5–21 | The documents explicitly separate installation, helper execution, agent behavior and live browsing, and say the six external model clients and live X collection were not run. This review adds current-reviewer task execution only. |

## Product requirements checked

| Requirement | Evidence and assessment |
| --- | --- |
| Evidence-based guidance distilled from the report | Shared guide scopes public snapshots, original citations, uncertainty and practical action. W01/W02 retained the counting stage and coefficients; W03/W06 retained format and metric uncertainty. Full distillation accuracy is covered by the knowledge reviewers. |
| Opening, length, media and format review | W04 produced complete usable Chinese copy, quoted the real opening, measured 4,788 trimmed / 4,789 raw code points, located the result at raw position 4,709, removed 85 repeated paragraphs, gave ordered evidence-specific imagery and kept one coherent Post. |
| Explanation separate from audit | W01 answered frequency directly without asking for an account/draft. W08 delivered only the requested introductory copy after the review. |
| Published-content inspection with truthful coverage | W05 used supplied observations and retained body/carrier and image-description limits. W11 stopped at the actual missing material. Live collection/pixel inspection remains unexecuted. |
| Distinguishable certainty | Historical code, editorial judgment, supplied observations, missing internal states and current-provider availability were not merged. All claims in the trial answers are scoped to the bundled snapshot or supplied facts. |
| Natural-language and follow-up routing | Router chose smallest useful procedure, respected explicit Article choice, did not audit an unrelated algebraic x, and reused observations. Automatic native discovery remains host-dependent and untested here. |
| Standalone portability | Bundled helpers for all eight skills resolved K01-033 from cwd=/ using absolute script paths, without a native skill invocation. All 13 fallback links resolved; all eight generated metadata files equal canonical metadata. This is not a new isolated installation test. |
| Real image-tool discovery | Current catalog exposes native `image_gen__imagegen`; its instructions were available/read. Runway tools also exist, but auth/model readiness was not checked and was not claimed. No tool call was invented. |
| Private visual preferences, no temporary overwrite | Shared workflow locates private storage, distinguishes durable versus ephemeral retention, reads before asking, scopes default/account/series explicitly and separates temporary overrides. Actual read-only selection and absent-file read were exercised. Real persistence remains unexecuted. |

## Per-file coverage

All ranges below were read in full, rather than searched only for keywords. Metadata files were also compared with their generated `agents/openai.yaml` copies. Exact file hashes are in the JSON coverage artifact.

| Canonical file | Lines read | Execution/assessment coverage |
| --- | --- | --- |
| `workflows/x-assistant.md` | 1–24 | W01, W04, W08, W09 |
| `workflows/x-create-visuals.md` | 1–18 | W07 |
| `workflows/x-explain.md` | 1–26 | W01 |
| `workflows/x-format-advisor.md` | 1–18 | W03 |
| `workflows/x-myth-check.md` | 1–18 | W02 |
| `workflows/x-publish-checklist.md` | 1–26 | W04, W10 |
| `workflows/x-reach-diagnosis.md` | 1–20 | W06 |
| `workflows/x-review-posts.md` | 1–28 | W05, W11, W12 |
| `routing.json` | 1–97 | W01, W04, W08, W09 |
| `shared/browsing.md` | 1–12 | W05, W11, W12 |
| `shared/knowledge-guide.md` | 1–58 | W01, W02, W03, W04, W05, W06, W10 |
| `shared/observations.md` | 1–30 | W05, W06, W12 |
| `shared/visual-workflow.md` | 1–108 | W04, W07 |
| `README.md` | 1–156 | W01, W02, W03, W04, W05, W06, W07, W08 |
| `README.zh-CN.md` | 1–156 | W01, W02, W03, W04, W05, W06, W07, W08 |
| `docs/compatibility.md` | 1–35 | W07, W10, W11 |
| `metadata/x-assistant.yaml` | 1–4 | Metadata semantics and generated equality |
| `metadata/x-create-visuals.yaml` | 1–4 | Metadata semantics and generated equality |
| `metadata/x-explain.yaml` | 1–4 | Metadata semantics and generated equality |
| `metadata/x-format-advisor.yaml` | 1–4 | Metadata semantics and generated equality |
| `metadata/x-myth-check.yaml` | 1–4 | Metadata semantics and generated equality |
| `metadata/x-publish-checklist.yaml` | 1–4 | Metadata semantics and generated equality |
| `metadata/x-reach-diagnosis.yaml` | 1–4 | Metadata semantics and generated equality |
| `metadata/x-review-posts.yaml` | 1–4 | Metadata semantics and generated equality |

## Representative task matrix

| ID | Workflow | Observed assessment |
| --- | --- | --- |
| W01 | x-explain | Useful direct answer; no forced audit, daily quota or invented interval. |
| W02 | x-myth-check | All supplied propositions addressed; original URLs resolved from corpus; no performance promise. |
| W03 | x-format-advisor | Chooses by actual evidence volume; avoids making the 4000-character path a publishing limit; respects confirmed access. |
| W04 | x-publish-checklist | Complete copy and material-specific media plan produced; no invented test; original count and delayed finding are concrete. Did not start creation or ask style questions for review-only request. |
| W05 | x-review-posts | Coverage, actual changes and three usable revisions present; blocked content/rounded counts/cold-start/format causality not overstated. |
| W06 | x-reach-diagnosis | Provides current decision plus discriminators; no label diagnosis, invented lifetime reconstruction, or forced account audit. |
| W07 | x-create-visuals | Actual discovery and helper behavior, no fake provider availability or generation; one-time override did not change default or series. |
| W08 | x-assistant mixed/follow-up | Requested complete introductory copy only; preserves selected Article and unknown date/error examples; no repeated collection or questions. |
| W09 | x-assistant no-match | The unrelated variable did not trigger an X audit. |
| W10 | x-publish-checklist constrained no-tool branch | Completes useful review without invented count or demanding tool installation. |
| W11 | x-review-posts constrained missing-reader branch | Honest coverage; smallest useful substitute rather than a false review. |
| W12 | x-review-posts URL-less screenshot transcription fixture | Evidence not discarded or deduplicated by guessed identity; pixel-inspection coverage remains untested. |

The original draft/post fixtures are fully embedded in the JSON artifact to keep the trials reproducible without relying on their scratch paths. Raw helper JSON is also embedded, including previews and normalized inputs, not just success claims.

## Exact tasks and useful outputs

### W01 — x-explain

**Exact input**

Using the bundled October 29 snapshot, how many times per day should I post on X? Does the third post need a four-hour wait?

**Execution actually performed**

Read standalone workflow and evidence guide; executed the standalone search/get helper for K01-006/K01-032/K01-033 and Q02; answered without requesting a draft/account.

**Answer produced in this review**

There is no daily optimum or four-hour reset established by this author-diversity function. Its 0.625 multiplier applies to the second-ranked candidate from the same author in one scoring call; counts are rebuilt on each call, and a later post can rank first. It changes a score term, not a guaranteed percentage of reach. [Code](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L183-L237)

Publish the third piece when it adds a useful finding or correction. If it repeats the first two, combine the material instead. Choose timing around your readers and your capacity; compare similar pieces at the same age before adopting a schedule. The bundled snapshot does not establish every live request's settings.

**Assessment:** Useful direct answer; no forced audit, daily quota or invented interval.

### W02 — x-myth-check

**Exact input**

Check these against the bundled snapshot: each like earns 0.66 points; each attached picture adds 0.05; my second daily post gets only 62.5% and a four-hour break restores it.

**Execution actually performed**

Split four propositions, grouping the common daily-counter/reset error explicitly; ran search and get for K01-057/K01-060/K01-078 and reused K01-032/K01-033/Q02.

**Answer produced in this review**

| Claim | Verdict and usable correction |
| --- | --- |
| Each like earns 0.66 points | Misread. 0.66 is the Home Mixer public default multiplying predicted like probability; VM Ranker's same-named default is 0.5. It is not a balance credited per actual like. |
| Each picture adds 0.05 | Misread. The term multiplies predicted photo-expansion probability, not attachment count. Use a picture when it supplies readable evidence. |
| Second daily post gets 62.5% | Misread. With the specified VM defaults, the second same-author candidate by score within one call receives 0.625. Publication order and percentage of views do not follow. |
| Four hours restores the weight | Not established by this function. It has no daily counter or four-hour timer. |

[Prediction coefficients](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/params/param.rs#L367-L513) · [VM defaults](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/vm-ranker/params.rs#L3-L155) · [Prediction blending](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L57-L139) · [Author counting](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L183-L237)

Corrected copy: “The public scoring paths combine personalized predictions. Same-author candidates can compete within one scoring call, but these constants do not supply fixed points per like, points per image, or a daily posting schedule.”

**Assessment:** All supplied propositions addressed; original URLs resolved from corpus; no performance promise.

### W03 — x-format-advisor

**Exact input**

I have access to all three formats. For the following complete text, choose a long Post, Article or Thread and give me the packaging. Use the bundled snapshot, not claims about today's deployment.

Twenty clear Chinese invoice scans from one department: A 1.2 was correct on 17/20 and B 2.0 on 19/20. Both received the same files, checked manually. Phone photos were not tested. Check fields before accounting import; this small test does not establish a universal winner.

**Execution actually performed**

Measured exact supplied text with standalone inspect_draft.py; read six-layer comparison entries plus Q44–Q49; selected one self-contained Post.

**Answer produced in this review**

Use one Post. The supplied text is 274 Unicode code points, so there is no editorial need to expand it into a long Post, Article or Thread. This is not a check of X's weighted editor count.

Opening: “On the same 20 clear invoice scans, A 1.2 was correct on 17 and B 2.0 on 19. This small, one-department test excludes phone photos.” Follow with the shared-input/manual-check method and field-verification advice. A single results image can repeat 17/20 and 19/20, tool versions and the sample limits.

An Article becomes useful if you add multiple image-quality groups, field-level errors and reproducible examples. A Thread becomes useful if the material grows into separate questions that each remain understandable alone. Neither change has a demonstrated fixed exposure bonus; the examined final inputs and scoring functions do not establish one. [Inputs](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/inputs.rs#L1-L22) · [Scoring](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L68-L143)

**Assessment:** Chooses by actual evidence volume; avoids making the 4000-character path a publishing limit; respects confirmed access.

### W04 — x-publish-checklist

**Exact input**

Complete fixture embedded in `coverage/workflows.json`.

- Path: `/workspace/scratch/8875c799c753/work/x_skills_eval/draft_case.txt`
- SHA-256: `fde800ae1c73f42894c1a9ba27306ad28cf18a9a9e73b9dc3052873923a696d0`

**Execution actually performed**

Read complete original fixture, screened all seven topic catalogs, retrieved applicable conditions and related unknowns, measured exact draft following 草稿：. No news/current-product claims required; no image files supplied. Native image-generation tool discovered but not called.

**Answer produced in this review**

先把结果移到开头，合并重复的操作记录，并把结果图排在第一张。原开头“这次我们对两款 OCR 工具作了一次测试，整理了测试过程和结果。”只交代做过测试，没有告诉读者得到什么。

原稿去除首尾空白后实测 4,788 个 Unicode 码点，原始字符串为 4,789；含标点、空格和内部换行，不是 X 编辑器的加权计数。“测试结果”从原始字符串第 4,709 个码点开始，前面重复了 85 段相同操作记录。这里应删重复，而不是为了凑进 4,000 字符机械裁稿；4,000 是所查 V8.2 文本路径的处理边界，不是统一发布上限。[文本路径](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer_v82.py#L33-L50)

完整改稿：

同一批 20 份已脱敏中文发票清晰扫描件，A 1.2 正确识别 17 份，B 2.0 正确识别 19 份。B 在这批样本中多正确 2 份，但不能据此认定它在所有票据场景都更准。

测试时间为 2026-10-28。样本来自同一部门；两款工具输入相同文件，再逐份比对识别文本与原始字段，只记录可复核的错误。

这次没有测试手机照片、模糊或倾斜票据。如果要用于自己的业务，应先拿实际会遇到的票据复测；导入账务前，仍需按字段核对原件。

保留单条 Post 的安排就足以承载这些已知材料；不需要把重复文字搬进 Article。配图顺序建议：①结果对照，17/20 与 19/20、工具版本、同部门清晰扫描件及未测手机照片的限制同屏；②方法与样本范围。真实操作界面和错误对照可作为③④，但目前没有素材，不能伪造界面、错误样例或正确值。若拿不到它们，就用前两张，不硬凑四张。首图前置有独立阅读价值；V8.2 只在一个指定路径选择首个可用媒体，上传图片也不是固定加分。[媒体路径](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer_v82.py#L285-L314) · [预测融合](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L57-L139)

当前环境可原生生成概念配图；这份精确结果图应依据上述数据排版，真实证据面板需要原件。我可以据此继续制作。此处只审稿与给方案，未生成图片、未建立风格档案。

第三篇不必因这段作者多样性代码固定等四小时。它按一次评分中的候选次序计数。若前两篇已讲过同一结果，应合并；若本篇提供新结果或纠正旧结论，可以按读者习惯安排。当前没有前两篇内容，不能替你判定是否重复。[作者计数](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L183-L237)

保留版本、日期和样本边界。补充“正确识别一份”的判定标准；不要宣称未给出的误识别样例。现稿无外链、视频、Thread、话题标签或已知标签，相关具体检查无材料可审；内部推荐状态不可由稿件判断。

**Assessment:** Complete copy and material-specific media plan produced; no invented test; original count and delayed finding are concrete. Did not start creation or ask style questions for review-only request.

### W05 — x-review-posts

**Exact input**

Complete fixture embedded in `coverage/workflows.json`.

- Path: `/workspace/scratch/8875c799c753/work/x_skills_eval/posts_case.md`
- SHA-256: `6b317eb580354b1b70f6395b5f836709ef0e7421d956c148b97d5c575446a18b`

**Execution actually performed**

Read supplied fictional record, normalized it anew, ran standalone summary and per-object text measurements; supplied media descriptions were not represented as inspected pixels. Reused observations for requested reach questions.

**Answer produced in this review**

优先改 B 的“又测了一次”，然后让 C 的导出说明能独立读懂；A 保留真实结果与限定，D 暂不评价正文。

这次只分析你给的虚构浏览记录，没有访问 X。5 条记录对应 4 个帖子 URL，A 的置顶卡是重复项。A/B/C/D 在记录时分别发布了 168/6/24/48 小时；公开浏览分别为约 3.2K/280/900/500。A、D 是承载帖计数，不是 Article 页面阅读数。A 正文已提供，但承载帖文案未知；D 只有标题，正文被登录提示挡住。图片只有文字描述，我没有看到原始像素。

A：正文 127 个 Unicode 码点，标题 15 个。首句已经限定同部门、20 份、清晰扫描件，应保留。标题“20 份发票里的 OCR 错误”承诺错误示例，但正文只给总数；可改成“20 份清晰发票扫描件：两款 OCR 的结果与限制”。补真实测试日期与“正确”的标准，不编错误案例。开头可用：“同一部门的 20 份中文发票清晰扫描件，A 1.2 正确 17 份，B 2.0 正确 19 份。两款工具收到相同文件，并逐份人工比对原图；未测手机照片，不能据此选定所有票据的赢家。”描述中的首图已有分母和限定，建议保留；不需要为了数量增加图片。

B：可见转录 73 个码点，包含“链接指向记录 A”的占位描述，不是实际线上链接的长度。首句“今天又测了一次 OCR”承诺新测试，后文却只链接上周材料。先确认是否真有复测；没有就改为：“上周同一批 20 份清晰中文发票扫描件，A 1.2 正确 17 份，B 2.0 正确 19 份。样本来自同一部门，未测手机照片；导入账务前仍应逐字段核对。文章说明了方法与限制。”建议澄清现有 B；编辑不可用时可附更正，不默认再发一条相同导读。将装饰封面改成结果与限定图，这是建议，不是已完成修改。

C：标题文本/说明为 40 个码点。可改：“OCR 识别结果如何导出为表格：这段演示展示导出步骤。背景是上周对同部门 20 份清晰中文发票扫描件的测试，未测手机照片。导入账务前请逐字段核对原件。”视频完整性、实际步骤和截图是否为独立附件都未确认。播放器“0:10”不能证明毫秒级时长；指定视频索引的条件是每个媒体均为合格视频且严格大于 10,000 ms，当前结论只能是未知，不能建议为了曝光硬补时长。[索引条件](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix-rankall-strato/lib/eventProcessing.strato#L403-L417)

D：只测到 8 个码点的标题“更复杂的票据测试”。要判断承诺是否兑现，最小补充是正文与实际图片；不需要重抓整段账号历史。登录提示不证明限流或付费墙。

这些记录不能证明 Article 天生有更多流量，也不能证明账号被限流。A 的七天累计、置顶和两条已报道导读，与 B 的六小时及不同内容不可直接归因到格式；两条导读也未全部给出，B 可能已经包含在两条中。公开浏览不等于独立读者或完读，低浏览不能区分候选召回、排序、已读过滤与标签限制。[浏览定义](https://help.x.com/en/using-x/view-counts) · [候选流程](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/candidate_pipeline/phoenix_candidate_pipeline.rs#L420-L507)

下一篇先把导出教程讲完整，或取得新的实际测试结果。为后续相似主题记录发布后 24 小时和 7 天的同口径指标、置顶/推广/修订情况；分开记录 Article、承载帖和导读。没有历史快照就不回填增长曲线。

**Assessment:** Coverage, actual changes and three usable revisions present; blocked content/rounded counts/cold-start/format causality not overstated.

### W06 — x-reach-diagnosis

**Exact input**

Using the A–D observations already supplied, why does my Article keep getting views after a week while my other Posts have hundreds? Should I switch everything to Articles? Do not browse.

**Execution actually performed**

Reused W05 normalization and helper results; read reach hypotheses and age/metric conditions; did not recollect the account or demand analytics.

**Answer produced in this review**

Keep the next piece in the format its evidence needs; these records do not justify moving everything to Articles. First make C's export tutorial complete or publish genuinely new test material.

A has a rounded 3.2K carrier-post view count at 168 hours, a pin and two reported introductions. B has 280 at 6 hours; C has 900 at 24 hours. This establishes different observed totals, not an Article advantage. The record contains no daily history, so “keeps getting views” remains your report rather than a measured growth series.

| Hypothesis | What the record supports | Missing check and next action |
| --- | --- | --- |
| More time and redistribution | A is older, pinned and promoted | Start recording the same carrier counter at known times and annotate new introductions/reposts. Growth then measures that counter's change, not unique readers. |
| More useful content | A immediately supplies a result and limits; B mostly teases | Make the next comparable Post self-contained, keep one main change and compare the same-age windows. |
| Format effect | Different formats are present | Comparable topics, reader goals, time windows and promotion are absent. Track Article and carrier separately before testing a format effect. |
| Visibility/cold-start differences | No label or internal Home record was supplied | Public counts cannot identify either. Use a dated label/transparency record only if it is actually available; do not assume a hidden label. |

An ordinary candidate age check uses 48 hours, but it is not a sitewide expiry rule. Recent repost candidates and other source paths have distinct conditions; their existence does not identify how A was seen. [Age filter](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/filters/age_filter.rs#L16-L31) · [Repost IDs](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/sources/thunder_source.rs#L103-L113) · [Other source paths](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/candidate_pipeline/for_you_candidate_pipeline.rs#L219-L237)

For the next comparable pieces, capture the actual visible fields at 24 hours and seven days, including pins and promotion. Those intervals are observation choices, not a posting optimum.

**Assessment:** Provides current decision plus discriminators; no label diagnosis, invented lifetime reconstruction, or forced account audit.

### W07 — x-create-visuals

**Exact input**

For this test, use the supplied in-memory preference fixture: series:weekly-code is mixed/native, Blue line art, #102030, one finding per image; the default is separate. Reuse it for the OCR plan, changing only this request's palette to #553388 and #FFFFFF. Do not generate or save anything; show the plan and available production options.

**Execution actually performed**

Inspected actual current tool catalog (native image_gen__imagegen present; Runway tools present but auth/provider availability untested). Executed the actual bundled selection() with validated in-memory store and temporary override; no preference filesystem write. Ran first-read CLI against an absent private test path and checked that it stayed absent.

**Answer produced in this review**

The weekly-code series resolves to blue line art with one finding per image. For this request only, use purple #553388 and white #FFFFFF; the series and default remain unchanged.

I can generate conceptual images natively here. The precise 17/20 versus 19/20 comparison should be rendered from those exact values; real UI or error panels require supplied source material. Runway tools are exposed, but I have not checked an authenticated workspace or model availability, so I am not promising that provider.

Production brief, not generated images:

1. Results card: “20 clear Chinese invoice scans · one department”; A 1.2: 17/20; B 2.0: 19/20; “Phone photos not tested · not a universal winner.” Keep equal axes and denominators. Alt text: “In a 20-invoice clear-scan sample from one department, A 1.2 was correct on 17 invoices and B 2.0 on 19; phone photos were not tested.”
2. Method card: same files → each tool → manual comparison against originals → field check before accounting import. Alt text: “Both OCR tools received the same files; their output was checked manually against the originals, and accounting import still requires field verification.”

No image was generated and no preference was saved. The helper returned temporary_override=true; the entire fixture store was unchanged. A first read of an absent private test path returned profile=null and did not create a file.

**Assessment:** Actual discovery and helper behavior, no fake provider availability or generation; one-time override did not change default or series.

### W08 — x-assistant mixed/follow-up

**Exact input**

Continue the A–D review. Keep A as an Article. Now rewrite only its introductory Post in Chinese: give the established findings, unknowns and recommended action. Do not repeat the audit.

**Execution actually performed**

Applied follow-up combination; retained A's material and explicit Article decision. No format reselection, recollection, native invocation or repeated questions.

**Answer produced in this review**

同一部门的 20 份清晰中文发票扫描件，A 1.2 正确 17 份，B 2.0 正确 19 份。两款工具输入相同文件，再人工逐份比对原图。

这只能说明本次样本的结果：没有测试手机照片，也不能据此判定所有票据都应选 B。若用于你的业务，先用真实会遇到的票据复测；导入账务前仍要逐字段核对。

Article 里保留了这次测试的方法与范围，供你判断结果是否适用于自己的场景。

**Assessment:** Requested complete introductory copy only; preserves selected Article and unknown date/error examples; no repeated collection or questions.

### W09 — x-assistant no-match

**Exact input**

Solve 2x + 3 = 9.

**Execution actually performed**

Applied router's unrelated-x boundary; no specialist selected and no corpus lookup for this prompt.

**Answer produced in this review**

x = 3.

**Assessment:** The unrelated variable did not trigger an X audit.

### W10 — x-publish-checklist constrained no-tool branch

**Exact input**

Review only this excerpt. For this trial do not use a browser, Python, any counter or storage: “AI OCR is unbeatable. In 20 clear Chinese invoice scans from one department, A 1.2 got 17 right and B 2.0 got 19 right. Phone photos were not tested.”

**Execution actually performed**

Manually executed no-counter/no-browser/no-storage fallback using supplied text and already-read workflow; deliberately did not report an exact length. This is a constrained execution, not a claim that the current host actually lacks tools.

**Answer produced in this review**

Replace “AI OCR is unbeatable”: it promises more than the small test establishes. A usable opening is: “In one department's 20 clear Chinese invoice scans, A 1.2 was correct on 17 and B 2.0 on 19. Phone photos were not tested, so this is a result for that sample, not a universal winner.”

A single Post suits this one finding. One result card would help comparison: show both fractions, the versions, the common denominator and the clear-scan/one-department limits together. This is a proposed image; none was inspected or created.

The excerpt's length is unmeasured because this trial excludes reliable counters. Add the real test date and correctness criterion when available. No account data, full draft or media was supplied, so I cannot assess the rest of the text, actual image fidelity or reach causes.

**Assessment:** Completes useful review without invented count or demanding tool installation.

### W11 — x-review-posts constrained missing-reader branch

**Exact input**

Review https://x.com/example_creator/status/1900000000000000004. For this trial do not open the URL, use search or log in; no text or screenshots are supplied.

**Execution actually performed**

Executed missing-reading-evidence branch without accessing fictional URL or session; did not substitute a snippet.

**Answer produced in this review**

I cannot assess that post's opening, evidence or images from the URL alone under this trial's reading restriction. Supply the visible text and first image, or a saved view showing them; for an Article, include its body or the section you want reviewed. A single post is enough—I do not need the account's whole history. No content review or reach diagnosis has been completed yet.

**Assessment:** Honest coverage; smallest useful substitute rather than a false review.

### W12 — x-review-posts URL-less screenshot transcription fixture

**Exact input**

```json
[
  {
    "url": null,
    "source_method": "user_screenshot",
    "text": "Visible opening",
    "body_status": "partial",
    "metrics": {
      "views": "3K"
    }
  },
  {
    "source_method": "user_screenshot",
    "text": "Another crop",
    "metrics": {
      "views": null
    }
  }
]
```

**Execution actually performed**

Replayed the two supplied test transcriptions through actual standalone summarize_posts.py. No screenshot pixels were supplied or inspected.

**Answer produced in this review**

Both transcribed observations were retained, under separate provisional row IDs. Neither establishes a confirmed post identity: unique_posts=0, unique_content_items=0, unresolved_identity_records=2. “3K” remained rounded rather than exact; the other view count, ages and unseen media remained unknown. The crops cannot be counted as two distinct posts or merged as one without further identity evidence.

**Assessment:** Evidence not discarded or deduplicated by guessed identity; pixel-inspection coverage remains untested.

## Cross-topic applicability and format ledger

The draft and published-content trials screened all topic catalogs, then applied the relevant entries to actual supplied material. This ledger summarizes the substantive review rather than repeating every rule title.

| Topic | Actual evidence and action | Unavailable or inapplicable parts |
| --- | --- | --- |
| 00 Evidence limits | Used snapshot/revision; separated proposed copy, fixture observations and code. | No live production mapping or exposure score. |
| 01 Frequency, author diversity, predictions | Four-hour claim corrected with K01-006/032/033. Picture/like claims corrected with K01-057/060/078. | No actual candidate pool or live request parameters; no universal schedule. |
| 02 Reader task and payoff | Actual generic draft opening and B's teaser changed; 85 repeated paragraphs removed (K02-004/037). | No reader-history or dwell records; no claim that the new hook raises a predicted score. |
| 03 Format/text/media | W03 compares one finding against Article/Thread navigation. W04 measures delayed result and plans first-image conditions. W05 keeps A body separate from missing carrier copy and C duration unknown. | No source image pixels, video playback or Article-page metrics. Relevant missing media remains missing, not absent. |
| 04 Repetition, links, age, corrections | B's retest claim clarified instead of another identical introduction. Old-post paths explained only as possible mechanisms. | No destination URL beyond a record placeholder, no labeled URL state, no actual repost candidate data. |
| 05 Methods, title promises, comparisons, labels | Retained 20 samples, versions and conditions; requested actual correctness criterion/date where missing; refused Article winner or suppression verdict. | No account label report, private analytics, reader timezone or historical growth snapshots. No hashtag/video rules invented for the image-only draft. |
| 06 Unresolved questions | Q02/Q08/Q09/Q17/Q23/Q24/Q25/Q26/Q27/Q44–Q49 constrain the answers. | Unknown deployment, internal states and format causality remain unknown while practical editing proceeds. |

Format-selection evidence was evaluated in the six required layers: object/content identity (K03-007), V8.2 representation (K03-009/010/070), V5 representation (K03-020), behavior/event records (K03-031), examined candidates/scoring (K03-039/041), and visibility (K03-045). The reader-facing recommendation was still based on the supplied single finding; it did not dump implementation detail or claim that a missing explicit multiplier proves identical distribution.

## Exact helper execution summary

Commands used the generated installed-skill copies, not replacement functions:

- `python3 skills/x-explain/scripts/knowledge.py catalog`; topic catalogs 00–06 via `skills/x-assistant/scripts/knowledge.py catalog --topic NN`.
- `python3 skills/x-explain/scripts/knowledge.py search 'daily second post 0.625 four hour reset' --limit 5` returned K01-006 first.
- `python3 skills/x-myth-check/scripts/knowledge.py search 'likes 0.66 photo expand 0.03 image upload' --limit 5` returned Q04/K01-028/K01-031/K01-002/K01-078. The imperfect lexical order was not treated as truth: the catalog and `get` were used to select the actual relevant entries.
- `knowledge.py get` ran in batches of up to three IDs for the 43 full claims and 18 unknown entries listed in JSON.
- `python3 skills/x-publish-checklist/scripts/inspect_draft.py --text /dev/stdin` received exactly the portion following `草稿：\n` in the original fixture. Exit 0; raw=4789; trimmed=4788; after_4000=788. Independent string location found `测试结果：` at one-based raw position 4709 and 85 `操作记录：` paragraphs.
- `python3 skills/x-format-advisor/scripts/inspect_draft.py --text /dev/stdin` received W03's complete 274-code-point English material; exit 0; after_4000=0.
- `python3 skills/x-review-posts/scripts/summarize_posts.py --input /dev/stdin` received the fresh five-record normalization embedded in JSON. Exit 0; 4 unique_posts; 4 content identities; 1 duplicate; no invalid rows; ages 168/6/24/48. Sparse pin did not erase A's likes=21 or supplied Article body coverage.
- `inspect_draft.py` measured A body/title=127/15, B transcription=73, C caption=40, D title=8. Every count scope is explicit; B includes its supplied placeholder, not a fetched destination URL.
- Actual `inspect_video_gate([{'type':'video','duration_ms':None}], False)` returned `status='unknown'` for C, not a pass from player text 0:10.
- Actual `visual_preferences.selection(...)` used revision 7, series:weekly-code and a temporary purple/white override; `store_unchanged=true`.
- `python3 skills/x-create-visuals/scripts/visual_preferences.py --file /tmp/for-you-workflow-review-no-write/visual-preferences.json show --scope default` returned revision 0, profile null; the file remained absent.
- From cwd=/, `python3 /workspace/scratch/8875c799c753/for-you-skills/skills/<each-name>/scripts/knowledge.py get K01-033` succeeded for all eight skills with the same original code URL.

No no-tool branch is mislabeled as a real host outage. W10/W11 intentionally constrain available operations; the other cases use actual Python helpers and current tool discovery. No external CLI install was performed in this review.

## Remaining acceptance limits

Native model discovery and invocation, live authorized X reading, screenshot pixel inspection, image generation/correction/delivery, paid-provider authentication and durable preference writes are **not established** here. These are explicit test limits, not defects inferred from absent execution. README and compatibility wording already distinguish installation from model/browser behavior; it would be incorrect to turn these fresh helper results into a broader compatibility claim.
