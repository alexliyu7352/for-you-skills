# X 算法更新：停留权重涨了 25%，发文要跟着改吗？

[English](research-update.en.md)

代码核查：2026-11-08；文字修订：2026-11-09。对应 For You Skills 1.3.0。

X 把 Home Mixer 里的连续停留系数从 `0.006` 调到了 `0.0075`。涨了 25%。如果你正在考虑要不要把文章写长一点，先看这个数到底乘的是什么。

Home Mixer 参与组织首页推荐。它拿到的是针对某位读者、某篇帖子的预测：这个人有多大概率点赞、点击，会停留多久。假设同一个停留预测是 5 秒，旧系数算出 `5 × 0.006 = 0.03`，新系数算出 `5 × 0.0075 = 0.0375`。

增加 25% 的是这一个计分项。总分还要算其他预测，帖子能否出现在读者面前，还取决于筛选和与其他候选内容的竞争。单看这行改动，算不出曝光会增加多少。

这次对照的是旧研究最后查到的 `606b254` 和 `3b6919f`，中间有 7 次提交，合计改了 289 个文件。下文挑与发文有关的部分讲；逐项记录和完整提交列表放在[算法更新记录](../ALGORITHM_CHANGELOG.md)。这些结论来自公开代码，没有用线上流量实验验证效果。

## 权重表里改了七个数

Home Mixer 的公开默认值如下。表里的“一般分享”和转帖是两个项目，别混着看。

| 预测项目 | 旧值 | 新值 |
| --- | ---: | ---: |
| 点赞 | 0.66 | 0.708 |
| 点击 | 0.3 | 0.274 |
| 打开视频 | 0.02 | 0 |
| 一般分享 | 2 | 2.118 |
| 连续停留 | 0.006 | 0.0075 |
| 点击后停留 | 0.4 | 0.385 |
| 不感兴趣 | -52.272 | -53.07 |

可以直接对照[旧参数](https://github.com/xai-org/x-algorithm/blob/606b254b45be798bfaecfa8c23f5a9c51bc8000c/home-mixer/params/param.rs#L393-L500)和[新参数](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/params/param.rs#L404-L539)。点赞和一般分享的系数略升，点击略降，“不感兴趣”的扣减系数绝对值也略增。这些数用于计算预测值的贡献，不能拿实际收到的点赞数直接乘 `0.708` 算推荐分。

另一个排序服务 VM Ranker 仍保留自己的默认值：点赞 `0.5`，连续停留 `0.004`。所以，看到不同的权重表，得先查它引用的是哪一个服务。[VM Ranker 参数](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/vm-ranker/params.rs#L1-L131)也说明，不能把上面这一列新数值当成全站每次请求都在使用的配置。

“点击后停留”还留着一个没查清的问题：公开资料没有补齐模型输出到 Home Mixer 这个字段的完整转换过程。`0.385` 因而不能读成“每秒加 0.385 分”。这次调了系数，原来的证据缺口仍在。

写作上，拿这组变化来支持“把文章拉长”走得太远。比如开头承诺比较两种方案，正文却花很长篇幅交代背景，那就该检查读者要找的比较结果放在哪里。论证需要的细节可以留，拖延答案的段落可以删。这是编辑建议；代码没有给出一个适合所有文章的字数。

## 视频和 Grok 增加了哪些东西

Home Mixer 现在默认请求“点开视频后继续看多久”和“进入个人主页后停留多久”等已有预测。对应的直接计分系数，在检查的公开设置里仍是零。[预测开关](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/params/param.rs#L299-L315)和[VM Ranker 系数](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/vm-ranker/params.rs#L67-L101)要放在一起看，才知道“开始请求这个预测”和“用它加分”之间还隔着什么。

另一个叫 Video Carousel 的视频轮播模块，增加了点击预测模型、过滤已看内容的代码，以及安全过滤方面的改动。不过，它的总开关、新点击模型开关和已看过滤开关，公开默认值都还是关闭。新增的两项计分系数也是零。[模块设置](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/params/param.rs#L1223-L1355)没有告诉我们，线上哪些用户已经被分配到启用这些功能的配置。

这里还有一个容易看岔的地方。上表里的“打开视频”降到零，属于普通 Home Mixer 的参数；Video Carousel 自己的同名系数仍是 `1.0`。视频还有其他预测和推荐路径，不能据此判断所有视频都不再计分。

`GrokAnalyze` 是新增字段，`ReactWithVideo` 改名为 `PostVideo`。这两个字段在 [Home Mixer](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/params/param.rs#L484-L495) 和 [VM Ranker](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/vm-ranker/params.rs#L102-L113) 里的默认系数也都是零。单凭这些新增字段，推荐别人“叫 Grok 来回复，能涨曝光”没有依据。

这轮改动还不足以决定内容该换成视频。演示一个操作，用视频能直接看到过程；要让人反复查一组数据，表格或图片可能更方便。选择格式时，这些具体用途比尚未确认启用范围的系数更有用。

## 标签报告能查到更具体的帖子了

Under the Hood 是 X 的透明度报告。新代码能在报告里列出一部分被标记过的帖子 ID，方便从一个标签追到具体帖子。数据已经有了这条处理路径，但后台和界面各有开关，公开默认设置还没有把帖子清单普遍打开。[后台开关](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/under-the-hood/strato/lib/params.strato#L24-L37)和[界面开关](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/under-the-hood/jetfuel/routes/report.tsx#L333-L344)都能查到。

即使能看到清单，它也有数量和比例限制。报告统计的是一段时间内发生过什么；一篇帖子曾经被标记，后来移除了标签，仍可能出现在报告里。申诉说明会告诉你，支持申诉的帖子需要仍带有相应标签；报告本身没有替你检查当前状态。[清单规则](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/under-the-hood/strato/columns/underTheHoodReport.User.strato#L340-L367)和[申诉说明的生成条件](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/under-the-hood/strato/lib/underTheHoodLabels.strato#L437-L520)对应的是这两个问题。

另外，排序记录里增加了部分计分贡献的解释。它能指出某次计分中贡献较大的项目，不能单独解释一篇帖子的全部曝光。[相关代码](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/vm-ranker/scoring/value_model.rs#L187-L240)仍受请求条件限制。

如果你的账号有这个报告，查曝光时可以先留好报告月份、生成时间、标签名称和帖子链接。这样至少能核对同一段时间、同一篇帖子。只看到浏览量低，或者报告里没显示清单，都不足以判断帖子是否受过限制。

通知也有改动。提及、回复、媒体标记、点赞和转帖通知增加了检查；有的检查取决于接收者是否关注发送者，有的还取决于接收者的质量过滤设置。这些是[通知对应的规则](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/visibility-filtering/rules/levels.rs#L178-L278)，没有整套加入首页推荐。因此，别人没收到某条通知，不能直接用来证明你的帖子已从陌生人的首页里消失。

有一条安全检查现在会把正文提及和媒体里的用户标记合在一起，忽略大小写，按不同账号计数。门槛仍是两个账号，但这只是进入该检查的条件之一，后面还有其他条件和判断。[这段代码](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/grox/flows/ptos/task_filter.py#L37-L100)也推不出“标记两个人就会封号”。

## 第二篇、Article 和首图，原来的结论还成立

这次又查了一遍作者计数。它仍然针对某次推荐请求里的候选帖子，把同一作者的帖子按分数排好，再从零开始计数。在启用作者多样性处理并采用 VM Ranker 公开默认值时，前三篇的倍率是 `1`、`0.625`、`0.4375`。下午发的新帖可能排第一；它并不因为是你今天发的第二篇，就自动拿第二个倍率。[计数与计算代码](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/xai-value-model/scoring.rs#L265-L324)没有改。

这也算不出“发完等四小时恢复”。训练配置里新增的时间间隔，描述的是读者请求和展示历史的时间关系，不能拿来当创作者的发文间隔。[时间特征的处理代码](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/phoenix/xrex/models/recsys_feature_prep.py#L50-L80)说的是另一个对象。

Article 没有新增统一的格式加分项。V8.2 那条取第一个可用图片或视频的路径也没变，正文 `4,000` 字符的截断边界仍在。这个边界只属于特定处理路径；X 还有别的内容处理方式，不能概括成“所有模型只看首图”，也不能拿它规定平台的发文字数上限。[V8.2 源码](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/grox/flows/mm_emb/renderer_v82.py)在本次比较中没有变化。

还有一个和限流容易混淆的数字：安全标签缓存里的 24 小时。它规定缓存数据可以保留或使用多久，标签本身何时失效另有规则。它不能拿来算“账号被罚 24 小时”。[缓存设置](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/safety-label-source/dragonfly.rs#L25-L63)和[读取时的新鲜度判断](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/safety-label-source/dragonfly.rs#L246-L251)可以分别核对。

这些旧问题值得保留在更新里。作者最容易白忙的，往往就是为了一个代码里没有的每日折扣停稿，或者为了一个没证实的格式加分，把原本适合阅读的内容硬改成视频。

这篇是[原始研究](../provenance/research-report.zh-CN.md)的补充。v1.3.0 保留 578 个原始知识条目，另外加入 14 项更新核查；查询受影响的旧条目时，会一起返回新结论和对应源码。仓库每周检查算法主线，有新提交就列出差异，核对后再改技能和文档。已安装的技能需要更新才能拿到这些资料。以后查算法改动看 [ALGORITHM_CHANGELOG.md](../ALGORITHM_CHANGELOG.md)，查技能版本看 [CHANGELOG.md](../CHANGELOG.md)；外部博客和早期演示仍对应各自的写作、录制日期。
