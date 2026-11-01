**Stall log**

1. **Unexplained term — incomplete numerical explanation**

   > In our tests, the median build time fell from 20 minutes to 10 minutes.
   >
   > The median is the middle time when all measured build times are arranged from fastest to slowest.

   The adjacent definition explains “median” verbally, but no worked numerical example shows how measured build times produce a median. The reported 20-minute and 10-minute medians are results, not a worked example. This leaves the numerical explanation incomplete under the supplied rubric.

   **Required fix:** Include a clearly labelled illustrative example that orders several build times and identifies their middle value. Keep it separate from the author’s test results.

No other unresolved stalls found.

**Rubric checks**

1. **Reader meaning and action — PASS.** The paragraph identifies developers as the affected readers, explains that they wait less before checking their changes, and tells readers with repeated unchanged inputs to test the tool and compare build times before adopting it.

2. **Specialized terms and worked examples — FAIL.** “Median” receives an early plain-language definition, but the required worked numerical example is missing. The mechanism’s other terms are understandable for the supplied developer audience.

3. **Complete causal chain — PASS.** The paragraph states that the tool saves completed steps’ outputs, reuses those outputs when inputs remain unchanged, avoids rerunning those steps, reduces the work needed, and consequently reduces developers’ waiting time.

**FAIL for the complete supplied paragraph.** The missing worked numerical example is the sole identified defect.
