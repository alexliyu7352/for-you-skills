# Independent remediation knowledge review

Reviewed 2026-11-01 UTC against base `13834c3160e6f0e59fd19601001c6db46f213896`; final frozen implementation `5992e2fbeb587f9ab63c9866fdf79715982bb02f`.

**Result: no actionable findings in the requested knowledge-remediation scope.** This is an independent reading of the changed claims and primary source logic, not adoption of the implementer’s conclusions or a renewed audit of all 578 claims.

## Coverage and source checks

Read every changed field in all 17 changed claims, all 15 complete correction objects, `knowledge/README.md`, `shared/research-errata.md`, and `shared/knowledge-guide.md`. Compared original values through read-only base-object access and checked the mapped Chinese report units to establish error origin. The 12 unique findings divide into six inherited-report errors and six English-distillation errors; repeated metadata on the two age claims and the three related Under the Hood entries does not inflate the finding count. K00-002 and K00-003 remain historical uncertainties rather than asserted factual errors.

| Finding | Claims inspected | Primary-source conclusion checked |
| --- | --- | --- |
| KA-001 | K01-017 | Commit author/committer times do not establish first public availability or deployment. Baseline metadata was read from the pinned Git object; comparison author and committer timestamps were independently fetched from GitHub’s Git-commit API. UTC/PDT conversions are consistent. |
| KB-F01 | K04-049 | Ancillary removal needs a returned dropping visibility action; missing/error lookups alone do not satisfy that branch. Source-text fallback and candidate-author hydration filtering support the narrower wording. |
| KB-F02 | K04-046, K04-047 | `map(age <= max_age).unwrap_or(false)` preserves the inclusive boundary and rejects unavailable age; candidate ID and scope limits remain explicit. |
| KB-F03 | K04-077 | The production-only writer supplies zero; the general cache branch requires a present score at most 1.0. Kafka/Strato follow separately, and the entry preserves operation-failure limits. |
| KB-F04 | K02-089 | `MAX_BIO=500`, strip/slice/rstrip, and the bio call support the numeric renderer cap without a product-editor or ranking claim. |
| C-01 | K03-018 | Debias requires no cached posts and the parameter switch; pacing alone creates no candidate content features. |
| C-02 | K03-101 | MediaInjected excludes positive prior NSFW; absent/error prior results return false. LeadingFrames has a distinct missing-result rejection. |
| C-03 | K03-077 | The guard uses querying-viewer followers, excludes known counts at least 10000, permits missing counts, and separately requires present duration strictly above the configured minimum. Zero default weight remains separate. |
| KD-01 | K05-061 | Public classification and conditional label writing support abuse risk, not universal hashtag effects or proof that an undisclosed formula cannot exist. |
| KD-02 | K05-047 | Both general and reply consumers use the exact documented `bbq_` job names. |
| KD-03 | K05-034 | The selected matching-record count is compared with `minimumMatchingPosts`; five and three are the inspected rule defaults. |
| KD-04 | K05-069, K04-091, K05-066 | Eligible logical-post denominator, authored-month assignment, ordinary event horizon, ever-applied count and separate removal agree with the generating/publishing/report code. Snapshot and flag handling remain explicitly separate from the ordinary event horizon. |

Independently verified all 27 unique correction-cited code files against Git object bytes at `5ed796374ea48ee26058aab66ab10c266bea2bef`, including the 24 cached evidence files and three supplemental files. All cited line ranges are valid. The supplemental daily job, monthly publisher and core hydration filter match blobs `dbafd530b9a6405996677ab886db12cc339c849a`, `f576bd28f4de4dd38eb6b45a47850476a50d6621`, and `576b76dec45b1b2541f560d36f89b27429423fed`. Read relevant source context, including daily-job input selection and separate snapshot/flag paths, rather than treating line anchors or hashes as semantic proof.

## Provenance and lookup verification

Direct byte comparison with the base confirmed the original report, migration baseline, source-unit registry, and source registry unchanged. Across the corpus, all claim IDs, kinds, original source-unit mappings, evidence source IDs/indices and related-unknown mappings remain unchanged. The working prose and additive correction evidence are distinct from the immutable historical record.

Executed `get` for each of the 15 corrected claims and asserted exact preservation of its entire correction object. Direct JSON reading exposes the same evidence without Python. The guide expressly instructs readers to use correction sources and corrected conditions alongside the original citations, explains the direct-JSON fallback, and prevents archived wording from superseding a verified correction. The errata’s sibling guide link resolves in the shared references arrangement.

`python3 tools/knowledge.py audit` returned 578 claims, 49 unresolved questions, all 668 required source units covered, all 100 source groups cited, and no errors. This check establishes reference integrity, not semantic truth; semantic conclusions above came from source reading.

## Observed limits

The two assembly/14-group historical provenance statements remain unreconstructed and are correctly attributed. First public availability, live deployment, account-specific Under the Hood access, and causal exposure effects were not established or tested. The historical 403 observation is attributed to the earlier full review rather than presented as a new request. This review does not certify unchanged claims outside the remediation scope, generated-installation behavior, current live service behavior, or the independent engineering repairs.

Coordinator provenance note: the reviewed local commit was published with an identical Git tree (`36017698399f753f37aa5c6645fdf409c238f45f`) under the commit ID shown above. See [remediation](remediation.md) for subsequent fixes and release verification.
