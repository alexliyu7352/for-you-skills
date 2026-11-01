# Reader Review Remediation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task after implementation is authorized. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the existing reader-review stage executable from a genuinely fresh context, applicable to supported inputs, and honest about incomplete reviews.

**Architecture:** Keep the workflow in `workflows/x-publish-checklist.md` as the canonical source and regenerate its two distributed copies. Define a complete reviewer handoff and explicit completion states in that workflow; preserve behavioral evidence as review fixtures and transcripts rather than introducing a new execution framework.

**Tech Stack:** English Agent Skills Markdown; existing Python 3.9+ build/validation helpers and unittest suite; available host agents for behavioral probes.

**Spec:** Review of `alexliyu7352/for-you-skills` at `1b6a8224ded9c25def1a86c97e58b0d2d07b4729`, compared with `6d923bd83c6cd8eb14f8355e795cd1d0a5ab9807`. Confirmed findings: the fresh-reviewer handoff excludes the rubric it requires; mandatory cold reading has no applicable outcome for supported plan-only requests. Also address the missing termination contract and missing retained behavioral records. The implementation choices below are proposed, not implemented.

## Global Constraints

- Keep all eight skills, current routing intents, standalone installation, Python 3.9 compatibility and optional-Python operation.
- Keep skill instructions, fixtures and review records in English; responses still follow the user's language.
- Do not change the 578 knowledge claims, 49 question entries, original report or citation mappings.
- Preserve the current three stall classes and no-compression requirements, including the numerical worked-example requirement. Editorial judgments remain separate from algorithm evidence.
- Honor explicit user scope, protected wording and editing restrictions. Never invent facts to obtain a PASS, publish a post, or mislabel self-review as cold review.
- Only this plan is being delivered now. Implementation, version changes and publication are not performed by writing it.

## Review Focus

- An isolated reviewer must receive the actual standard, not reconstruct it from a reference to a missing step: case R1.
- A publishing plan without copy must remain reviewable without manufacturing a draft: R2.
- A title, excerpt or selected Thread part must not receive a whole-document PASS: R3.
- Missing facts, protected wording, repeated stalls and host limits must leave an honest unfinished outcome: R5–R7.
- Hosts without fresh contexts and users requesting quick checks must receive accurate method/scope labels: R4 and R8.

## Task 1: Repair and exercise the workflow contract

**Files:** Modify `workflows/x-publish-checklist.md`; create `docs/reviews/reader-review-remediation/cases.md` and `docs/reviews/reader-review-remediation/task-record.md`. Generate `skills/x-publish-checklist/SKILL.md` and `skills/x-assistant/references/workflows/x-publish-checklist.md` through `tools/build.py` only.

**Interfaces:** The authoring agent hands off `draft`, `scope`, `audience`, `constraints`, optional `model_paragraphs`, the complete `review_protocol` and the complete `rubric`. These are documented handoff fields, not a new CLI or JSON API. The reviewer returns quoted stalls and PASS/FAIL for the supplied text; the coordinator records `mode`, `status`, `rounds`, `reviewed_scope`, and unresolved stalls with reasons and next actions.

- [ ] Before implementation, fetch and verify the current remote head, then create an isolated repair branch from the reviewed commit or its verified successor. If another agent has changed the affected workflow, review that delta first and preserve its work; do not overwrite it with this plan's snapshot.
- [ ] Retain exact baseline inputs and delegated prompts for R1 and R2, run them against the frozen 1.2.0 package and record actual outputs. If a model compensates for the defective instructions, say so; do not manufacture a failing run. The prior review observed R1's limited handoff passing a median example that failed when given the complete rubric, but its historical transcript must not be reconstructed as a new run.
- [ ] Replace the restrictive handoff at line 31 with an explicit allow-list containing all fields above. Include the complete pure-read procedure, all three stall definitions, all three no-compression requirements and output rules. Exclude prior verdicts, notes, stall logs and explanations of intended meaning. Preserve actual media/formatting within the reviewed scope; unreadable or absent evidence remains unavailable.
- [ ] Gate reader review on actual draft text. For plan-only inputs, report `not_applicable` because no copy exists and finish the available publishing checks. If the user requested review of an unavailable draft, report `missing` for that text and still finish independent work. For excerpts or selected parts, review only those parts and label that scope. A quick-check skip is `skipped`, with a reason.
- [ ] Separate execution method from result. Use `mode: cold | self | none` and `status: pass | unresolved | not_applicable | missing | skipped`. Report rounds as actual completed reviewer passes, with zero when no reader pass ran. A stage skipped or unavailable is never a PASS; self-review can report its result but cannot claim independence.
- [ ] Replace unconditional looping with a proposed default of **three completed reviewer passes total**, including the initial pass. This is an operational budget, not a readability threshold; an explicit user instruction may change it. Stop earlier for missing facts, conflicting protected wording, the same unresolved substantive stall after an attempted repair, or inability to complete either a cold review or an honest self-review. Lack of fresh context alone uses the self-review fallback. Each cold review of changed text uses a fresh context when available. At the limit, report `unresolved`, the remaining quoted problems and the needed input/action. Do not keep rewriting, weaken the standard, or describe an unreviewed revision as passed.
- [ ] Recheck only evidence affected by edits before final delivery: final text length and scope, changed claims/qualifications and citations, and any changed media/format recommendations. Label illustrative arithmetic as illustrative rather than measured results. Preserve the original evidence-review findings that still apply.
- [ ] Run `python tools/build.py`, then execute the cases below using the standalone checklist and the router's bundled fallback. R1, R2 and R9 must exercise both entry paths; the remaining cases may use either path with the chosen path recorded. Keep hosts without fresh-context capability as explicitly constrained tests, not proof of six native-client runs.

| Case | Exact behavior to establish |
| --- | --- |
| R1: incomplete median explanation | A text defining median but omitting a worked numerical example reaches a genuinely isolated reviewer with the complete rubric; the missing example is identified with a verbatim quote. A repaired illustrative example can pass this rule. |
| R2: plan only | Input: “Review my publishing plan: an Article on Tuesday, an introductory Post on Wednesday, and three charts. The copy is not written yet.” Complete applicable plan checks, report no-copy/not-applicable, use zero reader rounds, and do not invent a draft. |
| R3: partial draft | Review only a supplied title and excerpt; report that scope and make no whole-Article PASS claim. |
| R4: no independent context | With fresh review explicitly unavailable, perform the separated self-review and label it; do not claim a second agent ran. |
| R5: missing factual mechanism | A draft's claimed improvement lacks its actual cause; no source or author explanation is available. Quote the missing connection, request the specific fact as a next action, and return unresolved without fabricating a mechanism. |
| R6: protected text/no progress | A quoted stall cannot be corrected within the user's explicit protected-wording constraint, or persists after an attempted repair. Return unresolved with the conflict; do not override the constraint or repeat indefinitely. |
| R7: round budget | Use three controlled FAIL responses on distinct substantive defects to verify stopping at three completed rounds with unresolved status. Label this a simulated coordination test, not three independent real reader runs. |
| R8: quick check | A quick-check request can skip the stage only with an explicit skip disclosure and zero rounds. |
| R9: clean control | A clear complete draft with defined terms, supported consequences and required examples passes without invented stalls; retain the actual output, including an empty stall log. |
| R10: revised draft | After adding an explanatory example, the delivered count matches the delivered text and the example is labeled illustrative; supported facts and citations retain their scope. |

- [ ] Retain exact user inputs, drafts at every round, full reviewer prompts, verbatim outputs, entry path, actual model/host where exposed, context isolation method, mock declarations, commit identity and disposition. Distinguish an intermediate reviewer FAIL from failure of an acceptance case; an honest unresolved result is the expected success for R5–R7. If a case does not meet its expected behavior, repair and rerun it before declaring it passed.
- [ ] Run `python tools/validate.py`, `python tools/build.py --check`, `python -m unittest discover -s tests -v`, and `git diff --check`. Require no corpus errors, no generated drift, passing existing tests and a clean diff. Do not add keyword-presence tests that merely mirror the new Markdown.
- [ ] Commit the workflow repair, generated copies and retained case records together after the behavioral evidence supports the documented outcomes.

## Task 2: Align public claims and obtain independent acceptance

**Files:** Modify `README.md`, `README.zh-CN.md`, `CHANGELOG.md`, `docs/validation/results.md`; create `docs/reviews/reader-review-remediation/review.md`.

**Interfaces:** Consume Task 1's actual case record and final workflow. Produce accurate documentation and a fresh independent review tied to the tested commit.

- [ ] Update both README reader-review bullets with the fresh-context capability condition, self-review fallback and possibility of unresolved results. Document plan-only behavior without promising a reader pass on absent text.
- [ ] Add an Unreleased repair entry to the changelog. Link the retained case records from validation results and distinguish observed behavior, simulated control-flow checks, unchanged automated checks and untested hosts. Preserve the earlier 1.2.0 report as a historical claim; do not backfill invented transcripts.
- [ ] Verify every public statement against the records and check the local links and generated artifacts. Commit the documentation only when its claims match what was actually observed.
- [ ] Request one fresh independent review of the entire repair against this plan and the two confirmed findings. The reviewer must inspect the handoff, applicability, stopping paths, retained evidence and standalone/router consistency, rather than accept the test count as behavioral proof.
- [ ] Resolve verified findings and rerun only the affected checks. Deliver the final diff, commit IDs, case outcomes and explicit remaining limits. Any release creation or installed-skill refresh should be reported separately, not assumed completed by a source commit.

## Execution recommendation

Use one implementer for this small, tightly coupled workflow repair, followed by one independent reviewer. Keep the observed 1.2.0 tests and the new repair evidence distinct. No implementation has started as part of producing this plan.
