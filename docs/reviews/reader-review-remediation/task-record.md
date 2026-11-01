# Reader-review repair: observed task behavior

Date: 2026-11-01 (America/Los_Angeles). Baseline: `1b6a8224ded9c25def1a86c97e58b0d2d07b4729`. The repair changes the workflow and its generated copies, not the knowledge corpus. See [cases](cases.md), [execution ledger](progress.md) and [artifact manifest](manifest.json).

## Method and retained evidence

Coordinators received ordinary task requests, isolated copies of the applicable skill, and a request to retain exact inputs/outputs. They were not given expected verdicts, the implementation plan, the diagnosis or sibling-run records. Their outer contexts used `fork_turns: none`. The standalone and router runs retain actual child-dispatch messages and context settings in `dispatches.json`; each cold reader received its own packet with no inherited conversation. Actual model identifiers were not exposed by the host, so none is inferred.

Files under `records/` preserve request files, complete answers, reviewer packets, reviewer responses and available draft/measurement artifacts. Local absolute paths in these raw records identify the original isolated directories; they are not public download links. To repeat a request in another environment, install the same package and substitute only the local path prefix. The manifest records file hashes and the tested workflow hash. These records permit inspection and repetition, not a guarantee that a stochastic model will produce identical wording.

The constrained-host run was instructed that independent contexts were unavailable; it exercised labeled self-review and non-reading outcomes. Its budget case is explicitly a **simulation** with three supplied FAIL outcomes, not a claim that three real reviewers ran. Full plan reviews screened the corpus and retained original citations; this execution did not re-audit the entire research corpus or verify every external link live.

## Baseline observations

- [Limited reader packet](records/baseline-r1/request.md) → [actual response](records/baseline-r1/response.md): PASS with an empty stall log for a draft that defines median without a worked example. The permitted packet omitted the stricter standard. This failed R1's acceptance expectation. It is a newly executed baseline observation, not a reconstructed transcript from the earlier review.
- [Plan-only request](records/baseline-r2/request.md) → [actual response](records/baseline-r2/response.md): the old coordinator completed a useful plan review and declined to claim a reader PASS because no copy existed. It compensated for the missing workflow branch. This input did **not** reproduce a bad runtime outcome, and is not counted as a baseline failure.

## Fixed-package observations

| Case | Observed outcome | Raw evidence |
| --- | --- | --- |
| R1, standalone | First cold reader identified the missing worked example; the revised text passed a new cold reader in round 2. | [Round 1](records/fixed-standalone/request-1-round-1-response.md), [round 2](records/fixed-standalone/request-1-round-2-response.md), [delivered answer](records/fixed-standalone/request-1-response.md) |
| R1, router fallback | Same defect identified in round 1; a revised version with an explicitly illustrative example passed in round 2. | [Round 1](records/fixed-router/request-1-round-1-response.md), [round 2](records/fixed-router/request-1-round-2-response.md), [delivered answer](records/fixed-router/request-1-response.md) |
| R2, both paths | Full available plan checks completed; no draft invented; `none / not_applicable / 0` reported. | [Standalone](records/fixed-standalone/request-2-response.md), [router](records/fixed-router/request-2-response.md) |
| R3 and R4 | Title and excerpt retained; `self / pass / 1` applied only to those parts, explicitly excluding the rest of the Article. | [Scoped self-review](records/fixed-boundaries/request-1-response.md) |
| R5 | Readability improved while the unsupported causal mechanism remained explicitly unresolved; no mechanism or measurement fabricated. | [Missing mechanism](records/fixed-boundaries/request-2-response.md) |
| R6 | Protected sentences remained unchanged; ambiguity and missing reader consequence were quoted, with `self / unresolved / 1`. | [Protected wording](records/fixed-boundaries/request-3-response.md) |
| R7 | Simulation stopped at three hypothetical completed passes with unresolved status; actual execution was explicitly zero real reviewer passes. | [Budget simulation](records/fixed-boundaries/request-6-response.md) |
| R8 | Quick check disclosed `none / skipped / 0`; no reader PASS claimed. | [Quick check](records/fixed-boundaries/request-4-response.md) |
| R9, both paths | Both new cold readers returned PASS with empty stall logs in round 1; the 185-character Post remained unchanged. | [Standalone](records/fixed-standalone/request-3-response.md), [router](records/fixed-router/request-3-response.md) |
| R10, both paths | Final counts independently recomputed as 793 and 888 Unicode code points; final copy matches the last reviewed draft, preserves the supplied test scope and labels the example as illustrative. | [Standalone final copy](records/fixed-standalone/request-1-draft-final.txt), [router final copy](records/fixed-router/request-1-final-draft.txt) |
| R11 | Missing Article text reported as missing; useful independent plan checks completed, without fabricated copy or a PASS. | [Absent attachment](records/fixed-boundaries/request-5-response.md) |

The exact task files for the fixed runs are [standalone](records/fixed-standalone/request.md), [router](records/fixed-router/request.md) and [constrained host](records/fixed-boundaries/request.md). R5–R7 succeeding means the coordinator correctly retained an unresolved result, not that the defective text became publishable.

## Engineering checks and limits

- Existing 81 automated tests passed on Python 3.12.14 both before and after the workflow change. The final run took 6.673 seconds. [Baseline output](records/baseline-tests.log); [fixed output](records/fixed-tests.log).
- Integrity validation: 578 claims, 49 questions, 668/668 source units, 100 source groups and 396 URLs; no errors. Build comparison: no drift across 182 generated files/eight skills. Both changed skills passed the skill-creator frontmatter validator. The existing suite includes isolated-package audits and helper checks.
- No native six-client model matrix, production X operation, image generation or exposure improvement was tested. The constrained-host simulation is not proof that a particular client lacks delegation. Repeated-stall termination is specified but has no separate actual repeated-stall replay; R6 exercises the protected-wording stop. These are finite observed cases, not exhaustive model-behavior guarantees.
