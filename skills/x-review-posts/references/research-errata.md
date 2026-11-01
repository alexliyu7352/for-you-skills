# Research corrections and historical limits

Correction date: **2026-10-31**. These corrections apply to the working English knowledge. The original Chinese report, its source-unit hashes, source registry, migration mappings, and frozen review remain preserved as historical records. The primary baseline is `xai-org/x-algorithm@5ed796374ea48ee26058aab66ab10c266bea2bef`; the comparison revision is `606b254b45be798bfaecfa8c23f5a9c51bc8000c`.

The full review identified **12 knowledge findings affecting 13 claims**: six findings were inherited from the original report, and six were introduced during English distillation. KD-04 also requires consistent wording in the two nearby tool descriptions K04-091 and K05-066. Each corrected claim retains its original evidence references and adds `correction` metadata with the finding ID, origin, date, summary, and primary-source links. Use those links with the corrected conditions when answering; the archived wording returned by `original U...` may still contain the documented error.

These are source-scoped corrections. They do not establish current deployment, live account eligibility, or causal exposure effects. See the [knowledge guide](knowledge-guide.md) for lookup and application instructions.

## Six findings inherited from the original report

### KA-001 — K01-017: commit time is not first public availability

Original units U0014–U0017 identify precise commit times as public-release times. The baseline commit's author and committer timestamps are `2026-10-28T02:49:03Z`; the comparison commit's are `2026-10-29T02:57:55Z`. The UTC/PDT conversions remain correct. These fields record commit metadata, not the moment a commit first became public or an experiment reached production traffic. The working claim now separates commit time, public availability, announcements, and deployment.

Evidence: [baseline commit](https://github.com/xai-org/x-algorithm/commit/5ed796374ea48ee26058aab66ab10c266bea2bef), [comparison commit](https://github.com/xai-org/x-algorithm/commit/606b254b45be798bfaecfa8c23f5a9c51bc8000c), and [GitHub's distinction between making local commits and pushing them to a remote](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository).

### KB-F01 — K04-049: no universal original-post retrieval prerequisite is shown

U0386 says original-post data must be retrievable. The cited ancillary path instead drops a repost candidate when the original has a successfully returned dropping visibility action. A missing or errored original lookup does not itself satisfy that branch. Core-data hydration can use the candidate's own core text when source-post text is unavailable, and its filter checks the candidate's author ID. The working claim asks for actual retrieval and visibility outcomes without inventing a mandatory original-data gate. Other filters or returned dropping actions can still prevent display.

Evidence: [ancillary visibility decision](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/candidate_hydrators/vf_candidate_hydrator.rs#L140-L169), [source-text fallback](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/candidate_hydrators/core_data_candidate_hydrator.rs#L103-L124), [core-data filter](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/filters/core_data_hydration_filter.rs#L6-L15), and [ancillary-drop filter](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/filters/ancillary_vf_filter.rs#L7-L17).

### KB-F02 — K04-046 and K04-047: unavailable age also fails AgeFilter

U0380 and U0384 say only older candidates are removed. The predicate maps a decoded age through `age <= max_age` and otherwise returns false. Exactly 48 hours therefore passes only when the age is successfully decoded; an older or unavailable age fails. The helper's implementation is outside this repository, so the correction does not invent which particular IDs produce an unavailable age. The candidate-ID basis and the warning against treating 48 hours as a platform-wide lifetime remain intact.

Evidence: [complete age predicate and candidate-ID use](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/filters/age_filter.rs#L16-L31) and [48-hour constant](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/params/config.rs#L38-L43).

### C-03 — K03-077: VQV eligibility also depends on the querying viewer

U0291 describes the duration condition but omits the viewer guard. `vqv_eligible` requires present video duration strictly above the configured minimum, whose public default is 10000 milliseconds, and rejects a querying viewer with a known follower count of at least 10000. A missing viewer count does not trigger that exclusion. This is the viewer's count, not the video author's. Eligibility remains separate from the weight: the cited Home Mixer `VqvWeight` default is 0.0, and no exposure guarantee follows.

Evidence: [viewer guard, duration condition, and weight application](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/util/candidates_util.rs#L4-L57), [duration default](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/params/param.rs#L688-L693), and [separate zero-weight default](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/params/param.rs#L431).

### KD-02 — K05-047: exact scheduled-job names include `bbq_`

U0466 omits the prefix from the general duplicate-text bot's accepted job names. The exact names are `bbq_duplicate_text_unigrams` and `bbq_duplicate_text_characters_cjk`. The reply consumer uses `bbq_duplicate_text_unigrams_replies` and `bbq_duplicate_text_characters_replies_cjk`. The conclusion that CJK text is within these consumers' scope is unchanged; receiving a cluster does not disclose the unpublished cluster-generation thresholds.

Evidence: [general job-name equality checks](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/botmaker-rules/scarecrow/bot/BBQDuplicateTextProd.bot#L8-L11) and [reply job-name equality checks](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/botmaker-rules/scarecrow/bot/BBQDuplicateTextRepliesProd.bot#L8-L11).

### KD-04 — K05-069, with K04-091 and K05-066: post-label counts follow authored-post cohorts

U0483's description of posts carrying a label “during the period” is insufficient to define the temporal scope. The denominator counts eligible logical posts authored in the reported cohort, excluding reposts and nullcast posts and deduplicating logical IDs. For ordinary safety-label events, the generating job observes a configurable period after creation, seven days by default, bounded by the batch cutoff. It counts whether a label was ever applied within that horizon and records removal separately. The monthly publisher uses `authoredYyyymmdd`, so an October 31 post labeled on November 2 can contribute to October's cohort under that default event path.

The corrected claim and the two nearby tool descriptions distinguish this cohort from account-label day counts and from a calendar-month log of all label events. Snapshot gap filling, post flags, and takedowns have separate logic; the ordinary event horizon must not be imposed on those paths without checking. A post-label proportion is not an exposure-loss rate. Live or account-specific Under the Hood availability remains unverified; the full review's unauthenticated endpoint request returned 403.

Evidence: [eligible cohort and denominator](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthDailyPostsJob.scala#L215-L250), [event horizon](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthDailyPostsJob.scala#L311-L322), [ever-applied count and separate removal](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthDailyPostsJob.scala#L360-L393), [seven-day default](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthDailyPostsJob.scala#L421-L422), [authored-month assignment](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/scalding/UthUserMonthMhPublisherJob.scala#L237-L245), and [report numerator, denominator, and separate account-day calculation](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/under-the-hood/strato/columns/underTheHoodReport.User.strato#L320-L355).

## Six English-distillation fixes

### KB-F03 — K04-077: preserve zero-score publication scope

U0402 describes the multi-step writer publishing `score=0.0`; the English title, conclusion, and conditions generalized this to all accepted scores. The working claim now specifies zero scores and explains that the publisher writes caches only when a score is present and `<=1.0`. Kafka and Strato operations follow separately. A score above 1.0 is not expected to take the cache branch. Publication code does not establish that every destination successfully received a record.

Evidence: [multi-step writer and zero score](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/reply_spam/task_multi_step_reply_spam.py#L151-L198) and [cache gate plus Kafka/Strato operations](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/reply_spam/strato_loader.py#L20-L53).

### KB-F04 — K02-089: the V8.2 bio cap is specified

U0221 correctly mentions a bio character cap. The English limit incorrectly added that no number was available. The renderer defines `MAX_BIO=500`, strips outer whitespace, slices the Python string, and removes trailing whitespace before adding the bio to text input. This is the renderer's input cap; it is not evidence of the profile editor's limit, a keyword bonus, or use by every production representation.

Evidence: [constant and truncation helper](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer_v82.py#L33-L50) and [bio call](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/mm_emb/renderer_v82.py#L213-L215).

### C-01 — K03-018: content-feature transmission is conditional

U0244 says length and newline information can be transmitted; the English conclusion asserted transmission without the enabling condition. Candidate content features are populated only inside the debias branch, enabled when `query.has_cached_posts` is false and `VMRankerSendDebiasInputs` is true. A pacing-only candidate experiment payload can omit them. These inputs do not establish a fixed positive reward or optimal character count.

Evidence: [conditional candidate features](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/scorers/vm_ranker_debias_payload.rs#L33-L48), [cache and feature-switch prerequisites](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/scorers/vm_ranker_request.rs#L17-L23), and [pacing-or-debias payload envelope](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/home-mixer/scorers/vm_ranker_request.rs#L70-L72).

### C-02 — K03-101: MediaInjected does not require an existing prior result

U0319 excludes already-NSFW results without requiring a prior result to exist. The English expansion added that prerequisite. The MediaInjected filter skips when its prior-NSFW helper returns true; that helper returns false for absent results and lookup errors. Author, video, and configured fav prerequisites remain. LeadingFrames is a different task with an explicit missing-prior-result rejection; its condition must not be transferred to MediaInjected.

Evidence: [MediaInjected filter](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/task_safety_ptos_media_injected_adult_infrared_video_spam_detection_filter.py#L32-L47), [prior helper](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/prior_nsfw.py#L16-L34), and [distinct LeadingFrames prerequisite](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/task_safety_ptos_adult_content_leading_frames_filter.py#L53-L57).

### KD-01 — K05-061: missing public evidence does not prove nonexistence

U0475 says no common numeric hashtag formula has been made public. The English conclusion instead asserted that no sitewide formula exists. The working claim now says the cited public evidence provides no such formula. The public abuse category and conditional label write establish neither zero value for every hashtag nor an undisclosed system's absence; the repository expressly omits prompts and some rules.

Evidence: [hashtag-abuse category](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/state.py#L37-L46), [conditional Spam write](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/task_write_safety_post_annotations_result_sink.py#L233-L248), [unpublished prompt notice](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/grox/flows/ptos/prompts.py#L11-L31), and [repository disclosure](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/README.md#L428-L447).

### KD-03 — K05-034: compare the matching count with the threshold

U0456 correctly describes taking at most five records and checking for at least three matches under the public defaults. The English checklist accidentally compared the configuration value `minimumMatchingPosts` with three. The corrected check compares the matching-record count with `minimumMatchingPosts`, whose default is three. It remains a count threshold after selecting the window, not a percentage threshold or a requirement to wait for five records.

Evidence: [selected-window matching count](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/safety-label-user-agg/postToUserLabelRules.strato#L266-L283) and [five-record/three-match defaults](https://github.com/xai-org/x-algorithm/blob/5ed796374ea48ee26058aab66ab10c266bea2bef/safety-label-user-agg/postToUserLabelRules.strato#L395-L425).

## Historical provenance not independently reconstructed

These two limits are separate from the 12 factual findings above. They do not assert that the original report's historical statements are false.

- **K00-002 / U0660:** The pinned snapshots and date conversions are supported. The original report describes a shared conversation, a 23-page research report, and the “latest version 7” manuscript, but the exact assembly lineage was not independently reconstructed from the retained records. Attribute that lineage to the original report unless the specific conversation/version record is recovered.
- **K00-003 / U0661:** The exact named 14 visibility rule/field groups and the earlier comparison result were not independently reconstructed. The separate 14-file renderer comparison is not evidence for this count. Preserve the original attribution and request the historical named groups/results before claiming that exact comparison has been reproduced.

The working entries make those limits explicit while preserving their source-unit mappings. Historical verification records and source checks also remain distinct from tests run in the present task and from production exposure experiments.
