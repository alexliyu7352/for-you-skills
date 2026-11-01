---
name: x-publish-checklist
description: Use when a user asks to review, improve or check an unpublished X.com/Twitter Post, long Post, Article, Thread or publishing plan before posting, including its opening, length, images, links and reader usefulness.
---

# Review before publishing

For a new natural-language request, use `x-assistant` first when installed. If this workflow was explicitly selected, delegated with `routed_by: x-assistant`, or installed alone, execute directly; do not route back.

This is a full evidence-based draft review, including concrete edits. Use [the evidence guide](../knowledge-guide.md); screen every topic, then evaluate all applicable entries. Answer in the user's language. General algorithm questions belong to the explanation workflow, not a forced draft audit.

## Review

1. Read the full supplied draft and media. Identify format, target reader and intended result from the material. Keep Article title, introduction/carrier and body separate; review each Thread part. Missing media is not a reason to skip a media recommendation.
2. Quote the actual title and opening lines. Explain whether they establish the reader's problem, a concrete finding and a reason to continue, and whether the body fulfills the promise. Provide a usable replacement or a specific reason to retain the opening. Hook quality is an editorial judgment, not a code-mandated phrase pattern.
3. Measure complete text with `python3 scripts/inspect_draft.py --text draft.txt` when Python is available; otherwise follow the evidence guide's measurement fallback. State the counting scope and unit. Inspect where the central finding and qualifying conditions fall, including the relevant first-4000-character preview. Do not impose a universal 4000-character limit or add filler to meet a threshold. If only an excerpt is supplied, measure that excerpt and label it.
4. Inspect supplied images. If no images are supplied, decide whether evidence, comparisons, steps or a checklist would help this actual draft. Give specific image content and required source material. When multiple images help, specify their order and purpose: the first should independently convey the most useful supported finding and its key conditions; subsequent images add evidence or instructions. A text-only recommendation needs a material-specific reason. Explain the relevant image-expansion prediction and media-selection path accurately; uploading a picture is not a guaranteed fixed score increase.
5. When images would help, use [the visual workflow](../visual-workflow.md) to discover available creation options. Explicitly mention native generation if available and offer a concrete next step. Record the draft, ordered image purpose/content, sources and existing assets as `visual_brief`. If creation was requested, hand it to `x-create-visuals` with retained context, or execute the bundled visual workflow directly when installed alone. A review-only request stops at the offer; ask/save style preferences when creation or style setup begins.
6. Evaluate every other applicable rule: evidence/reading payoff, share/save usefulness, format, video conditions, links and pinned destinations, duplication, replies/interaction, labels/hashtags, correction plan and performance comparison. For each keep actual evidence, verdict, concrete action or retention reason, explanation and original citation. Mark unavailable internal states as missing.
7. Fact-check news claims against necessary primary sources. This supports the review; it does not replace opening, length, media and publishing checks. Preserve unique evidence and the author's voice. Do not label every controversial word as a known platform penalty.

## Deliver

Lead with the changes most consequential for this draft, then explain all applicable findings, including strengths worth retaining. Supply measured length, a usable opening, a concrete image plan and a justified format/publishing arrangement. Summarize inapplicable topics and precise evidence gaps. Group overlapping rules without losing their citations.

“Review this” requests an audit plus necessary local edits. A requested rewrite or introductory Post requires complete copy. An Article introduction should quickly convey what can be concluded, what remains unresolved and what the reader can do; detailed proof belongs in the Article. Keep proposed copy separate from commentary. Never publish automatically or claim to have edited a live post.
