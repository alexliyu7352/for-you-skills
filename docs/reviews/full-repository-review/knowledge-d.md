# Topic 05 semantic and evidence audit

Frozen repository: `9193233924df388727296c4e76948db919ac32eb`. Scope: all **109 claims**, `K05-001` through `K05-109`, in `knowledge/topic-05.json`. Every English field was read, including conditions, practical advice, checklists, limits, evidence descriptions, and unknown references. Every mapped `source_units` range was compared with the original Chinese in `provenance/research-report.zh-CN.md` (topic coverage: lines 1408–1638). No previous review verdict was used.

The four findings below include two English-field defects and two defects inherited from the Chinese report. Most of the topic correctly preserves distinctions between label creation and consumption, reader and entry-point predicates, configurable defaults and actual deployment, and editorial advice and algorithmic claims.

## Findings

### KD-01 — P2 / medium: lack of public evidence becomes proof of nonexistence

- **Claim/location:** `K05-061`, `knowledge/topic-05.json:2669` (`conclusion`); related wording at line 2687 (`limits`).
- **English:** “there is no sitewide formula deducting a fixed score above a fixed count.”
- **Original:** `U0475`, `provenance/research-report.zh-CN.md:1538`, says “没有公开一条所有人共用、超过几个 hashtag 就扣几分的公式” — no such common formula has been made public. It does not establish that none exists.
- **Primary evidence:** The pinned [Spam branch](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/task_write_safety_post_annotations_result_sink.py#L233-L248) and [policy enumeration](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/state.py#L37-L46) establish a classification and conditional write, without a numerical hashtag formula. The [prompt loader](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/prompts.py#L11-L31) and [repository disclosure](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/README.md#L428-L447) expressly leave prompts and some rules unpublished.
- **Effect:** A myth-check answer could replace an unsupported penalty formula with an equally unsupported assurance that no sitewide formula exists.
- **Correction:** Say “the cited public evidence provides no sitewide formula…” and change “absence of a formula” in the limit to “absence of a publicly established formula.” Retain the existing warning that abuse can still carry risk.
- **Classification:** Translation/English expansion defect; the Chinese distinction is sound.

### KD-02 — P3 / low: exact scheduled-job names lose their prefix

- **Claim/location:** `K05-047`, `knowledge/topic-05.json:2079` (`conclusion`).
- **English and original:** The English names `duplicate_text_unigrams` and `duplicate_text_characters_cjk`; `U0466`, `provenance/research-report.zh-CN.md:1516`, uses the same incomplete names.
- **Primary evidence:** [BBQDuplicateTextProd.bot lines 8–9](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/botmaker-rules/scarecrow/bot/BBQDuplicateTextProd.bot#L8-L9) compares `jobName` with `bbq_duplicate_text_unigrams` and `bbq_duplicate_text_characters_cjk`. The [reply consumer](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/botmaker-rules/scarecrow/bot/BBQDuplicateTextRepliesProd.bot#L8-L9) similarly uses `bbq_duplicate_text_unigrams_replies` and `bbq_duplicate_text_characters_replies_cjk`.
- **Effect:** The main conclusion about CJK processing remains correct, but a reader following an exact job name cannot reproduce the named equality test or reliably match a job record.
- **Correction:** Restore `bbq_` in both names, or explicitly describe the shorter strings as suffixes rather than exact names. Treat the original report as needing an erratum; do not call the English a mistranslation.
- **Classification:** Original-report code-identifier error faithfully inherited by the English.

### KD-03 — P3 / low: the verification instruction compares the threshold instead of the count

- **Claim/location:** `K05-034`, `knowledge/topic-05.json:1496` (`check.verify[1]`).
- **English:** `Verify minimumMatchingPosts>=3, not a ratio threshold`.
- **Original:** `U0456`, `provenance/research-report.zh-CN.md:1488`, correctly says to check whether the number of matching records is at least three after `take(5)`.
- **Primary evidence:** [postToUserLabelRules.strato lines 269–283](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/safety-label-user-agg/postToUserLabelRules.strato#L269-L283) filters the selected window and compares its `.size` with `condition.minimumMatchingPosts`. [The public default](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/safety-label-user-agg/postToUserLabelRules.strato#L395-L425) sets that threshold to three.
- **Effect:** The checklist's written expression checks a configuration value, which is true for the default even when there are zero matching records. The claim's conclusion and practical advice otherwise state the correct rule.
- **Correction:** Use “Verify matching-record count >= minimumMatchingPosts, whose public default is 3; this is not a ratio threshold.”
- **Classification:** English checklist expansion defect.

### KD-04 — P2 / medium: post-label statistics are described as calendar-period label incidence

- **Claim/location:** `K05-069`, `knowledge/topic-05.json:3040` (`conclusion`); its inputs at lines 3049–3051 should also preserve cohort and denominator definitions.
- **English and original:** The English says how many posts “carried that label during the period.” `U0483`, `provenance/research-report.zh-CN.md:1562`, likewise says “期间内有多少篇帖子带有该标签，以及相应比例.” The cited UI strings establish the units but do not establish this temporal definition.
- **Primary evidence, beyond the cited UI:**
  - [UthDailyPostsJob.scala lines 215–250](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthDailyPostsJob.scala#L215-L250) selects eligible logical posts by creation time, excluding reposts and nullcast posts, and deduplicates logical IDs for the denominator.
  - [Lines 311–322 and 360–393](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthDailyPostsJob.scala#L311-L393) constrain ordinary label events to the post's observation horizon and count `everApply`; removal is recorded separately. A post need not still carry the label at reporting time.
  - [Lines 421–422](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthDailyPostsJob.scala#L421-L422) give `postObservationDays` a configurable default of seven.
  - [UthUserMonthMhPublisherJob.scala lines 237–245](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthUserMonthMhPublisherJob.scala#L237-L245) assigns the row to a month using `authoredYyyymmdd`, not the label-event month.
  - [underTheHoodReport.User.strato lines 320–355](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/strato/columns/underTheHoodReport.User.strato#L320-L355) uses the eligible-post count as the denominator and sums `carried` for the numerator.
- **Effect:** With the default event-based path, an October 31 post labeled on November 2 can contribute to October's post statistics. Conversely, label activity on an older post during October is not automatically part of that month's authored-post cohort or the post's observation horizon. Treating the report as all calendar-month label activity can misalign troubleshooting dates and overstate coverage. The account-label day metric is a different calculation and remains correctly distinguished in `K05-070`.
- **Correction:** Define Post labels as labeled eligible posts in the reported authored-post cohort, with the generating path's observation rules. Explain that the ordinary safety-label path observes a configurable period after creation, seven days by default, and can include labels later removed. Do not impose that horizon on special flag/takedown paths without checking their logic. Preserve the existing warning that a post proportion is not an exposure-loss proportion. Clarify broad period shorthand in nearby tool descriptions when reused for troubleshooting.
- **Classification:** Original-report temporal/denominator omission faithfully inherited by the English; the cited presentation layer is insufficient to validate the stronger definition.

## Evidence checks and limits

- All 76 distinct referenced URLs were attempted or their exact pinned file and cited ranges were inspected. They resolve to 48 baseline source files, three comparison files, and two web endpoints; multiple ranges share files. The 48 baseline cached files independently matched blob SHAs from a fresh, non-truncated GitHub tree for `5ed796374ea48ee26058aab66ab10c266bea2bef`. The three comparison files matched fresh `fetch_file` blob SHAs for `606b254b45be798bfaecfa8c23f5a9c51bc8000c`.
- Fresh commit metadata dates `606b254` to October 29, 2026. Expanding reusable rule lists independently preserved Home's 7 author and 32 post rules, HomeRecommendations' 20 author and 46 post rules, HomeHydration's six author rules, and its 76 own post rules, in order. Old and new FOSNR defaults and expressions were read separately. This verifies the scoped structural comparison in `K05-002`/`K05-012`, not all production behavior.
- Reader predicates, Home Mixer routing, attached-content routing, normal and fallback FOSNR paths, public-interest dates and source selection, NonCompliant fallback, final treatment assembly, and feature-switch policy resolution were inspected together. Tests were treated as local expectations, not production observations.
- Aggregation configuration, triggering event, account exclusions, timeline order, repost-original label lookup, timeline-ID age basis, take-before-match counting, write-time TTL, existing-label exclusion, forwarding delay, and the separate HLL path were all read. The ten-record/eleven-match default is unreachable on its stated settings. No exposure guarantees or fixed production values were inferred.
- For `K05-052`, a fresh full-file text search covered all **425** baseline blobs under `home-mixer/` (267), `vm-ranker/` (16), and `visibility-filtering/` (142). Every fetched SHA matched the fresh pinned tree; there were no retrieval failures. Case-insensitive `copypasta` searching with underscores removed found no direct mention. This independently supports only the bounded negative result; it does not establish the absence of indirect or unpublished consumers. GitHub indexed searches were also checked but were not substituted for the pinned search because their results referenced a later revision.
- Under the Hood's report builder, eligibility gate, best-effort notice, date fallback, UI units, label explanations, and the additional upstream jobs noted in KD-04 were inspected. The signed-in product endpoint `https://x.com/i/jf/under_the_hood` returned **403** through web retrieval; live account availability remains **unverified**, and `K05-066` is marked accordingly despite its independently verified pinned-code description. No signed-in session was probed.
- [The official view-count help page](https://help.x.com/en/using-x/view-counts), fetched November 1, 2026, explicitly permits multiple views by the same viewer and counts views across several surfaces. This supports the non-deduplicated-view distinctions in `K05-065` and `K05-080`.
- Editorial examples and recommendations were checked for fidelity, internal consistency, and inappropriate conversion into algorithmic guarantees. Claims with no external factual assertion and no cited evidence use `not_applicable` for evidence status. No empirical posting experiment or production-account diagnostic was performed or implied.

The companion `coverage/knowledge-d.json` contains one explicit row per claim, source URLs checked, per-claim notes, separate translation/evidence status, and finding IDs. All 109 entries were examined; no sampling was used. Production content was not edited.
