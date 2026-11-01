# Independent review: knowledge topics 02 and 04

Reviewed repository commit: `9193233924df388727296c4e76948db919ac32eb`.

All **199 assigned claims** were read in full: 97 in `knowledge/topic-02.json` and 102 in `knowledge/topic-04.json`. The review compared title, kind, conclusion, conditions, practical meaning, every check field, limits, evidence descriptions and related-unknown references with the mapped Chinese source units. It then independently inspected the cited primary code and relevant caller/filter context. This was not a sample or a link-presence audit.

There are **four findings affecting five claims**: one P2 and three P3. Two findings are wording introduced during distillation; two reproduce an overstatement already in the original report. The principal retrieval, CREAD, indexing, cold-start, FairShare and score-scope explanations hold up under the examined public source. They generally keep model inputs, predictions, intermediate candidate selection and production exposure separate.

The complete per-claim record is [coverage/knowledge-b.json](coverage/knowledge-b.json). Translation statuses: 197 verified, 2 finding. Evidence statuses: 165 verified, 5 finding, 28 not applicable, 1 unverified.

## Method and evidence limits

The primary baseline is `xai-org/x-algorithm@5ed796374ea48ee26058aab66ab10c266bea2bef`; the explicit comparison is `606b254b45be798bfaecfa8c23f5a9c51bc8000c`. Historical assertions were checked against their own cited revisions, including October 8, 9, 13, 21 and 22, and against retrieved commit metadata/patches where dates or additions mattered. I used the newly retrieved exact-ref files in `/workspace/scratch/8875c799c753/work/full-review-evidence`, whose manifest records source URL, local path, SHA-256 and Git blob identity. I inspected source contents independently rather than accepting prior review conclusions.

For `K02-035`, I also inspected the existing original-function CPU result and runner in `work/verification/phoenix_loss_results.json` and `phoenix_cpu_validation.py`. The result's three source hashes match the freshly fetched pinned files. Its numerical boundary agrees with the actual loss code. The legacy artifact calls the inputs seconds; this claim correctly avoids treating that wording as proof of upstream click-event units. For `K04-009`, I inspected the reimplementation result and source manifest in `work/verification/ranking_validation`; the cold-start and parameter hashes match the fresh files, and the 199/200 result agrees with the source predicate. Neither record was treated as production validation, and this review did not rerun those historical experiments.

In the coverage file, `verified` for an `unknown` claim means that its **bounded statement of the evidence gap and its caution are supported**; it does not mean that rollout, causal reach or a missing adapter has been resolved. Editorial recommendations without a factual external premise have evidence status `not_applicable`. Editorial examples with source-dependent mechanics or arithmetic were checked and can have status `verified`. Source URLs include inspected targets and, for the one inaccessible live URL, the attempted target with the failure explained in the row.

I opened the official view-count documentation and checked its distinction from Home-only impressions. The live `https://x.com/i/jf/under_the_hood` entry returned **403**. Accordingly `K04-091` is marked `unverified` for live/account-specific availability, while its report-period, fields, label descriptions and conditional advice are supported by the pinned README and report code. No authenticated account report was available or inferred.

## KB-F01 — P2: a universal original-post retrieval requirement is not established

**Claim:** `K04-049`, `knowledge/topic-04.json:2222` (title) and `:2224` (conclusion).

**English:** The original post's data “must still be retrievable” even when a recent repost passes its own age check. The sole selected evidence is `S039[9]`, ancillary visibility handling.

**Original report:** `U0386`, `provenance/research-report.zh-CN.md:1282`, also says “原文资料要能取得”. This is an **inherited source-report overstatement**, not a translation reversal.

**Primary evidence:** [vf_candidate_hydrator.rs lines 140–169](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/candidate_hydrators/vf_candidate_hydrator.rs#L140-L169) sets ancillary drop only when a returned `Some(Ok(visibility))` has a dropping action. A missing or errored lookup does not satisfy that branch; the function returns false if no applicable returned action drops. [Core-data hydration lines 103–124](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/candidate_hydrators/core_data_candidate_hydrator.rs#L103-L124) also explicitly falls back to the candidate's core text when source-post data is missing or errored. The independently fetched [CoreDataHydrationFilter](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/filters/core_data_hydration_filter.rs#L6-L15) checks `author_id != 0`, not original-data availability. [AncillaryVFFilter](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/filters/ancillary_vf_filter.rs#L7-L17) removes the drop flag rather than imposing a separate mandatory successful lookup.

**Effect:** A diagnostic answer could wrongly declare an original-data fetch failure to be a necessary reason a repost was excluded. The visible path distinguishes an explicit returned visibility action from missing/error lookup results. These checks do not prove a candidate will eventually display; other filters and returned `NotEvaluated`/drop actions can still remove it.

**Correction:** Say that returned visibility actions for a reposted original can remove the candidate, and inspect actual retrieval/visibility outcomes. Remove the blanket “must be retrievable” prerequisite unless an additional mandatory gate is cited. Preserve the useful statement that passing the age check is insufficient for display.

## KB-F02 — P3: the age predicate also rejects an unavailable age

**Claims:** `K04-046`, `knowledge/topic-04.json:2067`; `K04-047`, `knowledge/topic-04.json:2126`.

**English:** Both say that only older candidates are removed. The own-ID basis, forty-eight-hour maximum and inclusive comparison are correct.

**Original report:** `U0380`, `provenance/research-report.zh-CN.md:1262`, says “超过才排除”; `U0384`, `:1278`, says “超过才移除”. This is an **inherited omission**. The narrower “assessing only this age-comparison expression” condition in `K04-047` reduces the practical risk but does not remove the absolute wording in its conclusion.

**Primary evidence:** [age_filter.rs lines 16–19](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/filters/age_filter.rs#L16-L19) evaluates `duration_since_creation_opt(tweet_id).map(|age| age <= self.max_age).unwrap_or(false)`. Thus `None` also fails the predicate. The public helper implementation is outside this repository, so this review does not invent which particular IDs yield `None`.

**Effect:** An eligibility explanation could mistakenly treat an unavailable age as necessarily passing because it was not shown to exceed forty-eight hours. The central inclusive-boundary explanation remains valid for a successfully decoded age.

**Correction:** “For a successfully decoded age, exactly forty-eight hours passes; an older age or an unavailable age fails this filter.” Retain the existing warning against treating this as a platform-wide lifetime or a second-level publishing tactic.

## KB-F03 — P3: preserve the zero-score scope of the cache-publication claim

**Claim:** `K04-077`, `knowledge/topic-04.json:3435` (title) and `:3437` (conclusion).

**English:** “Accepted reply scores are published to the corresponding cache, Kafka, and Strato records.” Its only condition is execution of score publication.

**Original report:** `U0402`, `provenance/research-report.zh-CN.md:1330`, describes the multi-step writer publishing **`score=0.0`**, then says these scores are written to cache, Kafka and Strato. The English conclusion drops that restriction. Its `check.when` does mention a zero reply score, which partly preserves the original context; the standalone title/conclusion/conditions are broader. This is **distillation scope drift**, not a defect in the original zero-score statement.

**Primary evidence:** [strato_loader.py lines 20–53](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/reply_spam/strato_loader.py#L20-L53) defines `_CACHE_FANOUT_SCORE_MAX = 1.0` and calls the two cache puts only when the score is present and `<= 1.0`. The Kafka/Strato operations follow separately. A published score greater than one is a concrete counterexample to the broad cache statement; zero satisfies the cache condition.

**Effect:** A diagnostic using the broad conclusion could mistake an intentionally absent cache entry for a failed publication, despite the score being outside the cache-fanout range.

**Correction:** Make title, conclusion and conditions explicitly about **the zero scores produced by this multi-step writer**. Alternatively, describe the general publisher and state its cache condition. Keep the existing distinction between sending and successful receipt.

## KB-F04 — P3: the cited renderer does supply a numeric bio truncation limit

**Claim:** `K02-089`, `knowledge/topic-02.json:4003` (`limits`).

**English:** “This scope provides no numeric character limit; do not invent one.” The main conclusion that this renderer reads the bio is correct.

**Original report:** `U0221`, `provenance/research-report.zh-CN.md:756`, says only that the bio is subject to a character cap before entering the text input. It does **not** say the numeric cap is unavailable. The added limitation is **distillation wording**. If “this scope” was intended only to mean that this knowledge record omits the number, it should say so; it currently reads as an evidence limitation.

**Primary evidence:** The claim itself selects `S044[1]`: [renderer_v82.py lines 33–50](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer_v82.py#L33-L50), which defines `MAX_BIO = 500` and the slice-based `_truncate`. [Lines 213–215](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer_v82.py#L213-L215) call `_truncate(user.bio or "", MAX_BIO)`.

**Effect:** A user asking about this renderer's actual input cap could be incorrectly told that the numeric value is unavailable, although the selected evidence directly supplies it. This is a renderer input cap, not evidence of the user-facing bio editor's limit or a keyword bonus.

**Correction:** Remove the unsupported no-number assertion, or state “This V8.2 renderer sets `MAX_BIO=500`; that does not establish the profile editor's limit, a ranking benefit or coverage across all production representations.”

## Checks that did not produce findings

The complete coverage rows record each claim's reasoning. Particular checks included:

- Reader history versus author behavior; author/post representations; `ld` training/inference and historical additions; named head weights versus production coverage.
- Binary click-dwell `>10`, untraced upstream units/adapter, CREAD logarithmic thresholds, strict labels, interval reconstruction, clipping, Huber settings, masks and training-versus-fusion weights.
- Favorite-event first/cached paths, all five cached gates, threshold advancement, race handling, separate reply/creation/video routes, named storage windows and the lack of a traced ordinary `32fav_1day` serving consumer in the cited chain.
- Cold-start cohort, missing counts, exact age/follower/impression boundaries, nonzero-position cutoff, Beta posterior inputs, top-k then score selection, small-pool behavior, one-post `max` lift, later multipliers and final blending.
- FairShare served-type grouping, fallback and tie order, largest-remainder allocation, original within-group order, request cap, activation conditions and the candidate-slot-only forty-percent example.
- Bookmark seed/training versus fusion, mutual-follow eligibility and coefficient arithmetic, distinct DM/copy predictions, local-versus-VM defaults and relationship filtering.
- Seen versus served, direct-parent/original IDs, repost age identity, source-specific age handling, stale-edit rules, multi-step reply filtering/classification/publication, ancillary visibility actions, URL bot conditions, account versus post labels and pinned-label expiration.

One additional wording sensitivity was considered but not counted as a defect: `K04-017`'s “invalid prior” should be read as the explicit `top_k==0`, `alpha0<=0` or `beta0<=0` guard. The function separately substitutes a neutral `0.5` sample for a per-candidate Beta-construction failure. The complete claim's condition restricts its statement to parameters that trigger the fallback, so I did not elevate the broad title alone into another finding.

No production knowledge, source-unit, provenance, skill or routing files were edited by this review. Only this report and its assigned coverage JSON were written.
