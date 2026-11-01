---
name: x-publish-checklist
description: Use when a user asks to review, improve or check an unpublished X.com/Twitter Post, long Post, Article, Thread or publishing plan before posting, including its opening, length, images, links, reader usefulness and a fresh-reader review.
---

# Review before publishing

For a new natural-language request, use `x-assistant` first when installed. If this workflow was explicitly selected, delegated with `routed_by: x-assistant`, or installed alone, execute directly; do not route back.

This is a full evidence-based draft review, including concrete edits. Use [the evidence guide](references/knowledge-guide.md); screen every topic, then evaluate all applicable entries. Answer in the user's language. General algorithm questions belong to the explanation workflow, not a forced draft audit.

## Review

1. Read the full supplied draft and media. Identify format, target reader and intended result from the material. Keep Article title, introduction/carrier and body separate; review each Thread part. Missing media is not a reason to skip a media recommendation.
2. Quote the actual title and opening lines. Explain whether they establish the reader's problem, a concrete finding and a reason to continue, and whether the body fulfills the promise. Provide a usable replacement or a specific reason to retain the opening. Hook quality is an editorial judgment, not a code-mandated phrase pattern.
3. Measure complete text with `python3 scripts/inspect_draft.py --text draft.txt` when Python is available; otherwise follow the evidence guide's measurement fallback. State the counting scope and unit. Inspect where the central finding and qualifying conditions fall, including the relevant first-4000-character preview. Do not impose a universal 4000-character limit or add filler to meet a threshold. If only an excerpt is supplied, measure that excerpt and label it.
4. Inspect supplied images. If no images are supplied, decide whether evidence, comparisons, steps or a checklist would help this actual draft. Give specific image content and required source material. When multiple images help, specify their order and purpose: the first should independently convey the most useful supported finding and its key conditions; subsequent images add evidence or instructions. A text-only recommendation needs a material-specific reason. Explain the relevant image-expansion prediction and media-selection path accurately; uploading a picture is not a guaranteed fixed score increase.
5. When images would help, use [the visual workflow](references/visual-workflow.md) to discover available creation options. Explicitly mention native generation if available and offer a concrete next step. Record the draft, ordered image purpose/content, sources and existing assets as `visual_brief`. If creation was requested, hand it to `x-create-visuals` with retained context, or execute the bundled visual workflow directly when installed alone. A review-only request stops at the offer; ask/save style preferences when creation or style setup begins.
6. Evaluate every other applicable rule: evidence/reading payoff, share/save usefulness, format, video conditions, links and pinned destinations, duplication, replies/interaction, labels/hashtags, correction plan and performance comparison. For each keep actual evidence, verdict, concrete action or retention reason, explanation and original citation. Mark unavailable internal states as missing.
7. Fact-check news claims against necessary primary sources. This supports the review; it does not replace opening, length, media and publishing checks. Preserve unique evidence and the author's voice. Do not label every controversial word as a known platform penalty.

## Reader review

The evidence review above checks the draft against the corpus. It does not establish that a first-time reader can follow the text. Whoever produced a draft — a person or a model — silently supplies whatever the text left out: a missing subject, antecedent or connective reads as complete to its author and broken to a new reader. Run this stage after the evidence review and before delivery. Run it by default on a full review; if the user asked only for a quick check, this stage may be skipped, but the delivery must state that it was skipped. Everything in this stage is editorial judgment, not algorithm evidence; do not cite knowledge entries as authority for a readability verdict.

1. **Pure read first.** Read the finished draft from the first sentence to the last, in order, without consulting your notes, the review above, or any statement of what the draft intends. Complete nothing on the text's behalf. Write down every stall — each place a reader must re-read, look back, or guess — as a stall log kept with the review. Three standing stall classes, defined by cause:
   - *Unresolved reference:* a pronoun or pointing word ("it", "this", "that one") whose antecedent is not the nearest plausible subject, or can only be found by searching backwards past another subject.
   - *Unexplained term:* a specialized term used before the text has explained it, where the surrounding sentences do not carry its meaning either (the standard in step 3 applies).
   - *Broken chain:* a sentence whose point depends on a step the text never states — a mechanism with its consequence missing, or a consequence whose reason is missing.
   No stall log, no claim that the draft was read through. A checklist pass is not a read.
2. **Cold review by a fresh reader.** Where the host supports a separate agent or a fresh context, hand the draft to a reviewer who did not write it. Give that reviewer only the draft, the three stall classes above, and any model paragraphs the author supplied. Never give it your notes, your verdicts, or what the draft was meant to say; a reviewer shown the intent becomes another author. The reviewer pure-reads first and returns its stall log, then applies step 3 and returns PASS or FAIL. A FAIL must quote each offending sentence verbatim, name its stall class, and state what would fix it; it may only fail the draft on quoted text, never on a general impression. Revise, then resubmit the complete revised draft to a fresh cold review. Loop until PASS. If no fresh-context reviewer is available, do a separated second pass yourself — after other work, from the text alone — and label it in the delivery as self-review, not cold review. Never present a self-review as a cold review.
3. **The no-compression standard.** Both passes judge the draft against three requirements:
   - Every central mechanism or finding states what it means for the reader: who is affected, what changes for them, and what they should do or stop doing. A fact whose consequence the reader must infer for themselves is unfinished.
   - Every specialized term meets one of three conditions at its first use: a plain explanation in place, an explanation earlier in the text, or an everyday example that does the term's job. A term the whole piece depends on is explained once, early; where a number is involved, the explanation includes a worked example. A term meeting none of the three is a defect.
   - No causal step is skipped. Between "X does A" and "so B follows", every intermediate step the conclusion needs is on the page. Test each consequence by asking why it follows; if the answer is not in the text, the step is missing.
   Compression is the default failure of generated text. The scaffolding that lets a reader follow — restated context, spelled-out connectives, a consequence stated after its mechanism — is not padding, and it is not cut in the name of brevity.

## Deliver

Lead with the changes most consequential for this draft, then explain all applicable findings, including strengths worth retaining. Supply measured length, a usable opening, a concrete image plan and a justified format/publishing arrangement. Summarize inapplicable topics and precise evidence gaps. Group overlapping rules without losing their citations.

Report the reader-review outcome with the review: cold review PASS and the number of rounds, or the self-review label where no fresh reviewer was available, plus the stall classes found and how each was resolved. If the stage was skipped for a quick check, state that instead.

“Review this” requests an audit plus necessary local edits. A requested rewrite or introductory Post requires complete copy. An Article introduction should quickly convey what can be concluded, what remains unresolved and what the reader can do; detailed proof belongs in the Article. Keep proposed copy separate from commentary. Never publish automatically or claim to have edited a live post.
