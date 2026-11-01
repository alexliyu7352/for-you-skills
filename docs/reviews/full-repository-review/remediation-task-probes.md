# 打包技能任务实测：三份用户答复

本文件记录通过 `skills/x-assistant/SKILL.md` 执行的三项实际任务。知识范围为包内研究截止日 **2026-10-29** 的固定代码证据：基线 `5ed796374ea48ee26058aab66ab10c266bea2bef`，比较版本 `606b254b45be798bfaecfa8c23f5a9c51bc8000c`。使用包内修订后的工作条目；条目的修订日期不代表引用了更晚的算法版本。原始链接由包内条目解析，未联网打开或验证当前可访问性。

## 答复一：hashtag 固定扣分与算法公开时间

**两句话都不宜原样写进攻略。** 第一处把“公开证据没有确立公式”写成了“证明公式不存在”；第二处把 Git 提交元数据当成了首次公开时间。

可以直接使用这版：

> 截至本次研究覆盖的 2026 年 10 月 29 日公开快照，所引证据未给出全站统一的“超过多少个 hashtag，就固定扣多少分”公式。这不能证明系统中绝不存在未公开的规则，也不能证明所有 hashtag 都没有价值。公开代码确有 hashtag 滥用分类及有条件的标签写入分支；实际风险仍取决于分类结果和执行条件。
>
> 本文列出的时间是 Git 元数据记载的提交时间：基线版本 `5ed7963` 为 2026 年 10 月 28 日 02:49:03 UTC，比较版本 `606b254` 为 10 月 29 日 02:57:55 UTC。这些时间不能单独证明代码首次向公众可见的准确时刻，更不能证明功能全量上线的时刻。首次公开、官方公告和生产部署应分别核对证据。

依据和适用边界：

| 待核实说法 | 判断 | 能支持到哪里 |
| --- | --- | --- |
| “公开代码证明 hashtag 根本没有固定扣分公式” | **未被确立，不能这样断言** | 包内引用没有建立统一的数量扣分公式；未公开的规则与提示词仍是证据缺口。 |
| “Git commit 时间就是算法公开的准确时间” | **误读证据类型** | 作者和提交者时间是提交元数据；它们不记录首次公开可访问或全量部署的事件。 |

- `SpamHashTagAbuse` 出现在[分类枚举](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/state.py#L37-L46)中；[写入分支](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/task_write_safety_post_annotations_result_sink.py#L233-L248)保留其他 Spam 类别的作者资格判断。包内引用还记录了[提示词未公开](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/prompts.py#L11-L31)及[仓库披露范围](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/README.md#L428-L447)。因此不能把未检出公开公式改写为不存在任何公式。（K05-060、K05-061、Q43）
- 正常 hashtag 相关行为也不是完全缺席：Phoenix 的[历史行为列表](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix/xrex/data/recsys/history_id_lists.py#L25-L36)包含 `CLICK_HASHTAG`；[SimClusters 的前四个 hashtag 上限](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/simclusters/simclusters_v2/summingbird/common/TweetEntityExtractor.scala#L14-L40)属于一个实体提取器的选取范围。这些都不是每个 hashtag 的固定加分，也不是“零个最佳”“四个最佳”或“第五个开始扣分”的全站证据。（K05-062、K05-063、Q43）
- 时间来自包内保留的[基线提交](https://github.com/xai-org/x-algorithm/commit/5ed796374ea48ee26058aab66ab10c266bea2bef)与[比较提交](https://github.com/xai-org/x-algorithm/commit/606b254b45be798bfaecfa8c23f5a9c51bc8000c)元数据。对应洛杉矶时间分别为 10 月 27 日 19:49:03 PDT、10 月 28 日 19:57:55 PDT。若攻略还写“今天更新”，需补原帖发表时间、作者时区和所指事件；[README 的功能日期](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/README.md#L32-L44)也应与提交时间分开。（K01-017、Q01、Q02）

实用写法是保留与主题直接相关、方便读者识别的标签，不承诺一个固定最佳数量；这是编辑建议，不是从代码推导的流量保证。缺少首次公开事件记录时，就把时间明确标成“提交时间”。

## 答复二：跨月加标签、后来移除，Under the Hood 算哪月

**按这份快照的普通帖子安全标签事件路径，在满足观察窗口与数据覆盖条件时，这条帖子应归入 10 月的 Post labels 发帖批次。** 月份跟着帖子的创建日期，不能因为 11 月 2 日才加标签就直接归到 11 月。标签后来被移除，也不会抹掉该路径中“曾被添加”的计数；移除是另外记录的状态。仅凭这三个日期，尚不能保证某一份实际报告一定已经收录了它。

理由是月度发布任务使用 `authoredYyyymmdd` 分配月份；普通安全标签事件在帖子创建后的可配置窗口中观察，公开默认 `postObservationDays=7`，同时受批次截点约束。10 月 31 日发帖、11 月 2 日加标签符合这个默认窗口的日期关系，但还要确认该批次确实读到了事件。[发帖月份分配](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthUserMonthMhPublisherJob.scala#L237-L245)、[事件窗口](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthDailyPostsJob.scala#L311-L322)、[七天默认值](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthDailyPostsJob.scala#L421-L422)、[曾添加计数与移除记录](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthDailyPostsJob.scala#L360-L393)。（K05-069）

具体需要核对：

| 条件 | 要核对什么 | 对解释的影响 |
| --- | --- | --- |
| 统计项目 | 是 **Post labels**，还是 **Account labels** | 前者按合格帖子计数；后者统计报告期间带有账户标签的天数，不能混用。 |
| 合格发帖批次与分母 | 是否是该月份创作的合格逻辑帖子；是否为转帖或 nullcast；逻辑 ID 是否已去重 | 分母不是所有导出行，也不是所有标签事件；普通转帖和 nullcast 不进入这项分母。 |
| 事件路径 | 普通安全标签事件，还是快照补缺、帖子标志、下架等其他路径 | 七天窗口不能不加区分地套到所有路径上。 |
| 观察范围 | 实际 `postObservationDays`、创建与加标签的准确时间和时区、批次截点、数据是否已入批次 | 默认值不是每次运行配置的证明；过早生成的报告可能尚未覆盖 11 月 2 日事件。 |
| 报告范围 | 实际显示的 **Period**、生成时间、数据是否就绪、是否回退到更早月份 | 页面写“上个月”并不保证这次返回的一定是上个月。 |
| 标签状态与作用 | 标签名称、添加与移除时间、**What it means**、**Effect on visibility** | “曾添加”不等于“生成报告时仍生效”；作用还可能限于特定受众或入口。 |

分母排除与逻辑去重见[合格帖子集合](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthDailyPostsJob.scala#L215-L250)；帖子占比与账户天数分别计算见[报告聚合](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/strato/columns/underTheHoodReport.User.strato#L320-L355)；数据未就绪的回退见[报告周期选择](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/strato/columns/underTheHoodReport.User.strato#L423-L458)；作用范围见[标签解释](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/strato/lib/underTheHoodLabels.strato)。（K05-067、K05-069、K05-070、K05-073）

**不能据此算出你这个月少了多少曝光。** 带标签的帖子比例以“帖子”为单位，账户标签比例以“天”为单位，都不是丢失曝光的比例。比如“3 篇 / 40 篇 = 7.5%”只是一个说明单位的假设例子，不能读成曝光损失 7.5%。十月发帖批次的标签占比，也不能直接当作十一月曝光下降率。（K05-071、K05-072）

要计算“实际观测值比上期少多少”，还需你选定月份、同口径的曝光或浏览数据及可比观察窗口；要进一步归因于标签，还需标签生效时间、作用入口和受众，以及能排除内容、分发时长等同时变化因素的证据。这个假设没有提供这些数据。报告本身是 [best effort 的汇总](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/strato/columns/underTheHoodReport.User.strato#L47-L65)，不是每次展示机会的因果日志；移除标签也不能据此推算何时恢复多少曝光。（K05-076、Q17、Q27、Q31）

## 答复三：同帖、同时刻、不同统计范围的两条导出

**这是 1 个帖子、2 条观测；按现有记录，不是两篇帖子，也不是两条应直接合并的同口径重复行。** 两行时间虽然都是 **2026-10-30 12:00:00 UTC**，但 `metric_scope` 分别为 `post` 和 `owner_analytics`，应保留各自范围。

能确定的导出数值如下；“未知”表示没有提供，不是 0：

| 统计范围 | views | likes | replies | 正文覆盖 |
| --- | ---: | ---: | ---: | --- |
| `post` | 100 | 5 | 未知 | 记录提供“正文”，标记为 complete |
| `owner_analytics` | 未知 | 未知 | 2 | 未提供正文，状态未知 |

三个数字在输入中都是未缩写的整数字符串，工具按精确值解析；这是**对所给导出记录的整理**，未独立核实平台页面。不能把后台的 replies=2 自动填成公开帖子范围的 replies，也不能从公开记录向后台范围补 views 或 likes。

实际运行整理工具得到：

| 输出字段 | 值 | 含义 |
| --- | ---: | --- |
| `input_rows` | 2 | 输入记录数 |
| `unique_posts` | 1 | 确认的永久链接身份数 |
| `retained_observations` | 2 | 保留的统计范围观测数 |
| `duplicate_rows` | 0 | 同一帖子、**同一 metric_scope** 的额外输入观测数；这里两个范围不同 |
| `unique_content_items` | 1 | 已提供记录中解析出的内容组数 |
| `content_count_complete` | true | 这两条输入的身份和关系解析没有未解决项；不表示已覆盖账号全部历史或全部指标 |
| `format_counts.unknown` | 2 | 两条观测均未提供 format；不是“有两篇未知格式帖子” |

因此，**保留两条观测是正确的；把行数 2 当成帖子数或独立样本数 2，才会重复计算这一个帖子。** 当前没有两个同范围的 views 值要相加，也没有依据声称总曝光是 200。这里的“duplicate_rows=0”只是整理工具的范围内去重结果，不是对上游平台计数方式的独立验证。

还不能判断：

- 不能由 100 views 得出 100 个独立读者、100 次 Home 展示或 100 次完整阅读；也不能把后台回复数与另一范围的浏览数直接组成有定义的回复率。需先核对指标定义、分母与统计窗口。包内保留的[官方浏览数定义](https://help.x.com/en/using-x/view-counts)说明公共 views 并非独立人数。（K05-079、K05-080、K05-083、Q49）
- 未提供发帖时间，所以无法算帖龄或对齐“发布后 24 小时”；这里只有一个观测时刻，不能算增长趋势、下降幅度或速度。
- 未提供转帖、引用、收藏等数字，它们均未知；媒体未提供，不能据此认定没有图片或视频。
- 第一条的“正文”原始长度和去首尾空白后的长度均为 **2 个 Unicode 码点**；第二条正文未提供。这个计数不是 X 的加权长度，也不能据它判断内容质量、推荐分、隐藏标签、曝光受限原因或应该选择哪种内容格式。

后续可继续使用“帖子身份 + 指标范围 + 观测时间”保存记录，同时补上可靠的发表时间、每个指标的定义和统计窗口。不同范围可以并排展示，但合并或计算比例前应先确认口径兼容。

## 执行范围与证据缺口

本次只读取了指定打包技能内的 SKILL、routing、工作流、知识指南、观察契约、修订说明和知识条目。未读取仓库测试、Git 历史、仓库审计报告或实现笔记；未运行仓库测试套件；未调用网络、X 页面、图片生成或子代理。包内 `research-errata.md` 是知识指南要求读取的修订依据；其中关于过去校验或访问的叙述不视为本次重现，本答复没有以其历史测试结果或端点状态为凭。

| 请求 | 实际使用的流程 | 未获取或无法由当前材料确定的证据 |
| --- | --- | --- |
| 1 | `x-assistant → x-myth-check` | 未公开的模型提示词、全模型与全入口的 hashtag 因果实验、首次公开事件记录、当前或逐请求生产配置；未独立重验 Git 元数据或网络链接 |
| 2 | `x-assistant → x-explain` | 实际报告 Period/生成时间、具体标签与来源路径、运行配置和批次截点、准确事件日志、合格帖子分母、实际曝光数据及因果对照 |
| 3 | `x-assistant → x-review-posts` 的导出整理步骤 | 平台页面核验、发表时间、指标窗口与完整定义、未提供的指标/媒体/第二条正文；无账号内容审核或因果诊断的证据 |

本次未遇到 Python 不可用；全部已记录 helper 调用退出码均为 0。知识检索只解析本地包内资料，不验证外部链接可达性，也不重演线上推荐。

针对第三项做了主题适用性检查：00 的证据边界、05 的统计口径与缺失值、06 的测量未知项适用；01 的发布频率/排序权重、02 的读者匹配、03 的格式媒体机制、04 的冷启动/旧帖机制均不适用于这次仅要求导出清理的任务。没有据两字正文扩展成内容审稿、媒体方案或账号审计。

| 规则或契约 | 输入证据 | 状态 | 处理 |
| --- | --- | --- | --- |
| observations：身份与 scope | 同 URL、同时间，scope 不同 | pass | 1 个帖子、2 条观测，各自保留来源行 |
| observations：最新时间选择 | 两行均为带 Z 的时间 | pass | 每个身份/scope 桶内使用给定时间；不声称是全网最新观测 |
| K05-079、K05-083 | 仅给出三个数值字段 | missing | 其余保留 null/unknown，跨范围不回填 |
| K05-080、Q49 | 只给 views，没有去重人数或后台定义 | missing | 不换算人数、完读或 Home 展示 |
| observations：帖龄 | 无 published_at | missing | age_hours=null，不估算 |
| 正文测量 | 仅 post 行有“正文” | pass / missing | 对实际两字执行计数；另一个范围正文未知 |
| 因果与内容建议 | 无时间序列、媒体或实际内容材料 | not_applicable | 不判断推荐原因或给出未经支持的内容结论 |

## 原始输入与主要 helper 输出

以下输入按请求原样保存到 `/tmp/x-assistant-remediation-probes/observations.json`，没有补字段或改变 scope：

```json
[{"url":"https://x.com/demo/status/123","observed_at":"2026-10-30T12:00:00Z","metric_scope":"post","text":"正文","body_status":"complete","metrics":{"views":"100","likes":"5"}},{"url":"https://x.com/demo/status/123","observed_at":"2026-10-30T12:00:00Z","metric_scope":"owner_analytics","metrics":{"replies":"2"}}]
```

正文计数输入 `/tmp/x-assistant-remediation-probes/post.txt` 的精确内容为 `正文`，无结尾换行。

所有 helper 的运行目录均为：

```text
/workspace/scratch/8875c799c753/for-you-skills-fixes/skills/x-assistant
```

### 导出整理：实际命令与原始 stdout

```bash
python3 scripts/summarize_posts.py --input /tmp/x-assistant-remediation-probes/observations.json
```

退出码：0。

```json
{
  "input_rows": 2,
  "unique_posts": 1,
  "duplicate_rows": 0,
  "retained_observations": 2,
  "unique_content_items": 1,
  "unresolved_identity_records": 0,
  "unresolved_content_identities": 0,
  "content_count_complete": true,
  "relationship_conflicts": [],
  "duplicates": [],
  "invalid_rows": [],
  "format_counts": {
    "unknown": 2
  },
  "posts": [
    {
      "url": "https://x.com/demo/status/123",
      "observed_at": "2026-10-30T12:00:00Z",
      "metric_scope": "post",
      "text": "正文",
      "body_status": "complete",
      "metrics": {
        "views": {
          "raw": "100",
          "value": 100,
          "precision": "exact"
        },
        "likes": {
          "raw": "5",
          "value": 5,
          "precision": "exact"
        },
        "replies": {
          "raw": null,
          "value": null,
          "precision": "unknown"
        },
        "reposts": {
          "raw": null,
          "value": null,
          "precision": "unknown"
        },
        "quotes": {
          "raw": null,
          "value": null,
          "precision": "unknown"
        },
        "bookmarks": {
          "raw": null,
          "value": null,
          "precision": "unknown"
        }
      },
      "format": "unknown",
      "media_status": "not_viewed",
      "identity_status": "permalink",
      "source_observations": [
        {
          "row": 0,
          "record": {
            "url": "https://x.com/demo/status/123",
            "observed_at": "2026-10-30T12:00:00Z",
            "metric_scope": "post",
            "text": "正文",
            "body_status": "complete",
            "metrics": {
              "views": "100",
              "likes": "5"
            }
          }
        }
      ],
      "selected_observation_rows": [
        0
      ],
      "selection_status": "latest_confirmed_timestamp",
      "content_identity": "status:123",
      "content_identity_status": "resolved",
      "age_hours": null
    },
    {
      "url": "https://x.com/demo/status/123",
      "observed_at": "2026-10-30T12:00:00Z",
      "metric_scope": "owner_analytics",
      "metrics": {
        "views": {
          "raw": null,
          "value": null,
          "precision": "unknown"
        },
        "likes": {
          "raw": null,
          "value": null,
          "precision": "unknown"
        },
        "replies": {
          "raw": "2",
          "value": 2,
          "precision": "exact"
        },
        "reposts": {
          "raw": null,
          "value": null,
          "precision": "unknown"
        },
        "quotes": {
          "raw": null,
          "value": null,
          "precision": "unknown"
        },
        "bookmarks": {
          "raw": null,
          "value": null,
          "precision": "unknown"
        }
      },
      "format": "unknown",
      "body_status": "unknown",
      "media_status": "not_viewed",
      "identity_status": "permalink",
      "source_observations": [
        {
          "row": 1,
          "record": {
            "url": "https://x.com/demo/status/123",
            "observed_at": "2026-10-30T12:00:00Z",
            "metric_scope": "owner_analytics",
            "metrics": {
              "replies": "2"
            }
          }
        }
      ],
      "selected_observation_rows": [
        1
      ],
      "selection_status": "latest_confirmed_timestamp",
      "content_identity": "status:123",
      "content_identity_status": "resolved",
      "age_hours": null
    }
  ],
  "scope": "Latest confirmed timestamp per (permalink identity, metric_scope), plus independent observations without comparable timestamps and all URL-less evidence. source_observations preserves original records including older dated snapshots; selected_observation_rows identifies the current evidence. unique_posts counts confirmed identities, while retained_observations and format_counts count output observations. duplicate_rows counts additional input observations of the same identity and scope, not independent samples. unique_content_items counts resolved observed content groups, not a complete total when content_count_complete is false. Unresolved identities and conflicting Article links are excluded from that count and reported separately. Content relationships never combine metrics. Unknown relationships are not inferred. Displayed counts are not unique people or Home impressions. Differing ages, content, promotion and source prevent a causal format comparison."
}
```

### 正文计数：实际命令与原始 stdout

```bash
python3 scripts/inspect_draft.py --text /tmp/x-assistant-remediation-probes/post.txt
```

退出码：0。

```json
{
  "source_snapshot": "5ed796374ea48ee26058aab66ab10c266bea2bef",
  "text": {
    "raw_characters": 2,
    "raw_preview_4000": "正文",
    "characters": 2,
    "preview_4000": "正文",
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

## 知识 helper 的实际调用与原始输出

以下逐条保留实际执行的检索、目录和完整条目调用。目录查询曾在多项同时显示时触发宿主总输出截断，因此单独重读 topic 05；部分已完成调用的完整结果也从会话存储重新显示。下列记录保存的是各命令返回的完整 stdout，没有将截断画面当作完整证据。

<details>
<summary>1. python3 scripts/knowledge.py search &quot;hashtag&quot;</summary>

```bash
python3 scripts/knowledge.py search "hashtag"
```

退出码：0。

```json
{
  "retrieval": "lexical with topic synonyms; read topic catalog if relevant coverage is unclear",
  "results": [
    {
      "match_score": 18,
      "id": "K05-063",
      "title": "Four hashtags is the selection limit of one extractor",
      "kind": "code",
      "topic_file": "topic-05.json",
      "when": "When MaxHashtagsPerTweet is used to prove a universally optimal count"
    },
    {
      "match_score": 13,
      "id": "K05-060",
      "title": "SpamHashTagAbuse is a spam class with conditional label writing",
      "kind": "code",
      "topic_file": "topic-05.json",
      "when": "When discussing the risk of hashtag stuffing"
    },
    {
      "match_score": 13,
      "id": "K05-061",
      "title": "Advice to limit hashtags is not proof of zero value or a uniform deduction formula",
      "kind": "myth",
      "topic_file": "topic-05.json",
      "when": "When reviewing claims that all hashtags have zero value or incur count-based penalties"
    },
    {
      "match_score": 13,
      "id": "K05-062",
      "title": "CLICK_HASHTAG behavior can be an input to Phoenix",
      "kind": "code",
      "topic_file": "topic-05.json",
      "when": "When someone asserts the system completely ignores hashtags or calculates bonuses by count"
    },
    {
      "match_score": 13,
      "id": "K05-064",
      "title": "Choose hashtags directly related to the topic or event",
      "kind": "editorial",
      "topic_file": "topic-05.json",
      "when": "When reviewing hashtags alongside the body"
    },
    {
      "match_score": 13,
      "id": "Q43",
      "title": "Is the optimal number of hashtags zero, four, or some other fixed number?",
      "kind": "unknown",
      "topic_file": "topic-06.json",
      "when": "The question or copy concerns: Is the optimal number of hashtags zero, four, or some other fixed number?"
    },
    {
      "match_score": 5,
      "id": "K02-005",
      "title": "Understand topic consistency through reader tasks; no fixed purity formula was found",
      "kind": "myth",
      "topic_file": "topic-02.json",
      "when": "When a draft proposes topic purity, fixed hashtag counts, topic-change resets, or penalties for mixing Chinese and English."
    }
  ]
}
```

</details>

<details>
<summary>2. python3 scripts/knowledge.py search &quot;commit&quot;</summary>

```bash
python3 scripts/knowledge.py search "commit"
```

退出码：0。

```json
{
  "retrieval": "lexical with topic synonyms; read topic catalog if relevant coverage is unclear",
  "results": [
    {
      "match_score": 9,
      "id": "K01-017",
      "title": "Checking 'today' requires distinguishing commit time, public availability, announcements, and deployment",
      "kind": "code",
      "topic_file": "topic-01.json",
      "when": "When reviewing date assertions such as 'updated today' or 'October 28/29 update'"
    },
    {
      "match_score": 9,
      "id": "K02-013",
      "title": "The October 13 public commit added ld configuration and model handling",
      "kind": "code",
      "topic_file": "topic-02.json",
      "when": "When review requires establishing when ld appeared in public code."
    },
    {
      "match_score": 1,
      "id": "K00-002",
      "title": "Research snapshots and the report revision date",
      "kind": "editorial",
      "topic_file": "topic-00.json",
      "when": "The answer concerns report completeness, verification records, source dates, or strength of evidence."
    },
    {
      "match_score": 1,
      "id": "K00-003",
      "title": "How historical parameters and the visibility refactor were checked",
      "kind": "editorial",
      "topic_file": "topic-00.json",
      "when": "The answer concerns report completeness, verification records, source dates, or strength of evidence."
    },
    {
      "match_score": 1,
      "id": "K00-009",
      "title": "V5 and V8.2 function checks and cross-version comparisons",
      "kind": "editorial",
      "topic_file": "topic-00.json",
      "when": "The answer concerns report completeness, verification records, source dates, or strength of evidence."
    },
    {
      "match_score": 1,
      "id": "K01-030",
      "title": "A cross-service difference of 0.006 versus 0.004 cannot establish an increase this month",
      "kind": "code",
      "topic_file": "topic-01.json",
      "when": "When a draft directly uses 0.006÷0.004 to claim an increase this month"
    },
    {
      "match_score": 1,
      "id": "K01-071",
      "title": "Public defaults and meaning of Continuous dwell (ContDwellTime)",
      "kind": "code",
      "topic_file": "topic-01.json",
      "when": "When a draft cites values for Continuous dwell (ContDwellTime), compares the value of actions, or converts them to exposure"
    },
    {
      "match_score": 1,
      "id": "K02-014",
      "title": "The October 28 README addition recorded the October 13 update",
      "kind": "official",
      "topic_file": "topic-02.json",
      "when": "When a draft treats the October 28 README addition as ld's first appearance."
    }
  ]
}
```

</details>

<details>
<summary>3. python3 scripts/knowledge.py search &quot;Under the Hood&quot;</summary>

```bash
python3 scripts/knowledge.py search "Under the Hood"
```

退出码：0。

```json
{
  "retrieval": "lexical with topic synonyms; read topic catalog if relevant coverage is unclear",
  "results": [
    {
      "match_score": 24,
      "id": "K05-067",
      "title": "Check Period and generation time first in Under the Hood",
      "kind": "code",
      "topic_file": "topic-05.json",
      "when": "When using an Under the Hood report to diagnose recent changes"
    },
    {
      "match_score": 18,
      "id": "K04-091",
      "title": "Under the Hood can help check labels within its report coverage and cohort definitions",
      "kind": "official",
      "topic_file": "topic-04.json",
      "when": "When checking clues about pinned content or account labels"
    },
    {
      "match_score": 18,
      "id": "K05-066",
      "title": "Under the Hood is an officially listed pilot transparency entry point",
      "kind": "official",
      "topic_file": "topic-05.json",
      "when": "When seeking account-visibility clues"
    },
    {
      "match_score": 13,
      "id": "K02-084",
      "title": "Replying under a large account is ineligible for the non-reply mutual-follow bonus",
      "kind": "code",
      "topic_file": "topic-02.json",
      "when": "When a draft uses the mutual-follow coefficient of 20 to prove first comments under large accounts guarantee more exposure."
    },
    {
      "match_score": 9,
      "id": "K01-093",
      "title": "Make research and tutorials understandable on their own and easy to reuse through reposts",
      "kind": "editorial",
      "topic_file": "topic-01.json",
      "when": "When reviewing a summary, tutorial, or long-form piece intended for peers to repost"
    },
    {
      "match_score": 9,
      "id": "K01-096",
      "title": "Reply depth changes Thunder eligibility checks",
      "kind": "code",
      "topic_file": "topic-01.json",
      "when": "When a draft says any old post can be recommended again merely through a reply"
    },
    {
      "match_score": 9,
      "id": "K03-045",
      "title": "The rule filtering unpublished Articles is registered under TimelineHomeHydration",
      "kind": "code",
      "topic_file": "topic-03.json",
      "when": "An Article cannot be accessed through an entry point, or state rules are being explained"
    },
    {
      "match_score": 9,
      "id": "K04-042",
      "title": "A new correction reply under an old post may still be blocked because the parent was seen",
      "kind": "code",
      "topic_file": "topic-04.json",
      "when": "When deciding where to publish an important correction"
    }
  ]
}
```

</details>

<details>
<summary>4. python3 scripts/knowledge.py catalog --topic 00</summary>

```bash
python3 scripts/knowledge.py catalog --topic 00
```

退出码：0。

```json
{
  "snapshot": "5ed796374ea48ee26058aab66ab10c266bea2bef",
  "research_through": "2026-10-29",
  "topics": [
    {
      "file": "topic-00.json",
      "topic": "Report scope and use of evidence",
      "rule_count": 11
    },
    {
      "file": "topic-01.json",
      "topic": "Posting frequency, October updates, recommendation stages, author diversity, threads, prediction weights, and reposts and replies (original report lines 1–438)",
      "rule_count": 97
    },
    {
      "file": "topic-02.json",
      "topic": "Reader matching, reading-related retrieval and dwell modeling, like indexes, bookmarks, follow relationships, profiles, and negative feedback",
      "rule_count": 97
    },
    {
      "file": "topic-03.json",
      "topic": "Long Posts, Articles, lead images, video indexing, and safety-check thresholds",
      "rule_count": 113
    },
    {
      "file": "topic-04.json",
      "topic": "Cold start, FairShare, corrections and older posts, age and editing, reply scoring, multiple layers of reply spam, quote visibility, external links, and pinned posts",
      "rule_count": 102
    },
    {
      "file": "topic-05.json",
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "rule_count": 109
    },
    {
      "file": "topic-06.json",
      "topic": "49 questions still awaiting confirmation",
      "rule_count": 49
    }
  ],
  "rules": [
    {
      "id": "K00-001",
      "title": "Questions awaiting verification should distinguish what is known, the gaps, and the current assessment",
      "kind": "editorial",
      "when": "The answer concerns report completeness, verification records, source dates, or strength of evidence."
    },
    {
      "id": "K00-002",
      "title": "Research snapshots and the report revision date",
      "kind": "editorial",
      "when": "The answer concerns report completeness, verification records, source dates, or strength of evidence."
    },
    {
      "id": "K00-003",
      "title": "How historical parameters and the visibility refactor were checked",
      "kind": "editorial",
      "when": "The answer concerns report completeness, verification records, source dates, or strength of evidence."
    },
    {
      "id": "K00-004",
      "title": "Historical assertion groups must not be combined and presented as official integration tests",
      "kind": "editorial",
      "when": "The answer concerns report completeness, verification records, source dates, or strength of evidence."
    },
    {
      "id": "K00-005",
      "title": "The verification scope of local functions, numeric results, and miniature simulations",
      "kind": "editorial",
      "when": "The answer concerns report completeness, verification records, source dates, or strength of evidence."
    },
    {
      "id": "K00-006",
      "title": "An official recommendation score cannot be calculated from arbitrary body text",
      "kind": "editorial",
      "when": "The answer concerns report completeness, verification records, source dates, or strength of evidence."
    },
    {
      "id": "K00-007",
      "title": "Code facts, examples, and editorial advice have different roles",
      "kind": "editorial",
      "when": "The answer concerns report completeness, verification records, source dates, or strength of evidence."
    },
    {
      "id": "K00-008",
      "title": "The scope of the Article candidate and visibility search",
      "kind": "editorial",
      "when": "The answer concerns report completeness, verification records, source dates, or strength of evidence."
    },
    {
      "id": "K00-009",
      "title": "V5 and V8.2 function checks and cross-version comparisons",
      "kind": "editorial",
      "when": "The answer concerns report completeness, verification records, source dates, or strength of evidence."
    },
    {
      "id": "K00-010",
      "title": "The evidentiary roles of third-party observations and official product materials",
      "kind": "editorial",
      "when": "The answer concerns report completeness, verification records, source dates, or strength of evidence."
    },
    {
      "id": "K00-011",
      "title": "Writing references used to reduce AI-like prose in the original text",
      "kind": "editorial",
      "when": "The answer concerns report completeness, verification records, source dates, or strength of evidence."
    }
  ]
}
```

</details>

<details>
<summary>5. python3 scripts/knowledge.py catalog --topic 05</summary>

```bash
python3 scripts/knowledge.py catalog --topic 05
```

退出码：0。

```json
{
  "snapshot": "5ed796374ea48ee26058aab66ab10c266bea2bef",
  "research_through": "2026-10-29",
  "topics": [
    {
      "file": "topic-00.json",
      "topic": "Report scope and use of evidence",
      "rule_count": 11
    },
    {
      "file": "topic-01.json",
      "topic": "Posting frequency, October updates, recommendation stages, author diversity, threads, prediction weights, and reposts and replies (original report lines 1–438)",
      "rule_count": 97
    },
    {
      "file": "topic-02.json",
      "topic": "Reader matching, reading-related retrieval and dwell modeling, like indexes, bookmarks, follow relationships, profiles, and negative feedback",
      "rule_count": 97
    },
    {
      "file": "topic-03.json",
      "topic": "Long Posts, Articles, lead images, video indexing, and safety-check thresholds",
      "rule_count": 113
    },
    {
      "file": "topic-04.json",
      "topic": "Cold start, FairShare, corrections and older posts, age and editing, reply scoring, multiple layers of reply spam, quote visibility, external links, and pinned posts",
      "rule_count": 102
    },
    {
      "file": "topic-05.json",
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "rule_count": 109
    },
    {
      "file": "topic-06.json",
      "topic": "49 questions still awaiting confirmation",
      "rule_count": 49
    }
  ],
  "rules": [
    {
      "id": "K05-001",
      "title": "Writing labels and applying visibility actions are separate steps",
      "kind": "code",
      "when": "When discussing visibility changes caused by labels"
    },
    {
      "id": "K05-002",
      "title": "Scope of verification for the October 29 visibility update",
      "kind": "observation",
      "when": "When a draft interprets the 606b254 update as expanded safety enforcement"
    },
    {
      "id": "K05-003",
      "title": "insults removes candidates for non-authors at HomeRecommendations",
      "kind": "code",
      "when": "When claims say 'insults only penalizes non-followers' or 'it is removed for every reader'"
    },
    {
      "id": "K05-004",
      "title": "Home Mixer routes safety checks by in_network",
      "kind": "code",
      "when": "When explaining Home display using a single safety rule"
    },
    {
      "id": "K05-005",
      "title": "Attached content has its own visibility-check routing",
      "kind": "code",
      "when": "When explaining why threads, quotes, or reposts display different content"
    },
    {
      "id": "K05-006",
      "title": "TimelineHome lacks the same insults removal rule",
      "kind": "code",
      "when": "When someone expands drop at one entry point into drop at every entry point, or treats allow as guaranteed visibility"
    },
    {
      "id": "K05-007",
      "title": "HomeHydration treatment of insults for non-followers",
      "kind": "code",
      "when": "When discussing non-follower visibility at HomeHydration"
    },
    {
      "id": "K05-008",
      "title": "HomeHydration applies soft intervention for followers",
      "kind": "code",
      "when": "When comparing what followers and unfamiliar readers see"
    },
    {
      "id": "K05-009",
      "title": "HomeHydration shows authors appealable enforcement information",
      "kind": "code",
      "when": "When using what the author sees to judge visibility for all readers"
    },
    {
      "id": "K05-010",
      "title": "allow for one label does not rule out other removal rules",
      "kind": "code",
      "when": "When using a single allow test to guarantee complete visibility"
    },
    {
      "id": "K05-011",
      "title": "Legacy-client fallback can remove for Everyone",
      "kind": "code",
      "when": "When insults enforcement differs between clients"
    },
    {
      "id": "K05-012",
      "title": "The ClientSwitch rewrite did not change the stated FOSNR defaults",
      "kind": "code",
      "when": "When the ClientSwitch rewrite is interpreted as universal removal by default"
    },
    {
      "id": "K05-013",
      "title": "PTOS insults labeling has classification, language, and author conditions",
      "kind": "code",
      "when": "When analyzing whether this branch will write insults for a text"
    },
    {
      "id": "K05-014",
      "title": "PTOS test accounts return PtosReviewed earlier",
      "kind": "code",
      "when": "When explaining why a test account lacks the same label despite the same classification"
    },
    {
      "id": "K05-015",
      "title": "The English-language condition does not establish exemptions for other languages or manual paths",
      "kind": "unknown",
      "when": "When a local language or author exception is treated as a sitewide exemption"
    },
    {
      "id": "K05-016",
      "title": "Criticism should focus on verifiable conditions and numbers",
      "kind": "editorial",
      "when": "When reviewing a critical draft"
    },
    {
      "id": "K05-017",
      "title": "The public-interest warning rule applies to Everyone and has a date condition",
      "kind": "code",
      "when": "When encountering claims that 'lowquality/misinfo warnings apply only to non-followers'"
    },
    {
      "id": "K05-018",
      "title": "MISINFO here specifically denotes four post labels",
      "kind": "code",
      "when": "When checking misinformation labels and interaction restrictions"
    },
    {
      "id": "K05-019",
      "title": "LOW_QUALITY selects NonCompliant as the restriction reason",
      "kind": "code",
      "when": "When deriving interaction restrictions from LOW_QUALITY"
    },
    {
      "id": "K05-020",
      "title": "MISINFO source affects the restriction reason and action scope",
      "kind": "code",
      "when": "When summarizing MISINFO treatment or comparing different sources"
    },
    {
      "id": "K05-021",
      "title": "Final restricted actions are assembled from the feature-switch policy",
      "kind": "code",
      "when": "When answering which buttons are restricted for a particular reader"
    },
    {
      "id": "K05-022",
      "title": "The NonCompliant test action list has a specific scope",
      "kind": "code",
      "when": "When a draft lists actions restricted by NonCompliant"
    },
    {
      "id": "K05-023",
      "title": "Sharing-related behaviors are distinct actions",
      "kind": "code",
      "when": "When a draft uses 'sharing is prohibited' to cover multiple behaviors"
    },
    {
      "id": "K05-024",
      "title": "MISINFO without a source may still restrict interactions through fallback",
      "kind": "code",
      "when": "When a conclusion says 'no source means no interaction restrictions'"
    },
    {
      "id": "K05-025",
      "title": "Post LOW_QUALITY and URL LOW_QUALITY refer to different objects",
      "kind": "code",
      "when": "When ordinary content, incomplete information, or including an external link is equated with the same warning"
    },
    {
      "id": "K05-026",
      "title": "NSFW account states can affect multiple candidates from an author",
      "kind": "code",
      "when": "When recommendation eligibility changes for multiple new posts at once"
    },
    {
      "id": "K05-027",
      "title": "Other named account labels also conditionally remove recommendations",
      "kind": "code",
      "when": "When a report contains spam, compromised, read-only, impersonation, abuse, or do-not-amplify account labels"
    },
    {
      "id": "K05-028",
      "title": "Account-rule audiences and Home entry points are not uniform",
      "kind": "code",
      "when": "When every account label is summarized as having one effect"
    },
    {
      "id": "K05-029",
      "title": "Official account-label explanations do not imply invisibility at every entry point",
      "kind": "official",
      "when": "When an official label explanation is rewritten as all external reach falling to zero"
    },
    {
      "id": "K05-030",
      "title": "Keep account-label records when multiple posts lose unfamiliar-audience reach",
      "kind": "editorial",
      "when": "When reach declines across multiple pieces of content"
    },
    {
      "id": "K05-031",
      "title": "Complete public defaults for three-of-five aggregation",
      "kind": "code",
      "when": "When a draft says 'three adult images among the last five images' or a similar threshold"
    },
    {
      "id": "K05-032",
      "title": "Take the first five reverse-ordered userTimeline records before filtering age and labels",
      "kind": "code",
      "when": "When manually calculating three-of-five or explaining 'recent'"
    },
    {
      "id": "K05-033",
      "title": "The five-record counting example preserves post units and assumptions",
      "kind": "editorial",
      "when": "When explaining the counting unit in three-of-five"
    },
    {
      "id": "K05-034",
      "title": "take(5) does not require five records to be present first",
      "kind": "code",
      "when": "When explaining samples with fewer than five records or converting three-of-five into a ratio"
    },
    {
      "id": "K05-035",
      "title": "Aggregation is triggered by an Applied label event whose post must be within sixty days",
      "kind": "code",
      "when": "When assuming aggregation necessarily runs on every ordinary post or changes immediately on the third post"
    },
    {
      "id": "K05-036",
      "title": "Reposts use the original post's labels but the timeline record's ID for age",
      "kind": "code",
      "when": "When someone assumes aggregation ignores reposts or directly uses the original post's date"
    },
    {
      "id": "K05-037",
      "title": "The processor cannot establish complete timeline retention, deletion, or pagination behavior",
      "kind": "unknown",
      "when": "When the user's manual post count differs from the expected aggregation result"
    },
    {
      "id": "K05-038",
      "title": "Three-of-five excludes nsfwAdmin and accounts already carrying the same label",
      "kind": "code",
      "when": "When inferring repeated account labeling solely from three labeled posts"
    },
    {
      "id": "K05-039",
      "title": "Three-of-five does not enable nsfwUser or high-PageRank/gray-badge exclusions",
      "kind": "code",
      "when": "When citing other bots' eligibility to explain three-of-five"
    },
    {
      "id": "K05-040",
      "title": "Three-of-five writes account NSFW_HIGH_PRECISION with a seven-day TTL",
      "kind": "code",
      "when": "When reviewing 'how long the three-of-five label lasts'"
    },
    {
      "id": "K05-041",
      "title": "Excluding an existing same-named label prevents a simple per-match renewal inference",
      "kind": "code",
      "when": "When calculating expiration after repeated matches"
    },
    {
      "id": "K05-042",
      "title": "Aggregation has a ten-minute delay and a twenty-minute maxLag target",
      "kind": "code",
      "when": "When explaining when labels take effect or promising real-time penalties"
    },
    {
      "id": "K05-043",
      "title": "Feature-switch configuration can override the three-of-five default",
      "kind": "code",
      "when": "When the five-post rule is presented as uniform for all accounts at all times"
    },
    {
      "id": "K05-044",
      "title": "The ten/eleven possibly_nsfw_account default is unreachable",
      "kind": "code",
      "when": "When enabled=true is used to assert that this default penalizes, or unreachability is used to assert the label never appears"
    },
    {
      "id": "K05-045",
      "title": "The earlier NSFW media HLL path differs from the three-of-five timeline path",
      "kind": "code",
      "when": "When a one-day threshold, media scores, or exemptions are mixed into three-of-five"
    },
    {
      "id": "K05-046",
      "title": "Aggregation-label investigations should retain post, account, and date records",
      "kind": "editorial",
      "when": "When aggregation-related account labels appear in a report"
    },
    {
      "id": "K05-047",
      "title": "The duplicate-text bot processes general and CJK scheduled clusters",
      "kind": "code",
      "when": "When reviewing whether Chinese duplicate content enters processing scope"
    },
    {
      "id": "K05-048",
      "title": "Duplicate-text processing also has replies jobs",
      "kind": "code",
      "when": "When someone asserts that copying only in replies avoids duplicate-content processing"
    },
    {
      "id": "K05-049",
      "title": "Duplicate-cluster similarity, count, and text-length thresholds have not been fully traced",
      "kind": "unknown",
      "when": "When a draft proposes repetition-count, text-length, or similarity penalty formulas"
    },
    {
      "id": "K05-050",
      "title": "COPYPASTA writing has post-eligibility and data-retrieval return conditions",
      "kind": "code",
      "when": "When inferring every post in a cluster has been labeled"
    },
    {
      "id": "K05-051",
      "title": "COPYPASTA writing also depends on author exceptions and rate limits",
      "kind": "code",
      "when": "When explaining a cluster without an observed label"
    },
    {
      "id": "K05-052",
      "title": "The downstream exposure effects of COPYPASTA_SPAM remain incompletely verified",
      "kind": "unknown",
      "when": "When a COPYPASTA label is immediately used to calculate demotion or zero exposure"
    },
    {
      "id": "K05-053",
      "title": "Reusing old material should add information needed for the current question",
      "kind": "editorial",
      "when": "When reviewing copied promotions, citations of old posts, or repeated replies"
    },
    {
      "id": "K05-054",
      "title": "Three engagement-spam classes directly set should_label_for_spam to true",
      "kind": "code",
      "when": "When reviewing code interpretations of engagement baiting, engagement farming, or card manipulation"
    },
    {
      "id": "K05-055",
      "title": "Other non-NoViolation Spam classes separately check author eligibility",
      "kind": "code",
      "when": "When a draft presents author exceptions as identical across all Spam classes"
    },
    {
      "id": "K05-056",
      "title": "The high-PageRank condition cannot be rewritten as a follower-count threshold",
      "kind": "code",
      "when": "When account size is used to explain exemptions or guaranteed penalties for the three classes"
    },
    {
      "id": "K05-057",
      "title": "PTOS Spam writing requires production, while test accounts return earlier",
      "kind": "code",
      "when": "When the three special Spam assignments are described as unconditional penalties"
    },
    {
      "id": "K05-058",
      "title": "Unpublished Spam prompts cannot yield a list of guaranteed-penalty phrases",
      "kind": "unknown",
      "when": "When determining whether a call for engagement necessarily incurs a penalty"
    },
    {
      "id": "K05-059",
      "title": "Use engagement questions to help continue checking the content",
      "kind": "editorial",
      "when": "When reviewing a closing CTA or invitation to comment"
    },
    {
      "id": "K05-060",
      "title": "SpamHashTagAbuse is a spam class with conditional label writing",
      "kind": "code",
      "when": "When discussing the risk of hashtag stuffing"
    },
    {
      "id": "K05-061",
      "title": "Advice to limit hashtags is not proof of zero value or a uniform deduction formula",
      "kind": "myth",
      "when": "When reviewing claims that all hashtags have zero value or incur count-based penalties"
    },
    {
      "id": "K05-062",
      "title": "CLICK_HASHTAG behavior can be an input to Phoenix",
      "kind": "code",
      "when": "When someone asserts the system completely ignores hashtags or calculates bonuses by count"
    },
    {
      "id": "K05-063",
      "title": "Four hashtags is the selection limit of one extractor",
      "kind": "code",
      "when": "When MaxHashtagsPerTweet is used to prove a universally optimal count"
    },
    {
      "id": "K05-064",
      "title": "Choose hashtags directly related to the topic or event",
      "kind": "editorial",
      "when": "When reviewing hashtags alongside the body"
    },
    {
      "id": "K05-065",
      "title": "A few dozen views alone cannot diagnose low reach",
      "kind": "unknown",
      "when": "When explaining low views for a post"
    },
    {
      "id": "K05-066",
      "title": "Under the Hood is an officially listed pilot transparency entry point",
      "kind": "official",
      "when": "When seeking account-visibility clues"
    },
    {
      "id": "K05-067",
      "title": "Check Period and generation time first in Under the Hood",
      "kind": "code",
      "when": "When using an Under the Hood report to diagnose recent changes"
    },
    {
      "id": "K05-068",
      "title": "Report eligibility and recommendation eligibility are separate conditions",
      "kind": "code",
      "when": "When a user lacks a report or the entry point is unavailable"
    },
    {
      "id": "K05-069",
      "title": "Post labels counts labeled eligible posts in the reported authored-post cohort",
      "kind": "code",
      "when": "When explaining a Post labels percentage"
    },
    {
      "id": "K05-070",
      "title": "Account labels counts labeled days and their proportion",
      "kind": "code",
      "when": "When explaining an Account labels percentage"
    },
    {
      "id": "K05-071",
      "title": "Three of forty posts, or 7.5%, is not an exposure-loss rate",
      "kind": "editorial",
      "when": "When annotating Post labels figures"
    },
    {
      "id": "K05-072",
      "title": "Five of thirty-one days does not mean five days of complete invisibility",
      "kind": "editorial",
      "when": "When annotating Account labels duration"
    },
    {
      "id": "K05-073",
      "title": "Read What it means together with Effect on visibility",
      "kind": "official",
      "when": "When organizing or explaining a visibility report"
    },
    {
      "id": "K05-074",
      "title": "A follower friend opening the post does not rule out non-follower recommendation restrictions",
      "kind": "editorial",
      "when": "When a friend's ability to open a post or a label's existence is used to judge sitewide status"
    },
    {
      "id": "K05-075",
      "title": "Save reports and align concurrent changes before correcting or appealing",
      "kind": "editorial",
      "when": "When a report lists relevant labels"
    },
    {
      "id": "K05-076",
      "title": "An empty report means only that this report lists no relevant records",
      "kind": "unknown",
      "when": "When an empty report is used to prove there are no recommendation issues whatsoever"
    },
    {
      "id": "K05-077",
      "title": "Content can still be improved item by item when visibility clues are absent",
      "kind": "editorial",
      "when": "When views are low but the report offers no clear clues"
    },
    {
      "id": "K05-078",
      "title": "Choose only one main change per comparison",
      "kind": "editorial",
      "when": "When designing the next posting comparison"
    },
    {
      "id": "K05-079",
      "title": "Use actual analytics fields and preserve missing values",
      "kind": "editorial",
      "when": "When building a posting-analytics record"
    },
    {
      "id": "K05-080",
      "title": "Views are not deduplicated audience, and thread views cannot be summed as people",
      "kind": "official",
      "when": "When summarizing thread performance or estimating unique readers"
    },
    {
      "id": "K05-081",
      "title": "Comparison records should first retain content identity and publishing conditions",
      "kind": "editorial",
      "when": "When building a minimal posting-comparison table"
    },
    {
      "id": "K05-082",
      "title": "24 and 48 hours are consistent observation points, not independent samples",
      "kind": "editorial",
      "when": "When comparing performance after publication"
    },
    {
      "id": "K05-083",
      "title": "Record shares, replies, profile clicks, follows, and similar metrics by definition; do not fill missing values with zero",
      "kind": "editorial",
      "when": "When cleaning an analytics table or comparing metrics across posts"
    },
    {
      "id": "K05-084",
      "title": "Account-goal outcomes can supplement exposure metrics",
      "kind": "editorial",
      "when": "When deciding which topics or content formats to retain"
    },
    {
      "id": "K05-085",
      "title": "Record trending events, revisions, and known labels as comparison context",
      "kind": "editorial",
      "when": "When numbers rise or fall after an edit"
    },
    {
      "id": "K05-086",
      "title": "Use distributions and medians across posts so a viral post does not dominate",
      "kind": "editorial",
      "when": "When comparing overall performance across topics, formats, or changes"
    },
    {
      "id": "K05-087",
      "title": "Each impression cannot be treated as an independent random experimental sample",
      "kind": "editorial",
      "when": "When assessing whether differences are stable or causal"
    },
    {
      "id": "K05-088",
      "title": "With enough samples, bootstrap intervals at the post level",
      "kind": "editorial",
      "when": "When adding uncertainty estimates to a multiple-post comparison"
    },
    {
      "id": "K05-089",
      "title": "A one-month observation schedule has four stages",
      "kind": "editorial",
      "when": "When starting a content-observation cycle"
    },
    {
      "id": "K05-090",
      "title": "One post daily or three to five weekly is only an experimental starting point",
      "kind": "editorial",
      "when": "When a user asks how many posts to publish daily or a draft claims rewards for a fixed frequency"
    },
    {
      "id": "K05-091",
      "title": "The OCR publishing example is only an organizational hypothetical using one batch of Chinese invoices",
      "kind": "editorial",
      "when": "When turning the OCR example into a publishable article"
    },
    {
      "id": "K05-092",
      "title": "The OCR opening should serve tool selection and manual-verification tasks",
      "kind": "editorial",
      "when": "When drafting an OCR test's title and opening"
    },
    {
      "id": "K05-093",
      "title": "The complete OCR opening draft retains scope, input, and usage guidance",
      "kind": "editorial",
      "when": "When a concrete, usable test-opening example is needed"
    },
    {
      "id": "K05-094",
      "title": "Test methods should list sample count, version, date, quality, and evaluation method",
      "kind": "editorial",
      "when": "When reviewing a comparison test's verifiability"
    },
    {
      "id": "K05-095",
      "title": "Use a representative error-versus-correct comparison in the first image and label conditions",
      "kind": "editorial",
      "when": "When selecting the first image for an OCR test"
    },
    {
      "id": "K05-096",
      "title": "Choose a single post, long article, or three-post summary thread by evidence volume",
      "kind": "editorial",
      "when": "When choosing a comparison test's publishing format"
    },
    {
      "id": "K05-097",
      "title": "Each summary-thread post should stand alone, with core data not confined to the middle",
      "kind": "editorial",
      "when": "When reviewing individual-post comprehensibility in a long thread"
    },
    {
      "id": "K05-098",
      "title": "Examples and conditions promised in the opening must appear in the body",
      "kind": "editorial",
      "when": "When reviewing promise fulfillment and delaying paragraphs in a test article"
    },
    {
      "id": "K05-099",
      "title": "Every middle paragraph should add information, with conditions beside conclusions",
      "kind": "editorial",
      "when": "When shortening or improving the middle of a long test article"
    },
    {
      "id": "K05-100",
      "title": "CREAD cannot choose an article's optimal word count or paragraphing",
      "kind": "editorial",
      "when": "When CREAD is used to justify length rules"
    },
    {
      "id": "K05-101",
      "title": "Access to complete comparison materials should deliver promised content and disclose barriers in advance",
      "kind": "editorial",
      "when": "When publishing a test article linking externally to complete materials"
    },
    {
      "id": "K05-102",
      "title": "Recheck the destination page and link purpose after pinning",
      "kind": "editorial",
      "when": "When updating a bio or pinned post, or checking long-term access to materials"
    },
    {
      "id": "K05-103",
      "title": "Schedule publication around primary readers' time zones and habits",
      "kind": "editorial",
      "when": "When choosing publication times or explaining late-night posting"
    },
    {
      "id": "K05-104",
      "title": "Public views cannot calculate the remainder of a 200-view Home quota",
      "kind": "myth",
      "when": "When public numbers are treated as a cold-start progress bar"
    },
    {
      "id": "K05-105",
      "title": "Reusability, relayability, and accessibility each have independent content value",
      "kind": "editorial",
      "when": "When assessing whether content merits bookmarking, sharing, or long-term maintenance"
    },
    {
      "id": "K05-106",
      "title": "Verify questions after publication and publish conclusion-changing findings as separate updates",
      "kind": "editorial",
      "when": "When receiving reader questions, counterexamples, or corrections"
    },
    {
      "id": "K05-107",
      "title": "Keep distribution duration similar in the next comparison and acknowledge remaining changes",
      "kind": "editorial",
      "when": "When reviewing the next round of first-image or summary changes"
    },
    {
      "id": "K05-108",
      "title": "Whether to publish a third post depends on new information and correction needs",
      "kind": "editorial",
      "when": "When deciding whether to keep publishing on the same day"
    },
    {
      "id": "K05-109",
      "title": "Finally check the first image and opening from an unfamiliar reader's perspective",
      "kind": "editorial",
      "when": "When completing the final prepublication check"
    }
  ]
}
```

</details>

<details>
<summary>6. python3 scripts/knowledge.py catalog --topic 05</summary>

```bash
python3 scripts/knowledge.py catalog --topic 05
```

退出码：0。

```json
{
  "snapshot": "5ed796374ea48ee26058aab66ab10c266bea2bef",
  "research_through": "2026-10-29",
  "topics": [
    {
      "file": "topic-00.json",
      "topic": "Report scope and use of evidence",
      "rule_count": 11
    },
    {
      "file": "topic-01.json",
      "topic": "Posting frequency, October updates, recommendation stages, author diversity, threads, prediction weights, and reposts and replies (original report lines 1–438)",
      "rule_count": 97
    },
    {
      "file": "topic-02.json",
      "topic": "Reader matching, reading-related retrieval and dwell modeling, like indexes, bookmarks, follow relationships, profiles, and negative feedback",
      "rule_count": 97
    },
    {
      "file": "topic-03.json",
      "topic": "Long Posts, Articles, lead images, video indexing, and safety-check thresholds",
      "rule_count": 113
    },
    {
      "file": "topic-04.json",
      "topic": "Cold start, FairShare, corrections and older posts, age and editing, reply scoring, multiple layers of reply spam, quote visibility, external links, and pinned posts",
      "rule_count": 102
    },
    {
      "file": "topic-05.json",
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "rule_count": 109
    },
    {
      "file": "topic-06.json",
      "topic": "49 questions still awaiting confirmation",
      "rule_count": 49
    }
  ],
  "rules": [
    {
      "id": "K05-001",
      "title": "Writing labels and applying visibility actions are separate steps",
      "kind": "code",
      "when": "When discussing visibility changes caused by labels"
    },
    {
      "id": "K05-002",
      "title": "Scope of verification for the October 29 visibility update",
      "kind": "observation",
      "when": "When a draft interprets the 606b254 update as expanded safety enforcement"
    },
    {
      "id": "K05-003",
      "title": "insults removes candidates for non-authors at HomeRecommendations",
      "kind": "code",
      "when": "When claims say 'insults only penalizes non-followers' or 'it is removed for every reader'"
    },
    {
      "id": "K05-004",
      "title": "Home Mixer routes safety checks by in_network",
      "kind": "code",
      "when": "When explaining Home display using a single safety rule"
    },
    {
      "id": "K05-005",
      "title": "Attached content has its own visibility-check routing",
      "kind": "code",
      "when": "When explaining why threads, quotes, or reposts display different content"
    },
    {
      "id": "K05-006",
      "title": "TimelineHome lacks the same insults removal rule",
      "kind": "code",
      "when": "When someone expands drop at one entry point into drop at every entry point, or treats allow as guaranteed visibility"
    },
    {
      "id": "K05-007",
      "title": "HomeHydration treatment of insults for non-followers",
      "kind": "code",
      "when": "When discussing non-follower visibility at HomeHydration"
    },
    {
      "id": "K05-008",
      "title": "HomeHydration applies soft intervention for followers",
      "kind": "code",
      "when": "When comparing what followers and unfamiliar readers see"
    },
    {
      "id": "K05-009",
      "title": "HomeHydration shows authors appealable enforcement information",
      "kind": "code",
      "when": "When using what the author sees to judge visibility for all readers"
    },
    {
      "id": "K05-010",
      "title": "allow for one label does not rule out other removal rules",
      "kind": "code",
      "when": "When using a single allow test to guarantee complete visibility"
    },
    {
      "id": "K05-011",
      "title": "Legacy-client fallback can remove for Everyone",
      "kind": "code",
      "when": "When insults enforcement differs between clients"
    },
    {
      "id": "K05-012",
      "title": "The ClientSwitch rewrite did not change the stated FOSNR defaults",
      "kind": "code",
      "when": "When the ClientSwitch rewrite is interpreted as universal removal by default"
    },
    {
      "id": "K05-013",
      "title": "PTOS insults labeling has classification, language, and author conditions",
      "kind": "code",
      "when": "When analyzing whether this branch will write insults for a text"
    },
    {
      "id": "K05-014",
      "title": "PTOS test accounts return PtosReviewed earlier",
      "kind": "code",
      "when": "When explaining why a test account lacks the same label despite the same classification"
    },
    {
      "id": "K05-015",
      "title": "The English-language condition does not establish exemptions for other languages or manual paths",
      "kind": "unknown",
      "when": "When a local language or author exception is treated as a sitewide exemption"
    },
    {
      "id": "K05-016",
      "title": "Criticism should focus on verifiable conditions and numbers",
      "kind": "editorial",
      "when": "When reviewing a critical draft"
    },
    {
      "id": "K05-017",
      "title": "The public-interest warning rule applies to Everyone and has a date condition",
      "kind": "code",
      "when": "When encountering claims that 'lowquality/misinfo warnings apply only to non-followers'"
    },
    {
      "id": "K05-018",
      "title": "MISINFO here specifically denotes four post labels",
      "kind": "code",
      "when": "When checking misinformation labels and interaction restrictions"
    },
    {
      "id": "K05-019",
      "title": "LOW_QUALITY selects NonCompliant as the restriction reason",
      "kind": "code",
      "when": "When deriving interaction restrictions from LOW_QUALITY"
    },
    {
      "id": "K05-020",
      "title": "MISINFO source affects the restriction reason and action scope",
      "kind": "code",
      "when": "When summarizing MISINFO treatment or comparing different sources"
    },
    {
      "id": "K05-021",
      "title": "Final restricted actions are assembled from the feature-switch policy",
      "kind": "code",
      "when": "When answering which buttons are restricted for a particular reader"
    },
    {
      "id": "K05-022",
      "title": "The NonCompliant test action list has a specific scope",
      "kind": "code",
      "when": "When a draft lists actions restricted by NonCompliant"
    },
    {
      "id": "K05-023",
      "title": "Sharing-related behaviors are distinct actions",
      "kind": "code",
      "when": "When a draft uses 'sharing is prohibited' to cover multiple behaviors"
    },
    {
      "id": "K05-024",
      "title": "MISINFO without a source may still restrict interactions through fallback",
      "kind": "code",
      "when": "When a conclusion says 'no source means no interaction restrictions'"
    },
    {
      "id": "K05-025",
      "title": "Post LOW_QUALITY and URL LOW_QUALITY refer to different objects",
      "kind": "code",
      "when": "When ordinary content, incomplete information, or including an external link is equated with the same warning"
    },
    {
      "id": "K05-026",
      "title": "NSFW account states can affect multiple candidates from an author",
      "kind": "code",
      "when": "When recommendation eligibility changes for multiple new posts at once"
    },
    {
      "id": "K05-027",
      "title": "Other named account labels also conditionally remove recommendations",
      "kind": "code",
      "when": "When a report contains spam, compromised, read-only, impersonation, abuse, or do-not-amplify account labels"
    },
    {
      "id": "K05-028",
      "title": "Account-rule audiences and Home entry points are not uniform",
      "kind": "code",
      "when": "When every account label is summarized as having one effect"
    },
    {
      "id": "K05-029",
      "title": "Official account-label explanations do not imply invisibility at every entry point",
      "kind": "official",
      "when": "When an official label explanation is rewritten as all external reach falling to zero"
    },
    {
      "id": "K05-030",
      "title": "Keep account-label records when multiple posts lose unfamiliar-audience reach",
      "kind": "editorial",
      "when": "When reach declines across multiple pieces of content"
    },
    {
      "id": "K05-031",
      "title": "Complete public defaults for three-of-five aggregation",
      "kind": "code",
      "when": "When a draft says 'three adult images among the last five images' or a similar threshold"
    },
    {
      "id": "K05-032",
      "title": "Take the first five reverse-ordered userTimeline records before filtering age and labels",
      "kind": "code",
      "when": "When manually calculating three-of-five or explaining 'recent'"
    },
    {
      "id": "K05-033",
      "title": "The five-record counting example preserves post units and assumptions",
      "kind": "editorial",
      "when": "When explaining the counting unit in three-of-five"
    },
    {
      "id": "K05-034",
      "title": "take(5) does not require five records to be present first",
      "kind": "code",
      "when": "When explaining samples with fewer than five records or converting three-of-five into a ratio"
    },
    {
      "id": "K05-035",
      "title": "Aggregation is triggered by an Applied label event whose post must be within sixty days",
      "kind": "code",
      "when": "When assuming aggregation necessarily runs on every ordinary post or changes immediately on the third post"
    },
    {
      "id": "K05-036",
      "title": "Reposts use the original post's labels but the timeline record's ID for age",
      "kind": "code",
      "when": "When someone assumes aggregation ignores reposts or directly uses the original post's date"
    },
    {
      "id": "K05-037",
      "title": "The processor cannot establish complete timeline retention, deletion, or pagination behavior",
      "kind": "unknown",
      "when": "When the user's manual post count differs from the expected aggregation result"
    },
    {
      "id": "K05-038",
      "title": "Three-of-five excludes nsfwAdmin and accounts already carrying the same label",
      "kind": "code",
      "when": "When inferring repeated account labeling solely from three labeled posts"
    },
    {
      "id": "K05-039",
      "title": "Three-of-five does not enable nsfwUser or high-PageRank/gray-badge exclusions",
      "kind": "code",
      "when": "When citing other bots' eligibility to explain three-of-five"
    },
    {
      "id": "K05-040",
      "title": "Three-of-five writes account NSFW_HIGH_PRECISION with a seven-day TTL",
      "kind": "code",
      "when": "When reviewing 'how long the three-of-five label lasts'"
    },
    {
      "id": "K05-041",
      "title": "Excluding an existing same-named label prevents a simple per-match renewal inference",
      "kind": "code",
      "when": "When calculating expiration after repeated matches"
    },
    {
      "id": "K05-042",
      "title": "Aggregation has a ten-minute delay and a twenty-minute maxLag target",
      "kind": "code",
      "when": "When explaining when labels take effect or promising real-time penalties"
    },
    {
      "id": "K05-043",
      "title": "Feature-switch configuration can override the three-of-five default",
      "kind": "code",
      "when": "When the five-post rule is presented as uniform for all accounts at all times"
    },
    {
      "id": "K05-044",
      "title": "The ten/eleven possibly_nsfw_account default is unreachable",
      "kind": "code",
      "when": "When enabled=true is used to assert that this default penalizes, or unreachability is used to assert the label never appears"
    },
    {
      "id": "K05-045",
      "title": "The earlier NSFW media HLL path differs from the three-of-five timeline path",
      "kind": "code",
      "when": "When a one-day threshold, media scores, or exemptions are mixed into three-of-five"
    },
    {
      "id": "K05-046",
      "title": "Aggregation-label investigations should retain post, account, and date records",
      "kind": "editorial",
      "when": "When aggregation-related account labels appear in a report"
    },
    {
      "id": "K05-047",
      "title": "The duplicate-text bot processes general and CJK scheduled clusters",
      "kind": "code",
      "when": "When reviewing whether Chinese duplicate content enters processing scope"
    },
    {
      "id": "K05-048",
      "title": "Duplicate-text processing also has replies jobs",
      "kind": "code",
      "when": "When someone asserts that copying only in replies avoids duplicate-content processing"
    },
    {
      "id": "K05-049",
      "title": "Duplicate-cluster similarity, count, and text-length thresholds have not been fully traced",
      "kind": "unknown",
      "when": "When a draft proposes repetition-count, text-length, or similarity penalty formulas"
    },
    {
      "id": "K05-050",
      "title": "COPYPASTA writing has post-eligibility and data-retrieval return conditions",
      "kind": "code",
      "when": "When inferring every post in a cluster has been labeled"
    },
    {
      "id": "K05-051",
      "title": "COPYPASTA writing also depends on author exceptions and rate limits",
      "kind": "code",
      "when": "When explaining a cluster without an observed label"
    },
    {
      "id": "K05-052",
      "title": "The downstream exposure effects of COPYPASTA_SPAM remain incompletely verified",
      "kind": "unknown",
      "when": "When a COPYPASTA label is immediately used to calculate demotion or zero exposure"
    },
    {
      "id": "K05-053",
      "title": "Reusing old material should add information needed for the current question",
      "kind": "editorial",
      "when": "When reviewing copied promotions, citations of old posts, or repeated replies"
    },
    {
      "id": "K05-054",
      "title": "Three engagement-spam classes directly set should_label_for_spam to true",
      "kind": "code",
      "when": "When reviewing code interpretations of engagement baiting, engagement farming, or card manipulation"
    },
    {
      "id": "K05-055",
      "title": "Other non-NoViolation Spam classes separately check author eligibility",
      "kind": "code",
      "when": "When a draft presents author exceptions as identical across all Spam classes"
    },
    {
      "id": "K05-056",
      "title": "The high-PageRank condition cannot be rewritten as a follower-count threshold",
      "kind": "code",
      "when": "When account size is used to explain exemptions or guaranteed penalties for the three classes"
    },
    {
      "id": "K05-057",
      "title": "PTOS Spam writing requires production, while test accounts return earlier",
      "kind": "code",
      "when": "When the three special Spam assignments are described as unconditional penalties"
    },
    {
      "id": "K05-058",
      "title": "Unpublished Spam prompts cannot yield a list of guaranteed-penalty phrases",
      "kind": "unknown",
      "when": "When determining whether a call for engagement necessarily incurs a penalty"
    },
    {
      "id": "K05-059",
      "title": "Use engagement questions to help continue checking the content",
      "kind": "editorial",
      "when": "When reviewing a closing CTA or invitation to comment"
    },
    {
      "id": "K05-060",
      "title": "SpamHashTagAbuse is a spam class with conditional label writing",
      "kind": "code",
      "when": "When discussing the risk of hashtag stuffing"
    },
    {
      "id": "K05-061",
      "title": "Advice to limit hashtags is not proof of zero value or a uniform deduction formula",
      "kind": "myth",
      "when": "When reviewing claims that all hashtags have zero value or incur count-based penalties"
    },
    {
      "id": "K05-062",
      "title": "CLICK_HASHTAG behavior can be an input to Phoenix",
      "kind": "code",
      "when": "When someone asserts the system completely ignores hashtags or calculates bonuses by count"
    },
    {
      "id": "K05-063",
      "title": "Four hashtags is the selection limit of one extractor",
      "kind": "code",
      "when": "When MaxHashtagsPerTweet is used to prove a universally optimal count"
    },
    {
      "id": "K05-064",
      "title": "Choose hashtags directly related to the topic or event",
      "kind": "editorial",
      "when": "When reviewing hashtags alongside the body"
    },
    {
      "id": "K05-065",
      "title": "A few dozen views alone cannot diagnose low reach",
      "kind": "unknown",
      "when": "When explaining low views for a post"
    },
    {
      "id": "K05-066",
      "title": "Under the Hood is an officially listed pilot transparency entry point",
      "kind": "official",
      "when": "When seeking account-visibility clues"
    },
    {
      "id": "K05-067",
      "title": "Check Period and generation time first in Under the Hood",
      "kind": "code",
      "when": "When using an Under the Hood report to diagnose recent changes"
    },
    {
      "id": "K05-068",
      "title": "Report eligibility and recommendation eligibility are separate conditions",
      "kind": "code",
      "when": "When a user lacks a report or the entry point is unavailable"
    },
    {
      "id": "K05-069",
      "title": "Post labels counts labeled eligible posts in the reported authored-post cohort",
      "kind": "code",
      "when": "When explaining a Post labels percentage"
    },
    {
      "id": "K05-070",
      "title": "Account labels counts labeled days and their proportion",
      "kind": "code",
      "when": "When explaining an Account labels percentage"
    },
    {
      "id": "K05-071",
      "title": "Three of forty posts, or 7.5%, is not an exposure-loss rate",
      "kind": "editorial",
      "when": "When annotating Post labels figures"
    },
    {
      "id": "K05-072",
      "title": "Five of thirty-one days does not mean five days of complete invisibility",
      "kind": "editorial",
      "when": "When annotating Account labels duration"
    },
    {
      "id": "K05-073",
      "title": "Read What it means together with Effect on visibility",
      "kind": "official",
      "when": "When organizing or explaining a visibility report"
    },
    {
      "id": "K05-074",
      "title": "A follower friend opening the post does not rule out non-follower recommendation restrictions",
      "kind": "editorial",
      "when": "When a friend's ability to open a post or a label's existence is used to judge sitewide status"
    },
    {
      "id": "K05-075",
      "title": "Save reports and align concurrent changes before correcting or appealing",
      "kind": "editorial",
      "when": "When a report lists relevant labels"
    },
    {
      "id": "K05-076",
      "title": "An empty report means only that this report lists no relevant records",
      "kind": "unknown",
      "when": "When an empty report is used to prove there are no recommendation issues whatsoever"
    },
    {
      "id": "K05-077",
      "title": "Content can still be improved item by item when visibility clues are absent",
      "kind": "editorial",
      "when": "When views are low but the report offers no clear clues"
    },
    {
      "id": "K05-078",
      "title": "Choose only one main change per comparison",
      "kind": "editorial",
      "when": "When designing the next posting comparison"
    },
    {
      "id": "K05-079",
      "title": "Use actual analytics fields and preserve missing values",
      "kind": "editorial",
      "when": "When building a posting-analytics record"
    },
    {
      "id": "K05-080",
      "title": "Views are not deduplicated audience, and thread views cannot be summed as people",
      "kind": "official",
      "when": "When summarizing thread performance or estimating unique readers"
    },
    {
      "id": "K05-081",
      "title": "Comparison records should first retain content identity and publishing conditions",
      "kind": "editorial",
      "when": "When building a minimal posting-comparison table"
    },
    {
      "id": "K05-082",
      "title": "24 and 48 hours are consistent observation points, not independent samples",
      "kind": "editorial",
      "when": "When comparing performance after publication"
    },
    {
      "id": "K05-083",
      "title": "Record shares, replies, profile clicks, follows, and similar metrics by definition; do not fill missing values with zero",
      "kind": "editorial",
      "when": "When cleaning an analytics table or comparing metrics across posts"
    },
    {
      "id": "K05-084",
      "title": "Account-goal outcomes can supplement exposure metrics",
      "kind": "editorial",
      "when": "When deciding which topics or content formats to retain"
    },
    {
      "id": "K05-085",
      "title": "Record trending events, revisions, and known labels as comparison context",
      "kind": "editorial",
      "when": "When numbers rise or fall after an edit"
    },
    {
      "id": "K05-086",
      "title": "Use distributions and medians across posts so a viral post does not dominate",
      "kind": "editorial",
      "when": "When comparing overall performance across topics, formats, or changes"
    },
    {
      "id": "K05-087",
      "title": "Each impression cannot be treated as an independent random experimental sample",
      "kind": "editorial",
      "when": "When assessing whether differences are stable or causal"
    },
    {
      "id": "K05-088",
      "title": "With enough samples, bootstrap intervals at the post level",
      "kind": "editorial",
      "when": "When adding uncertainty estimates to a multiple-post comparison"
    },
    {
      "id": "K05-089",
      "title": "A one-month observation schedule has four stages",
      "kind": "editorial",
      "when": "When starting a content-observation cycle"
    },
    {
      "id": "K05-090",
      "title": "One post daily or three to five weekly is only an experimental starting point",
      "kind": "editorial",
      "when": "When a user asks how many posts to publish daily or a draft claims rewards for a fixed frequency"
    },
    {
      "id": "K05-091",
      "title": "The OCR publishing example is only an organizational hypothetical using one batch of Chinese invoices",
      "kind": "editorial",
      "when": "When turning the OCR example into a publishable article"
    },
    {
      "id": "K05-092",
      "title": "The OCR opening should serve tool selection and manual-verification tasks",
      "kind": "editorial",
      "when": "When drafting an OCR test's title and opening"
    },
    {
      "id": "K05-093",
      "title": "The complete OCR opening draft retains scope, input, and usage guidance",
      "kind": "editorial",
      "when": "When a concrete, usable test-opening example is needed"
    },
    {
      "id": "K05-094",
      "title": "Test methods should list sample count, version, date, quality, and evaluation method",
      "kind": "editorial",
      "when": "When reviewing a comparison test's verifiability"
    },
    {
      "id": "K05-095",
      "title": "Use a representative error-versus-correct comparison in the first image and label conditions",
      "kind": "editorial",
      "when": "When selecting the first image for an OCR test"
    },
    {
      "id": "K05-096",
      "title": "Choose a single post, long article, or three-post summary thread by evidence volume",
      "kind": "editorial",
      "when": "When choosing a comparison test's publishing format"
    },
    {
      "id": "K05-097",
      "title": "Each summary-thread post should stand alone, with core data not confined to the middle",
      "kind": "editorial",
      "when": "When reviewing individual-post comprehensibility in a long thread"
    },
    {
      "id": "K05-098",
      "title": "Examples and conditions promised in the opening must appear in the body",
      "kind": "editorial",
      "when": "When reviewing promise fulfillment and delaying paragraphs in a test article"
    },
    {
      "id": "K05-099",
      "title": "Every middle paragraph should add information, with conditions beside conclusions",
      "kind": "editorial",
      "when": "When shortening or improving the middle of a long test article"
    },
    {
      "id": "K05-100",
      "title": "CREAD cannot choose an article's optimal word count or paragraphing",
      "kind": "editorial",
      "when": "When CREAD is used to justify length rules"
    },
    {
      "id": "K05-101",
      "title": "Access to complete comparison materials should deliver promised content and disclose barriers in advance",
      "kind": "editorial",
      "when": "When publishing a test article linking externally to complete materials"
    },
    {
      "id": "K05-102",
      "title": "Recheck the destination page and link purpose after pinning",
      "kind": "editorial",
      "when": "When updating a bio or pinned post, or checking long-term access to materials"
    },
    {
      "id": "K05-103",
      "title": "Schedule publication around primary readers' time zones and habits",
      "kind": "editorial",
      "when": "When choosing publication times or explaining late-night posting"
    },
    {
      "id": "K05-104",
      "title": "Public views cannot calculate the remainder of a 200-view Home quota",
      "kind": "myth",
      "when": "When public numbers are treated as a cold-start progress bar"
    },
    {
      "id": "K05-105",
      "title": "Reusability, relayability, and accessibility each have independent content value",
      "kind": "editorial",
      "when": "When assessing whether content merits bookmarking, sharing, or long-term maintenance"
    },
    {
      "id": "K05-106",
      "title": "Verify questions after publication and publish conclusion-changing findings as separate updates",
      "kind": "editorial",
      "when": "When receiving reader questions, counterexamples, or corrections"
    },
    {
      "id": "K05-107",
      "title": "Keep distribution duration similar in the next comparison and acknowledge remaining changes",
      "kind": "editorial",
      "when": "When reviewing the next round of first-image or summary changes"
    },
    {
      "id": "K05-108",
      "title": "Whether to publish a third post depends on new information and correction needs",
      "kind": "editorial",
      "when": "When deciding whether to keep publishing on the same day"
    },
    {
      "id": "K05-109",
      "title": "Finally check the first image and opening from an unfamiliar reader's perspective",
      "kind": "editorial",
      "when": "When completing the final prepublication check"
    }
  ]
}
```

</details>

<details>
<summary>7. python3 scripts/knowledge.py get K05-060 K05-061 K05-062</summary>

```bash
python3 scripts/knowledge.py get K05-060 K05-061 K05-062
```

退出码：0。

```json
{
  "research_through": "2026-10-29",
  "claims": [
    {
      "id": "K05-060",
      "title": "SpamHashTagAbuse is a spam class with conditional label writing",
      "kind": "code",
      "conclusion": "The public Spam policy includes SpamHashTagAbuse; after the model classifies it as such, it follows the author-eligibility branch for other Spam classes and may write post SpamHighRecall if conditions pass.",
      "conditions": [
        "Model classifies as SpamHashTagAbuse",
        "Author eligibility for other Spam classes and prerequisites hold"
      ],
      "practical_meaning": "Explain that a hashtag-abuse class exists while retaining model and author conditions.",
      "check": {
        "when": "When discussing the risk of hashtag stuffing",
        "needed": [
          "Model policy",
          "Author eligibility",
          "PTOS execution prerequisites"
        ],
        "verify": [
          "Check the classification enumeration",
          "Check the other-Spam branch"
        ],
        "if_missing": "Without a policy result, do not declare a violation directly from hashtag count."
      },
      "limits": [
        "No universal hashtag-count deduction formula is public."
      ],
      "source_units": [
        "U0475"
      ],
      "evidence": [
        {
          "source_id": "S054",
          "link_indices": [
            1,
            2
          ],
          "supports": "SpamHashTagAbuse enumeration and author branch for other Spam classes",
          "title": "[54] Engagement baiting, hashtag abuse, and normal hashtag features.",
          "links": [
            {
              "label": "Baiting, farming, card manipulation, and other spam branches",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/task_write_safety_post_annotations_result_sink.py#L233-L248"
            },
            {
              "label": "Named classes including SpamHashTagAbuse",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/state.py#L37-L46"
            }
          ]
        }
      ],
      "related_unknowns": [
        "Q43"
      ],
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    },
    {
      "id": "K05-061",
      "title": "Advice to limit hashtags is not proof of zero value or a uniform deduction formula",
      "kind": "myth",
      "conclusion": "'Piling on hashtags does not help' can be an editorial reminder, but the cited public evidence cannot establish that all hashtags have zero value and provides no sitewide formula deducting a fixed score above a fixed count.",
      "conditions": [
        "Distinguish editorial reminders from code facts"
      ],
      "practical_meaning": "Explain relevance, usefulness for reader recognition, and abuse risk separately; do not claim a universally optimal count.",
      "check": {
        "when": "When reviewing claims that all hashtags have zero value or incur count-based penalties",
        "needed": [
          "Named classification evidence",
          "Actual experiments on count effects, if any"
        ],
        "verify": [
          "Check whether an abuse class is being equated with all hashtags",
          "Check whether a uniform numeric rule is actually provided"
        ],
        "if_missing": "Without a corresponding experiment or formula, remove definitive numeric conclusions."
      },
      "limits": [
        "The absence of a publicly established formula does not mean abuse carries no risk or prove that no undisclosed formula exists."
      ],
      "source_units": [
        "U0475"
      ],
      "evidence": [
        {
          "source_id": "S054",
          "link_indices": [
            1,
            2
          ],
          "supports": "Establishes an abuse class, but cannot establish effects for all hashtags",
          "title": "[54] Engagement baiting, hashtag abuse, and normal hashtag features.",
          "links": [
            {
              "label": "Baiting, farming, card manipulation, and other spam branches",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/task_write_safety_post_annotations_result_sink.py#L233-L248"
            },
            {
              "label": "Named classes including SpamHashTagAbuse",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/state.py#L37-L46"
            }
          ]
        }
      ],
      "related_unknowns": [
        "Q43"
      ],
      "correction": {
        "review_finding": "KD-01",
        "origin": "english_distillation",
        "date": "2026-10-31",
        "summary": "Restore the original evidence boundary: no sitewide numeric hashtag formula is established by the cited public evidence, which is not proof that none exists.",
        "sources": [
          {
            "label": "Named hashtag-abuse classification",
            "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/state.py#L37-L46"
          },
          {
            "label": "Conditional Spam label writing",
            "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/task_write_safety_post_annotations_result_sink.py#L233-L248"
          },
          {
            "label": "Prompt loader states prompts are excluded",
            "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/prompts.py#L11-L31"
          },
          {
            "label": "Repository disclosure of unpublished prompts and rules",
            "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/README.md#L428-L447"
          }
        ]
      },
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    },
    {
      "id": "K05-062",
      "title": "CLICK_HASHTAG behavior can be an input to Phoenix",
      "kind": "code",
      "conclusion": "Phoenix history data and feature lists include CLICK_HASHTAG; this supports hashtag-related behavior being an input, not each added hashtag yielding a fixed final-score bonus.",
      "conditions": [
        "The cited Phoenix history and feature paths"
      ],
      "practical_meaning": "Accurately say 'a related behavioral input exists'; do not turn an input field into a score authors can redeem.",
      "check": {
        "when": "When someone asserts the system completely ignores hashtags or calculates bonuses by count",
        "needed": [
          "Historical behavior set",
          "Feature list",
          "Final-scoring evidence, if any"
        ],
        "verify": [
          "Confirm CLICK_HASHTAG is listed",
          "Distinguish user behavior from the number of hashtags added by an author"
        ],
        "if_missing": "Without complete usage and effect evidence, do not estimate recommendation gains."
      },
      "limits": [
        "A feature's existence does not mean every model or request uses it in the same way."
      ],
      "source_units": [
        "U0476"
      ],
      "evidence": [
        {
          "source_id": "S054",
          "link_indices": [
            7,
            8
          ],
          "supports": "CLICK_HASHTAG history and feature lists",
          "title": "[54] Engagement baiting, hashtag abuse, and normal hashtag features.",
          "links": [
            {
              "label": "Phoenix history data includes CLICK_HASHTAG",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix/xrex/data/recsys/history_id_lists.py#L25-L36"
            },
            {
              "label": "Feature list containing CLICK_HASHTAG",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix/xrex/data/recsys/id_list_features.py#L108-L120"
            }
          ]
        }
      ],
      "related_unknowns": [
        "Q43"
      ],
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    }
  ],
  "related_unknowns": [
    "Q43"
  ]
}
```

</details>

<details>
<summary>8. python3 scripts/knowledge.py get K05-063 K05-064 Q43</summary>

```bash
python3 scripts/knowledge.py get K05-063 K05-064 Q43
```

退出码：0。

```json
{
  "research_through": "2026-10-29",
  "claims": [
    {
      "id": "K05-063",
      "title": "Four hashtags is the selection limit of one extractor",
      "kind": "code",
      "conclusion": "The SimClusters entity extractor sets MaxHashtagsPerTweet=4 and retains only the first four hashtags when extracting text entities. Four is this extractor's data-selection cap, not a sitewide optimum of four or a penalty starting with the fifth.",
      "conditions": [
        "This SimClusters entity extractor path"
      ],
      "practical_meaning": "Specify the component and input cap when introducing this number; prioritize relevance without promising that the first four all increase recommendations.",
      "check": {
        "when": "When MaxHashtagsPerTweet is used to prove a universally optimal count",
        "needed": [
          "Extractor code",
          "Whether the claimed effect exceeds this component's scope"
        ],
        "verify": [
          "Verify only the first four are taken",
          "Distinguish input truncation from penalties or rewards",
          "Retain the possibility that other models read text or different features"
        ],
        "if_missing": "Without cross-model effect experiments, do not recommend four as an algorithmic guarantee."
      },
      "limits": [
        "Other models may read text or different features.",
        "A local processing cap is not an effect experiment for the whole system."
      ],
      "source_units": [
        "U0477"
      ],
      "evidence": [
        {
          "source_id": "S054",
          "link_indices": [
            6
          ],
          "supports": "MaxHashtagsPerTweet=4 and entity selection",
          "title": "[54] Engagement baiting, hashtag abuse, and normal hashtag features.",
          "links": [
            {
              "label": "SimClusters entity extractor takes at most four hashtags",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/simclusters/simclusters_v2/summingbird/common/TweetEntityExtractor.scala#L14-L40"
            }
          ]
        }
      ],
      "related_unknowns": [
        "Q43"
      ],
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    },
    {
      "id": "K05-064",
      "title": "Choose hashtags directly related to the topic or event",
      "kind": "editorial",
      "conclusion": "Hashtags can help readers recognize and find related topics or events; the body must still clearly state tool names, versions, and results. Piling on trending tags cannot replace that information.",
      "conditions": [],
      "practical_meaning": "Keep only tags matching the body's purpose, and check that the test content is understandable without relying on them.",
      "check": {
        "when": "When reviewing hashtags alongside the body",
        "needed": [
          "Topic or event",
          "Tool names, versions, and results",
          "Proposed hashtags"
        ],
        "verify": [
          "Check each for direct relevance",
          "Verify key facts remain in the body"
        ],
        "if_missing": "Without a directly relevant purpose, reduce tags rather than applying an unknown optimal count."
      },
      "limits": [
        "This is editorial advice.",
        "Public code has not selected an optimal count for all accounts."
      ],
      "source_units": [
        "U0478"
      ],
      "evidence": [
        {
          "source_id": "S054",
          "link_indices": [
            6,
            7,
            8
          ],
          "supports": "Four is a local extractor cap, while hashtag behavioral inputs also exist; this evidence gives no optimal count for all accounts, and choosing for relevance is editorial advice.",
          "title": "[54] Engagement baiting, hashtag abuse, and normal hashtag features.",
          "links": [
            {
              "label": "SimClusters entity extractor takes at most four hashtags",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/simclusters/simclusters_v2/summingbird/common/TweetEntityExtractor.scala#L14-L40"
            },
            {
              "label": "Phoenix history data includes CLICK_HASHTAG",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix/xrex/data/recsys/history_id_lists.py#L25-L36"
            },
            {
              "label": "Feature list containing CLICK_HASHTAG",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix/xrex/data/recsys/id_list_features.py#L108-L120"
            }
          ]
        }
      ],
      "related_unknowns": [
        "Q43"
      ],
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    },
    {
      "id": "Q43",
      "title": "Is the optimal number of hashtags zero, four, or some other fixed number?",
      "kind": "unknown",
      "conclusion": "There is a SpamHashTagAbuse category, a `CLICK_HASHTAG` historical feature, and a limit in one SimClusters extractor that takes only the first four hashtags.",
      "conditions": [
        "Research is current through 2026-10-29; fixed public snapshots can establish the known portions, while incomplete links remain unknown."
      ],
      "practical_meaning": "Explain abuse risks and available features, interpreting four as a local data-selection limit; this does not prove that all hashtags have zero value or that penalties begin with the fifth.",
      "check": {
        "when": "The question or copy concerns: Is the optimal number of hashtags zero, four, or some other fixed number?",
        "needed": [
          "There is no complete account of usage and causal comparisons across all models and entry points for different hashtag counts, relevance levels, and topics; nor has a universal per-hashtag bonus or penalty formula been disclosed."
        ],
        "verify": [
          "Distinguish this known fact from the information still missing.",
          "Check whether the user’s conclusion exceeds the known scope stated below; obtain the outstanding information when a definitive conclusion is required."
        ],
        "if_missing": "Clearly state what can currently be confirmed and why the rest cannot be determined; use practical_meaning to provide actions that can still be taken."
      },
      "limits": [
        "There is no complete account of usage and causal comparisons across all models and entry points for different hashtag counts, relevance levels, and topics; nor has a universal per-hashtag bonus or penalty formula been disclosed."
      ],
      "source_units": [
        "U0639",
        "U0640",
        "U0641"
      ],
      "evidence": [
        {
          "source_id": "S054",
          "link_indices": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8
          ],
          "supports": "The known mechanisms and evidence gaps for this question in the original report; retain the original materials in this citation group.",
          "title": "[54] Engagement baiting, hashtag abuse, and normal hashtag features.",
          "links": [
            {
              "label": "Prerequisite handling of test accounts, PageRank, and gray badges",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/task_write_safety_post_annotations_result_sink.py#L175-L194"
            },
            {
              "label": "Baiting, farming, card manipulation, and other spam branches",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/task_write_safety_post_annotations_result_sink.py#L233-L248"
            },
            {
              "label": "Named classes including SpamHashTagAbuse",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/state.py#L37-L46"
            },
            {
              "label": "Safety writes execute only in PTOS production",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/task_write_safety_post_annotations_result_sink.py#L48-L49"
            },
            {
              "label": "Disabling conditions outside PTOS production",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/disable_rules.py#L6-L11"
            },
            {
              "label": "Spam-classification prompt is not public",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/prompts.py#L11-L31"
            },
            {
              "label": "SimClusters entity extractor takes at most four hashtags",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/simclusters/simclusters_v2/summingbird/common/TweetEntityExtractor.scala#L14-L40"
            },
            {
              "label": "Phoenix history data includes CLICK_HASHTAG",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix/xrex/data/recsys/history_id_lists.py#L25-L36"
            },
            {
              "label": "Feature list containing CLICK_HASHTAG",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix/xrex/data/recsys/id_list_features.py#L108-L120"
            }
          ]
        }
      ],
      "related_unknowns": [],
      "topic": "49 questions still awaiting confirmation",
      "topic_file": "topic-06.json"
    }
  ],
  "related_unknowns": [
    "Q43"
  ]
}
```

</details>

<details>
<summary>9. python3 scripts/knowledge.py get K01-017</summary>

```bash
python3 scripts/knowledge.py get K01-017
```

退出码：0。

```json
{
  "research_through": "2026-10-29",
  "claims": [
    {
      "id": "K01-017",
      "title": "Checking 'today' requires distinguishing commit time, public availability, announcements, and deployment",
      "kind": "code",
      "conclusion": "5ed796374ea48ee26058aab66ab10c266bea2bef has author and committer timestamps of 2026-10-28 at 02:49:03 UTC (October 27, 19:49:03 PDT); 606b254b45be798bfaecfa8c23f5a9c51bc8000c has author and committer timestamps of 2026-10-29 at 02:57:55 UTC (October 28, 19:57:55 PDT). These recorded commit times establish neither first public availability nor when an experiment was deployed to all traffic.",
      "conditions": [
        "Los Angeles used PDT, UTC−7, on those dates",
        "Interpreting 'today' in an original post also requires the author's posting time, time zone, and the event referenced"
      ],
      "practical_meaning": "When publishing an interpretation of updates, state the time bases alongside each other and distinguish recorded commit times, first public availability, announcements, and production experiments.",
      "check": {
        "when": "When reviewing date assertions such as 'updated today' or 'October 28/29 update'",
        "needed": [
          "Exact time of the original post",
          "Author's time zone",
          "Referenced feature or configuration",
          "Corresponding commit or announcement"
        ],
        "verify": [
          "Complete the time-zone conversion",
          "Confirm whether the statement concerns commit metadata, first public availability, an announcement, or a production feature date",
          "Do not judge the original post incorrect solely from the current report date"
        ],
        "if_missing": "If the original post's time or referent is unclear, preserve the ambiguity; do not declare its 'today' incorrect."
      },
      "limits": [
        "Commit metadata establishes the recorded commit timestamps; it does not establish first public availability or production rollout time",
        "The time a README note was added may differ from the feature date"
      ],
      "source_units": [
        "U0014",
        "U0015",
        "U0016",
        "U0017"
      ],
      "evidence": [
        {
          "source_id": "S011",
          "link_indices": [
            0,
            1,
            2
          ],
          "supports": "Recorded timestamps of the two commits and separately stated feature dates in the README; not first public availability or production rollout time.",
          "title": "[11] Public update dates, pinned commits, and time zones.",
          "links": [
            {
              "label": "Public commit on October 28 UTC",
              "url": "https://github.com/xai-org/x-algorithm/commit/5ed796374ea48ee26058aab66ab10c266bea2bef"
            },
            {
              "label": "Public commit on October 29 UTC",
              "url": "https://github.com/xai-org/x-algorithm/commit/606b254b45be798bfaecfa8c23f5a9c51bc8000c"
            },
            {
              "label": "Officially listed October 8 and October 13 updates",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/README.md#L32-L44"
            }
          ]
        },
        {
          "source_id": "S012",
          "link_indices": [
            0,
            1
          ],
          "supports": "Location of the synchronized public defaults; this cannot replace per-request deployment evidence.",
          "title": "[12] Synchronization of public defaults and usage paths in Home Mixer and VM Ranker.",
          "links": [
            {
              "label": "Cron synchronization explanation for main production defaults",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/README.md#L428-L434"
            },
            {
              "label": "Synchronization time in the Home Mixer parameter file",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/params/param.rs#L1"
            }
          ]
        }
      ],
      "related_unknowns": [
        "Q01",
        "Q02"
      ],
      "correction": {
        "review_finding": "KA-001",
        "origin": "original_report",
        "date": "2026-10-31",
        "summary": "Remove the inherited claim that recorded commit timestamps establish first public availability; the recorded times and UTC/PDT conversions are unchanged.",
        "sources": [
          {
            "label": "Baseline commit metadata",
            "url": "https://github.com/xai-org/x-algorithm/commit/5ed796374ea48ee26058aab66ab10c266bea2bef"
          },
          {
            "label": "Comparison commit metadata",
            "url": "https://github.com/xai-org/x-algorithm/commit/606b254b45be798bfaecfa8c23f5a9c51bc8000c"
          },
          {
            "label": "GitHub documents pushing already-created local commits to a remote repository",
            "url": "https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository"
          }
        ]
      },
      "topic": "Posting frequency, October updates, recommendation stages, author diversity, threads, prediction weights, and reposts and replies (original report lines 1–438)",
      "topic_file": "topic-01.json"
    }
  ],
  "related_unknowns": [
    "Q01",
    "Q02"
  ]
}
```

</details>

<details>
<summary>10. python3 scripts/knowledge.py get K05-067 K05-068 K05-069</summary>

```bash
python3 scripts/knowledge.py get K05-067 K05-068 K05-069
```

退出码：0。

```json
{
  "research_through": "2026-10-29",
  "claims": [
    {
      "id": "K05-067",
      "title": "Check Period and generation time first in Under the Hood",
      "kind": "code",
      "conclusion": "The page mentions previous-month statistics, but the service depends on month conditions and data readiness and falls back to an earlier period when necessary; check Period and generation time first when opening a report.",
      "conditions": [
        "Month eligibility and data readiness affect the reporting period"
      ],
      "practical_meaning": "Align the date of the issue being analyzed with report coverage; avoid explaining today's new post through an older month's aggregate.",
      "check": {
        "when": "When using an Under the Hood report to diagnose recent changes",
        "needed": [
          "Period",
          "Report generation time",
          "Date the issue occurred"
        ],
        "verify": [
          "Check whether it fell back to an earlier period",
          "Confirm the post or account change discussed falls within that period"
        ],
        "if_missing": "If periods do not match, use it only as historical evidence, not a conclusion about today."
      },
      "limits": [
        "The page's 'previous month' wording does not guarantee each actual response covers the previous month."
      ],
      "source_units": [
        "U0481"
      ],
      "evidence": [
        {
          "source_id": "S072",
          "link_indices": [
            2
          ],
          "supports": "Reporting period and fields",
          "title": "[72] Official Under the Hood entry point and how to read its reports.",
          "links": [
            {
              "label": "Report fields and units",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/jetfuel/routes/report.tsx#L25-L51"
            }
          ]
        },
        {
          "source_id": "S082",
          "link_indices": [
            2,
            4
          ],
          "supports": "Fallback when data is not ready and previous-month wording",
          "title": "[82] Under the Hood report eligibility and data periods.",
          "links": [
            {
              "label": "Fallback to the previous period when the month is not ready",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/strato/columns/underTheHoodReport.User.strato#L423-L458"
            },
            {
              "label": "Page explanation of previous-month aggregation",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/jetfuel/routes/index.tsx#L14-L32"
            }
          ]
        }
      ],
      "related_unknowns": [],
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    },
    {
      "id": "K05-068",
      "title": "Report eligibility and recommendation eligibility are separate conditions",
      "kind": "code",
      "conclusion": "Public Under the Hood code includes a pilot switch and report-eligibility requirements such as an account age of about one year and at least ten qualifying posts in the specified month. Missing a report cannot establish restrictions; these conditions govern report provision, not authors' recommendation eligibility.",
      "conditions": [
        "The cited public report service",
        "Pilot and month conditions"
      ],
      "practical_meaning": "When investigating a missing report, first check service availability and report eligibility; do not diagnose a recommendation penalty.",
      "check": {
        "when": "When a user lacks a report or the entry point is unavailable",
        "needed": [
          "Pilot switch/account availability",
          "Account age",
          "Count of qualifying posts in the specified month"
        ],
        "verify": [
          "Retain the scope of 'about one year' and 'at least ten qualifying posts in the specified month'",
          "Distinguish report eligibility from recommendation eligibility"
        ],
        "if_missing": "Without eligibility information, say only that no report was provided; do not infer throttling."
      },
      "limits": [
        "Actual availability is determined by the account interface.",
        "Do not present ten posts as recommendation eligibility or a creator's minimum posting quota."
      ],
      "source_units": [
        "U0482"
      ],
      "evidence": [
        {
          "source_id": "S082",
          "link_indices": [
            0,
            3
          ],
          "supports": "Account age, monthly posting eligibility, and service switches",
          "title": "[82] Under the Hood report eligibility and data periods.",
          "links": [
            {
              "label": "Account age, post count, and time conditions",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/strato/columns/underTheHoodReport.User.strato#L17-L22"
            },
            {
              "label": "Service switch",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/strato/lib/params.strato#L15-L22"
            }
          ]
        }
      ],
      "related_unknowns": [],
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    },
    {
      "id": "K05-069",
      "title": "Post labels counts labeled eligible posts in the reported authored-post cohort",
      "kind": "code",
      "conclusion": "Post labels reports a labeled-post count for the eligible logical posts authored in the reported cohort and its proportion of that eligible-post count. The denominator excludes reposts and nullcast posts and deduplicates logical post IDs. For ordinary safety-label events, the generating job observes a configurable period after creation, seven days by default, and counts whether the label was ever applied within that horizon; a later removal does not erase that count. Rows are assigned to the post's authored month, not the label-event month.",
      "conditions": [
        "The specific reported authored-post cohort and its data coverage",
        "The Post labels item and its label-generating path",
        "The ordinary safety-label event horizon is bounded by creation plus postObservationDays and the batch cutoff; its public default is seven days"
      ],
      "practical_meaning": "Align the post's creation date, label-event date, observation horizon, and report coverage before diagnosing a date mismatch. For example, under the ordinary default event path, an October 31 post labeled on November 2 can contribute to October's post cohort. Keep numerator and denominator in eligible posts and check Effect on visibility separately.",
      "check": {
        "when": "When explaining a Post labels percentage",
        "needed": [
          "Reported authored-post cohort, coverage, and report generation time",
          "Eligible logical-post count used as the denominator",
          "The label's carried-post count, label-event dates, and source path",
          "Configured postObservationDays and any snapshot, flag, or takedown handling"
        ],
        "verify": [
          "Verify that the numerator and denominator concern eligible logical posts, not impressions or all label activity in the calendar month",
          "Assign ordinary event-based label counts to the post's authored month and apply that post's observation horizon",
          "Distinguish ever-applied labels from labels still active at report time; removal is counted separately",
          "Check special flag, snapshot, or takedown rules before applying the ordinary event-horizon description",
          "Do not describe label proportion as reach-loss rate"
        ],
        "if_missing": "If cohort, denominator, or generating-path definitions are unclear, report those limits; do not equate the figure with all label activity during the calendar month, current active labels, or exposure loss."
      },
      "limits": [
        "A post carrying a label does not directly reveal how much exposure it actually lost",
        "The seven-day default describes ordinary safety-label events; snapshot gap filling, post flags, and takedown paths have their own logic and must not be assigned that horizon without checking",
        "Account-label statistics use a separate day-based calculation; see K05-070"
      ],
      "source_units": [
        "U0483"
      ],
      "evidence": [
        {
          "source_id": "S072",
          "link_indices": [
            2
          ],
          "supports": "Post labels presentation fields and post-based units; the additional correction sources establish cohort, denominator, and observation rules",
          "title": "[72] Official Under the Hood entry point and how to read its reports.",
          "links": [
            {
              "label": "Report fields and units",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/jetfuel/routes/report.tsx#L25-L51"
            }
          ]
        }
      ],
      "related_unknowns": [],
      "correction": {
        "review_finding": "KD-04",
        "origin": "original_report",
        "date": "2026-10-31",
        "summary": "Replace the inherited calendar-period label-incidence shorthand with the authored-post cohort, eligible denominator, and generating-path observation rules; labels later removed can still be counted.",
        "sources": [
          {
            "label": "Eligible logical-post cohort, exclusions, and deduplicated denominator",
            "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthDailyPostsJob.scala#L215-L250"
          },
          {
            "label": "Ordinary safety-label event observation horizon",
            "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthDailyPostsJob.scala#L311-L322"
          },
          {
            "label": "Count ever-applied labels and record removal separately",
            "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthDailyPostsJob.scala#L360-L393"
          },
          {
            "label": "Configurable default observation period of seven days",
            "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthDailyPostsJob.scala#L421-L422"
          },
          {
            "label": "Assign post-label rows to months using authoredYyyymmdd",
            "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthUserMonthMhPublisherJob.scala#L237-L245"
          },
          {
            "label": "Report sums carried counts and divides by the eligible-post count; account labels use days",
            "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/strato/columns/underTheHoodReport.User.strato#L320-L355"
          }
        ]
      },
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    }
  ],
  "related_unknowns": []
}
```

</details>

<details>
<summary>11. python3 scripts/knowledge.py get Q01 Q02</summary>

```bash
python3 scripts/knowledge.py get Q01 Q02
```

退出码：0。

```json
{
  "research_through": "2026-10-29",
  "claims": [
    {
      "id": "Q01",
      "title": "Which update does “today” in the original Post actually refer to?",
      "kind": "unknown",
      "conclusion": "The public commit for 5ed7963 is dated 2026-10-28 02:49:03 UTC, which is 10/27 19:49:03 in Los Angeles; 606b254 is dated 2026-10-29 02:57:55 UTC, which is 10/28 19:57:55 in Los Angeles. Official Notable Updates separately lists feature dates such as 10/8 and 10/13.",
      "conditions": [
        "Research is current through 2026-10-29; fixed public snapshots can establish the known portions, while incomplete links remain unknown."
      ],
      "practical_meaning": "List UTC and Los Angeles dates separately to explain the sequence of public snapshots; do not judge the original Post to be wrong solely from the date of this text, or treat commit time as the time of full deployment.",
      "check": {
        "when": "The question or copy concerns: Which update does “today” in the original Post actually refer to?",
        "needed": [
          "The original Post’s precise publication time, the author’s time zone, and the configuration, feature, or public commit to which “today” refers."
        ],
        "verify": [
          "Distinguish this known fact from the information still missing.",
          "Check whether the user’s conclusion exceeds the known scope stated below; obtain the outstanding information when a definitive conclusion is required."
        ],
        "if_missing": "Clearly state what can currently be confirmed and why the rest cannot be determined; use practical_meaning to provide actions that can still be taken."
      },
      "limits": [
        "The original Post’s precise publication time, the author’s time zone, and the configuration, feature, or public commit to which “today” refers."
      ],
      "source_units": [
        "U0513",
        "U0514",
        "U0515"
      ],
      "evidence": [
        {
          "source_id": "S011",
          "link_indices": [
            0,
            1,
            2
          ],
          "supports": "The known mechanisms and evidence gaps for this question in the original report; retain the original materials in this citation group.",
          "title": "[11] Public update dates, pinned commits, and time zones.",
          "links": [
            {
              "label": "Public commit on October 28 UTC",
              "url": "https://github.com/xai-org/x-algorithm/commit/5ed796374ea48ee26058aab66ab10c266bea2bef"
            },
            {
              "label": "Public commit on October 29 UTC",
              "url": "https://github.com/xai-org/x-algorithm/commit/606b254b45be798bfaecfa8c23f5a9c51bc8000c"
            },
            {
              "label": "Officially listed October 8 and October 13 updates",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/README.md#L32-L44"
            }
          ]
        }
      ],
      "related_unknowns": [],
      "topic": "49 questions still awaiting confirmation",
      "topic_file": "topic-06.json"
    },
    {
      "id": "Q02",
      "title": "Are the public defaults the live configuration for every reader?",
      "kind": "unknown",
      "conclusion": "The official explanation says cron mirrors the main production defaults; Home Mixer and VM Ranker have different values under the same names in the same commit, and the implementation also contains parameter-reading, caching, and fallback branches.",
      "conditions": [
        "Research is current through 2026-10-29; fixed public snapshots can establish the known portions, while incomplete links remain unknown."
      ],
      "practical_meaning": "Describe them as the public main defaults and specify the applicable path; do not dismiss them as arbitrary examples or claim they are identical for every viewer.",
      "check": {
        "when": "The question or copy concerns: Are the public defaults the live configuration for every reader?",
        "needed": [
          "Per-request feature switches, all experiment assignments, and the correspondence between service deployments and checkpoints."
        ],
        "verify": [
          "Distinguish this known fact from the information still missing.",
          "Check whether the user’s conclusion exceeds the known scope stated below; obtain the outstanding information when a definitive conclusion is required."
        ],
        "if_missing": "Clearly state what can currently be confirmed and why the rest cannot be determined; use practical_meaning to provide actions that can still be taken."
      },
      "limits": [
        "Per-request feature switches, all experiment assignments, and the correspondence between service deployments and checkpoints."
      ],
      "source_units": [
        "U0516",
        "U0517",
        "U0518"
      ],
      "evidence": [
        {
          "source_id": "S012",
          "link_indices": [
            0,
            1,
            2,
            3,
            4,
            5
          ],
          "supports": "The known mechanisms and evidence gaps for this question in the original report; retain the original materials in this citation group.",
          "title": "[12] Synchronization of public defaults and usage paths in Home Mixer and VM Ranker.",
          "links": [
            {
              "label": "Cron synchronization explanation for main production defaults",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/README.md#L428-L434"
            },
            {
              "label": "Synchronization time in the Home Mixer parameter file",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/params/param.rs#L1"
            },
            {
              "label": "Local weighting, cold start, and RPC fallback",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/scorers/vm_ranker.rs#L59-L135"
            },
            {
              "label": "VM request includes heads, cached scores, and compute_value_model",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/scorers/vm_ranker_request.rs#L26-L68"
            },
            {
              "label": "VM Ranker obtains coefficients from its own params",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/vm-ranker/scoring/value_model.rs#L71-L118"
            },
            {
              "label": "Handling when a cached weighted score is available",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L282-L327"
            }
          ]
        },
        {
          "source_id": "S027",
          "link_indices": [
            0,
            1,
            2,
            3,
            4,
            5
          ],
          "supports": "The known mechanisms and evidence gaps for this question in the original report; retain the original materials in this citation group.",
          "title": "[27] Current coefficients in two locations, probability multiplication, and mutual-follow conditions.",
          "links": [
            {
              "label": "Home Mixer prediction coefficients and official interpretive annotations",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/params/param.rs#L367-L513"
            },
            {
              "label": "Same-named VM Ranker defaults",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/vm-ranker/params.rs#L3-L155"
            },
            {
              "label": "Prediction-term multiplication and summation",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L57-L139"
            },
            {
              "label": "Subsequent shifting of positive and negative scores",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/scoring.rs#L161-L179"
            },
            {
              "label": "Mutual-follow candidates must not be replies or reposts",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/inputs.rs#L19-L22"
            },
            {
              "label": "General reply coefficient plus mutual-follow boost",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/xai-value-model/weights.rs#L84-L99"
            }
          ]
        }
      ],
      "related_unknowns": [],
      "topic": "49 questions still awaiting confirmation",
      "topic_file": "topic-06.json"
    }
  ],
  "related_unknowns": []
}
```

</details>

<details>
<summary>12. python3 scripts/knowledge.py get K05-070 K05-071 K05-072</summary>

```bash
python3 scripts/knowledge.py get K05-070 K05-071 K05-072
```

退出码：0。

```json
{
  "research_through": "2026-10-29",
  "claims": [
    {
      "id": "K05-070",
      "title": "Account labels counts labeled days and their proportion",
      "kind": "code",
      "conclusion": "Account labels in the report indicates how many days the account carried that label during the period and the corresponding proportion of days.",
      "conditions": [
        "Specified reporting period",
        "Account labels item"
      ],
      "practical_meaning": "Record labeled days separately from label effects; do not treat them as affected-post counts or days of complete invisibility.",
      "check": {
        "when": "When explaining an Account labels percentage",
        "needed": [
          "Days in the reporting period",
          "Labeled days",
          "Official effect explanation"
        ],
        "verify": [
          "Confirm the unit is days",
          "Check the label's actual scope"
        ],
        "if_missing": "Without an effect explanation, report only the day-count record."
      },
      "limits": [
        "The proportion of days is not the proportion of lost exposure."
      ],
      "source_units": [
        "U0483"
      ],
      "evidence": [
        {
          "source_id": "S072",
          "link_indices": [
            2
          ],
          "supports": "Account labels report fields and units",
          "title": "[72] Official Under the Hood entry point and how to read its reports.",
          "links": [
            {
              "label": "Report fields and units",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/jetfuel/routes/report.tsx#L25-L51"
            }
          ]
        }
      ],
      "related_unknowns": [],
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    },
    {
      "id": "K05-071",
      "title": "Three of forty posts, or 7.5%, is not an exposure-loss rate",
      "kind": "editorial",
      "conclusion": "Suppose 3 of 40 posts carry a label: 3/40=7.5% is the proportion of labeled posts, not a loss of 7.5% of exposure.",
      "conditions": [
        "Hypothetical report example",
        "Numerator 3 posts, denominator 40 posts"
      ],
      "practical_meaning": "Write '3 posts / 40 posts, a post proportion of 7.5%'; do not attach a causal exposure interpretation.",
      "check": {
        "when": "When annotating Post labels figures",
        "needed": [
          "Labeled-post count and total post count",
          "Official field definition"
        ],
        "verify": [
          "Check the arithmetic of 3/40",
          "Check that the ratio is still named a post proportion"
        ],
        "if_missing": "Without an actual report, explicitly identify this as a teaching hypothetical, not an account measurement."
      },
      "limits": [
        "Not actual account data."
      ],
      "source_units": [
        "U0484"
      ],
      "evidence": [
        {
          "source_id": "S072",
          "link_indices": [
            2
          ],
          "supports": "The report's post-based units support this hypothetical calculation",
          "title": "[72] Official Under the Hood entry point and how to read its reports.",
          "links": [
            {
              "label": "Report fields and units",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/jetfuel/routes/report.tsx#L25-L51"
            }
          ]
        }
      ],
      "related_unknowns": [],
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    },
    {
      "id": "K05-072",
      "title": "Five of thirty-one days does not mean five days of complete invisibility",
      "kind": "editorial",
      "conclusion": "Suppose an account label is present on 5 of 31 days: the unit is days; this does not mean posts were entirely invisible at every entry point on those 5 days.",
      "conditions": [
        "Hypothetical report example",
        "Specified 31-day period with an account label on 5 days"
      ],
      "practical_meaning": "Record the 5 days and specific label effect; explain duration separately from visibility scope.",
      "check": {
        "when": "When annotating Account labels duration",
        "needed": [
          "Labeled days",
          "Days in the period",
          "Label's Effect on visibility"
        ],
        "verify": [
          "Retain days as the unit",
          "Check which entry points and readers are restricted"
        ],
        "if_missing": "Without the label effect, do not infer all-day, sitewide, or zero-exposure consequences."
      },
      "limits": [
        "Not actual account data."
      ],
      "source_units": [
        "U0484"
      ],
      "evidence": [
        {
          "source_id": "S072",
          "link_indices": [
            2,
            3
          ],
          "supports": "Account-label day counts and effect explanations",
          "title": "[72] Official Under the Hood entry point and how to read its reports.",
          "links": [
            {
              "label": "Report fields and units",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/jetfuel/routes/report.tsx#L25-L51"
            },
            {
              "label": "Label names and explanations of effects",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/strato/lib/underTheHoodLabels.strato"
            }
          ]
        }
      ],
      "related_unknowns": [
        "Q27"
      ],
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    }
  ],
  "related_unknowns": [
    "Q27"
  ]
}
```

</details>

<details>
<summary>13. python3 scripts/knowledge.py get K05-079 K05-080 K05-083</summary>

```bash
python3 scripts/knowledge.py get K05-079 K05-080 K05-083
```

退出码：0。

```json
{
  "research_through": "2026-10-29",
  "claims": [
    {
      "id": "K05-079",
      "title": "Use actual analytics fields and preserve missing values",
      "kind": "editorial",
      "conclusion": "Use analytics already available to the account; if the platform actually provides profile clicks, follows, bookmarks, or other fields, record them according to their definitions, and leave unavailable fields blank.",
      "conditions": [],
      "practical_meaning": "Keep visible field names and definitions; do not invent official algorithm scores or fill gaps with substitute metrics.",
      "check": {
        "when": "When building a posting-analytics record",
        "needed": [
          "Fields actually available to the account",
          "Each field's definition and measurement window"
        ],
        "verify": [
          "Preserve each field's meaning",
          "Distinguish nonexistent fields, unavailable data, and actual zero values"
        ],
        "if_missing": "Leave unavailable fields blank and mark them missing."
      },
      "limits": [
        "Do not assume different accounts have identical available fields."
      ],
      "source_units": [
        "U0491",
        "U0492"
      ],
      "evidence": [],
      "related_unknowns": [
        "Q49"
      ],
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    },
    {
      "id": "K05-080",
      "title": "Views are not deduplicated audience, and thread views cannot be summed as people",
      "kind": "official",
      "conclusion": "Public view counts are not deduplicated people; the views of individual posts in a thread cannot be summed and called a unique audience.",
      "conditions": [
        "When using the platform's public view numbers"
      ],
      "practical_meaning": "Report each post's views and their definition separately; without a deduplicated metric, do not manufacture a deduplicated total of people.",
      "check": {
        "when": "When summarizing thread performance or estimating unique readers",
        "needed": [
          "Views for each post",
          "Official view definition",
          "Deduplicated metric, if actually provided"
        ],
        "verify": [
          "Distinguish views from people",
          "Do not infer audience by simply adding across posts"
        ],
        "if_missing": "Without deduplicated data, list only views; do not label them unique readers."
      },
      "limits": [
        "Total views cannot reconstruct a reader's repeat views or views across posts."
      ],
      "source_units": [
        "U0491"
      ],
      "evidence": [
        {
          "source_id": "S059",
          "link_indices": [
            0
          ],
          "supports": "Official view-count definition is not a deduplicated person count",
          "title": "[59] Official definition of public view counts.",
          "links": [
            {
              "label": "X View counts",
              "url": "https://help.x.com/en/using-x/view-counts"
            }
          ]
        }
      ],
      "related_unknowns": [
        "Q49"
      ],
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    },
    {
      "id": "K05-083",
      "title": "Record shares, replies, profile clicks, follows, and similar metrics by definition; do not fill missing values with zero",
      "kind": "editorial",
      "conclusion": "Record shares, replies, profile clicks, follows, and other metrics actually provided by the platform, interpreting each by its definition; leave unavailable values blank rather than entering zero.",
      "conditions": [],
      "practical_meaning": "Record data availability separately from values, preserving field units and windows.",
      "check": {
        "when": "When cleaning an analytics table or comparing metrics across posts",
        "needed": [
          "Visible metrics",
          "Definitions, denominators, and observation windows",
          "Missing-data status"
        ],
        "verify": [
          "Confirm zero means an observed zero rather than an unavailable value",
          "Retain names of distinct actions"
        ],
        "if_missing": "Keep unavailable fields null."
      },
      "limits": [
        "Even identically named fields should not be compared outside platform definitions."
      ],
      "source_units": [
        "U0493"
      ],
      "evidence": [],
      "related_unknowns": [
        "Q49"
      ],
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    }
  ],
  "related_unknowns": [
    "Q49"
  ]
}
```

</details>

<details>
<summary>14. python3 scripts/knowledge.py get K05-073 K05-075 K05-076</summary>

```bash
python3 scripts/knowledge.py get K05-073 K05-075 K05-076
```

退出码：0。

```json
{
  "research_through": "2026-10-29",
  "claims": [
    {
      "id": "K05-073",
      "title": "Read What it means together with Effect on visibility",
      "kind": "official",
      "conclusion": "What it means and Effect on visibility in the report provide label meanings and effects; some restrict recommendations to non-followers, while others concern content warnings, regional restrictions, or other limits. Do not compress them all into the same 'throttling.'",
      "conditions": [
        "Specific report labels and explanations"
      ],
      "practical_meaning": "Record each label name, meaning, and effect, then explain it using precise audience and entry-point wording.",
      "check": {
        "when": "When organizing or explaining a visibility report",
        "needed": [
          "Label name",
          "What it means",
          "Effect on visibility"
        ],
        "verify": [
          "Check whether the effect is a recommendation restriction, warning, regional restriction, or something else",
          "Retain the applicable scope"
        ],
        "if_missing": "Without an explanation, do not invent a uniform penalty."
      },
      "limits": [
        "A label name cannot replace the full effect explanation."
      ],
      "source_units": [
        "U0485"
      ],
      "evidence": [
        {
          "source_id": "S072",
          "link_indices": [
            2,
            3
          ],
          "supports": "Report display fields and explanations of label effects",
          "title": "[72] Official Under the Hood entry point and how to read its reports.",
          "links": [
            {
              "label": "Report fields and units",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/jetfuel/routes/report.tsx#L25-L51"
            },
            {
              "label": "Label names and explanations of effects",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/strato/lib/underTheHoodLabels.strato"
            }
          ]
        }
      ],
      "related_unknowns": [
        "Q27"
      ],
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    },
    {
      "id": "K05-075",
      "title": "Save reports and align concurrent changes before correcting or appealing",
      "kind": "editorial",
      "conclusion": "When relevant labels appear, save the reporting period, names, and explanations and compare account or content changes in the same period; use an applicable correction or appeal entry point to address the issue. Today's title change cannot explain last month's aggregate.",
      "conditions": [],
      "practical_meaning": "Create chronologically ordered report and change records, retaining original materials needed for corrections or appeals.",
      "check": {
        "when": "When a report lists relevant labels",
        "needed": [
          "Reporting period, names, and explanations",
          "Concurrent account or content changes",
          "Correction or appeal entry point"
        ],
        "verify": [
          "Match temporal order",
          "Confirm the submitted issue falls within that label's scope"
        ],
        "if_missing": "Without contemporaneous information, do not identify the latest edit as the cause."
      },
      "limits": [
        "Report aggregates provide clues; they do not automatically prove a single change caused a label."
      ],
      "source_units": [
        "U0487"
      ],
      "evidence": [],
      "related_unknowns": [
        "Q27",
        "Q31"
      ],
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    },
    {
      "id": "K05-076",
      "title": "An empty report means only that this report lists no relevant records",
      "kind": "unknown",
      "conclusion": "When no label is listed, you can only say that this report has no relevant records. It is marked best effort, is not a complete causal log of individual impressions, and does not explain why one post lost to another; an empty report cannot establish that every ranking was normal.",
      "conditions": [
        "The reporting period read and its best effort scope"
      ],
      "practical_meaning": "Clearly state 'no records listed,' then turn to content, available analytics fields, and comparison methods.",
      "check": {
        "when": "When an empty report is used to prove there are no recommendation issues whatsoever",
        "needed": [
          "Actual report",
          "Coverage period",
          "Best effort explanation"
        ],
        "verify": [
          "Do not equate no records with verification of every process",
          "Do not reconstruct request-by-request competitive ranking from the report"
        ],
        "if_missing": "Without complete request logs, leave ranking causes unknown."
      },
      "limits": [
        "Empty records are not reverse proof of a hidden penalty either."
      ],
      "source_units": [
        "U0488"
      ],
      "evidence": [
        {
          "source_id": "S082",
          "link_indices": [
            1
          ],
          "supports": "The report's best effort explanation",
          "title": "[82] Under the Hood report eligibility and data periods.",
          "links": [
            {
              "label": "Best effort explanation",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/strato/columns/underTheHoodReport.User.strato#L47-L65"
            }
          ]
        }
      ],
      "related_unknowns": [
        "Q17"
      ],
      "topic": "Safety labels, account aggregation, duplication and engagement bait, transparency reports, data comparisons, and publishing examples",
      "topic_file": "topic-05.json"
    }
  ],
  "related_unknowns": [
    "Q17",
    "Q27",
    "Q31"
  ]
}
```

</details>

<details>
<summary>15. python3 scripts/knowledge.py get Q27 Q49</summary>

```bash
python3 scripts/knowledge.py get Q27 Q49
```

退出码：0。

```json
{
  "research_through": "2026-10-29",
  "claims": [
    {
      "id": "Q27",
      "title": "Does an insult label or account label make content invisible to all non-followers at every entry point?",
      "kind": "unknown",
      "conclusion": "Home, HomeRecommendations, and HomeHydration have different rules and audiences; named labels can remove candidates at specific entry points, while followers and the author may receive different treatment.",
      "conditions": [
        "Research is current through 2026-10-29; fixed public snapshots can establish the known portions, while incomplete links remain unknown."
      ],
      "practical_meaning": "Specify the entry points and reader conditions that were verified; describe the corresponding effect as “restricting recommendations to non-followers,” without claiming that all external reach or all ways of opening the content fall to zero.",
      "check": {
        "when": "The question or copy concerns: Does an insult label or account label make content invisible to all non-followers at every entry point?",
        "needed": [
          "These rules do not provide complete proof of consistency across every entry point, such as search, profiles, conversation pages, direct messages, or direct links; nor are there observations of a real account at each entry point."
        ],
        "verify": [
          "Distinguish this known fact from the information still missing.",
          "Check whether the user’s conclusion exceeds the known scope stated below; obtain the outstanding information when a definitive conclusion is required."
        ],
        "if_missing": "Clearly state what can currently be confirmed and why the rest cannot be determined; use practical_meaning to provide actions that can still be taken."
      },
      "limits": [
        "These rules do not provide complete proof of consistency across every entry point, such as search, profiles, conversation pages, direct messages, or direct links; nor are there observations of a real account at each entry point."
      ],
      "source_units": [
        "U0591",
        "U0592",
        "U0593"
      ],
      "evidence": [
        {
          "source_id": "S077",
          "link_indices": [
            0,
            1,
            2,
            3,
            4,
            5
          ],
          "supports": "The known mechanisms and evidence gaps for this question in the original report; retain the original materials in this citation group.",
          "title": "[77] Insults-label application conditions, reader scope, and entry-point differences.",
          "links": [
            {
              "label": "insults, followers, authors, and legacy-client fallback",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/visibility-filtering/rules/tweet_rules.rs#L161-L204"
            },
            {
              "label": "Separate visibility queries for in-network, out-of-network, and attached content",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/candidate_hydrators/vf_candidate_hydrator.rs#L67-L110"
            },
            {
              "label": "Tests of the same label at different safety levels",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/visibility-filtering/rules/golden_corpus/oon_tweet_label.rs#L192-L268"
            },
            {
              "label": "PTOS test-account and author-eligibility evaluation",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/task_write_safety_post_annotations_result_sink.py#L175-L194"
            },
            {
              "label": "English, specific insults classification, and author exceptions",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/task_write_safety_post_annotations_result_sink.py#L258-L268"
            },
            {
              "label": "Official report's explanation of insults-label effects",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/strato/lib/underTheHoodLabels.strato#L99-L104"
            }
          ]
        },
        {
          "source_id": "S075",
          "link_indices": [
            0,
            1,
            2,
            3,
            4
          ],
          "supports": "The known mechanisms and evidence gaps for this question in the original report; retain the original materials in this citation group.",
          "title": "[75] How specific account labels affect recommendation eligibility.",
          "links": [
            {
              "label": "Author rules differ between Home and HomeRecommendations",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/visibility-filtering/rules/levels.rs#L96-L164"
            },
            {
              "label": "NSFW, spam, impersonation, abuse, and other named account rules",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/visibility-filtering/rules/author_rules.rs#L155-L243"
            },
            {
              "label": "Exact definitions of NonAuthors and NonFollowers",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/visibility-filtering/rules/rule_spec/engine.rs#L74-L76"
            },
            {
              "label": "Official visibility explanations for account labels",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/strato/lib/underTheHoodLabels.strato#L117-L180"
            },
            {
              "label": "Home filtering distinguishes removal from content warnings",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/filters/vf_filter.rs#L8-L26"
            }
          ]
        }
      ],
      "related_unknowns": [],
      "topic": "49 questions still awaiting confirmation",
      "topic_file": "topic-06.json"
    },
    {
      "id": "Q49",
      "title": "Can the Article metrics visible to creators represent completed reads or the model’s reading labels?",
      "kind": "unknown",
      "conclusion": "Public Post views allow repeated views and the author’s own views; the help pages examined do not define Article reading metrics sufficiently to map them to internal training labels.",
      "conditions": [
        "Research is current through 2026-10-29; fixed public snapshots can establish the known portions, while incomplete links remain unknown."
      ],
      "practical_meaning": "Record each genuinely visible field separately and leave missing values empty; do not substitute view counts, bookmarks, or internal dwell names for the number of readers who finished.",
      "check": {
        "when": "The question or copy concerns: Can the Article metrics visible to creators represent completed reads or the model’s reading labels?",
        "needed": [
          "The open, reading, duration, and completion fields actually available to the account, and their denominators, deduplication, timing, statistical windows, and backend measurement definitions."
        ],
        "verify": [
          "Distinguish this known fact from the information still missing.",
          "Check whether the user’s conclusion exceeds the known scope stated below; obtain the outstanding information when a definitive conclusion is required."
        ],
        "if_missing": "Clearly state what can currently be confirmed and why the rest cannot be determined; use practical_meaning to provide actions that can still be taken."
      },
      "limits": [
        "The open, reading, duration, and completion fields actually available to the account, and their denominators, deduplication, timing, statistical windows, and backend measurement definitions."
      ],
      "source_units": [
        "U0657",
        "U0658",
        "U0659"
      ],
      "evidence": [
        {
          "source_id": "S059",
          "link_indices": [
            0
          ],
          "supports": "The known mechanisms and evidence gaps for this question in the original report; retain the original materials in this citation group.",
          "title": "[59] Official definition of public view counts.",
          "links": [
            {
              "label": "X View counts",
              "url": "https://help.x.com/en/using-x/view-counts"
            }
          ]
        },
        {
          "source_id": "S091",
          "link_indices": [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ],
          "supports": "The known mechanisms and evidence gaps for this question in the original report; retain the original materials in this citation group.",
          "title": "[91] Known paths and gaps from reading labels to training and serving.",
          "links": [
            {
              "label": "Training reads existing action vectors and continuous values",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix/xrex/data/recsys/recsys_batch.py#L810-L831"
            },
            {
              "label": "Home Mixer fetches aggregated history from an external service",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/query_hydrators/scoring_sequence_query_hydrator.rs#L92-L117"
            },
            {
              "label": "The public repository lacks production data sources and internal telemetry",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix/README.md#L9-L21"
            },
            {
              "label": "CLICK_DWELL_TIME binary-classification threshold 10",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix/xrex/configs/xrecsys.py#L776-L783"
            },
            {
              "label": "Labels use strictly greater than the threshold; output is probability",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix/xrex/models/loss_recsys.py#L190-L212"
            },
            {
              "label": "Binary outputs do not undergo continuous-value inverse scaling",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix/xrex/models/recsys_model.py#L532-L553"
            },
            {
              "label": "Separate feature processing for historical dwell and click dwell",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix/xrex/models/recsys_feature_prep.py#L945-L975"
            }
          ]
        }
      ],
      "related_unknowns": [],
      "topic": "49 questions still awaiting confirmation",
      "topic_file": "topic-06.json"
    }
  ],
  "related_unknowns": []
}
```

</details>

<details>
<summary>16. python3 scripts/knowledge.py get Q17 Q31</summary>

```bash
python3 scripts/knowledge.py get Q17 Q31
```

退出码：0。

```json
{
  "research_through": "2026-10-29",
  "claims": [
    {
      "id": "Q17",
      "title": "Does being written to an index guarantee that unfamiliar readers will see the content?",
      "kind": "unknown",
      "conclusion": "The public code distinguishes index production, dataset reads, personalized retrieval, filtering, scoring, and selection; candidates pass through more than one step.",
      "conditions": [
        "Research is current through 2026-10-29; fixed public snapshots can establish the known portions, while incomplete links remain unknown."
      ],
      "practical_meaning": "It is valid to say that a Post is eligible as a candidate on a given path when the conditions hold; do not provide guaranteed exposure counts, guaranteed upgrades to traffic pools, or a fixed ratio for exchanging likes for exposure.",
      "check": {
        "when": "The question or copy concerns: Does being written to an index guarantee that unfamiliar readers will see the content?",
        "needed": [
          "Static code cannot reconstruct the source configuration, candidate set, model outputs, ranking, and final display of each real reader request for an individual piece of content."
        ],
        "verify": [
          "Distinguish this known fact from the information still missing.",
          "Check whether the user’s conclusion exceeds the known scope stated below; obtain the outstanding information when a definitive conclusion is required."
        ],
        "if_missing": "Clearly state what can currently be confirmed and why the rest cannot be determined; use practical_meaning to provide actions that can still be taken."
      },
      "limits": [
        "Static code cannot reconstruct the source configuration, candidate set, model outputs, ranking, and final display of each real reader request for an individual piece of content."
      ],
      "source_units": [
        "U0561",
        "U0562",
        "U0563"
      ],
      "evidence": [
        {
          "source_id": "S037",
          "link_indices": [
            0,
            1,
            2,
            3
          ],
          "supports": "The known mechanisms and evidence gaps for this question in the original report; retain the original materials in this citation group.",
          "title": "[37] Like-event index-update thresholds, throttling, and age boundaries.",
          "links": [
            {
              "label": "Event counts, cache branch, and ignoring non-Favorite events",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix-rankall-strato/columns/favoriteEventProcessor.strato#L96-L156"
            },
            {
              "label": "Writing the next power-of-two threshold and update time",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix-rankall-strato/columns/favoriteEventProcessor.strato#L14-L57"
            },
            {
              "label": "49-hour post age, 48-hour update period, one-minute interval, and count cap",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix-rankall-strato/lib/eventProcessing.strato#L28-L70"
            },
            {
              "label": "Sending Favorite index events to the candidate processor",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix-rankall-strato/stream_forwarders/favoritePhoenixIndexingEventForwarder.strato#L3-L17"
            }
          ]
        },
        {
          "source_id": "S038",
          "link_indices": [
            0,
            1,
            2,
            3,
            4
          ],
          "supports": "The known mechanisms and evidence gaps for this question in the original report; retain the original materials in this citation group.",
          "title": "[38] Actual production conditions for 1fav, 32fav, search, and reply indexes.",
          "links": [
            {
              "label": "Count races among search_unfiltered, 32fav, and 1fav",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix-rankall-strato/columns/phoenix_rank_all/phoenixRankAllCandidateProcessor.strato#L46-L98"
            },
            {
              "label": "Reply indexes 1fav_reply and 32fav_reply",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix-rankall-strato/columns/phoenix_rank_all/phoenixRankAllCandidateProcessor.strato#L277-L298"
            },
            {
              "label": "The post_creation index at creation",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix-rankall-strato/columns/phoenix_rank_all/phoenixRankAllCandidateProcessor.strato#L301-L309"
            },
            {
              "label": "Rereading engagement counts and author data",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix-rankall-strato/columns/phoenix_rank_all/phoenixRankAllCandidateProcessor.strato#L437-L455"
            },
            {
              "label": "Routing order for sources, communities, reposts, replies, and visibility",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix-rankall-strato/columns/phoenix_rank_all/phoenixRankAllCandidateProcessor.strato#L470-L529"
            }
          ]
        },
        {
          "source_id": "S034",
          "link_indices": [
            0,
            1,
            2,
            3,
            4,
            5
          ],
          "supports": "The known mechanisms and evidence gaps for this question in the original report; retain the original materials in this citation group.",
          "title": "[34] Index windows and retrieval datasets: production data is not actual delivered impressions.",
          "links": [
            {
              "label": "Index windows for Main and Sid modes",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix-rankall/src/config/mod.rs#L168-L224"
            },
            {
              "label": "Routing to the corresponding window by index name",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix-rankall/src/store/base.rs#L1195-L1220"
            },
            {
              "label": "HOME, HOME_COLD, and HOME_HOT all reference 1fav_1day",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix/xrex/data/retrieval_dataset.py#L247-L282"
            },
            {
              "label": "HOME_COLD and HOME_HOT split data from the same source",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/phoenix/xrex/data/retrieval_dataset.py#L437-L479"
            },
            {
              "label": "Phoenix source activation conditions and actual retrieval requests",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/sources/phoenix_source.rs#L104-L149"
            },
            {
              "label": "Retrieval is still followed by filtering, scoring, and selection",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/candidate_pipeline/phoenix_candidate_pipeline.rs#L420-L507"
            }
          ]
        }
      ],
      "related_unknowns": [],
      "topic": "49 questions still awaiting confirmation",
      "topic_file": "topic-06.json"
    },
    {
      "id": "Q31",
      "title": "Do a ten-minute delay and seven-day TTL guarantee that recommendations begin or resume at a particular time?",
      "kind": "unknown",
      "conclusion": "The aggregation forwarder sets a ten-minute delay and maxLag target; the account label’s expiration is calculated as seven days after the write time; the three-out-of-five rule excludes accounts that already have the same account label.",
      "conditions": [
        "Research is current through 2026-10-29; fixed public snapshots can establish the known portions, while incomplete links remain unknown."
      ],
      "practical_meaning": "Treat delay, expiration, and exposure as separate concepts; do not promise immediate effect on the third entry, a seven-day extension on every match, or automatic restoration of the original view count on the eighth day.",
      "check": {
        "when": "The question or copy concerns: Do a ten-minute delay and seven-day TTL guarantee that recommendations begin or resume at a particular time?",
        "needed": [
          "There are no complete observations of actual per-event delays, failed-task retries, label-expiration reads, or removal or relabeling by other systems; nor are there causal data about actual exposure after expiration."
        ],
        "verify": [
          "Distinguish this known fact from the information still missing.",
          "Check whether the user’s conclusion exceeds the known scope stated below; obtain the outstanding information when a definitive conclusion is required."
        ],
        "if_missing": "Clearly state what can currently be confirmed and why the rest cannot be determined; use practical_meaning to provide actions that can still be taken."
      },
      "limits": [
        "There are no complete observations of actual per-event delays, failed-task retries, label-expiration reads, or removal or relabeling by other systems; nor are there causal data about actual exposure after expiration."
      ],
      "source_units": [
        "U0603",
        "U0604",
        "U0605"
      ],
      "evidence": [
        {
          "source_id": "S079",
          "link_indices": [
            0,
            1,
            2,
            3,
            4,
            5
          ],
          "supports": "The known mechanisms and evidence gaps for this question in the original report; retain the original materials in this citation group.",
          "title": "[79] Default account-label aggregation for three of the latest five records.",
          "links": [
            {
              "label": "Three-of-five, mediaOnly=false, 60 days, seven-day TTL, and author exclusions",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/safety-label-user-agg/postToUserLabelRules.strato#L395-L425"
            },
            {
              "label": "Taking the window, then counting existing post labels",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/safety-label-user-agg/postToUserLabelRules.strato#L251-L283"
            },
            {
              "label": "Evaluating trigger events and user exclusions",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/safety-label-user-agg/postToUserLabelRules.strato#L119-L142"
            },
            {
              "label": "mediaOnly as a configurable option and its scan scope",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/safety-label-user-agg/postToUserLabelRules.strato#L152-L177"
            },
            {
              "label": "Another possible-NSFW default requires eleven matches among ten records",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/safety-label-user-agg/postToUserLabelRules.strato#L360-L394"
            },
            {
              "label": "Feature switches can override public JSON",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/safety-label-user-agg/postToUserLabelRules.strato#L430-L432"
            }
          ]
        },
        {
          "source_id": "S080",
          "link_indices": [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ],
          "supports": "The known mechanisms and evidence gaps for this question in the original report; retain the original materials in this citation group.",
          "title": "[80] Account-aggregation events, timeline, reposts, and expiration.",
          "links": [
            {
              "label": "Applied events and label-dependent trigger rules",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/safety-label-user-agg/safetyLabelToUserLevelAggregationV2Processor.strato#L12-L28"
            },
            {
              "label": "Reverse-ordered userTimeline, repost-original labels, and event time",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/safety-label-user-agg/safetyLabelToUserLevelAggregationV2Processor.strato#L56-L83"
            },
            {
              "label": "Writing account labels with current time plus TTL",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/safety-label-user-agg/safetyLabelToUserLevelAggregationV2Processor.strato#L89-L106"
            },
            {
              "label": "Stream's ten-minute delay and maxLag target",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/safety-label-user-agg/safetyLabelToUserLevelAggregationV2Forwarder.strato#L3-L20"
            },
            {
              "label": "A separate NSFW media-event path",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/botmaker-rules/scarecrow/bot/NsfwTweetMediaProcessor.bot#L3-L30"
            },
            {
              "label": "A separate path aggregating one-day events by post ID",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/botmaker-rules/scarecrow/derived-feature/ApplyNsfwUserLabel.df#L19-L45"
            },
            {
              "label": "Labeling or review-submission conditions and validity periods on the separate path",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/botmaker-rules/scarecrow/derived-feature/ApplyNsfwUserLabelOrCreateReport.df#L2-L81"
            }
          ]
        },
        {
          "source_id": "S074",
          "link_indices": [
            0,
            1,
            2
          ],
          "supports": "The known mechanisms and evidence gaps for this question in the original report; retain the original materials in this citation group.",
          "title": "[74] Seven-day account label for problematic pinned URLs.",
          "links": [
            {
              "label": "Pinned after and before states, URL resolution, exemptions, and seven-day expiration",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/botmaker-rules/scarecrow/bot/PinnedLowQualityOrBadUrl.bot#L2-L44"
            },
            {
              "label": "SpamHighRecall account rule",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/visibility-filtering/rules/author_rules.rs#L204-L208"
            },
            {
              "label": "Recommendation entry point where the account rule executes",
              "url": "https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/visibility-filtering/rules/levels.rs#L142-L164"
            }
          ]
        }
      ],
      "related_unknowns": [],
      "topic": "49 questions still awaiting confirmation",
      "topic_file": "topic-06.json"
    }
  ],
  "related_unknowns": []
}
```

</details>

## 其他实际读取与输入准备命令

最初执行了以下本地读取与文件名查找（没有打开未列出的仓库文件）：

```bash
cat /workspace/scratch/8875c799c753/for-you-skills-fixes/skills/x-assistant/SKILL.md
cat references/routing.json
cat references/knowledge-guide.md
rg --files workflows scripts references | sort
```

最后一项发现根目录没有 `workflows` 子目录，输出 `rg: workflows: No such file or directory (os error 2)`；技能工作流实际位于 `references/workflows/`，随后按 routing 表读取了正确路径。该查找没有尝试读取仓库测试、审计报告或实现说明。

其余读取命令：

```bash
cat references/workflows/x-myth-check.md
cat references/workflows/x-explain.md
cat references/workflows/x-review-posts.md
cat references/observations.md
cat references/research-errata.md
```

临时输入文件的实际准备命令及输出：

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('/tmp/x-assistant-remediation-probes')
p.mkdir(exist_ok=True)
raw = '[{"url":"https://x.com/demo/status/123","observed_at":"2026-10-30T12:00:00Z","metric_scope":"post","text":"正文","body_status":"complete","metrics":{"views":"100","likes":"5"}},{"url":"https://x.com/demo/status/123","observed_at":"2026-10-30T12:00:00Z","metric_scope":"owner_analytics","metrics":{"replies":"2"}}]'
(p / 'observations.json').write_text(raw, encoding='utf-8')
(p / 'post.txt').write_text('正文', encoding='utf-8')
print(raw)
print('post.txt bytes:', (p / 'post.txt').read_bytes())
PY
```

退出码：0。

```text
[{"url":"https://x.com/demo/status/123","observed_at":"2026-10-30T12:00:00Z","metric_scope":"post","text":"正文","body_status":"complete","metrics":{"views":"100","likes":"5"}},{"url":"https://x.com/demo/status/123","observed_at":"2026-10-30T12:00:00Z","metric_scope":"owner_analytics","metrics":{"replies":"2"}}]
post.txt bytes: b'\xe6\xad\xa3\xe6\x96\x87'
```
