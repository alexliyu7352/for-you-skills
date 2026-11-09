# X's algorithm update: a 25% increase in the dwell weight

[中文版](research-update.zh-CN.md)

Code reviewed: November 8, 2026. Text revised: November 9, 2026. Covers For You Skills 1.3.0.

X changed Home Mixer's continuous dwell coefficient from `0.006` to `0.0075`, an increase of 25%. Before treating that as a reason to write longer posts, it helps to work through what the coefficient actually multiplies.

Home Mixer helps assemble the Home feed. It uses predictions about a particular reader and post: how likely that reader is to like or click it, and how long they might stay. Hold the dwell prediction at five seconds. The old coefficient gives `5 × 0.006 = 0.03`; the new one gives `5 × 0.0075 = 0.0375`.

That contribution to the score has increased by 25%. Other predictions still contribute to the total, and the post must pass filters and compete with other candidates before it reaches the reader. This change alone cannot tell us how many more impressions a post will get.

This review compares `606b254`, where the previous research stopped, with `3b6919f`: seven commits and 289 changed files. The sections below cover changes relevant to publishing. The [algorithm changelog](../ALGORITHM_CHANGELOG.md) has the complete commit list and detailed findings. This is a review of public source code; it does not include a production traffic experiment.

## Seven changes to the weight table

These are Home Mixer's public defaults. General sharing and reposting are separate predictions.

| Predicted outcome | Previous coefficient | Reviewed coefficient |
| --- | ---: | ---: |
| Like | 0.66 | 0.708 |
| Click | 0.3 | 0.274 |
| Open a video | 0.02 | 0 |
| General share | 2 | 2.118 |
| Continuous dwell | 0.006 | 0.0075 |
| Click dwell | 0.4 | 0.385 |
| Not interested | -52.272 | -53.07 |

The [previous parameters](https://github.com/xai-org/x-algorithm/blob/606b254b45be798bfaecfa8c23f5a9c51bc8000c/home-mixer/params/param.rs#L393-L500) and [reviewed parameters](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/params/param.rs#L404-L539) show small increases for likes and general shares, a decrease for clicks, and a slightly larger negative coefficient for "not interested." They weight predictions. Multiplying the likes a post has already received by `0.708` will not give you its recommendation score.

VM Ranker, another ranking service, retains its own defaults: `0.5` for likes and `0.004` for continuous dwell. If two weight tables disagree, check which service each one describes. The [VM Ranker parameters](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/vm-ranker/params.rs#L1-L131) are also a reason not to treat the table above as the configuration used for every request across X.

One uncertainty remains around click dwell. The public evidence has not established the full conversion from the model's output to Home Mixer's field. A coefficient of `0.385` therefore cannot be read as "0.385 points per second." Changing the coefficient has not filled that gap in the evidence.

For a writer, "make the post longer" is too much to infer from these numbers. If an opening promises a comparison of two options, check how far the reader has to get before finding that comparison. Keep the detail needed to make the case; cut paragraphs that merely delay it. That is editorial advice. The code supplies no ideal length for every post.

## What was added for video and Grok

Home Mixer now requests existing predictions for time spent watching after opening a video and time spent visiting a profile by default. The corresponding direct scoring coefficients remain zero in the public settings reviewed. Reading the [prediction switch](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/params/param.rs#L299-L315) alongside the [VM Ranker coefficients](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/vm-ranker/params.rs#L67-L101) shows why requesting a prediction does not by itself establish a score bonus.

A separate Video Carousel module adds a click prediction model, code for filtering previously seen posts, and changes to safety filtering. Its overall switch, new click-model switch and seen-filter switch all remain off in the public defaults. Two new scoring coefficients are zero as well. These [module settings](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/params/param.rs#L1223-L1355) do not tell us which users, if any, have been assigned configurations that enable those features.

The zero for opening a video in the table above needs the same care. That is the ordinary Home Mixer parameter. Video Carousel's own video-open coefficient is still `1.0`. Video has other predictions and recommendation paths, so this is not evidence that all video has stopped contributing to ranking.

`GrokAnalyze` is a new field, and `ReactWithVideo` has been renamed `PostVideo`. Both fields have zero default weights in [Home Mixer](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/home-mixer/params/param.rs#L484-L495) and [VM Ranker](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/vm-ranker/params.rs#L102-L113). Their presence does not support telling people to summon Grok in a reply for extra reach.

There is too little here to decide that a piece should become a video. Video can show the steps of an operation directly. A table or image may be easier to return to when the reader needs to check numbers. Those are useful reasons to choose a format; the rollout of the new scoring options remains unverified.

## Label reports can point to individual posts

Under the Hood is X's transparency report. The new code can list IDs of some posts that have been labeled, allowing a reader to follow a label back to a particular post. The data path exists, but the backend and interface have separate switches. The public defaults do not turn the lists on generally. Both the [backend switches](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/under-the-hood/strato/lib/params.strato#L24-L37) and [interface switch](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/under-the-hood/jetfuel/routes/report.tsx#L333-L344) are visible in the code.

Even where a list is available, count and percentage limits apply. The report describes what happened during a period. A post that had a label removed can still appear. Appeal guidance says that a supported post-label appeal requires the label to remain present; the report does not check its current state for you. The [list rules](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/under-the-hood/strato/columns/underTheHoodReport.User.strato#L340-L367) and [appeal guidance conditions](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/under-the-hood/strato/lib/underTheHoodLabels.strato#L437-L520) address those separate questions.

Ranking traces also gain explanations of some weighted score contributions. They can identify larger contributions in a particular scoring calculation, but cannot explain all the impressions a post received. The [contribution code](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/vm-ranker/scoring/value_model.rs#L187-L240) runs only when requested.

If your account has the report, save its reporting period, generation time, label names and post links when investigating reach. That lets you compare the same posts over the same period. Low view counts, or the absence of a post list, are insufficient to establish whether a post has been restricted.

Notifications have changed too. Mentions, replies, media tags, likes and repost notifications gain checks. Some depend on whether the recipient follows the sender; others also depend on the recipient's quality-filter setting. These are [notification rules](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/visibility-filtering/rules/levels.rs#L178-L278). They have not been added wholesale to Home recommendation rules. A missing notification therefore does not prove that strangers can no longer see the post in their feeds.

One safety task now counts distinct accounts mentioned in the text together with accounts tagged in media, ignoring case. The threshold is still two accounts, but reaching it is only one condition for entering that task. Other eligibility checks and classification follow. The [task code](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/grox/flows/ptos/task_filter.py#L37-L100) does not establish an automatic ban for tagging two people.

## The second post, Articles and the first image

The author-counting code was checked again. It still takes candidates for a particular recommendation request, sorts the same author's posts by score, and starts counting from zero. With author diversity enabled and the public VM Ranker defaults, the first three multipliers are `1`, `0.625` and `0.4375`. A new afternoon post could rank first. Being your second post of the day does not automatically assign it the second multiplier. The [counting and scoring code](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/xai-value-model/scoring.rs#L265-L324) is unchanged.

It also gives no basis for a four-hour recovery period. The time gaps added to the training configuration describe relationships between reader requests and impression history. The [time-feature code](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/phoenix/xrex/models/recsys_feature_prep.py#L50-L80) concerns those events, not an interval creators must leave between posts.

No universal Article format bonus was added. The V8.2 path that selects the first available image or video is unchanged, as is its `4,000`-character text truncation boundary. That boundary belongs to a particular processing path. X has other content-processing paths, so neither "every model only sees the first image" nor a universal publishing-length limit follows from it. The [V8.2 source](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/grox/flows/mm_emb/renderer_v82.py) did not change in this comparison.

Another number worth keeping separate is the 24 hours in the safety-label cache. Cache settings govern how long cached data is stored or accepted; the labels have their own expiry rules. They cannot establish a 24-hour account penalty. The [cache settings](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/safety-label-source/dragonfly.rs#L25-L63) and [read-freshness checks](https://github.com/xai-org/x-algorithm/blob/3b6919f87532e57063bb3f1e85c2f509323b513e/safety-label-source/dragonfly.rs#L246-L251) can be inspected separately.

These older questions belong in an update because they still affect publishing decisions. Waiting to avoid a daily discount that the code does not impose, or turning a readable article into a video for an unverified bonus, can waste more work than any of these coefficient changes justify.

This article supplements the [original research](../provenance/research-report.zh-CN.md). Version 1.3.0 retains its 578 original knowledge entries and adds 14 dated updates and rechecks. Looking up an affected historical entry also returns the newer finding and its source. A weekly repository check lists new commits on the algorithm's main branch; the skills and documentation are updated after review. Existing installations must be updated to receive those changes. Use [ALGORITHM_CHANGELOG.md](../ALGORITHM_CHANGELOG.md) for algorithm findings and [CHANGELOG.md](../CHANGELOG.md) for package releases. External blog posts and earlier demonstrations retain their own writing and recording dates.
