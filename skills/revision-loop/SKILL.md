---
name: revision-loop
description: Use when the user has review feedback, self-review findings, advisor comments, or rebuttal concerns and needs a structured revision plan for a paper
---

# Revision Loop

Turn criticism into a prioritized revision plan.

Read `../../references/review-rubric.md` and `../../references/evidence-rules.md` before revising.

## Inputs

- Draft or section under revision
- Review comments or findings
- Experiment constraints
- Submission timeline if relevant

## Workflow

1. Normalize all feedback into discrete issues.
2. Merge duplicates.
3. Label each issue:
   - claim problem
   - evidence problem
   - novelty problem
   - writing problem
   - figure problem
4. Prioritize:
   - must fix before submission
   - should fix if time allows
   - acknowledge but do not overreact
5. Produce a revision plan.
6. After changes, re-run `paperpowers:paper-review` on the updated artifact.

## Output Format

Return:
- `Normalized issue list`
- `Priority buckets`
- `Revision tasks`
- `Evidence still missing`
- `Recommended follow-up skill`

## Save Artifact

If useful, save to:
- `docs/paperpowers/revisions/YYYY-MM-DD-revision-plan.md`

## Red Flags

- Revising wording while leaving the main evidence gap unresolved
- Expanding scope dramatically late in the cycle
- Treating all comments as equally important
- Defending claims that the data cannot support
