# Full Review Remediation Implementation Plan

> **For agentic workers:** Use the parallel-agent workflow for the three disjoint implementation domains below; the coordinator owns integration and an independent final review. Follow test-driven development for executable changes. Human prose is reviewed against sources, not tested by matching exact sentences.

**Goal:** Resolve the 22 findings from the full repository review and update all eight installable skills with verifiable corrections.

**Architecture:** Preserve the original report, source registry order, migration mapping and frozen review. Correct working knowledge with explicit additive correction metadata and bundled errata. Fix helper behavior at its current interfaces, then rebuild all generated skills from canonical inputs.

**Tech Stack:** Python 3.9+, standard library only; Agent Skills Markdown/JSON; existing Linux/Windows CI.

**Spec:** [Full review](../../reviews/full-repository-review/README.md) and [22 findings](../../reviews/full-repository-review/findings.json), reviewed at `9193233924df388727296c4e76948db919ac32eb`. Implementation starts from `13834c3160e6f0e59fd19601001c6db46f213896`.

## Global Constraints

- Preserve all 578 claim IDs, 49 Q IDs, original source-unit mappings, original citations and original report bytes.
- Keep runtime instructions, knowledge and errata in English; retain Chinese user-facing documentation.
- Add no third-party Python dependency; support Python 3.9 and 3.12 on Linux and Python 3.12 on Windows.
- Unknown measurements stay unknown; public views, owner analytics, content identity and post identity remain separate.
- No exposure guarantees, new optimal posting rules or claim that live X/image/native-model paths were tested.
- Existing authorizations cover the repository update and updating the installed skills. Do not alter real visual preferences.
- Preserve the frozen audit as history. Add a separate closure ledger and link it from the audit; do not rewrite its original findings as if they never existed.
- Coordinator alone changes Git state, builds generated files, publishes, and updates installed copies. Implementers own disjoint files.

## Review Focus

1. Reordering three or more same-time observations must not change count meaning or hide text conflicts.
2. Unknown metric scope must never be promoted into a known scope; different scopes must retain their source data.
3. Cyclic/contradictory content links must terminate and be flagged without silently joining unrelated Articles.
4. A malformed nested corpus value must produce an actionable validation error, not a traceback, including standalone commands.
5. A single installed skill must contain valid licensing, correction evidence and helpers; links must work without the parent repository.

## Task 1: Correct the knowledge and expose errata

**Owner/files:** Knowledge implementer: `knowledge/topic-00.json` through `topic-05.json`, `knowledge/README.md`, new `shared/research-errata.md`. Do not change immutable mappings or the frozen report.

**Interfaces:** Each corrected claim retains its existing fields and adds optional `correction` with exactly `review_finding` (string), `origin` (`original_report` or `english_distillation`), `date` (`2026-10-31`), `summary` (string), and `sources` (nonempty list of `{label: string, url: https URL}`). Existing `expand_claim` already preserves additive metadata; Task 3 validates this shape. Additional primary sources go in correction metadata, never by mutating original citation indices.

- [x] Read each of the 12 knowledge findings and its primary source context; confirm the correction is justified.
- [x] Correct all 13 affected claims, including conditions/checks/limits that repeat the defect; attach correction evidence.
- [x] Record all six inherited-report errata and six distillation fixes with claim/finding IDs and citations in the bundled English errata. Explicitly annotate the two unreconstructed historical provenance claims as unverified, without asserting they are false.
- [x] Verify the frozen original report, source URLs, identity and migration mappings remain byte/structurally unchanged.
- [x] Have an independent reader inspect every corrected claim and use the skill on realistic questions without being shown expected answers.
- [x] Coordinator commits the coherent knowledge correction with its provenance and lookup support.

## Task 2: Preserve observation meaning and content identity

**Owner/files:** Observation implementer: `tools/summarize_posts.py`, `tests/test_post_records.py`, `shared/observations.md`. Findings ENG-04, ENG-05, ENG-08, ENG-09 and the summarize CLI portion of ENG-10.

**Interfaces:** Keep `summarize(rows)` and JSON CLI. `posts` may retain separate latest observations for each `(permalink identity, metric_scope)`; `unique_posts` must count distinct confirmed identities, not rows. Preserve raw merged source observations/provenance in the result. Clarify the contract and any added counts. Content relationships may group identities but never merge their metrics.

- [x] Add failing regressions for public/owner/unknown scope separation, three text alternatives, repeated conflicting snapshots, exact `1000` versus `"1,000"`, transitive Article/carrier/Thread links, permutations/cycles/contradictions, and malformed CLI root/row shapes.
- [x] Run `python3 -m unittest discover -s tests -p test_post_records.py -v`; confirm each new regression catches the intended failure.
- [x] Implement scope-aware selection, persistent conflict alternatives, exact-value comparison and deterministic transitive grouping with explicit conflicts. Keep later timestamps independent of older completeness/metrics.
- [x] Reject invalid JSON roots cleanly and retain actionable invalid-row diagnostics; do not silently coerce unknown categories or discard valid URL-less evidence.
- [x] Run the same tests and the full suite; report any generated-file drift separately until integration rebuilds it.
- [x] Coordinator reviews and commits the helper, contract and regressions together.

## Task 3: Enforce corpus, provenance and frontmatter integrity

**Owner/files:** Validator implementer: `tools/knowledge.py`, `tools/validate.py`, new `tests/test_validation.py`; edit `tests/test_lookup.py` only if a public interface legitimately needs adjustment. Findings ENG-01, ENG-02 and ENG-03.

**Interfaces:** Preserve existing lookup/CLI commands and compatible function calls. Add optional report text/bytes to `validate` or a separate shared source-unit validator; both repository and standalone audit/original paths must check bounds, unique IDs and hashes. Validate optional Task 1 correction metadata without requiring it on unchanged claims. Full validation must short-circuit unsafe iteration on malformed containers.

- [x] Add failing mutations for duplicate/out-of-bounds/reversed source units, wrong slice hashes, unknown source IDs; wrong nested types/null lists/nonobjects; and missing/duplicate/malformed frontmatter.
- [x] Run `python3 -m unittest discover -s tests -p test_validation.py -v`; failures must be the expected clean-error assertions.
- [x] Validate complete consumed shapes before lookup/iteration. Verify each source slice hash against the unchanged report. Return structured errors or concise CLI errors, never fabricated empty originals.
- [x] Require complete frontmatter and a documented dependency-free supported scalar subset for `name`/`description`; reject unsupported/ambiguous YAML instead of pretending to parse it.
- [x] Add tests that additive correction evidence is preserved by `get` and malformed correction evidence fails cleanly.
- [x] Run targeted/full suites; coordinator rebuilds and checks actual isolated installation after integration.
- [x] Coordinator commits validation and negative tests together.

## Task 4: Correct raw input handling and standalone attribution

**Owner/files:** Coordinator: `tools/inspect_draft.py`, `tools/build.py`, `tests/test_draft_checks.py`, `tests/test_packaging.py`, `shared/knowledge-guide.md`. Findings ENG-06, ENG-07 and the inspect CLI portion of ENG-10.

**Interfaces:** Preserve existing Unicode code-point semantics. Read UTF-8 using `open(..., newline='')` before trimming. Each skill includes root `LICENSE` and a standalone-safe `NOTICE.md`; copied references remain self-contained. The shared guide explains corrected working knowledge versus preserved historical report and instructs agents to use correction citations.

- [x] Add failing CLI tests: `b'A\r\n' * 2000` reports raw 6000, trimmed 5998 and 1998 after 4000; LF/lone-CR variants preserve input; null/scalar/missing-media root yields a useful nonzero exit without traceback.
- [x] Add failing isolated-package assertions for license/notice presence and self-contained references.
- [x] Run targeted tests and confirm intended failures; implement the minimal corrections.
- [x] Run targeted tests, rebuild via `python3 tools/build.py`, then run validation and the full suite.
- [x] Coordinator commits helper and distribution corrections with regression evidence.

## Task 5: Independent acceptance, release and installed updates

**Owner/files:** Coordinator and fresh reviewers: generated `skills/`, new `docs/reviews/full-repository-review/remediation.md` and `remediation.json`, validation log, changelog and compatibility/count text only where needed.

- [ ] Reconcile all 22 findings to changed files, source checks or regression tests; leave historical limitations visible.
- [ ] Run `python3 tools/validate.py`, `python3 tools/build.py --check`, `python3 -m unittest discover -s tests -v`, syntax compatibility, and isolated helper execution.
- [ ] Dispatch fresh independent source/engineering review and realistic task probes. Fix substantive new failures with a failing regression first.
- [ ] Install all eight generated skills with the real cached Skills CLI into temporary six-target projects, compare bytes, and run bundled lookup/audit from an unrelated directory.
- [ ] Publish the reviewed changes using the existing repository authorization; verify remote tree and Linux/Windows CI. Do not claim CI success before observing it.
- [ ] Update each of the eight existing personal skills, validate its actual installed directory, save separately and verify persisted content after reconciliation.
- [ ] Publish the closure record with exact validation evidence, unresolved limits and installation results. Report any remaining blocker explicitly.

## Execution notes

- Planning and execution are both requested in the current message; no additional plan-approval pause is needed.
- Three independent implementers may work concurrently on the disjoint scopes above. Integration waits for them; generated output is rebuilt once from the integrated canonical files.
- A sibling Git worktree keeps the original checkout intact without introducing a nested worktree path into the package.

Implementation note: canonical fixes and generated packages were committed together after integrated verification, to keep the corrected knowledge and its installable copies in one coherent revision. The independent review follow-up has a separate regression/fix commit.
