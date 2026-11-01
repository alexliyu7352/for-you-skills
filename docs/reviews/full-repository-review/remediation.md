# Review remediation — 1.1.1

The **22 original findings are fixed and verified within the scope below**. An independent engineering reviewer found one additional sparse-card coverage issue; that was also fixed with a regression that first failed. The changes are published on `main`, all three Linux/Windows CI jobs pass, and all eight installed personal skills have been saved and read back successfully.

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
| Cross-platform runtime | Ubuntu/Python 3.9, Ubuntu/Python 3.12 and Windows/Python 3.12 each pass integrity checks, build comparison and all 81 tests; [CI run](https://github.com/alexliyu7352/for-you-skills/actions/runs/41275934299) |
| Real installer | Six targets; 16 physical skill copies, 364 byte-matched files and 16 passing isolated audits (Skills CLI 1.7.4) |
| Task execution | Three fresh-context user requests exercise claim correction, label-period explanation and scope-separated observations; see the retained answers |
| Personal installation | Eight skills saved separately; 174 files verified byte for byte against persisted content, eight host-managed UI files checked semantically, validators and offline audits passed |

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

- The [successful CI run](https://github.com/alexliyu7352/for-you-skills/actions/runs/41275934299) at `30c1ed389c23353da1c06362ce84ca7624fa0a95` passed Ubuntu/Python 3.9, Ubuntu/Python 3.12 and Windows/Python 3.12. Every job ran integrity validation, generated-file comparison and all 81 tests. Verification completed on 2026-11-01 UTC.
- The [first run](https://github.com/alexliyu7352/for-you-skills/actions/runs/41275658188) passed both Ubuntu jobs but failed three Windows tests: text-mode writing translated newlines in a temporary report fixture, invalidating its expected byte hash. The fixture now writes exact UTF-8 bytes; the runtime hash checks remain unchanged. The successful run above verifies this correction.
- All eight existing personal skills were updated in place, validated, saved separately and verified from persisted content: **174 exact files** plus eight semantically checked UI metadata files. Host-managed icons were preserved. One transient HTTP 500 interrupted a readback fetch after a successful save; a subsequent fetch verified it and the remaining updates completed. No user visual preference store was created or changed.
- The final closure publication only updates documentation and the machine-readable ledger; the tested runtime and installation contents are identical to the successful CI revision.
