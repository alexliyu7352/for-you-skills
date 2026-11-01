Read this draft once, from the first sentence to the last, as a first-time reader. Complete nothing on the text's behalf. Return a stall log, then PASS or FAIL. A FAIL must quote each offending sentence verbatim, name its stall class, and state what would fix it. Do not use external facts or other reviewers.

Stall classes:
- Unresolved reference: a pronoun or pointing word ("it", "this", "that one") whose antecedent is not the nearest plausible subject, or can only be found by searching backwards past another subject.
- Unexplained term: a specialized term used before the text has explained it, where the surrounding sentences do not carry its meaning either.
- Broken chain: a sentence whose point depends on a step the text never states — a mechanism with its consequence missing, or a consequence whose reason is missing.

Draft:
Waiting for a build means waiting to see whether your code changes work. In our tests, the median build time fell from 20 minutes to 10 minutes. The median is the middle time when all measured build times are arranged from fastest to slowest. Our tool saves the output of each completed build step. When a step's inputs have not changed, the tool reuses its saved output instead of running that step again. Skipping unchanged steps reduces the work needed to finish a build, so developers wait less before checking their changes. If your builds repeatedly perform steps whose inputs have not changed, try the tool on a test project and compare build times before adopting it.
