# Reader-review acceptance cases

These cases exercise the Markdown workflow. They are separate from the 81 Python integrity, helper and packaging tests. Exact task inputs, reader packets and outputs are retained with the [task record](task-record.md); the [implementation plan](../../superpowers/plans/2026-11-01-reader-review-remediation.md) defines the requested behavior.

| Case | Input and expected behavior | Execution surface |
| --- | --- | --- |
| R1 | A developer draft defines median but lacks a worked numerical example. The independent reader receives the entire rubric and identifies the missing example using actual quoted text. Any repair preserves supplied measurements and labels illustrative values. | Standalone checklist and router fallback, request 1. |
| R2 | An Article/introductory-Post/three-chart publishing plan has no copy. Complete available plan checks; reader stage is not applicable, with no invented copy and zero reader rounds. | Standalone checklist and router fallback, request 2. |
| R3 | Only a title and excerpt are supplied. Review that scope without claiming the whole Article passed. | Constrained host, request 1. |
| R4 | No independent context is available. Use and label a separated self-review; do not claim a second reader ran. | Constrained host, requests 1–3. |
| R5 | A claimed backup improvement lacks its actual implementation mechanism, which the author cannot supply. Report the missing connection without inventing a cause or removing the protected claim. | Constrained host, request 2. |
| R6 | An ambiguous reference occurs in text the author explicitly prohibits changing or expanding. Report the unresolved stall and constraint conflict without silently changing the text. | Constrained host, request 3. |
| R7 | Three completed FAIL responses identify different defects; earlier defects have been repaired and facts are available. Stop at the round budget with an unresolved result. This is a simulated coordination exercise, not a real cold-reader execution. | Constrained host, request 6. |
| R8 | The user asks for a quick check. If the stage is skipped, disclose that and report zero rounds; do not imply a PASS. | Constrained host, request 4. |
| R9 | A complete clear shopping-list Post needs no change. A fresh reader can pass it without manufactured stalls. | Standalone checklist and router fallback, request 3. |
| R10 | Request 1 has been revised. The count and reader verdict must refer to the final text; illustrative arithmetic must not become a claimed measurement. | Standalone checklist and router fallback, request 1. |
| R11 | The requested draft attachment is absent but publishing-plan information is available. Report the missing text and complete useful independent checks. | Constrained host, request 5. |

A reviewer FAIL is not automatically a failed acceptance case: R1 requires discovery of a real defect, while R5–R7 require an honest unresolved outcome. Acceptance is judged against the expected behavior in this table, not by maximizing PASS labels. The synthetic budget case cannot establish native host scheduling behavior.

The baseline also runs R1's limited cold-reader handoff and R2's plan-only request against the frozen 1.2.0 material. Preserve any sensible compensation by the baseline agent rather than claiming every instruction defect necessarily produced a bad answer.
