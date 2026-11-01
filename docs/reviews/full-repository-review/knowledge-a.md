# Independent knowledge audit: topics 00, 01, and 06

Reviewed all **157 entries** at frozen repository commit `9193233924df388727296c4e76948db919ac32eb`: 11 in topic 00, 97 in topic 01, and 49 in topic 06. Every assigned English entry was read in full, including conclusion, conditions, practical meaning, checks, and limits, and compared with every referenced Chinese source unit. This was not a sample or a citation-count audit.

There is **one factual finding inherited from the original Chinese report**, **no substantive translation drift found**, and **two unresolved historical-provenance checks**. The production knowledge and original evidence were not edited.

| Coverage status | Entries |
| --- | ---: |
| Translation verified | 157 |
| Evidence verified within stated scope | 139 |
| Evidence finding | 1 |
| Historical evidence not fully verified | 2 |
| Editorial advice; empirical verification not applicable | 15 |

The [coverage ledger](coverage/knowledge-a.json) has one explicit row per claim, original source-unit line ranges, checked source URLs, findings, and claim-specific notes. For an unknown-question entry, “evidence verified” means the stated **known mechanism and its evidentiary limit** were checked. It does not mean the open production question has been answered.

## KA-001 — Medium / P2: commit timestamps are incorrectly treated as public-release timestamps

**Location:** `knowledge/topic-01.json:914`, K01-017, conclusion and first limit. Original basis: U0014–U0017, particularly `provenance/research-report.zh-CN.md:68`.

The English conclusion says the two commits “was made public on” their precise UTC timestamps, and its first limit says: “A commit establishes only when a snapshot was made public.” The Chinese original already says “提交时间只证明代码快照何时公开”. Thus this is a faithful translation of an original-report error, not an English-only mistranslation.

I independently fetched the [5ed7963 commit](https://github.com/xai-org/x-algorithm/commit/5ed796374ea48ee26058aab66ab10c266bea2bef) and [606b254 commit](https://github.com/xai-org/x-algorithm/commit/606b254b45be798bfaecfa8c23f5a9c51bc8000c). Their `commit.author.date` and `commit.committer.date` values are respectively `2026-10-28T02:49:03Z` and `2026-10-29T02:57:55Z`. Those are commit metadata fields, not publication timestamps. GitHub's [push documentation](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository) distinguishes making local commits from subsequently pushing them to the remote. The UTC-to-PDT conversions in K01-017 are correct; the unsupported step is identifying commit time with first public availability.

**Practical effect:** An answer explaining whether an algorithm changed “today” can incorrectly claim a precisely verified publication time. The correct deployment caveat does not repair this separate public-availability overclaim.

**Proposed correction:** In the working English knowledge, say each commit “is dated” or “has author/committer timestamps of” the recorded time. Replace the limit with: “Commit metadata establishes the recorded commit timestamps; it does not establish first public availability or production rollout time.” Preserve the Chinese report unchanged and add an explicit erratum or correction record linked to U0017. Q01 already uses the more careful “is dated” wording and does not need the same correction.

## Historical-provenance checks left unverified

These are limitations on reconstructing earlier work, not findings that the underlying algorithm explanation is wrong.

- **K00-002, `knowledge/topic-00.json:34`, U0660:** The pinned snapshots and date conversions are supported. The retained original report has 23 page separators, and its build manifest ends at page 23. The exact shared-conversation and “latest version 7” assembly lineage was not independently reconstructible from the inspected records. Keep this identified as the original report's provenance statement unless the specific conversation/version record is attached.
- **K00-003, `knowledge/topic-00.json:63`, U0661 / Chinese line 2040:** The report says “此前对最新可见性重构还展开比较过 14 组规则列表与字段”. I read the actual baseline/comparison visibility registrations, rule audiences, and client-switch refactor, but did not locate a retained result identifying those exact 14 historical rule/field groups. The separate 14-file renderer comparison is not evidence for this count. Attach the original named groups/results if recovered, or annotate that this historical count has not been independently reproduced. Do not rewrite the preserved original to hide the gap.

## Evidence and boundaries checked

Primary implementation reading covered the full assigned subject matter: per-reader probability fusion and both default coefficient sets; local/cache/RPC/fallback paths; author-diversity sorting and fresh counts; DPP selection and zero-score handling; conversation assembly and post-scoring deduplication; cold-start guards and Thompson sampling; FairShare; favorite-trigger/index production and read-side routing; repost/reply/network handling; age and ancillary visibility checks; video target/index conditions; account and post labels; URL rules; video safety thresholds; multistep reply-spam safeguards; Article identity, media, renderer, action, subscription, and visibility paths. Conditions, signs, threshold inclusivity, service differences, execution switches, and claims about unexposed production behavior were checked against those implementations.

The root-provided cache was freshly retrieved through the GitHub connector at exact refs. I independently matched all 165 cached file byte hashes to its SHA256 and Git-blob manifest. Relevant implementations were then read for meaning; those hash checks were not treated as semantic proof. Three resources use floating `main` refs (the 2023 HeavyRanker documentation and two writing references); their current content was inspected and their mutable provenance is retained as a limitation.

The historical parameter concern was resolved by independent extraction of **all 20** freshly fetched October `home-mixer/params/param.rs` snapshots, with retrieval hashes checked. They support the observed October 13 changes `.004 → .006`, `.5 → .6`, `.07 → .02`, the October 14 changes `.6 → .66` and `−47.52 → −52.272`, and `.66` as the maximum within this examined set. They do not prove all-time maximums, first-publication times, or universal production rollout.

The existing historical result packages were inspected as records of earlier work, not claimed as rerun tests. The 143-assertion package includes 26 source-file consistency checks. The original smaller packages contain 22 checks/8 source hashes and 14 checks/4 source hashes; all those smaller-package source hashes match the freshly fetched pinned files. CPU records distinguish original-function calls, unchanged AST extraction, and miniature computations. The ten renderer records disclose their synthetic, already-hydrated objects and import substitutions. Their stored source hashes include the earlier serialization-added newline; removing that one newline restores the exact pinned blob. Independently comparing the 14 content-path files confirms 12 identical blobs and only organization-badge field additions in the other two; both changed comparison files were also fetched directly.

The retained Article bounded-search record contains 103 unique files. I matched their bytes to the pinned tree blobs, accounting for the same single serialization newline, and repeated its stated search. This supports the record's bounded negative result, not a claim that undisclosed models/services cannot learn or apply format differences.

Arithmetic examples were independently recalculated: author multipliers `1, .625, .4375`; A2 `.5625 → .39375` after the stipulated higher-scored same-author insertion; reply/copy `.1` versus `.02`; repost/dwell `.02` versus `.03`; and raw-total `.220 → .230`, approximately `4.545%`. Their artificial inputs and lack of exposure causality remain explicit.

Official product documentation was checked for longer Posts, Articles, threads, Premium reply priority, and public views. Hootsuite, the Playbook, Gridlok, SocialPilot, Bangerkit, and NotPeople were inspected as the primary records of their own claims or observations; their assertions were not accepted as primary proof of X's code. The advice/observation/code/official/unknown distinctions generally match the evidence. The editorial examples do not quietly become platform rules or causal experiments.

All 49 topic-06 questions still contain intentional open production questions, including event units/definitions and adapters, live configuration and model coverage, causal reach effects, missing index consumers, classifier prompts, account-label timing, Article-body population, and creator-metric mappings. The relevant known public portions are supported, and the unknowns were not converted into asserted facts. K01-090 likewise correctly retains the unresolved click-dwell adapter/unit boundary. No production model, safety service, real-account growth experiment, or causal exposure test was run for this audit.
