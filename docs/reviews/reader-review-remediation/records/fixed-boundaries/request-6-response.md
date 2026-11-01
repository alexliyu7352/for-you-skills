**Simulation only — no actual reviewer or draft evaluation was run.**

The coordinator stops the review cycle after the third completed FAIL and returns **`unresolved`, with `3` completed reviewer passes in the simulation**. The default limit is three completed passes total, including the first. Different defects and successful earlier repairs do not restart or extend that budget.

| Simulated pass | Simulated reviewed version | Assumed result | Coordinator action |
| --- | --- | --- | --- |
| 1 | V1, complete original draft | FAIL: undefined term | Repair the term; create V2. One pass used. |
| 2 | V2, complete revised draft | FAIL: missing reader consequence | Repair the consequence; create V3. Two passes used. |
| 3 | V3, complete revised draft | FAIL: ambiguous reference | Record the remaining ambiguity and stop at the three-pass limit. V3 is the last reviewed version and it failed. |

The resulting simulated record is **status `unresolved`; completed rounds `3`; reviewed_scope: the complete hypothetical V3 draft**. In this host, any hypothetical formal pass would use the labeled self-review fallback because fresh-context review is unavailable. This statement describes the simulation, not work performed.

The next action would be to report the remaining ambiguous reference and the precise clarification it needs. In a real review, that report must quote the offending sentence verbatim. This fixture supplies no sentence, so no quotation can honestly be provided. Naming the intended antecedent would be the repair. If that repair were made to create V4, V4 would be unreviewed and the delivery would still be `unresolved`, with three completed passes. An explicit user instruction increasing the budget would be required for another formal pass.

Actual execution record: **mode `none`; actual reviewer passes `0`; scope: procedure simulation only**. No real readability verdict, actual quoted stall, or PASS is claimed.
