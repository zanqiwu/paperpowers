# Experiment Checklist

Use this checklist when deciding what to run or when reviewing whether the paper already has enough evidence.

## Claim-To-Evidence Matrix

For each claim, write:
- claim
- strongest direct evidence
- indirect supporting evidence
- what could falsify it
- whether the current evidence is enough

## Main Evaluation Checks

- Strong baselines included
- Baselines configured fairly
- Metrics aligned with the task
- Dataset splits and preprocessing described
- Statistical treatment appropriate if variance matters
- Compute, latency, or memory included if efficiency is a claim

## Common Missing Pieces

- Best relevant baseline missing
- Ablation missing for the main design choice
- Sensitivity study missing for a claimed robustness point
- Error analysis missing when interpretation matters
- Qualitative examples shown without evaluation purpose

## Duplication Checks

Mark an experiment redundant if it only:
- repeats the same claim on near-identical settings
- adds another metric without changing interpretation
- adds another baseline that is clearly dominated and not standard
- produces another figure for the same conclusion

## Prioritization

- `Required`: needed to defend the main paper claims
- `Helpful`: strengthens interpretation or completeness
- `Optional`: nice to have but not decision-changing
