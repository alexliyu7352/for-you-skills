# Review remediation — 1.1.1

The **22 original findings are fixed and locally verified**. An independent engineering reviewer found one additional sparse-card coverage issue; that was also fixed with a regression that first failed. Remote CI and installed personal-skill verification are recorded separately below and are pending at this publication stage.

Date: 2026-10-31, America/Los_Angeles. The original review targeted `9193233`; remediation starts from `13834c3`. [Implementation plan](../../superpowers/plans/2026-10-31-review-remediation.md).

## Changed behavior

- Corrected 13 directly affected knowledge claims and two related Under the Hood explanations. Every correction includes its finding ID, origin and primary-source links; all eight packages include English research errata. Six findings originate in the Chinese report and six in English distillation. The two unreconstructed historical records are explicitly qualified.
- Kept all 578 IDs, 49 Q entries, original citations, source-unit mappings and original report bytes unchanged. Original report SHA-256 remains `039d8e0a1b3152dfae7730f4d514914a18c79328c0a6ac796892dab86f4f0908`.
- Separated observation scopes, retained raw historical records, preserved unresolved text alternatives and exact/rounded count meanings, and resolved explicit content links transitively with visible conflict handling. Sparse cards no longer erase fuller same-time coverage. Later timestamps do not inherit older completeness or unknown metrics.
- Preserved raw CRLF code points, returned concise malformed-input diagnostics, validated consumed nested schema and original-unit hashes before lookup, and enforced complete supported frontmatter.
- Included license and self-contained attribution in every standalone skill.

## Acceptance evidence

| Check | Observed result |
| --- | --- |
| Full local suite | **81 tests passed** on Python 3.12; baseline was 43 |
| Repository integrity | 578 claims, 49 Q entries, 668/668 substantive units, 100 source groups, 396 original URLs; zero errors |
| Distribution build | Eight skills, **182 files**, zero drift |
| Knowledge review | All 17 changed claims, 15 correction objects and 27 correction-cited code files independently checked; no actionable finding |
| Engineering review | Original 10 fixes inspected; 410 malformed-schema probes, permutation checks and eight isolated packages checked; one P3 follow-up fixed afterward |
| Compatibility syntax | 13 canonical tool/test files parse as Python 3.9; this is not a local 3.9 runtime run |
| Real installer | Six targets; 16 physical skill copies, 364 byte-matched files and 16 passing isolated audits (Skills CLI 1.7.4) |
| Task execution | Three fresh-context user requests exercise claim correction, label-period explanation and scope-separated observations; see the retained answers |

The engineering reviewer observed **80** tests at the reviewed implementation. The coordinator then added the sparse-card regression: all six permutations failed first, the fix passed, and the complete suite reached **81**. The original independent report is preserved; its finding is closed by the recorded follow-up rather than erased.

## Finding closure

All statuses refer to the working package, not an edit to the preserved historical report. Knowledge corrections and original ENG fixes are in `5992e2fbeb587f9ab63c9866fdf79715982bb02f`; the follow-up is in `18c0636b0be3506d3a6f784c3cb2085a636fa896`.

| Original finding | Status | Affected claims or executable acceptance |
| --- | --- | --- |
| KA-001 | Fixed | K01-017 |
| KB-F01 | Fixed | K04-049 |
| KB-F02 | Fixed | K04-046, K04-047 |
| KB-F03 | Fixed | K04-077 |
| KB-F04 | Fixed | K02-089 |
| C-01 | Fixed | K03-018 |
| C-02 | Fixed | K03-101 |
| C-03 | Fixed | K03-077 |
| KD-01 | Fixed | K05-061 |
| KD-02 | Fixed | K05-047 |
| KD-03 | Fixed | K05-034 |
| KD-04 | Fixed | K05-069 |
| ENG-01 | Fixed | Source-unit uniqueness, bounds, ordering, source IDs and slice hashes: test_validation.py; standalone original/audit reject corrupt inputs. |
| ENG-02 | Fixed | Nested schema/CLI mutation regressions: test_validation.py; independent 410-case probe returned clean diagnostics. |
| ENG-03 | Fixed | Complete supported frontmatter and malformed/duplicate scalar regressions: test_validation.py. |
| ENG-04 | Fixed | Scope-aware snapshots, unknown-scope retention and provenance permutations: test_post_records.py. |
| ENG-05 | Fixed | Persistent alternatives and partial conflict state across three or more observations: test_post_records.py. |
| ENG-06 | Fixed | CRLF/LF/lone-CR CLI raw counts: test_draft_checks.py; CRLF fixture reports 6000 raw / 5998 trimmed. |
| ENG-07 | Fixed | Eight standalone licenses/notices and contained local links: test_packaging.py and independent isolation checks. |
| ENG-08 | Fixed | Transitive Article/carrier/Thread groups, cyclic and contradictory input permutations: test_post_records.py. |
| ENG-09 | Fixed | Exact integer/comma count equivalence without rounded/scope promotion: test_post_records.py. |
| ENG-10 | Fixed | Malformed input roots/rows and file/JSON errors produce clear failures: test_post_records.py and test_draft_checks.py. |

**REM-ENG-01:** fixed. `test_sparse_same_time_cards_preserve_complete_observed_coverage` verifies all six orders of a complete observation, an explicit preview/partial card and a pinned card. Original full text and media notes survive; existing conflicting-text tests still require partial coverage.

## Independent records and remaining limits

- [Independent knowledge review](remediation-knowledge-review.md)
- [Independent engineering review and follow-up reproduction](remediation-engineering-review.md)
- [Actual task inputs, commands and user-facing outputs](remediation-task-probes.md)
- [Machine-readable closure ledger](remediation.json)

K00-002/K00-003's historical lineage records remain incompletely reconstructed. Live Under the Hood account access remains unverified. No authenticated X collection, real image output, six native model runtimes or causal exposure experiment was performed. They are capabilities outside this defect-fix acceptance, not passed tests.

## Release verification updates

- Remote Linux/Windows CI: pending publication and observation.
- Personal skill updates: pending save and persisted-content verification.
