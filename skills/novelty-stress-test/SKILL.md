---
name: novelty-stress-test
description: Use when the user wants to know whether a paper idea is actually novel, defensible, and reviewer-resistant after identifying related work
---

# Novelty Stress Test

Treat the current idea as if you are a skeptical reviewer looking for reasons to reject it.

Read `../../references/evidence-rules.md` before making novelty claims.

## Inputs You Need

- Current idea brief or draft summary
- The 3-5 nearest related papers
- Claimed contributions
- Available or planned evidence

If these are missing, gather them first or invoke `paperpowers:literature-mapping`.

You must not evaluate novelty against papers whose metadata and abstracts have not been verified.

## Review Questions

- What exactly is the delta from nearest prior work?
- Is the delta conceptual, empirical, systems-level, or merely implementation detail?
- Would a reviewer see this as a paper or as an ablation?
- What claim can be defended with available evidence?
- Which claim is too strong and should be downgraded?

## Output Contract

Return:
- `Defendable novelty claim`
- `Nearest-neighbor rebuttal table`
- `Likely reviewer attacks`
- `Claims to avoid`
- `Minimum evidence needed`

Use direct language:
- `Strong`
- `Borderline`
- `Weak`
- `Not novel as stated`

## Red Flags

- Claiming novelty before nearest-neighbor comparison
- Using title-only matches as novelty blockers
- Using broad statements like "unexplored" without evidence
- Counting engineering effort as scientific novelty
- Hiding a weak idea behind inflated writing
