# Topic 03: independent semantic and evidence audit

Reviewed all **113/113 claims** in `knowledge/topic-03.json` at repository commit `9193233924df388727296c4e76948db919ac32eb`. This was a complete read of every English title, conclusion, condition, practical implication, check, limitation, and evidence description, compared with each mapped `source_units` passage in `provenance/research-report.zh-CN.md`. Related unknown identifiers were also checked against their titles and conclusions.

**Result: two P2 wording/logic findings and one P3 condition-completeness finding.** No claim was skipped. The per-claim record is [coverage/knowledge-c.json](coverage/knowledge-c.json).

| Review dimension | Verified | Finding | Not applicable | Unverified |
| --- | ---: | ---: | ---: | ---: |
| Translation | 111 | 2 | 0 | 0 |
| Evidence | 85 | 3 | 25 | 0 |

`verified` means that the cited source supports the claim at its stated scope; it does not certify undisclosed production behavior or independently validate unpublished study data. `not_applicable` identifies explicitly editorial/methodological reasoning or a report-scoped research gap with no positive external factual claim to validate. It is not a passed source check. All eight external source pages used by this topic were accessible during this review, so no source-access failure is hidden in a passed row.

## Findings

### C-01 — P2: feature transmission loses its explicit enabling condition

**Claim and location:** `K03-018`, `knowledge/topic-03.json:721`, with the missing condition at line 723 and the evidence description at line 753.

The conclusion says the program constructs `weighted_text_len` and `newline_count` and “passes them into the relevant requests.” Chinese unit `U0244`, report line 842, says the information **can** be transmitted. The English conclusion is stronger, and its conditions do not identify the gate.

The pinned source populates candidate `content_features` only inside `if debias`. `RequestShape::from_query` sets that flag to `!query.has_cached_posts && query.params.get(VMRankerSendDebiasInputs)`. A request may contain an experiment payload for pacing while omitting these content features.

- Source: [candidate payload, lines 33–48](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/scorers/vm_ranker_debias_payload.rs#L33-L48).
- Additional condition: [request shape, lines 17–23](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/scorers/vm_ranker_request.rs#L17-L23).
- Pacing-or-debias envelope: [candidate request, lines 70–72](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/scorers/vm_ranker_request.rs#L70-L72).

**Reader-facing effect:** the record can be reused as unconditional proof that length and newline features reach a VM request, including a cached or pacing-only request. Its otherwise correct warning against a fixed length reward does not restore the missing transmission condition.

**Correction:** say the program **can include** these features in the candidate experiment payload when the debias input branch is enabled. Add the cache and feature-switch prerequisites to `conditions`, and retain the existing no-fixed-reward limitation.

### C-02 — P2: MediaInjected is given a prior-result prerequisite that its code does not have

**Claim and location:** `K03-101`, `knowledge/topic-03.json:4202`; related “Prior NSFW results” and missing-state wording occur at lines 4216 and 4222.

The English conclusion says the task requires an author, a video, sufficient favs, **and existing results** that have not classified the content as NSFW. Chinese `U0319`, report line 1059, excludes an already-NSFW result without saying a prior result must exist.

The filter skips only when `post_is_already_flagged_nsfw` is true. Its helper returns false when the result is absent and also when lookup raises an exception. That is materially different from LeadingFrames, whose filter explicitly skips on `prior is None`.

- Filter: [MediaInjected filter, lines 32–47](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/task_safety_ptos_media_injected_adult_infrared_video_spam_detection_filter.py#L32-L47).
- Missing-result and error behavior: [prior NSFW helper, lines 23–34](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/prior_nsfw.py#L23-L34).
- Actual prior-result prerequisite in the other task: [LeadingFrames filter, lines 53–57](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/task_safety_ptos_adult_content_leading_frames_filter.py#L53-L57).

The pinned helper was independently invoked with a mocked lookup: absent result, lookup exception, and an explicit non-NSFW result all returned false; an explicit NSFW result returned true. This reproduces the source behavior without contacting a production service.

**Reader-facing effect:** this wording makes MediaInjected look like LeadingFrames and can produce an incorrect explanation that missing prior results block a video that otherwise meets MediaInjected's conditions.

**Correction:** say the task skips only when the lookup positively reports existing NSFW status. State that this public helper treats absent results and lookup errors as not already flagged. Do not require prior results to exist.

### C-03 — P3: the VQV description omits the querying viewer's follower-count condition

**Claim and location:** `K03-077`, `knowledge/topic-03.json:3094`; the sole condition at line 3096 and evidence description at line 3125 also describe only the duration part.

The `>10000` millisecond duration comparison is correct. However, the conclusion says VQV eligibility “first checks” video length. The named function first computes whether the **querying viewer** has at least 10,000 followers, then returns the conjunction of the negated follower condition and a present `candidate.min_video_duration_ms` above the configured threshold. A missing viewer follower count does not trigger the follower exclusion. This omitted prerequisite is already absent from Chinese `U0291`, report line 972, so it is an original-report completeness issue rather than translation loss.

- Source: [VQV eligibility and follower constant, lines 1–33](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/util/candidates_util.rs#L1-L33).
- Duration default: [MinVideoDurationMs, lines 688–693](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/params/param.rs#L688-L693).

**Reader-facing effect:** a reader can mistake the duration branch for the operative eligibility check for every viewer. The existing limitation correctly denies guaranteed points/exposure, but does not identify this second eligibility condition.

**Correction:** call the duration comparison **one prerequisite** and add the viewer follower-count guard. Distinguish the viewer from the video author. Keep the separate zero-weight and no-exposure-guarantee qualifications.

## Independent source work and checks

The topic cites **112 distinct URLs**, consisting of 104 pinned code anchors across **61 source files** and eight external pages. Every cited code file was read from the freshly retrieved `5ed796374ea48ee26058aab66ab10c266bea2bef` cache; all 61 files were checked against the corresponding Git tree blob SHA. An extra trailing newline in the initial cache serialization was identified and reported to the root reviewer; after correction, all 61 matched exactly. Cache provenance is in the root review evidence manifest, not an earlier review conclusion.

For the bounded absence claims, this audit additionally fetched and searched all **77** pinned Home Mixer Rust files under `sources`, `filters`, `scorers`, `params`, and `candidate_pipeline`. The only Article-name hit was an `article_id: None` initializer. It also fetched and searched all **29** pinned `.strato` files: `getTweetypieResponse` occurred only at its definition and export; no `32fav_video` producer was found there. These are bounded negative results, not evidence about omitted services or production experiments.

The V5 and V8.2 functions were independently fetched, then invoked locally with controlled populated objects using their actual function bodies and inert type substitutes. These checks reproduced all reported cases: 4000 body characters with the trailing character omitted; no text-output change for the controlled tail-only edit; coexistence of body text with a 200-character Article title; V5 cover/attachment/embedded-image order; cover-only output at the one-image budget; V8.2 ordinary-attachment selection; empty V8.2 image output when images are confined to Article metadata; and V5 retention of the 4001-character test body. This verifies local reading behavior, not embedding quality or exposure.

The source-level checks also covered action IDs, page IDs, binary click-dwell threshold and units, final score fields, author counting, Article lifecycle registration, subscription filters, media authorization, strict video-index duration comparisons, all-media validation, enum/file mappings, general versus specialized video builders, and the distinct 64/512/30-second/10-second/60-second safety conditions. Each claim has its own result and limitations in the coverage file.

Freshly read external sources:

- [Official Post types](https://help.x.com/en/using-x/types-of-posts) and [Premium how-to](https://help.x.com/en/using-x/x-premium-how-to): product limit and reply/quote capability.
- [Official Articles help](https://help.x.com/en/using-x/articles): structure, publication/editing lifecycle, and excerpt distribution.
- [Official view counts](https://help.x.com/en/using-x/view-counts): repeat/self views and multiple entry points, without completed-reader meaning.
- [Historical creator announcement](https://blog.x.com/en/business/creator-updates-and-article-contest-replacement) and [Original Content Rewards](https://help.x.com/en/using-x/original-content-rewards): payout weighting and the former program's September 2026 end.
- [NotPeople's observational study](https://notpeople.ai/blog/how-to-make-money-on-x-2026): its stated 42/843/64 table, normalized 5.7× median, August data, September publication, and 6–28 satellite Posts. No row-level reanalysis was possible from the cited page.
- [Hootsuite's experiment](https://blog.hootsuite.com/experiment-x-threads-vs-longform-posts/): three threads followed by three long Posts after changing subscription status, with no native Article arm.

No implementation or knowledge files were changed by this audit. Only this review and its coverage file were written.
