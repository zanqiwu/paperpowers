---
name: claim-evidence-map
description: Use when a paper has multiple claims, experiments, figures, or review findings and the user needs a stable claim-to-evidence map instead of re-deriving support status every session
---

# Claim Evidence Map

Build and maintain a stable map between paper claims and the evidence that supports or fails to support them.

Read:
- `../../references/evidence-rules.md`
- `../../references/claim-evidence-map.md`
- `../../references/experiment-checklist.md`

## When To Use

Use this skill when:
- the paper has several claims and the support picture is getting unclear
- experiments exist but it is not obvious what each one proves
- figures and tables feel disconnected from the main story
- the user keeps re-asking what is missing
- review comments suggest evidence gaps or oversold claims

## Workflow

1. Enumerate the paper's claims.
2. Normalize each claim into calibrated language.
3. Inventory current evidence:
   - experiments
   - figures
   - tables
   - qualitative cases
   - error analyses
   - prior-work comparisons
4. Map evidence to claims.
5. Label each claim:
   - unsupported
   - weakly supported
   - supported
   - oversold
6. Identify:
   - missing evidence
   - redundant evidence
   - figures with no real job
7. Recommend the smallest next evidence set that changes the decision quality.

## Output Format

Return:
- `Paper thesis`
- `Claim table`
- `Evidence table`
- `Missing links`
- `Redundant support`
- `Highest-value next evidence`
- `Recommended next skill`

## Persistence

If the work is likely to continue, save or update:
- `docs/paperpowers/maps/YYYY-MM-DD-claim-evidence-map.md`

## Escalation

Route forward when needed:
- experiment gaps -> `paperpowers:experiment-design`
- paper-level strategy -> `paperpowers:academic-expert`
- draft-level critique -> `paperpowers:paper-review`
- revision planning -> `paperpowers:revision-loop`
