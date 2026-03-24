---
name: paper-review
description: Use when reviewing a paper draft, outline, section, rebuttal, or experiment story for technical soundness, evidence sufficiency, novelty, structure, and writing quality
---

# Paper Review

Review the paper like a serious reviewer, not a supportive coauthor.

Read `../../references/review-rubric.md` before reviewing.
Read `../../references/pdf-ingestion-with-mineru.md` when the review target is a PDF document.

## Scope

You may review:
- idea brief
- outline
- full draft
- single section
- rebuttal draft
- figure plan
- experiment section

If the review target is a PDF URL, extract its structure with MinerU before reviewing.

If your review comments depend on comparisons to prior papers, verify those papers' metadata and read at least their abstracts first.

## Review Order

Evaluate in this order:
1. Problem and contribution clarity
2. Technical correctness
3. Evidence sufficiency
4. Experimental design and fairness
5. Related work positioning
6. Figure and table usefulness
7. Writing clarity

## Findings Format

Findings come first. Do not start with praise.

For each finding include:
- severity: `Critical`, `Important`, or `Minor`
- location: section, paragraph, file, or figure if available
- issue
- why it matters
- precise fix direction

Group findings under:
- `Logic`
- `Novelty`
- `Evidence`
- `Experiments`
- `Presentation`

## Review Personas

If the draft is substantial, you may simulate these lenses sequentially:
- domain expert
- experimentalist
- skeptical reviewer
- writing editor

Keep the roles separate in the output.

## Save Artifact

If useful, save to:
- `docs/paperpowers/reviews/YYYY-MM-DD-draft-review.md`

## Red Flags

- Rewriting the paper before stating what is wrong
- Mixing technical flaws with style nitpicks
- Calling a paper strong when the evidence is incomplete
- Suggesting new claims instead of fixing the existing story
- Criticizing the draft based on a prior paper whose abstract you did not verify
