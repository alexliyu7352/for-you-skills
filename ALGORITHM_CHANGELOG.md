# Algorithm synchronization changelog

This log records reviewed changes in [X's public algorithm](https://github.com/xai-org/x-algorithm), separately from this package's [release history](CHANGELOG.md). [中文说明](docs/research-update.zh-CN.md).

## 2026-11-08 — For You Skills 1.3.0

**For creators:** the public Home Mixer settings put more weight on predicted reading time, with smaller changes to likes, clicks and sharing. This does not establish an equivalent increase in impressions. Video and transparency features gain implementation support, often behind disabled switches. The code still does not impose a daily second-post discount or a universal Article bonus.

| Review field | Value |
| --- | --- |
| Previous reviewed revision | `606b254b45be798bfaecfa8c23f5a9c51bc8000c` |
| Reviewed upstream head | `3b6919f87532e57063bb3f1e85c2f509323b513e` |
| Review date | 2026-11-08 UTC |
| Commit interval | 7 commits; latest committed 2026-11-07 04:10:51 UTC |
| Net diff | 289 files; 21,004 insertions and 8,914 deletions |
| Knowledge result | 14 dated findings/rechecks mapped to 73 original claim/unknown IDs |
| Original research | 578 entries and 49 unresolved questions preserved; original cutoff 2026-10-29 |
| Verification scope | Public source diff and relevant call paths, defaults and gates; no production rollout or reach experiment |

[Exact comparison](https://github.com/xai-org/x-algorithm/compare/606b254b45be798bfaecfa8c23f5a9c51bc8000c...3b6919f87532e57063bb3f1e85c2f509323b513e). The upstream README is unchanged across this interval; reviewing its changelog alone would miss these changes.

### Reviewed commits

Dates below use UTC, which can differ from dates shown in a local GitHub timezone. Every commit uses the same upstream subject, “Open-source X Recommendation Algorithm”; it is not a useful change summary by itself.

| Commit | Commit date (UTC) | Files touched in that commit |
| --- | --- | ---: |
| [7fef3ba](https://github.com/xai-org/x-algorithm/commit/7fef3ba19d82d1f76dec65f31b981ca817a2ea06) | 2026-10-30T01:27:43Z | 90 |
| [9106e9f](https://github.com/xai-org/x-algorithm/commit/9106e9f33ee9cc6a92929fc798ae6c566e2841cb) | 2026-10-31T02:25:48Z | 58 |
| [b220448](https://github.com/xai-org/x-algorithm/commit/b220448766ab4ee4c83d58a67d51f0cb5bda86c2) | 2026-11-03T02:56:51Z | 62 |
| [b508926](https://github.com/xai-org/x-algorithm/commit/b5089266c0fbad66f388051f8f89056e2a8f974d) | 2026-11-04T17:01:39Z | 119 |
| [021afa4](https://github.com/xai-org/x-algorithm/commit/021afa44cb5c5b10afa773cb52c0f5087603d478) | 2026-11-05T05:16:01Z | 69 |
| [2e2295b](https://github.com/xai-org/x-algorithm/commit/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe) | 2026-11-06T03:48:04Z | 71 |
| [3b6919f](https://github.com/xai-org/x-algorithm/commit/3b6919f87532e57063bb3f1e85c2f509323b513e) | 2026-11-07T04:10:51Z | 14 |

### What the skills now know

The entries below are also distributed as [machine-readable evidence](knowledge/algorithm-updates.json). Use `python tools/knowledge.py updates ID` for full details, affected historical IDs, practical implications and limits. Source links are pinned to reviewed revisions.

#### A20261108-01 — Home Mixer interaction weights: likes, clicks, sharing and dwell

The later Home Mixer defaults change seven coefficients. This supersedes the old coefficient table for this service at the reviewed revision, not the historical record or every live request.

- Favorite 0.66 -> 0.708; Click 0.3 -> 0.274; VideoOpen 0.02 -> 0; Share 2 -> 2.118; ContDwellTime 0.006 -> 0.0075; ContClickDwellTime 0.4 -> 0.385; NotInterested -52.272 -> -53.07. The change is in commit 021afa44cb5c5b10afa773cb52c0f5087603d478.
- Reply remains 5, Retweet remains 1, ShareViaCopyLink remains 20 and ShareViaDm remains 5. Share and Retweet are separate predictions.
- VM Ranker has its own unchanged defaults: Favorite 0.5, Click 0.3, VideoOpen 0.07, Share 2, ContDwellTime 0.004, ContClickDwellTime 0.4, NotInterested -47.52. Never label the Home Mixer numbers as universal VM Ranker values.
- Holding a 5-second prediction fixed, the Home Mixer continuous-dwell term goes from 5*0.006=0.03 to 5*0.0075=0.0375. That term increases 25%; the final score and impressions do not thereby increase 25%.
- The later FavoriteWeight of 0.708 disproves a present-tense claim that 0.66 is the highest value in all X history. The earlier maximum among the examined October snapshots stays 0.66; this review does not establish an all-time maximum across every version or experiment.

**Practical use:** Make the promise of the opening worth reading through. Do not optimize a publishing calendar or predict impressions from one coefficient.

**Limits:** These are public defaults for named services, not a dump of the effective feature switches for every request. Predictions, other score terms, filtering and competition still matter. The earlier October 0.004 -> 0.006 change remains a historical fact; do not rewrite Q03 as if the old 50% comparison never occurred. The public CLICK_DWELL_TIME training output is a binary probability; the full adapter to the Home Mixer field and its raw-label units remain unverified. The new 0.385 coefficient does not resolve Q05 and cannot be described as points per second.

**Sources:** [Current Home Mixer weights](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/params/param.rs#L404-L539) · [Before this review interval](https://github.com/xai-org/x-algorithm/blob/606b254b45be798bfaecfa8c23f5a9c51bc8000c/home-mixer/params/param.rs#L393-L500) · [Separate VM Ranker defaults](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/vm-ranker/params.rs#L1-L131) · [Home Mixer VM request and fallback](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/scorers/vm_ranker.rs#L60-L110)

#### A20261108-02 — Home excursion predictions: time after opening a video or profile

Home Mixer now enables existing excursion score support by default and selects an aggregation type with those heads.

- PhoenixAggregationType changes from DENSE_WITH_LONG_DWELL to DENSE_WITH_LONG_DWELL_HOME_EXCURSION; EnableHomeExcursionScores changes false -> true.
- The existing scorer can request home_video_continuation_secs and home_profile_visit_secs. These fields were not first invented in this interval.
- Public local and VM video-continuation/profile-visit coefficients remain zero. A prediction being requested is different from a nonzero direct score contribution.

**Practical use:** Judge a video or profile visit by whether the destination is useful. This change alone supplies no new guaranteed video or profile bonus.

**Limits:** An enabled prediction path does not establish the active model or scoring settings for all traffic.

**Sources:** [Aggregation and switch](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/params/param.rs#L169-L174) · [Excursion default](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/params/param.rs#L299-L315) · [Head request](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/scorers/phoenix_scorer.rs#L131-L182) · [VM coefficients](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/vm-ranker/params.rs#L67-L101) · [Local coefficients](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/scorers/value_model.rs)

#### A20261108-03 — Training configuration: time gaps, excursion history and view loss

The named home_direct_packed training configuration changes. Its view-loss reduction is not a halving of the ranking reward for reading.

- view_loss_weight changes 1 -> 0.5 for binary RECAP_DWELLED, RECAP_NOT_DWELLED and VIDEO_QUALITY_VIEW losses, not the continuous-dwell ranking coefficient.
- The config adds continuation loss 0.013 and profile-visit loss 0.0035, enables time-gap features (learning-rate scale 4) and excursion history. The gaps describe request/impression history, not a recommended interval between creator posts.
- The base continuous and immersive CREAD loss weights remain 0.1. CREAD predicts continuous actions; it is not a new explicit Article-completion reward.
- Other changes include packed candidate length [32,128] -> [128], history mean 510 -> 414, embedding decay 2.8e-4 -> 5.6e-4, stochastic rounding and optimizer settings. The named GB300 configuration does not inherit every home_direct_packed override.
- Ordinary DWELL_TIME label validation accepts 0 through 86400 seconds; this check does not establish excursion-label limits or a full-day reading reward.

**Practical use:** Keep writing for actual reader interest. These training settings cannot tell a creator to wait a fixed number of hours or target a specific word count.

**Limits:** A checked-in configuration does not prove deployment to every reader. Model-training loss weights and ranking coefficients belong to different stages.

**Sources:** [Named configurations and inherited base](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/phoenix/xrex/configs/xrecsys.py#L480-L584) · [Conditional excursion losses](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/phoenix/xrex/configs/xrecsys.py#L263-L313) · [Time-gap features](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/phoenix/xrex/models/recsys_feature_prep.py#L50-L80) · [Binary view targets](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/phoenix/xrex/data/recsys/constants.py#L566-L570) · [Loss application](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/phoenix/xrex/models/recsys_model.py#L5011-L5017) · [Ordinary dwell label validity](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/phoenix/xrex/models/recsys_model.py#L4628-L4635) · [Inherited training base](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/phoenix/xrex/configs/xrecsys.py#L316-L400)

#### A20261108-04 — Video Carousel click model, extra score terms and filters

The separate Video Carousel gains an optional click model and filtering support; its overall switch and the click-model switch remain false in public defaults.

- When a CTR model is available the helper returns its score from the video-open prediction and embedding. The linear model uses an intercept, a clipped-logit open term and 1024 embedding weights; its returned score is a logit, not directly a probability.
- The fallback is a*P(open) + b*immersiveVQV + c*P(open)*immersiveDwell + d*weightedScore + e*P(open)*continuationSecs. New d and e defaults are zero.
- EnableVideoCarousel=false, EnableVideoCarouselCtrModel=false, EnableVideoCarouselSeenFilter=false; high-risk filtering changes false -> true and medium-risk filtering defaults false. The high-risk filter also rejects candidates with missing brand-safety verdicts.
- The optional seen hydrator reads up to 2000 IDs over three days and checks both original and candidate IDs. Its operation is gated by Carousel and seen-filter switches.
- Carousel VideoOpenWeight remains 1.0; the ordinary Home Mixer VideoOpenWeight=0 does not replace it. The extra-candidate setting remains 30, now parameterized.

**Practical use:** Use video where movement or demonstration improves the explanation. There is no basis here to promise a platform-wide video boost.

**Limits:** Separate Carousel and ordinary Home paths, model availability and feature switches. Q12 remains unresolved for actual rollout and measured effects.

**Sources:** [Scoring branches](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/util/video_carousel.rs#L44-L74) · [Linear CTR model](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/util/video_carousel_ctr_model.rs#L19-L32) · [Feature switches and weights](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/params/param.rs#L1223-L1355) · [Seen history](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/query_hydrators/video_carousel_seen_query_hydrator.rs#L9-L37) · [High-risk and missing verdict filtering](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/filters/video_carousel_filter.rs#L37-L41)

#### A20261108-05 — Under the Hood: weighted top score contributions

Requested Under the Hood traces can now carry the largest weighted score contributions rather than only raw prediction heads.

- VM Ranker selects up to three terms by absolute contribution, retaining a term only when its absolute share of the sum of absolute contributions is at least 0.10.
- Named weighted_terms replace the old scalar-only sum. Cached scoring requests can also produce contributions when explicitly requested.
- The trace page requires login, a feature switch and a decodable payload. It returns unavailable/404 when the required path is unavailable.

**Practical use:** If the interface is available, use it as partial evidence about one scoring step, alongside candidate and visibility information.

**Limits:** This is not a full causal explanation of impressions, a list of every recommendation decision, or evidence that all accounts have access.

**Sources:** [Contribution selection](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/vm-ranker/scoring/value_model.rs#L187-L240) · [Score terms](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/xai-value-model/scoring.rs) · [Home trace payload](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/util/under_the_hood.rs) · [Gated trace page](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/under-the-hood/jetfuel/routes/trace.tsx#L13-L45)

#### A20261108-06 — Under the Hood: labeled post lists and conditional appeals

The report code adds labeled-post IDs and conditional appeal information, with backend and UI feature switches; public defaults do not make them universally visible.

- The data pipeline collects per-label IDs with a storage cap of 500. Serving normally shows up to three; above three it suppresses the list when labeled posts exceed 5% of the monthly cohort, otherwise selects up to 50 recent IDs. Takedown lists bypass that percentage rule.
- Backend report-post-ID, appeals and sensitive-media appeal flags default false; the report UI has its own post-ID flag. A visible list can include posts that had a label earlier, even after removal.
- Appeal guidance depends on label family and feature flags. For supported post-label appeals, the guidance says the label must still be present; the report does not verify its current state. Account-label appeals are always absent in this report implementation.
- Existing cohort rules remain: at least 10 eligible posts, account older than 365 days, the ten-day month-readiness window, and incomplete-data fallback. Reposts/nullcasts remain excluded and edit chains are deduplicated logically. Label categories and described effects did not gain a new penalty just because IDs became reportable.

**Practical use:** When available, save the actual report period and affected posts and inspect the stated label. A missing list or removed label does not prove there was no earlier label.

**Limits:** This is reporting and appeal plumbing, not a new universal punishment or rollout announcement. Existing eligibility and observation limits still apply.

**Sources:** [Report gates and limits](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/under-the-hood/strato/lib/params.strato#L24-L37) · [Serving rules](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/under-the-hood/strato/columns/underTheHoodReport.User.strato#L340-L367) · [Storage limit](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/under-the-hood/scalding/UnderTheHoodCommon.scala#L135-L146) · [UI gates](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/under-the-hood/jetfuel/routes/report.tsx#L333-L344) · [Appeal conditions](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/under-the-hood/strato/lib/underTheHoodLabels.strato#L437-L520)

#### A20261108-07 — New notification filters are not new Home recommendation penalties

Visibility evaluation expands to mention, reply, media-tag, like and repost notifications. Their rules must not be copied into claims about all Home recommendations.

- Mention/reply notifications add DUPLICATE_CONTENT and SMYTE_SPAM_TWEET drops for non-authors; LOW_QUALITY has an older-post condition (not newer than 2019-04-01).
- DUPLICATE_MENTION, ABUSIVE, UNTRUSTED_URL and DOWNRANK_SPAM_REPLY apply to non-followers with the viewer quality filter enabled; RISKY_HIGH_VIZ_REPLY applies to non-followers. Existing SPAM_HIGH_RECALL remains.
- Media-tag notification handling uses actor/account and follow-relationship rules with a community exception, not the whole mention/reply post-label list.
- Like/repost notifications check the actor and that the referenced post exists and belongs to the recipient; their PureCore post fetch does not hydrate the full safety-label rules.

**Practical use:** If an expected notification is missing, inspect its notification-specific audience and conditions. Do not infer account-wide reach suppression from that alone.

**Limits:** This diff does not add these mention/reply notification rules to the Home recommendation lists.

**Sources:** [Surface rule lists](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/visibility-filtering/rules/levels.rs#L178-L278) · [Tweet notification rules](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/visibility-filtering/rules/tweet_rules.rs#L961-L1027) · [Like/repost evaluation](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/visibility-filtering/post_evaluator/notification.rs#L46-L99) · [Like/repost PureCore hydration](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/visibility-filtering/rules/engine.rs#L364-L369)

#### A20261108-08 — Geographic media restriction and promoted hydration surfaces

GeoRestrictedMedia is added to ordinary TimelineHome with a non-author audience; a separate promoted-hydration surface is also introduced.

- The geographic media rule audience changes Everyone -> NonAuthors wherever that rule is used. HomeRecommendations already has its DMCA rule.
- TimelineHomePromotedHydration is a distinct rule list. Dynamic-product-ad limited-engagement reasons depend on feature/policy evaluation, not a blanket advertising exemption.
- EvaluateTweets can distinguish deleted and bounce-deleted results from not-found. Much of the rest is hydration and notice/appeal refactoring; action precedence remains unchanged.

**Practical use:** For a visibility diagnosis, identify the viewer region, author/non-author relation and exact display surface before drawing conclusions.

**Limits:** A different hydration surface does not mean advertisements bypass all moderation.

**Sources:** [Home and promoted lists](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/visibility-filtering/rules/levels.rs#L298-L382) · [Geographic media audience](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/visibility-filtering/rules/tweet_rules.rs#L884-L896)

#### A20261108-09 — Media tags now count in one mention-based safety task

One realtime safety-task eligibility check now counts unique text mentions together with media-tag handles.

- The numeric threshold remains two; unique, case-insensitive handle counting across text mentions and media tags is new. Previously this path counted whitespace-delimited words starting with @, including repetitions. High-PageRank/gray-badge exclusions, delay and prior SpamHighRecall checks remain.
- Selection for a classifier is not a violation result or an enforcement action. Classifier input can now include media tags.

**Practical use:** Tag people because they are relevant to the post. Do not interpret two tags as an automatic ban, and do not assume media tagging avoids mention-related checks.

**Limits:** This is one task-selection path, not a universal hashtag/mention limit.

**Sources:** [Eligibility conditions](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/grox/flows/ptos/task_filter.py#L37-L100) · [Post handle accessors](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/grox/core/data_loaders/data_types.py#L740-L752) · [Media tags in classifier input](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/grox/core/lm/post.py)

#### A20261108-10 — Safety cache and enforcement plumbing: keep cache time separate from penalties

Safety labels gain optional shared cache support and enforcement-control changes. Cache lifetimes are not label penalty durations.

- The new Dragonfly cache accepts found results for 24 hours and not-found results for ten minutes as read-freshness limits; physical writes use a 24-hour TTL for both. Shadow/serve rollout buckets default to zero. Existing local ten-second caching remains; stale outage fallback still filters expired labels.
- An unknown valid non-factory classifier head with no head/alias control row defaults to Recording rather than Rules. That default records without adding enforcement actions.
- PageActionSuspend adds permanent/policy options; the legacy default remains non-permanent PlatformManipulation. Permanent upgrades are distinguished in deduplication.
- The video hidden-overlay detector changes threshold -1.75 -> -1.0 and skips its reveal step for sufficiently opaque motion (>0.35), alongside prompt changes. This is detector behavior, not a new creator reward.

**Practical use:** Use the actual label and its applicability to diagnose restrictions. Do not tell creators that a cache setting establishes a 24-hour penalty.

**Limits:** Optional cache rollout, classifier eligibility, enforcement policy and label expiry are different layers.

**Sources:** [Label source and stale handling](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/safety-label-source/source.rs#L127-L175) · [Shared cache defaults](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/safety-label-source/dragonfly.rs#L25-L63) · [Unconfigured head handling](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/abuse-enforcement-service/service-lib/src/action_control.rs#L1071-L1095) · [Detector logic](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/grox/libs/video_tools/image.py) · [Cache read-freshness limits](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/safety-label-source/dragonfly.rs#L246-L251) · [Physical cache write TTL](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/safety-label-source/dragonfly.rs#L945-L955)

#### A20261108-11 — Grok Analyze and Post Video score fields have zero public weights

ReactWithVideo is renamed to PostVideo and GrokAnalyze is added. Both named weights remain zero in Home Mixer and VM Ranker.

- The value-model structure adds corresponding named predictions/terms. Existence of a field is not evidence of an active bonus.
- No separate explicit Article-completion reward is introduced by these fields.

**Practical use:** Do not advise creators to summon Grok or add video merely to collect a supposed new score bonus.

**Limits:** Effective production overrides are unknown; zero public defaults are not proof of every live setting either.

**Sources:** [Home weights](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/params/param.rs#L484-L495) · [VM weights](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/vm-ranker/params.rs#L102-L113) · [Weighted terms](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/xai-value-model/scoring.rs)

#### A20261108-12 — Optional retrieval and page-ranking extensions remain unproven creator bonuses

Two-tower retrieval and page reward code add options, without public nonzero/default-enabled evidence for universal use.

- Two-tower objective blending accepts tweet_click; w_tweet_click defaults to 0 and objective_head_weights is empty.
- PageRL adds DM/copy-link reward coefficients defaulting to zero; generic sharing remains 4.
- PageDecodeRewardHead is new with default 0; request fields eta, nu_author, nu_sid and prior_tau are left unset by Home Mixer. EnablePageDecodeRerank and EnablePageRlExploration remain false.
- Existing page completion_bonus=1 concerns an impressed slate and the final slot video-quality-view condition, not reading an Article to its final word.

**Practical use:** Do not turn an optional retrieval head or page reward into a rule that one share type, Article completion or posting cadence guarantees more exposure.

**Limits:** Training, retrieval, item scoring and whole-page selection are separate stages.

**Sources:** [Retrieval objectives](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/phoenix/xrex/models/recsys_two_tower_model.py#L2963-L2998) · [Page rewards](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/phoenix/xrex/models/page_rl.py#L63-L78) · [Page reward calculation](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/phoenix/xrex/models/page_rl.py#L348-L366) · [Home feature defaults](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/params/param.rs) · [Slate completion condition](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/phoenix/xrex/models/page_rl.py#L156-L168)

#### A20261108-13 — Unchanged: daily frequency myth, cold start, Article and first-image boundaries

The compared code still does not impose a daily second-post discount or a universal Article bonus; the relevant author-count, cold-start and V8.2 rendering mechanisms did not change.

- author_pool_counts and post-fusion behavior remain the same: per-candidate-batch counts, not an accumulating daily count. VM diversity defaults still yield 1, 0.625, 0.4375 with decay 0.5 and floor 0.25.
- author_cold_start.rs and fair_share_ranking_filter.rs are byte-identical over the interval. Ordinary AgeFilter retains 48 hours; that is not a universal lifetime for every surface.
- renderer_v82.py is byte-identical: a 4000-character text path, a 200-character Article-title path and the first available image/video media path remain. This is not all X models: V8 Search has a different multiple-media budget.
- Candidate filtering retains the same main predicates; allocation/partition refactoring does not establish a new posting rule.

**Practical use:** Keep choosing Article, Post or Thread by the material and reader needs. Publish a second useful piece when it is ready; the code supplies no daily second-post timer to wait out.

**Limits:** Rechecked source behavior is not verification of every production configuration, guaranteed exposure or unchanged model weights.

**Sources:** [Per-batch author counts and fusion](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/xai-value-model/scoring.rs#L265-L324) · [VM diversity defaults](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/vm-ranker/params.rs) · [Unchanged cold-start scorer](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/scorers/author_cold_start.rs) · [Source-level fair share](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/filters/fair_share_ranking_filter.rs) · [V8.2 text and media](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/grox/flows/mm_emb/renderer_v82.py)

#### A20261108-14 — Engineering changes and a reverted ads experiment

Not every changed line changes creator-facing behavior: this interval includes observability, storage, inference and test refactors, plus a reverted ads-blending default.

- AdsBlenderType changes multi_risk -> slot_spread in 9106e9f, then back in b220448; the interval has no net change to that default. Following ad-spacing logic is unchanged, while drop-cause logs and campaign metadata are added.
- Ad history gains an XDC cache-write default with a 300-second TTL and injection logging. Those are storage/diagnostic settings, not a publishing interval.
- The new candidate-pipeline result_size_for(query) method delegates to the existing result_size() by default, with no repository override found.
- Video inference handles cached candidates and missing predictions more explicitly; model-loading and cache fallback changes are operational behavior, not proof of increased video distribution.

**Practical use:** Use the separate upstream changelog to distinguish durable behavior changes from temporary settings and implementation maintenance.

**Limits:** The review compares public code. It does not measure production experiments or account-level effects.

**Sources:** [Home parameters](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/params/param.rs) · [Pipeline implementation](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/candidate-pipeline/candidate_pipeline.rs)

### How the next synchronization works

1. Run `python tools/check_upstream.py`. The [weekly/manual workflow](.github/workflows/check-upstream.yml) performs the same read-only check, writes a job summary, and retains the complete JSON commit/path report as a downloadable artifact for 30 days. It also runs when the checkpoint, checker or workflow changes on main. `up_to_date` means no newer main commit than the checkpoint; `review_required` means new commits exist. A fetch failure or divergent history is an error, never a clean result.
2. Review the complete interval and intermediate commits. Trace each affected service and feature switch; distinguish changed defaults, optional code, reversions and unchanged behavior. Do not infer production rollout from code presence.
3. Update `knowledge/algorithm-updates.json`, affected historical-ID mappings, shared instructions and both public-language explanations. Retain original report bytes, hashes, source IDs and historical evidence. Preserve previous reviewed states in release tags and append a new section to this log.
4. Advance the reviewed checkpoint only as part of the reviewed content change. Rebuild with `python tools/build.py`, then run `python tools/validate.py`, `python tools/build.py --check` and `python -m unittest discover -s tests -v`. Exercise the relevant creator questions from independent installed bundles.
5. Publish a new tested package version. The monitor never edits conclusions, closes unknowns, creates a release or updates existing personal installations automatically.

For an already-fetched local algorithm checkout, use `python tools/check_upstream.py --upstream /path/to/x-algorithm --ref main`. Local mode does not fetch or modify that checkout. It requires complete history for the comparison; use remote mode if it is shallow or partial. The report's changed files are the net base-to-head diff; inspect the listed commits as well to catch reverted changes.
