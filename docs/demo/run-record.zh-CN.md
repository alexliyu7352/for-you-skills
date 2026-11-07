# For You Skills 演示运行记录

当前影片入口：[中文版](https://youtu.be/TQfDplGaFXY?si=mNGTutX1lj7Py08r) · [English](https://youtu.be/QSL0kNQvs_E?si=VXDbXhogFb7bq7ip)。视频与 GIF 已从 Git 历史移除；下文文件名及制作状态是原始运行档案，不代表这些媒体仍可从仓库下载。见历史清理说明。

本页存档 2026-11-04 的制作记录、两次完整提问与回答、固定版本代码摘录及审稿核验结果。文中的访问结果和完成状态对应当次执行。执行环境的绝对路径已缩成文件名。

归档范围：本页收录最终导读稿、三轮阅读评审结果和下方核验记录。历史输出及文件清单描述的是原执行环境；其中列出的 v1/v2 中间稿和逐轮读者输入包，没有逐份收录到本仓库，也不是本页旁可下载的独立文件。

[观看演示](README.md) · [审稿逐项记录](review-ledger.json) · [项目说明](../../README.zh-CN.md)

---

# For You Skills 推广素材制作记录

制作日期：2026-11-04。项目版本：3f299df8f22e089716fbad2a4721c9ff0a1c5fbe。

## 这套素材展示什么

主卖点是 X.com / Twitter 运营问答：使用内置知识库定位结论，直接读取对应推荐代码，说明能做什么、依据是什么、还有什么不能确定。发布前审稿是第二个实际案例。

- 视频：for-you-skills-demo-zh.mp4，78 秒，1920×1080，24 fps，H.264，无音轨；主要信息直接呈现在画面上。
- 中文封面：for-you-skills-cover-zh.png。
- 英文封面：for-you-skills-cover-en.png。
- 运营问答对照图：for-you-skills-qa-card-zh.png。
- 中文、英文发布文案：promo-copy.zh-CN.md、promo-copy.en.md。
- 可选字幕：captions.zh-CN.srt。

## 真实性与范围

1. 两次输出实际使用已安装的 x-assistant 与它路由到的工作流。输入、完整输出、知识条目、固定版本代码摘录和原始测量保留在本文件后半部分。
2. 问答执行者通过 Git 对象读取固定提交；制作主代理另外在浏览器实际打开同一 GitHub 页面，并取得公开源码可见区域截图。视频中的源码画面来自该截图。
3. 影片是对真实结果的摘录、排版与剪辑回放，不是实时客户端操作、模型生成或安装录屏。环境没有桌面版 Claude/Codex 客户端，云浏览器也不允许打开本地演示文件，因此成片采用离线排版渲染。没有把这项限制包装成完成了客户端录屏。
4. 本次没有重新执行 npx 安装。末尾命令是供观众使用的安装入口，不是安装成功日志。
5. 代码固定在 5ed796374ea48ee26058aab66ab10c266bea2bef，知识研究截至 2026-10-29，并含后续修正。不宣称核验了全部当前线上配置。
6. 0.9、0.8、0.7 的分数是明确标记的示意算术。3K 曝光来自作者提供的个人观察，没有后台截图，不是技能效果、对照实验或已核实的独立读者数。
7. 示例导读最终 546 Unicode码点（去首尾空白），原始文件含末尾换行 547。独立阅读共 3 轮，最终 v3 PASS；仅涵盖正文可读性，不等于事实、图片或曝光验证。
8. 字体采用 Noto Sans CJK；成片已经完整解码检查、检查各幕静帧和文字边界。没有发布到 X.com、提交推广帖或修改仓库。

## 时间轴

| 时间 | 内容 |
| --- | --- |
| 00:00–00:06 | 提问：每天第二篇是否曝光打六折 |
| 00:06–00:15 | 实际回答：可以发，说明建议条件 |
| 00:15–00:26 | 对照固定提交中的作者计数函数 |
| 00:26–00:39 | 用具体算例解释分数倍率与曝光的区别 |
| 00:39–00:47 | 给出行动建议并列明未知 |
| 00:47–00:57 | 作者 Article 曝光观察作为审稿输入 |
| 00:57–01:07 | 展示最终改稿的格式选择部分 |
| 01:07–01:18 | 其他可问主题、安装总路由和仓库入口 |

## 原始运营问答输入

有人说每天发第二篇帖子，曝光就打六折。我今天已经发过一篇，现在有一条不同主题的新内容，到底能不能发？请对照 X.com 推荐代码解释；告诉我该怎么做、为什么，以及代码不能确定什么。

## 原始运营问答输出

**可以发。** 如果这条新内容确实回答了另一个问题，而且已经准备好，就不必因为“今天发过一篇”而强制等到明天。是否现在发，按内容时效、读者是否需要、你是否有余力回应来决定。这是编辑建议；代码没有给出一个保证曝光的发布时间。

“每天第二篇帖子，曝光就打六折”是把两个不同的计数对象混在了一起。已核对的公开代码，计算的是**同一次排序中，同一作者的候选帖子按分数排列后的次序**；没有按当天的发布顺序计数。[作者计数与倍率函数](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L183-L237)

代码中的“候选”，就是系统这次正在考虑给某位读者展示的帖子。只有你的多条帖子同时进入这次计算，才会在这个函数里一起按作者计数。`author_pool_counts` 先按传入分数从高到低排序，再为每位作者从 0 开始计数；每次调用都新建计数表。这里没有“今天已发几篇”、跨天累积或“四小时后恢复”的计时器。新帖如果在你的候选里分数最高，就是第一个；另一位读者的候选里如果只有这条新帖，它也可以是第一个。[代码 L187–204](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L187-L204)

在这个历史版本的 VM Ranker 公开默认值下，开关为开，衰减参数是 0.5，下限是 0.25，倍率为 `0.75 × 0.5^k + 0.25`。因此，同一作者在本次计算中按分数排第一、第二、第三的候选，倍率分别是 1、0.625、0.4375。**0.625 是这个排序步骤的倍率，不是曝光保留 62.5%，也不是“每天第二篇剩六成曝光”。** [参数默认值](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/vm-ranker/params.rs#L169-L197)；[倍率计算](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L183-L204)；[应用到排序分数的路径](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L282-L327)

举一个纯示意例子：忽略其他调整，若你的两条候选在这一步的输入分数分别为 0.9、0.8，另一位作者的一条为 0.7，应用作者倍率后可分别变成 0.9、0.5、0.7。第二条可能排到另一位作者之后，但这个例子算不出它会少多少曝光。你的新帖也可能是分数为 0.9 的那条；发布时间不决定谁先乘 1。此例是按上述函数做的算术说明，不是账户实验结果。

你今天可以这样做：

- 新帖开头直接说明这个新主题解决什么问题，让没有看过上一条的人也能理解。
- 如果有时效，现在发；如果没有时效，就按你已知的读者活跃习惯安排。没有读者数据时，也不用凭空设置“四小时恢复期”。
- 不把“不同主题”当成绕过作者倍率的办法：这个计数函数读取作者 ID 与排序分数，不读取主题；不同主题能给读者新增价值，是内容理由。[计数输入](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L187-L204)

代码不能确定你这条实际会进哪些读者的候选集合、走哪条服务路径、使用什么参数，也不能保证它不与上一条竞争，更不能承诺曝光不降。在同一提交里，Home Mixer 的本地权重明确关闭作者多样性，而 VM Ranker 从请求参数读取开关和数值，所以也不能把一组默认值当成所有请求的实际设置。[本地路径](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/scorers/value_model.rs#L45-L49)；[VM 参数读取](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/vm-ranker/scoring/value_model.rs#L71-L118)

证据范围：本次直接读取了固定提交 `5ed796374ea48ee26058aab66ab10c266bea2bef` 的 Git 原始文件，知识库研究截止于 2026-10-29。它足以指出这个“每天第二篇六折”解释不符合该函数；不能证明截至 2026-11-04 的全部线上配置或排除其他频率相关机制。在线源码页面本次未能打开，固定版本代码摘录与来源已另存，未把网页访问失败写成线上核验成功。


## 原始审稿请求

请使用 x-assistant 审查并把下面这段真实提问改成可以发到 X.com 的简体中文导读 Post。读者是想知道长文该发 Post 还是 Article 的创作者。需要：能直接使用的开头和完整短稿，格式建议，具体首图内容，明确区分能确定与不能确定的结论，每条算法判断附原始代码出处。素材只有作者的以下观察，没有后台分析截图，没有配图，也没有其他账户数据。不能把观察改成实验结果，不能编造曝光提升，不能假定研究文章涵盖未经核对的结论。可使用已知的研究文链接作为进一步阅读：https://blog.go5.si/posts/zh/x-algorithm-teardown/ 。保留作者提问的直接语气，不要写空泛的推广语言。

用户原文：
問題是我的一個article已經發了一周了, 每天還有新的曝光, 總曝光超過3K了, 我其他的post最多也就幾百.這是什麼原因?


## 完整审稿输出

建议发成**单条导读长 Post**：保留原来的提问和数字，先交代这些数字还不能说明什么，再给创作者一个选格式的方法。现有材料只有一组个人观察，不足以写成“Article 更容易获得长尾曝光”的结论。

原文没有独立标题，开头是：“問題是我的一個article已經發了一周了, 每天還有新的曝光, 總曝光超過3K了, 我其他的post最多也就幾百.這是什麼原因?” 这个问题具体，值得保留；需要补的是指标边界、读者的格式决策，以及下一步怎样比较。以下完整稿的第一段可直接作开头。

```text
我的一篇 Article 发了一周，每天还有新曝光，总曝光超过 3K（3000）；其他 Post 最多也就几百。这是为什么？长文就该改发 Article 吗？

这里的“曝光”沿用我的说法，后台到底统计哪种浏览、是否重复计数，还没有核对，不能把“超过 3000”直接当成超过 3000 位读者。各篇统计了多久、主题是否相近、有没有额外推广，也都需要核对。只凭这组个人观察，还不能确定差距是不是格式造成的，更不知道新增曝光从哪里来。

我的建议是先按阅读需要选：一个问题几段就能讲清，用一条 Post 把观点和解释连着读完；材料需要多节内容和图表，就按章节整理成 Article，让每节回答一个小问题，方便以后查阅。这是编辑建议，不是承诺哪种曝光更高。

若要比较表现，可以把多篇相近内容发布后 7 天的数据放在一起，避免一篇累计一周、另一篇只累计一天。如果参与比较的某篇 Article 还有介绍并链接该文的 Post，就分别记录这篇 Article 和这条 Post 的数字；转发、推广等差异也记下来，没有的数据留空。这样能改善比较，仍不能单凭这些数字认定格式带来了提升。

进一步阅读：
https://blog.go5.si/posts/zh/x-algorithm-teardown/
```

完整稿已实际测量：去首尾空白 **546 个 Unicode 码点**，原始文件含末尾换行 **547**；原文是 **65**。链接与段落换行计入，首 4000 码点预览包含全文。这不是 X 的加权字数，也没有验证账号发布权限；这份稿按单条较长 Post 使用，不声称通过普通短帖的长度限制。4000 只是所查 V8.2 文本处理函数的局部输入边界，不是发布上限或最佳篇幅。[清理、字符截取及常量](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer_v82.py#L33-L50)；[处理 full_text 的调用](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer_v82.py#L165-L167)

格式建议属于编辑判断：

| 形式 | 对这份材料的安排 |
| --- | --- |
| 单条较长 Post | 推荐。观察、限制、格式建议和下一步能连着读，不点链接也有收获。 |
| Article | 等有多节原始材料、截图、方法或逐段代码分析时再考虑；目前没有这些新证据。 |
| Thread | 这次无需拆分。跨条寻找限定条件会增加阅读步骤；没有依据为了所谓固定流量奖励而拆条。 |

代码能支持的边界有两条。第一，这份固定快照的最终输入与融合函数没有显式 Article 格式奖励项；这不能反过来证明两种格式在上游模型、候选来源和全部线上实验中完全相同。[最终输入](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/inputs.rs#L1-L22)；[预测融合函数](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L68-L143)

第二，普通候选 AgeFilter 的 48 小时检查，读取当前候选自己的 ID；成功解出年龄且不超过上限才通过，年龄缺失也不通过。这是特定路径的资格检查。顶层 For You 另有 PushToHome 等来源，不能把该检查改写成全站帖子的到期日，也不能据此认定你的 Article 有专属长期推荐机制。[48 小时常量](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/params/config.rs#L38-L43)；[完整年龄判定](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/filters/age_filter.rs#L16-L31)；[顶层来源与过滤列表](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/candidate_pipeline/for_you_candidate_pipeline.rs#L219-L237)

具体首图建议做一张信息卡，不做柱状图或模拟后台截图：

- 标题：**长文选 Post 还是 Article？**
- 左栏：**Post：一个问题，几段讲清**。右栏：**Article：多节内容、图表、反复查阅**。
- 页脚：**一篇 Article 一周后仍有新曝光、累计超过 3K；其他 Post 最多几百。作者个人观察，尚不能确认差距由格式造成。**

这张图的用途是让读者保存选择标准；没有配图素材可供检查。这里可以原生生成图稿，之后若制作可直接采用上述文案，并检查手机尺寸下的字和数字；本次按要求只交方案，没有生成图片。代码层面，V8.2 在纯图片媒体列表里遇到首个可用图片就返回，因此把主结论放首图有明确的局部输入依据；不能推广成所有模型只读首图。[媒体选择函数](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer_v82.py#L285-L314) 图片展开是一个预测加权项，不是每上传一张图就获得固定分数或曝光。[预测含义说明与 photo_expand 融合](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L28-L102)

仍缺的是原帖与 Article 的实际链接、后台指标定义、各条发布和截数时间，以及转发或推广记录。因此没有计算提升比例、完读率或独立读者数，也没有诊断账号受限。稿中的 7 天取自这次“一周后仍增长”的问题，用于统一累计时长；它不是算法推荐的最佳周期。将来若证据改变结论，应在原帖说明更正并给出可独立理解的更新。

研究文链接只保留为用户提供的“进一步阅读”入口。本次未能打开当前页面，未核验内容或完整重定向链；没有替它承诺某个具体结论。发布前仍需确认该链接可访问。正文没有新闻、视频、标签、置顶或回复链材料，相应专项判断不适用；未提供的账号标签与内部模型状态保留为未知。

所有代码判断限定于提交 `5ed796374ea48ee26058aab66ab10c266bea2bef`；知识研究截止于 2026-10-29，并查阅了 2026-10-31 的修正。它们不是截至 2026-11-04 的最新生产配置证明。完整的主题适用性、六层格式检查和逐项原始链接保存在 `review-ledger.json`。

独立阅读记录：由没有继承写作上下文的新读者完成 **3 轮**，最终 **v3 通过**，停顿日志为空。第 1 轮指出指标解释、格式理由和导读含义三处问题，已补齐；第 2 轮确认这些修复，但指出新出现的“这篇 Article”指代不明，现已在同句明确为“参与比较的某篇 Article”。第 3 轮对这份完整最终稿通过评审，之后未再改正文。该结果只涵盖正文可读性，不是事实或曝光验证；图片没有制作，也不在评审范围内。原始测量、全部稿件和逐轮评审记录均保留。


## 原始代码摘录

# 实际核对的固定版本源码摘录

核对日期：2026-11-04。来源是本地 Git 对象中固定提交的原始文件；不是网页摘要，也不代表当前线上配置。

`git rev-parse --verify` 已确认提交存在：`5ed796374ea48ee26058aab66ab10c266bea2bef`。

## xai-value-model/scoring.rs：183–237

[原始代码](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L183-L237)

```rust
183: pub fn diversity_multiplier(decay_factor: f64, floor: f64, exponent: f64) -> f64 {
184:     (1.0 - floor) * decay_factor.powf(exponent) + floor
185: }
186:
187: pub fn author_pool_counts(author_ids: &[u64], ordering_scores: &[f64]) -> Vec<u32> {
188:     let mut indexed: Vec<(usize, f64)> = ordering_scores
189:         .iter()
190:         .enumerate()
191:         .map(|(i, &s)| (i, s))
192:         .collect();
193:     indexed.sort_by(|(_, a), (_, b)| b.partial_cmp(a).unwrap_or(Ordering::Equal));
194:
195:     let mut counts = vec![0u32; author_ids.len()];
196:     let mut author_counts: FxHashMap<u64, u32> = FxHashMap::default();
197:     for (idx, _) in indexed {
198:         let author_id = author_ids[idx];
199:         let k = author_counts.get(&author_id).copied().unwrap_or(0);
200:         counts[idx] = k;
201:         author_counts.insert(author_id, k + 1);
202:     }
203:     counts
204: }
205:
206: fn oon_applies(weights: &ValueModelWeights, candidate: &CandidateScoringInputs) -> bool {
207:     match candidate.in_network {
208:         Some(false) => true,
209:         Some(true) => {
210:             weights.oon_rescore_in_network_replies_retweets
211:                 && (candidate.is_reply || candidate.is_retweet)
212:         }
213:         None => false,
214:     }
215: }
216:
217: pub fn post_fusion_multipliers(
218:     weights: &ValueModelWeights,
219:     ctx: &QueryScoringContext,
220:     candidates: &[CandidateScoringInputs],
221:     ordering_scores: &[f64],
222: ) -> Vec<PostFusionMultiplier> {
223:     let author_diversity: Vec<f64> = if weights.enable_author_diversity {
224:         let author_ids: Vec<u64> = candidates.iter().map(|c| c.author_id).collect();
225:         author_pool_counts(&author_ids, ordering_scores)
226:             .into_iter()
227:             .map(|k| {
228:                 diversity_multiplier(
229:                     weights.author_diversity_decay,
230:                     weights.author_diversity_floor,
231:                     f64::from(k),
232:                 )
233:             })
234:             .collect()
235:     } else {
236:         vec![1.0; candidates.len()]
237:     };
```

## xai-value-model/scoring.rs：282–327

[原始代码](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L282-L327)

```rust
282: pub fn compute_value_scores_with_adjustment<F>(
283:     weights: &ValueModelWeights,
284:     ctx: &QueryScoringContext,
285:     candidates: &[CandidateScoringInputs],
286:     adjust_base_scores: F,
287: ) -> ValueScores
288: where
289:     F: FnOnce(&[f64]) -> Vec<f64>,
290: {
291:     let weighted: Vec<f64> = candidates
292:         .iter()
293:         .map(|c| match c.weighted_score {
294:             Some(weighted) => weighted,
295:             None => offset_score(compute_weighted_score(weights, c), weights),
296:         })
297:         .collect();
298:
299:     if weights.multiplier_pre_offset {
300:         let multipliers = post_fusion_multipliers(weights, ctx, candidates, &weighted);
301:         let pre_offset_scaled: Vec<f64> = weighted
302:             .iter()
303:             .zip(candidates)
304:             .zip(&multipliers)
305:             .map(|((&weighted, c), m)| {
306:                 let net = unoffset_score(weighted, weights) + c.author_exploration_bonus;
307:                 let scaled = if net >= 0.0 { m.combined() * net } else { net };
308:                 offset_score(scaled, weights)
309:             })
310:             .collect();
311:         let scores = adjust_base_scores(&pre_offset_scaled);
312:         return ValueScores { weighted, scores };
313:     }
314:
315:     let base: Vec<f64> = weighted
316:         .iter()
317:         .zip(candidates)
318:         .map(|(&w, c)| add_exploration_bonus(w, c.author_exploration_bonus, weights))
319:         .collect();
320:     let adjusted = adjust_base_scores(&base);
321:     let multipliers = post_fusion_multipliers(weights, ctx, candidates, &adjusted);
322:     let scores = adjusted
323:         .iter()
324:         .zip(&multipliers)
325:         .map(|(&s, m)| m.apply(s))
326:         .collect();
327:     ValueScores { weighted, scores }
```

## vm-ranker/params.rs：169–197

[原始代码](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/vm-ranker/params.rs#L169-L197)

```rust
169: param!(
170:     EnableAuthorDiversity,
171:     bool,
172:     "rust_home_mixer_enable_author_diversity",
173:     true
174: );
175: param!(
176:     AuthorDiversityDecay,
177:     f64,
178:     "rust_home_mixer_author_diversity_decay",
179:     0.5
180: );
181: param!(
182:     AuthorDiversityFloor,
183:     f64,
184:     "rust_home_mixer_author_diversity_floor",
185:     0.25
186: );
187: param!(
188:     EnableOonRescoreForInNetworkRepliesRetweets,
189:     bool,
190:     "rust_home_mixer_enable_oon_rescore_for_in_network_replies_retweets",
191:     true
192: );
193: param!(
194:     MultiplierPreOffset,
195:     bool,
196:     "rust_home_mixer_multiplier_pre_offset",
197:     false
```

## vm-ranker/scoring/value_model.rs：71–118

[原始代码](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/vm-ranker/scoring/value_model.rs#L71-L118)

```rust
71: pub fn weights_from_params(params: &Params, viewer_id: u64) -> ValueModelWeights {
72:     ValueModelWeights {
73:         favorite: params.get(FavoriteWeight),
74:         reply: params.get(ReplyWeight),
75:         retweet: params.get(RetweetWeight),
76:         photo_expand: params.get(PhotoExpandWeight),
77:         video_open: params.get(VideoOpenWeight),
78:         click: params.get(ClickWeight),
79:         open_link: params.get(OpenLinkWeight),
80:         profile_click: params.get(ProfileClickWeight),
81:         vqv: params.get(VqvWeight),
82:         share: params.get(ShareWeight),
83:         share_via_dm: params.get(ShareViaDmWeight),
84:         share_via_copy_link: params.get(ShareViaCopyLinkWeight),
85:         dwell: params.get(DwellWeight),
86:         quote: params.get(QuoteWeight),
87:         quoted_click: params.get(QuotedClickWeight),
88:         quoted_vqv: params.get(QuotedVqvWeight),
89:         follow_author: params.get(FollowAuthorWeight),
90:         post_unexplored: params.get(PostUnexploredWeight),
91:         post_unexplored_include_out_of_network: params.get(PostUnexploredIncludeOutOfNetwork),
92:         react_with_video: params.get(ReactWithVideoWeight),
93:         not_interested: params.get(NotInterestedWeight),
94:         block_author: params.get(BlockAuthorWeight),
95:         mute_author: params.get(MuteAuthorWeight),
96:         report: params.get(ReportWeight),
97:         not_dwelled: params.get(NotDwelledWeight),
98:         cont_dwell_time: params.get(ContDwellTimeWeight),
99:         cont_click_dwell_time: params.get(ContClickDwellTimeWeight),
100:         video_continuation: params.get(VideoContinuationWeight),
101:         user_video_continuation: params.get(UserVideoContinuationWeight),
102:         profile_visit_secs: params.get(ProfileVisitSecsWeight),
103:         min_video_duration_ms: params.get(MinVideoDurationMs),
104:         enable_quoted_vqv_duration_check: params.get(EnableQuotedVqvDurationCheck),
105:         bidirectional_follow_reply_weight_boost: params.get(BidirectionalFollowReplyWeightBoost),
106:         bidirectional_follow_dwell_weight_boost: params.get(BidirectionalFollowDwellWeightBoost),
107:         enable_author_diversity: params.get(EnableAuthorDiversity),
108:         author_diversity_decay: params.get(AuthorDiversityDecay),
109:         author_diversity_floor: params.get(AuthorDiversityFloor),
110:         oon_rescore_in_network_replies_retweets: params
111:             .get(EnableOonRescoreForInNetworkRepliesRetweets),
112:         multiplier_pre_offset: params.get(MultiplierPreOffset),
113:     }
114:     .perturbed(
115:         params.get(WeightPerturbationSigma),
116:         &params.get(WeightPerturbationSalt),
117:         viewer_id,
118:     )
```

## home-mixer/scorers/value_model.rs：8–50

[原始代码](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/scorers/value_model.rs#L8-L50)

```rust
8: pub(crate) fn weights_for(query: &ScoredPostsQuery) -> ValueModelWeights {
9:     let params = &query.params;
10:     ValueModelWeights {
11:         favorite: params.get(FavoriteWeight),
12:         reply: params.get(ReplyWeight),
13:         retweet: params.get(RetweetWeight),
14:         photo_expand: params.get(PhotoExpandWeight),
15:         video_open: params.get(VideoOpenWeight),
16:         click: params.get(ClickWeight),
17:         open_link: params.get(OpenLinkWeight),
18:         profile_click: params.get(ProfileClickWeight),
19:         vqv: params.get(VqvWeight),
20:         share: params.get(ShareWeight),
21:         share_via_dm: params.get(ShareViaDmWeight),
22:         share_via_copy_link: params.get(ShareViaCopyLinkWeight),
23:         dwell: params.get(DwellWeight),
24:         quote: params.get(QuoteWeight),
25:         quoted_click: params.get(QuotedClickWeight),
26:         quoted_vqv: params.get(QuotedVqvWeight),
27:         follow_author: params.get(FollowAuthorWeight),
28:         post_unexplored: params.get(PostUnexploredWeight),
29:         post_unexplored_include_out_of_network: false,
30:         react_with_video: params.get(ReactWithVideoWeight),
31:         not_interested: params.get(NotInterestedWeight),
32:         block_author: params.get(BlockAuthorWeight),
33:         mute_author: params.get(MuteAuthorWeight),
34:         report: params.get(ReportWeight),
35:         not_dwelled: params.get(NotDwelledWeight),
36:         cont_dwell_time: params.get(ContDwellTimeWeight),
37:         cont_click_dwell_time: params.get(ContClickDwellTimeWeight),
38:         video_continuation: 0.0,
39:         user_video_continuation: 0.0,
40:         profile_visit_secs: 0.0,
41:         min_video_duration_ms: params.get(MinVideoDurationMs),
42:         enable_quoted_vqv_duration_check: params.get(EnableQuotedVqvDurationCheck),
43:         bidirectional_follow_reply_weight_boost: params.get(BidirectionalFollowReplyWeightBoost),
44:         bidirectional_follow_dwell_weight_boost: params.get(BidirectionalFollowDwellWeightBoost),
45:         enable_author_diversity: false,
46:         author_diversity_decay: 1.0,
47:         author_diversity_floor: 1.0,
48:         oon_rescore_in_network_replies_retweets: false,
49:         multiplier_pre_offset: false,
50:     }
```


## reader-review-record.json

```json
{
  "mode": "cold",
  "status": "pass",
  "completed_rounds": 3,
  "budget": 3,
  "reviewed_scope": "exact v3 introductory Post including opening, complete body, further-reading label and URL; text only, no media",
  "final_draft": "revised-post-v3.txt",
  "final_sha256": "b74183247bbbe2eb0e0f8b9edca347ec68fa1d6fce18bfe281d1f17dcb2bc487",
  "unresolved_stalls": [],
  "round_results": [
    {
      "round": 1,
      "draft": "revised-post-v1.txt",
      "result": "FAIL",
      "record": "cold-review-v1.json"
    },
    {
      "round": 2,
      "draft": "revised-post-v2.txt",
      "result": "FAIL",
      "record": "cold-review-v2.json"
    },
    {
      "round": 3,
      "draft": "revised-post-v3.txt",
      "result": "PASS",
      "record": "cold-review-v3.json"
    }
  ],
  "limits": "Editorial readability only; no factual verification, account analytics, image inspection or research webpage reading."
}
```


## final-checks.json

```json
{
  "status": "passed",
  "final_draft_version": "v3",
  "trimmed_unicode_code_points": 546,
  "raw_unicode_code_points": 547,
  "raw_sha256": "b74183247bbbe2eb0e0f8b9edca347ec68fa1d6fce18bfe281d1f17dcb2bc487",
  "delivered_text_equals_cold_review_packet": true,
  "delivered_text_equals_reviewed_version": true,
  "complete_copy_embedded_in_review_answer": true,
  "protected_original_unchanged": true,
  "all_indexed_output_files_present": true,
  "all_indexed_json_valid": true,
  "cold_review_status": "pass",
  "completed_cold_rounds": 3,
  "current_production_verification": false,
  "reach_measurement_performed": false,
  "images_created": false,
  "published": false
}
```


## measure-original.json

```json
{
  "source_snapshot": "5ed796374ea48ee26058aab66ab10c266bea2bef",
  "text": {
    "raw_characters": 65,
    "raw_preview_4000": "問題是我的一個article已經發了一周了, 每天還有新的曝光, 總曝光超過3K了, 我其他的post最多也就幾百.這是什麼原因?",
    "characters": 65,
    "preview_4000": "問題是我的一個article已經發了一周了, 每天還有新的曝光, 總曝光超過3K了, 我其他的post最多也就幾百.這是什麼原因?",
    "after_4000_characters": 0,
    "article_title_preview_200": "",
    "normalization": "characters and preview_4000 trim leading/trailing whitespace; raw_characters and raw_preview_4000 preserve the supplied string. Counts are Unicode code points, not grapheme clusters or X weighted-length units.",
    "scope": "Editorial preview of supplied strings, not reconstructed production renderer input; not a publishing limit."
  },
  "video_index_partial_check": {
    "status": "unknown",
    "reason": "No media metadata supplied."
  }
}
```


## measure-final.json

```json
{
  "source_snapshot": "5ed796374ea48ee26058aab66ab10c266bea2bef",
  "text": {
    "raw_characters": 547,
    "raw_preview_4000": "我的一篇 Article 发了一周，每天还有新曝光，总曝光超过 3K（3000）；其他 Post 最多也就几百。这是为什么？长文就该改发 Article 吗？\n\n这里的“曝光”沿用我的说法，后台到底统计哪种浏览、是否重复计数，还没有核对，不能把“超过 3000”直接当成超过 3000 位读者。各篇统计了多久、主题是否相近、有没有额外推广，也都需要核对。只凭这组个人观察，还不能确定差距是不是格式造成的，更不知道新增曝光从哪里来。\n\n我的建议是先按阅读需要选：一个问题几段就能讲清，用一条 Post 把观点和解释连着读完；材料需要多节内容和图表，就按章节整理成 Article，让每节回答一个小问题，方便以后查阅。这是编辑建议，不是承诺哪种曝光更高。\n\n若要比较表现，可以把多篇相近内容发布后 7 天的数据放在一起，避免一篇累计一周、另一篇只累计一天。如果参与比较的某篇 Article 还有介绍并链接该文的 Post，就分别记录这篇 Article 和这条 Post 的数字；转发、推广等差异也记下来，没有的数据留空。这样能改善比较，仍不能单凭这些数字认定格式带来了提升。\n\n进一步阅读：\nhttps://blog.go5.si/posts/zh/x-algorithm-teardown/\n",
    "characters": 546,
    "preview_4000": "我的一篇 Article 发了一周，每天还有新曝光，总曝光超过 3K（3000）；其他 Post 最多也就几百。这是为什么？长文就该改发 Article 吗？\n\n这里的“曝光”沿用我的说法，后台到底统计哪种浏览、是否重复计数，还没有核对，不能把“超过 3000”直接当成超过 3000 位读者。各篇统计了多久、主题是否相近、有没有额外推广，也都需要核对。只凭这组个人观察，还不能确定差距是不是格式造成的，更不知道新增曝光从哪里来。\n\n我的建议是先按阅读需要选：一个问题几段就能讲清，用一条 Post 把观点和解释连着读完；材料需要多节内容和图表，就按章节整理成 Article，让每节回答一个小问题，方便以后查阅。这是编辑建议，不是承诺哪种曝光更高。\n\n若要比较表现，可以把多篇相近内容发布后 7 天的数据放在一起，避免一篇累计一周、另一篇只累计一天。如果参与比较的某篇 Article 还有介绍并链接该文的 Post，就分别记录这篇 Article 和这条 Post 的数字；转发、推广等差异也记下来，没有的数据留空。这样能改善比较，仍不能单凭这些数字认定格式带来了提升。\n\n进一步阅读：\nhttps://blog.go5.si/posts/zh/x-algorithm-teardown/",
    "after_4000_characters": 0,
    "article_title_preview_200": "",
    "normalization": "characters and preview_4000 trim leading/trailing whitespace; raw_characters and raw_preview_4000 preserve the supplied string. Counts are Unicode code points, not grapheme clusters or X weighted-length units.",
    "scope": "Editorial preview of supplied strings, not reconstructed production renderer input; not a publishing limit."
  },
  "video_index_partial_check": {
    "status": "unknown",
    "reason": "No media metadata supplied."
  }
}
```


## qa-arithmetic.json

```json
{
  "type": "illustrative_arithmetic_not_account_measurement",
  "formula": "(1-floor)*decay**k+floor",
  "decay": 0.5,
  "floor": 0.25,
  "k": [
    0,
    1,
    2
  ],
  "multipliers": [
    1.0,
    0.625,
    0.4375
  ],
  "input_scores": [
    0.9,
    0.8,
    0.7
  ],
  "authors": [
    "A",
    "A",
    "B"
  ],
  "output_for_example": [
    0.9,
    0.5,
    0.7
  ]
}
```


## evidence-index.json

```json
{
  "schema_version": 1,
  "analysis_date": "2026-11-04",
  "knowledge_research_cutoff": "2026-10-29",
  "corrections_consulted": "2026-10-31",
  "pinned_commit": "5ed796374ea48ee26058aab66ab10c266bea2bef",
  "current_production_verified": false,
  "private_account_data_collected": false,
  "performed_actions": {
    "A01": "Read installed x-assistant, routing, evidence guide and selected workflows; executed locally, not native specialist invocation.",
    "A02": "Read topic catalogs for applicability and relevant complete knowledge entries plus related unknowns; read documented errata.",
    "A03": "Verified pinned commit exists with git rev-parse and read original source with read-only git show; preserved line-numbered excerpts and full-file SHA-256.",
    "A04": "Attempted web open of pinned source pages and supplied research URL; tool could not fetch them. No latest-production or webpage-content verification claimed.",
    "A05": "Computed illustrative author multipliers using public defaults; no reach measurement or production simulation.",
    "A06": "Wrote complete Simplified Chinese question answer and draft review; preserved user observation as unverified observation.",
    "A07": "Ran supplied inspect_draft.py on exact original, v1, v2 and v3; retained raw JSON outputs and remeasured delivered file.",
    "A08": "Performed author pure read and recorded stall log; three separate fresh-context readers received full self-contained packets. V1 FAIL, V2 FAIL, V3 PASS; no unresolved stalls in exact delivered text.",
    "A09": "Screened all topic scopes and kept relevant rule ledger with actual evidence, verdict, action, explanation and original citations; compared format evidence across six layers.",
    "A10": "Inspected image-generation availability; wrote one-image production brief only. Did not generate images or change preferences.",
    "A11": "Revised only supported readability defects; retained all drafts, packets, verdicts and hashes. No publishing, installation, repository or skill edits."
  },
  "outputs": {
    "qa-answer.md": {
      "knowledge_ids": [
        "K01-006",
        "K01-032",
        "K01-033",
        "K01-024",
        "K01-036",
        "K01-042",
        "K04-022",
        "Q02"
      ],
      "actions": [
        "A01",
        "A02",
        "A03",
        "A04",
        "A05",
        "A06"
      ],
      "code_source_ids": [
        "C01",
        "C02",
        "C03",
        "C04",
        "C05"
      ]
    },
    "review-answer.md": {
      "knowledge_ids": [
        "K03-001",
        "K03-007",
        "K03-009",
        "K03-010",
        "K03-011",
        "K03-020",
        "K03-021",
        "K03-031",
        "K03-033",
        "K03-034",
        "K03-035",
        "K03-039",
        "K03-040",
        "K03-041",
        "K03-043",
        "K03-045",
        "K03-047",
        "K03-048",
        "K04-046",
        "K04-048",
        "K04-055",
        "K03-070",
        "K01-078",
        "K04-085",
        "K02-004",
        "K02-037",
        "K02-038",
        "K03-002",
        "K03-003",
        "K03-057",
        "K03-062",
        "K03-065",
        "K03-066",
        "K03-067",
        "K04-086",
        "K04-088",
        "K05-053",
        "K05-059",
        "K05-106",
        "K05-109",
        "Q44",
        "Q45",
        "Q46",
        "Q47",
        "Q48",
        "Q49",
        "Q24",
        "Q25",
        "Q38",
        "Q40",
        "Q42"
      ],
      "actions": [
        "A01",
        "A02",
        "A03",
        "A04",
        "A06",
        "A07",
        "A08",
        "A09",
        "A10",
        "A11"
      ],
      "code_source_ids": [
        "C06",
        "C07",
        "C08",
        "C09",
        "C10",
        "C11",
        "C12",
        "C13",
        "C14",
        "C15",
        "C16",
        "C17",
        "C18",
        "C19"
      ]
    },
    "revised-post.txt": {
      "knowledge_ids": [
        "K02-004",
        "K03-001",
        "K03-002",
        "K03-003",
        "K03-057",
        "K03-062",
        "K03-065",
        "K03-066",
        "K03-067",
        "Q46",
        "Q49"
      ],
      "actions": [
        "A06",
        "A07",
        "A08",
        "A11"
      ],
      "claim_scope": "User-reported observation plus editorial/methodological guidance; no asserted algorithm mechanism in the copy.",
      "exact_reviewed_version": "v3",
      "unicode_code_points_trimmed": 546,
      "sha256": "b74183247bbbe2eb0e0f8b9edca347ec68fa1d6fce18bfe281d1f17dcb2bc487",
      "code_source_ids": []
    },
    "qa-code-excerpts.md": {
      "knowledge_ids": [
        "K01-006",
        "K01-032",
        "K01-033",
        "K01-024",
        "K01-036",
        "K01-042",
        "K04-022",
        "Q02"
      ],
      "actions": [
        "A03"
      ],
      "code_source_ids": [
        "C01",
        "C02",
        "C03",
        "C04",
        "C05"
      ]
    },
    "qa-code-provenance.json": {
      "knowledge_ids": [
        "K01-006",
        "K01-032",
        "K01-033",
        "K01-024",
        "K01-036",
        "K01-042",
        "K04-022",
        "Q02"
      ],
      "actions": [
        "A03"
      ],
      "code_source_ids": [
        "C01",
        "C02",
        "C03",
        "C04",
        "C05"
      ]
    },
    "qa-arithmetic.json": {
      "knowledge_ids": [
        "K01-032",
        "K01-033"
      ],
      "actions": [
        "A05"
      ],
      "code_source_ids": [
        "C01",
        "C02"
      ]
    },
    "review-code-excerpts.md": {
      "knowledge_ids": [
        "K03-007",
        "K03-009",
        "K03-010",
        "K03-020",
        "K03-021",
        "K03-033",
        "K03-040",
        "K03-041",
        "K03-045",
        "K03-070",
        "K04-046",
        "K04-055"
      ],
      "actions": [
        "A03"
      ],
      "code_source_ids": [
        "C06",
        "C07",
        "C08",
        "C09",
        "C10",
        "C11",
        "C12",
        "C13",
        "C14",
        "C15",
        "C16",
        "C17",
        "C18",
        "C19"
      ]
    },
    "review-code-provenance.json": {
      "knowledge_ids": [
        "K03-041",
        "K04-046",
        "K04-055"
      ],
      "actions": [
        "A03"
      ],
      "code_source_ids": [
        "C06",
        "C07",
        "C08",
        "C09",
        "C10",
        "C11",
        "C12",
        "C13",
        "C14",
        "C15",
        "C16",
        "C17",
        "C18",
        "C19"
      ]
    },
    "review-ledger.json": {
      "knowledge_ids": [
        "K03-001",
        "K03-007",
        "K03-009",
        "K03-010",
        "K03-011",
        "K03-020",
        "K03-021",
        "K03-031",
        "K03-033",
        "K03-034",
        "K03-035",
        "K03-039",
        "K03-040",
        "K03-041",
        "K03-043",
        "K03-045",
        "K03-047",
        "K03-048",
        "K04-046",
        "K04-048",
        "K04-055",
        "K03-070",
        "K01-078",
        "K04-085",
        "K02-004",
        "K02-037",
        "K02-038",
        "K03-002",
        "K03-003",
        "K03-057",
        "K03-062",
        "K03-065",
        "K03-066",
        "K03-067",
        "K04-086",
        "K04-088",
        "K05-053",
        "K05-059",
        "K05-106",
        "K05-109",
        "Q44",
        "Q45",
        "Q46",
        "Q47",
        "Q48",
        "Q49",
        "Q24",
        "Q25",
        "Q38",
        "Q40",
        "Q42"
      ],
      "actions": [
        "A02",
        "A09"
      ],
      "code_source_ids": [
        "C06",
        "C07",
        "C08",
        "C09",
        "C10",
        "C11",
        "C12",
        "C13",
        "C14",
        "C15",
        "C16",
        "C17",
        "C18",
        "C19"
      ]
    },
    "visual-brief.json": {
      "knowledge_ids": [
        "K03-002",
        "K03-003",
        "K03-070",
        "K01-078",
        "Q46",
        "Q47"
      ],
      "actions": [
        "A10"
      ],
      "code_source_ids": [
        "C11",
        "C12",
        "C13",
        "C15"
      ]
    },
    "knowledge-evidence.json": {
      "knowledge_ids": [
        "K01-006",
        "K01-032",
        "K01-033",
        "K01-024",
        "K01-036",
        "K01-042",
        "K04-022",
        "K03-001",
        "K03-007",
        "K03-009",
        "K03-010",
        "K03-011",
        "K03-020",
        "K03-021",
        "K03-031",
        "K03-033",
        "K03-034",
        "K03-035",
        "K03-039",
        "K03-040",
        "K03-041",
        "K03-043",
        "K03-045",
        "K03-047",
        "K03-048",
        "K04-046",
        "K04-048",
        "K04-055",
        "K03-070",
        "K01-078",
        "K04-085",
        "K02-004",
        "K02-037",
        "K02-038",
        "K03-002",
        "K03-003",
        "K03-057",
        "K03-062",
        "K03-065",
        "K03-066",
        "K03-067",
        "K04-086",
        "K04-088",
        "K05-053",
        "K05-059",
        "K05-106",
        "K05-109",
        "Q02",
        "Q44",
        "Q45",
        "Q46",
        "Q47",
        "Q48",
        "Q49",
        "Q24",
        "Q25",
        "Q38",
        "Q40",
        "Q42"
      ],
      "actions": [
        "A02"
      ],
      "code_source_ids": [
        "C01",
        "C02",
        "C03",
        "C04",
        "C05",
        "C06",
        "C07",
        "C08",
        "C09",
        "C10",
        "C11",
        "C12",
        "C13",
        "C14",
        "C15",
        "C16",
        "C17",
        "C18",
        "C19"
      ]
    },
    "workflow-record.json": {
      "knowledge_ids": [
        "K01-006",
        "K01-032",
        "K01-033",
        "K01-024",
        "K01-036",
        "K01-042",
        "K04-022",
        "K03-001",
        "K03-007",
        "K03-009",
        "K03-010",
        "K03-011",
        "K03-020",
        "K03-021",
        "K03-031",
        "K03-033",
        "K03-034",
        "K03-035",
        "K03-039",
        "K03-040",
        "K03-041",
        "K03-043",
        "K03-045",
        "K03-047",
        "K03-048",
        "K04-046",
        "K04-048",
        "K04-055",
        "K03-070",
        "K01-078",
        "K04-085",
        "K02-004",
        "K02-037",
        "K02-038",
        "K03-002",
        "K03-003",
        "K03-057",
        "K03-062",
        "K03-065",
        "K03-066",
        "K03-067",
        "K04-086",
        "K04-088",
        "K05-053",
        "K05-059",
        "K05-106",
        "K05-109",
        "Q02",
        "Q44",
        "Q45",
        "Q46",
        "Q47",
        "Q48",
        "Q49",
        "Q24",
        "Q25",
        "Q38",
        "Q40",
        "Q42"
      ],
      "actions": [
        "A01",
        "A02",
        "A03",
        "A04",
        "A05",
        "A06",
        "A07",
        "A08",
        "A09",
        "A10",
        "A11"
      ],
      "code_source_ids": [
        "C01",
        "C02",
        "C03",
        "C04",
        "C05",
        "C06",
        "C07",
        "C08",
        "C09",
        "C10",
        "C11",
        "C12",
        "C13",
        "C14",
        "C15",
        "C16",
        "C17",
        "C18",
        "C19"
      ]
    },
    "review-change-record.json": {
      "knowledge_ids": [],
      "actions": [
        "A06",
        "A11"
      ],
      "code_source_ids": []
    },
    "author-pure-read-v1.json": {
      "knowledge_ids": [],
      "actions": [
        "A08"
      ],
      "code_source_ids": []
    },
    "measure-original.json": {
      "knowledge_ids": [],
      "actions": [
        "A07"
      ],
      "scope": "Unicode text measurement only, not reach or X weighted-length measurement.",
      "code_source_ids": []
    },
    "measure-final.json": {
      "knowledge_ids": [],
      "actions": [
        "A07"
      ],
      "scope": "Unicode text measurement only, not reach or X weighted-length measurement.",
      "code_source_ids": []
    },
    "measure-v1.json": {
      "knowledge_ids": [],
      "actions": [
        "A07"
      ],
      "scope": "Unicode text measurement only, not reach or X weighted-length measurement.",
      "code_source_ids": []
    },
    "measure-v2.json": {
      "knowledge_ids": [],
      "actions": [
        "A07"
      ],
      "scope": "Unicode text measurement only, not reach or X weighted-length measurement.",
      "code_source_ids": []
    },
    "measure-v3.json": {
      "knowledge_ids": [],
      "actions": [
        "A07"
      ],
      "scope": "Unicode text measurement only, not reach or X weighted-length measurement.",
      "code_source_ids": []
    },
    "revised-post-v1.txt": {
      "knowledge_ids": [],
      "actions": [
        "A08",
        "A11"
      ],
      "status": "written",
      "code_source_ids": []
    },
    "cold-reader-packet-v1.json": {
      "knowledge_ids": [],
      "actions": [
        "A08",
        "A11"
      ],
      "status": "written",
      "code_source_ids": []
    },
    "cold-review-v1.json": {
      "knowledge_ids": [],
      "actions": [
        "A08",
        "A11"
      ],
      "status": "written",
      "code_source_ids": []
    },
    "revised-post-v2.txt": {
      "knowledge_ids": [],
      "actions": [
        "A08",
        "A11"
      ],
      "status": "written",
      "code_source_ids": []
    },
    "cold-reader-packet-v2.json": {
      "knowledge_ids": [],
      "actions": [
        "A08",
        "A11"
      ],
      "status": "written",
      "code_source_ids": []
    },
    "cold-review-v2.json": {
      "knowledge_ids": [],
      "actions": [
        "A08",
        "A11"
      ],
      "status": "written",
      "code_source_ids": []
    },
    "revised-post-v3.txt": {
      "knowledge_ids": [],
      "actions": [
        "A08",
        "A11"
      ],
      "status": "written",
      "code_source_ids": []
    },
    "cold-reader-packet-v3.json": {
      "knowledge_ids": [],
      "actions": [
        "A08",
        "A11"
      ],
      "status": "written",
      "code_source_ids": []
    },
    "cold-review-v3.json": {
      "knowledge_ids": [],
      "actions": [
        "A08",
        "A11"
      ],
      "status": "written",
      "code_source_ids": []
    },
    "reader-review-record.json": {
      "knowledge_ids": [],
      "actions": [
        "A08",
        "A11"
      ],
      "code_source_ids": []
    },
    "final-checks.json": {
      "knowledge_ids": [],
      "code_source_ids": [],
      "actions": [
        "A07",
        "A11"
      ]
    }
  },
  "reader_review": {
    "mode": "cold",
    "status": "pass",
    "completed_rounds": 3,
    "budget": 3,
    "reviewed_scope": "exact v3 introductory Post including opening, complete body, further-reading label and URL; text only, no media",
    "final_draft": "revised-post-v3.txt",
    "final_sha256": "b74183247bbbe2eb0e0f8b9edca347ec68fa1d6fce18bfe281d1f17dcb2bc487",
    "unresolved_stalls": [],
    "round_results": [
      {
        "round": 1,
        "draft": "revised-post-v1.txt",
        "result": "FAIL",
        "record": "cold-review-v1.json"
      },
      {
        "round": 2,
        "draft": "revised-post-v2.txt",
        "result": "FAIL",
        "record": "cold-review-v2.json"
      },
      {
        "round": 3,
        "draft": "revised-post-v3.txt",
        "result": "PASS",
        "record": "cold-review-v3.json"
      }
    ],
    "limits": "Editorial readability only; no factual verification, account analytics, image inspection or research webpage reading."
  },
  "user_supplied_inputs": [
    "request.txt",
    "user-original.txt"
  ],
  "excluded_actions": [
    "publish",
    "account mutations",
    "image creation",
    "installation",
    "repository edit",
    "skill edit"
  ],
  "further_reading_url": "https://blog.go5.si/posts/zh/x-algorithm-teardown/",
  "further_reading_content_verified": false,
  "code_sources": {
    "C01": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L183-L237",
    "C02": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L282-L327",
    "C03": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/vm-ranker/params.rs#L169-L197",
    "C04": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/vm-ranker/scoring/value_model.rs#L71-L118",
    "C05": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/scorers/value_model.rs#L8-L50",
    "C06": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/inputs.rs#L1-L22",
    "C07": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/phoenix_scores.rs#L1-L31",
    "C08": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/params/config.rs#L38-L43",
    "C09": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/filters/age_filter.rs#L1-L37",
    "C10": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/candidate_pipeline/for_you_candidate_pipeline.rs#L219-L237",
    "C11": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer_v82.py#L285-L321",
    "C12": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer_v82.py#L33-L50",
    "C13": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer_v82.py#L140-L184",
    "C14": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer.py#L65-L120",
    "C15": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L68-L143",
    "C16": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/botmaker/scarecrow_features/src/main/java/com/twitter/scarecrow/features/FeaturesOfTweet.java#L255-L263",
    "C17": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/visibility-filtering/rules/tweet_rules.rs#L247-L252",
    "C18": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/visibility-filtering/rules/levels.rs#L215-L256",
    "C19": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/filters/fair_share_ranking_filter.rs#L44-L65"
  }
}
```


## cold-review-v1.json

```json
{
  "result": "FAIL",
  "language": "简体中文",
  "scope": {
    "document": "revised-post-v1.txt",
    "draft_source": "cold-reader-packet-v1.json",
    "reviewed_parts": "packet 中 draft 字段的完整导读 Post，包含所有段落、进一步阅读标签及其 URL；以所提供的换行和段落为准。",
    "media": "未提供媒体；未进行图片检查。",
    "verification_limits": "仅评估首次阅读时的理解连续性及所给三项标准；没有浏览链接、核实平台功能、核实曝光数字或验证统计口径。"
  },
  "read_through": {
    "method": "从首句到末尾 URL 依次阅读；不替原文补充定义或选择格式的依据。",
    "ordered_log": [
      {
        "part": "第一段：个人观察及两个问题",
        "stall_ids": [
          "S1"
        ],
        "note": "比较的对象和提问能辨认；在数字所对应的指标含义及缩写处停顿。"
      },
      {
        "part": "第二段：暂不依据总数换格式及待核对因素",
        "stall_ids": [],
        "note": "“这是”接续上一段的个人观察，“差距”接续 Article 与其他 Post 的数字差异；没有需回找的指代。"
      },
      {
        "part": "第三段：依据阅读需要选择格式",
        "stall_ids": [
          "S2"
        ],
        "note": "建议的行动清楚，但从内容需求到格式选择之间的理由没有写出。"
      },
      {
        "part": "第四段：七天比较、分别记录及因果限制",
        "stall_ids": [
          "S3"
        ],
        "note": "统一为发布后七天的理由由一周与一天的例子说明；读到“导读 Post”时需猜其具体所指。末句对因果结论的限制能接上前文。"
      },
      {
        "part": "进一步阅读标签及 URL",
        "stall_ids": [],
        "note": "标签只提供继续阅读的入口，没有声称链接包含任何特定结论；未打开链接。"
      }
    ]
  },
  "stall_log": [
    {
      "id": "S1",
      "class": "unexplained_term",
      "class_zh": "未解释的术语",
      "offending_sentence": "我的一篇 Article 发了一周，每天还有新曝光，总曝光超过 3K；其他 Post 最多也就几百。",
      "location": "第一段第一句，“曝光”及“3K”的首次出现。",
      "explanation": "全文的比较依赖曝光这个数字，但这里没有说明它在本文中计的是什么，也没有展开 3K。只按包内明确给出的受众知识，读者需要自行把该指标理解为某种显示次数或看过的人数，并自行换算缩写；原文不能让读者确定自己的理解是否正确。",
      "required_fix_or_information": "首次出现时用普通话说明这里沿用的指标及其计数含义，展开 3K 的数量；若涉及次数与人数的区别，给一个简单计数例子。指标口径若尚未核对，应明确这一点，不补造定义。保留原观察的三个事实。"
    },
    {
      "id": "S2",
      "class": "broken_chain",
      "class_zh": "推理链断裂",
      "offending_sentence": "一个问题能在几段话里讲清，就用 Post；需要多节内容、图表和反复查阅，再考虑 Article。",
      "location": "第三段第二句。",
      "explanation": "句子直接把两组阅读需要分别配给 Post 和 Article，但没有说明各自的阅读呈现或组织方式为什么适合这些需要。下一句只说这是按阅读需要选择，没有补出适配理由。认识格式名称的读者仍需自行补上“这些需要为什么支持这个选择”。",
      "required_fix_or_information": "补出读者能理解的选择依据，说明哪些已知的呈现或组织差别会使几段内容或多节内容更便于阅读、查阅；只保留能够支持的具体理由。若这只是作者的使用习惯，应明确它的性质。"
    },
    {
      "id": "S3",
      "class": "unexplained_term",
      "class_zh": "未解释的术语",
      "offending_sentence": "Article 和导读 Post 分开记，转发、推广等差异也记下来；没有的数据就留空。",
      "location": "第四段第二句，“导读 Post”的首次出现。",
      "explanation": "此前的 Post 是与 Article 比较的内容格式，这里突然加入“导读 Post”，没有说明它与 Article 的关系。读者必须猜它是介绍并链接某一篇 Article 的另一条 Post，还是此前参与比较的普通 Post，因而也不能完全确定“分开记”要分开哪两组数据。",
      "required_fix_or_information": "在首次出现时交代导读 Post 是什么、对应哪篇 Article，并明确分别记录的是哪两个内容对象的数据；不要假定读者已知道发布 Article 时是否另有导读。"
    }
  ],
  "rubric_results": [
    {
      "requirement": "每项核心机制或发现都说明对读者的意义：影响谁、改变什么、应做或停止做什么。",
      "result": "PASS",
      "evidence": [
        "受众是正在选择长文发布格式的创作者，开头直接提出其决策问题。",
        "“先别只凭总数换格式”明确给出当前应停止的推断和行动。",
        "正文给出按阅读需要选择、统一发布后七天、分别记录及避免因果断言的具体行动。"
      ],
      "qualification": "行动和后果已经写出；选择依据与术语解释的问题分别记入后两项。"
    },
    {
      "requirement": "专门术语在首次使用时有就地解释、先前解释或起同等作用的日常例子；核心数字概念需有可理解的例子。",
      "result": "FAIL",
      "stall_ids": [
        "S1",
        "S3"
      ],
      "evidence": [
        "包内允许读者认识 Post 和 Article，因此没有把这两个名称本身列为停顿。",
        "曝光指标及 3K 的首次出现未得到说明。",
        "导读 Post 的首次出现没有交代它与 Article 的关系。",
        "一周与一天的例子清楚说明了统一统计时长的用途，但不能替代曝光指标的解释。"
      ]
    },
    {
      "requirement": "不跳过因果步骤，结论所需的中间理由都在文中。",
      "result": "FAIL",
      "stall_ids": [
        "S2"
      ],
      "evidence": [
        "由多节内容、图表、反复查阅推到考虑 Article 的适配理由未写出。",
        "统一七天比较的理由已由避免一周对一天的例子给出。",
        "正文明确没有把个人观察或这些记录变成格式造成曝光提升的结论。"
      ]
    }
  ],
  "verdict_reason": "完整顺读后有三处未解决的停顿，分别涉及核心指标说明、格式选择的中间理由和导读 Post 的含义；因此本轮不满足无未解决停顿的 PASS 条件。"
}
```


## cold-review-v2.json

```json
{
  "language": "简体中文",
  "result": "FAIL",
  "scope": {
    "document": "revised-post-v2.txt",
    "source": "cold-reader-packet-v2.json",
    "exact_text_basis": "仅评审本评审包 draft 字段中的完整原文，保留原有段落和换行；包含“进一步阅读”标签及其链接。",
    "audience_basis": "面向想知道长文该发 Post 还是 Article 的创作者；只预设读者认识 X.com、Post 和 Article 这些名称。",
    "limits": "本次仅为文本冷读，没有核验个人观察、平台统计口径、链接页面内容，也没有检查图片。"
  },
  "read_through": {
    "completed": true,
    "method": "依次从首句读到最后的链接，再检查三项完整性要求；未浏览其他资料，未替作者补写内容。",
    "ordered_findings": [
      {
        "position": "第1段",
        "finding": "个人观察和两个问题能够直接理解。3K 后的 3000 给出数字换算；本段并未把个人观察写成实验结论。"
      },
      {
        "position": "第2段",
        "finding": "解释“曝光”暂沿用作者称呼，并明确不能当作独立读者人数；统计时长、主题和推广差异尚待核对，因此暂不能判断差距的原因。读者可以理解目前不能得出什么结论。"
      },
      {
        "position": "第3段",
        "finding": "按篇幅组织和阅读用途选择格式，两种情况及各自的阅读收益均有说明。"
      },
      {
        "position": "第4段第1句",
        "finding": "用发布后相同的7天作比较，并用“一周”和“一天”的差别说明为什么要统一统计时长。"
      },
      {
        "position": "第4段第2句",
        "finding": "在“这篇 Article”处出现一次指代停顿，详见 stall_log。"
      },
      {
        "position": "第4段末句",
        "finding": "说明记录与统一口径只能改善比较，不能据此直接归因于格式；结论与前面的限制相接。"
      },
      {
        "position": "最后的标签和链接",
        "finding": "“进一步阅读”没有预告未经核对的具体结论，标签本身可以理解。"
      }
    ]
  },
  "stall_log": [
    {
      "id": "S1",
      "position": "第4段第2句",
      "quote": "若另发一条介绍并链接这篇 Article 的 Post，两条内容的数字要分开记；转发、推广等差异也记下来，没有的数据留空。",
      "trigger": "这篇 Article",
      "stall_class": "Unresolved reference",
      "stall_class_zh": "指代未解决",
      "explanation": "上一句谈的是“多篇相近内容”，并出现“一篇”和“另一篇”，没有选定其中哪一篇是 Article。此处突然用单数的“这篇 Article”，读者需要判断它是开头那篇已发布一周的 Article，还是比较对象中的某篇 Article；若按前者理解，则要越过多个对象回找开头。按照本次冷读协议的指代标准，这个对象不能由读者自行补齐。",
      "required_fix_or_missing_information": "在该句内明确 Article 的对象或适用范围：是开头的那篇 Article，还是比较中的任一 Article。补足对象即可，不需要补造数据或改动原观察。",
      "status": "未解决"
    }
  ],
  "rubric_results": [
    {
      "requirement": "每个核心机制或发现都说明对读者的意义、影响及应采取或停止的行动。",
      "result": "PASS",
      "assessment": "现有数据不能支持格式归因，对应的行动是先按阅读需要选择格式；Post 与 Article 的编辑建议分别说明连贯读完和按章节查阅的用途；比较建议给出统一统计时长、分开记录和保留未知项的做法。指代问题单独记录为 S1，不把它扩大为后果说明缺失。"
    },
    {
      "requirement": "专门术语在首次需要理解时有解释、先前说明或能承担解释作用的日常例子；涉及数字时有具体例子。",
      "result": "PASS",
      "assessment": "Post 和 Article 属于包内明确允许预设的名称。“曝光”以作者原观察的用词出现，紧接着用“浏览”和“是否重复计数”说明其口径尚未核对，并用超过3000不等于超过3000位读者作具体辨析；3K 也直接标为3000。统一统计时长另有一周对一天的例子。文本没有要求读者先懂推荐模型或统计学术语。此项通过不表示已核实曝光的后台定义。"
    },
    {
      "requirement": "因果推导没有跳过结论所需的中间步骤；保留读者理解所需的上下文和连接。",
      "result": "PASS",
      "assessment": "统计口径、时长、主题和推广尚未核对，因此不能把差异归因于格式；统一发布后的7天可避免累计时长不同，这一步有直接解释。格式建议依据阅读组织的需要，并明确不承诺曝光更高；改进比较也未被升级成证明格式有效。未发现另外缺失的因果步骤。"
    }
  ],
  "verdict_reason": "全文完成顺序冷读，发现1处尚未解决的指代停顿。三项完整性要求本身未发现独立缺陷，但 PASS 要求没有未解决停顿，因此本轮为 FAIL。"
}
```


## cold-review-v3.json

```json
{
  "result": "PASS",
  "language": "简体中文",
  "scope": {
    "document": "revised-post-v3.txt",
    "source_packet": "cold-reader-packet-v3.json",
    "reviewed_parts": "数据包 draft 字段中的整篇简体中文导读 Post，包括开头提问、全部正文、‘进一步阅读：’标签和紧随其后的 URL；段落及换行按提供的版本阅读。",
    "audience": "想知道长文该发 Post 还是 Article 的创作者；按数据包假设，读者认识 X.com、Post 和 Article 这些名称，不具备推荐模型或统计专业知识。",
    "media": "未提供媒体，本次仅评估文字。",
    "limitations": "这是独立新读者的可读性与论述完整性检查，不是事实核验；未查看账户数据、后台截图或配图，未打开进一步阅读链接，也不判断链接页面的实际内容。"
  },
  "read_through": {
    "completed": true,
    "method": "从首句到末尾 URL 顺序阅读，仅依据数据包中的准确草稿及其受众、约束和范围，没有替正文补充机制或前提。",
    "ordered_observations": [
    {
        "part": "第一段",
        "observation": "读者能识别个人观察中的两类内容及数字差距，也能识别作者要回答的格式选择问题。3K 随即标为 3000。"
      },
      {
        "part": "第二段",
        "observation": "‘这里的曝光’承接开头的曝光数字；正文直接交代计数口径和重复计数未核对，并用超过 3000 次曝光不能直接等同于超过 3000 位读者说明数字的解释边界。随后列出比较条件未核对，明确不能据此判断格式原因或新增曝光来源。"
      },
      {
        "part": "第三段",
        "observation": "‘先按阅读需要选’给出可执行的判断标准；几段能讲清的问题对应一条 Post，多节材料和图表对应分章节的 Article。连续阅读和以后查阅分别说明了这些选择对读者的用途。"
      },
      {
        "part": "第四段",
        "observation": "比较多篇相近内容时统一为发布后 7 天，紧接着用累计一周与累计一天说明需要避免的差异。若存在介绍并链接某篇 Article 的 Post，正文把两个记录对象逐一说清；记录转发、推广差异以及缺失数据留空的动作也明确。结尾交代这些记录只能改善比较，不能单凭数字认定格式造成提升。"
      },
      {
        "part": "链接标签及 URL",
        "observation": "‘进一步阅读’仅指向后续阅读材料，没有要求读者依赖该页面才能补齐正文，也没有承诺页面支持某项未经核对的结论。"
      }
    ]
  },
  "stall_log": [],
  "stall_class_results": [
    {
      "class": "Unresolved reference",
      "result": "PASS",
      "reason": "没有需要跨过另一个合理主体倒查的指代。‘这篇 Article 和这条 Post’在同一句中分别对应被链接的文章和介绍该文的 Post；‘这样’承接紧邻的记录与比较步骤。"
    },
    {
      "class": "Unexplained term",
      "result": "PASS",
      "reason": "未发现受众需要猜测的专门术语。Post 和 Article 的名称属于明确的受众前提；3K 有 3000 的就地释义；曝光的计数不确定性及其与读者人数的区别在开头观察之后直接说明。"
    },
      {
      "class": "Broken chain",
      "result": "PASS",
      "reason": "没有从个人观察直接跳到格式导致增长的结论。比较条件不明、无法归因、改按阅读需要选格式，以及采用共同观察时长改善比较的各步均在正文中明确交代。"
    }
  ],
  "rubric_results": [
    {
      "requirement": "每个核心机制或发现说明对读者的含义：谁受影响、有什么变化、应做或停止做什么。",
      "result": "PASS",
      "evidence": [
        "不能把“超过 3000”直接当成超过 3000 位读者。",
        "只凭这组个人观察，还不能确定差距是不是格式造成的，更不知道新增曝光从哪里来。",
        "我的建议是先按阅读需要选：一个问题几段就能讲清，用一条 Post 把观点和解释连着读完；材料需要多节内容和图表，就按章节整理成 Article，让每节回答一个小问题，方便以后查阅。",
        "这样能改善比较，仍不能单凭这些数字认定格式带来了提升。"
      ],
      "assessment": "面对格式选择的创作者能直接得到两类含义：不能把当前数字解释成独立读者数量或格式效果；可以依据材料的组织与查阅需要选格式，并在后续比较时统一观察时长、分别记录相关内容。阅读便利的用途与数据比较的限度都已写出。"
    },
    {
      "requirement": "专门术语在首次使用时具有白话说明、先前解释或承担解释作用的日常例子；涉及数字时提供可理解的具体示例。",
      "result": "PASS",
      "evidence": [
        "总曝光超过 3K（3000）",
        "后台到底统计哪种浏览、是否重复计数，还没有核对",
        "不能把“超过 3000”直接当成超过 3000 位读者。",
        "可以把多篇相近内容发布后 7 天的数据放在一起，避免一篇累计一周、另一篇只累计一天。"
      ],
      "assessment": "曝光在首段的浏览量比较中具有可理解的日常语境，紧接着的解释指出其平台计数定义尚未核实，并说明曝光数字与人数不能直接互换。3K 以 3000 直接展开。比较时长则用一周与一天的具体例子说明，不依赖统计术语或隐藏计算。正文没有引入需要另行解释的推荐模型概念。"
    },
    {
      "requirement": "因果链不跳步；每项结论所需的中间理由都在正文中。",
      "result": "PASS",
      "evidence": [
        "各篇统计了多久、主题是否相近、有没有额外推广，也都需要核对。只凭这组个人观察，还不能确定差距是不是格式造成的，更不知道新增曝光从哪里来。",
        "一个问题几段就能讲清，用一条 Post 把观点和解释连着读完",
        "材料需要多节内容和图表，就按章节整理成 Article，让每节回答一个小问题，方便以后查阅。",
        "可以把多篇相近内容发布后 7 天的数据放在一起，避免一篇累计一周、另一篇只累计一天。",
        "这是编辑建议，不是承诺哪种曝光更高。"
      ],
      "assessment": "作者对观察的解释止于条件尚未核对、不能确定原因，没有补写未获证据支持的推荐机制。格式建议依据明确的阅读和组织需求；共同观察时长的必要性用累计时长不一致直接说明。记录不同对象及推广差异后的结论也限定为改善比较，未跳到因果证明。"
    }
  ],
  "required_fixes": [],
  "verdict_reason": "在数据包规定的受众和纯文字范围内，完整顺读没有出现必须重读、回查或猜测才能继续的停顿；三项不压缩论述要求均通过。"
}
```
