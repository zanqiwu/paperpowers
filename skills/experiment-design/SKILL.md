---
name: experiment-design
description: Use when the user needs to determine which experiments are necessary, redundant, missing, or most valuable to support a paper's claims
---

# Experiment Design

Design experiments by working backward from claims.

Read `../../references/experiment-checklist.md` and `../../references/venue-expectations.md` before finalizing the plan.

## Core Rule

Every proposed experiment must map to a specific claim.

If a proposed experiment does not strengthen, falsify, or bound a claim, label it optional or remove it.

## Workflow

1. List the paper's claims.
2. For each claim, identify the minimum evidence required.
3. Check whether the user already has equivalent evidence.
4. Detect duplicated or low-yield experiments.
5. Produce a prioritized experiment matrix.

## Typical Experiment Buckets

- Main comparison against strongest baselines
- Ablation or component analysis
- Sensitivity or robustness
- Efficiency or scaling
- Qualitative analysis
- Error analysis
- Generalization or transfer

Not every paper needs every bucket. Use venue and claim strength to decide.

## Output Format

Return:
- `Claim-to-evidence matrix`
- `Required experiments`
- `Optional experiments`
- `Redundant experiments`
- `Execution order`
- `Figure opportunities`

For each experiment, include:
- goal
- exact claim it validates
- expected outcome
- failure interpretation
- dependencies

## Save Artifact

If useful, save to:
- `docs/paperpowers/experiments/YYYY-MM-DD-topic-plan.md`

## Red Flags

- Recommending fashionable but irrelevant analyses
- Adding more baselines without checking fairness and relevance
- Repeating the same point across multiple tables
- Suggesting experiments the user cannot run in time
