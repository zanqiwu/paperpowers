# Claim-Evidence Map

Use this when the paper has multiple claims, experiments, figures, or review findings and the current reasoning is becoming unstable across turns.

## Purpose

Create one stable artifact that answers:

- what the paper is actually claiming
- what evidence already supports each claim
- what evidence is still missing
- which figures or tables carry each claim
- where experiments are duplicated or irrelevant

## Core Objects

For each claim, track:

- claim id
- calibrated claim statement
- claim type
  - performance
  - efficiency
  - robustness
  - interpretability
  - theory
  - systems
- current support status
  - unsupported
  - weakly supported
  - supported
  - oversold

For each evidence item, track:

- evidence id
- artifact type
  - experiment
  - figure
  - table
  - qualitative case
  - error analysis
  - related-work comparison
- linked claim ids
- what it actually establishes
- major caveats

## Mapping Rules

- Every major claim must map to at least one concrete evidence item.
- Every major figure or table should justify its existence by linking to at least one claim.
- If two experiments support the same narrow point with no additional decision value, mark one as redundant.
- If a claim depends on a comparison to prior work, link the specific papers and note whether only the abstract or deeper sections were checked.

## Status Language

Use calibrated language:

- `supported`
- `partially supported`
- `weakly supported`
- `not yet established`
- `oversold relative to evidence`

Avoid:

- `proven`
- `fully validated`
- `obviously better`

unless the evidence clearly justifies it.

## Save Artifact

Preferred path:

- `docs/paperpowers/maps/YYYY-MM-DD-claim-evidence-map.md`
- Template: `docs/paperpowers/templates/claim-evidence-map.template.md`

Suggested sections:

1. paper snapshot
2. claim table
3. evidence table
4. claim-to-evidence links
5. missing evidence
6. redundant evidence
7. figure alignment
8. next highest-value experiments

Prefer short tables over long narrative paragraphs. The map should be readable quickly by both the user and other skills.
Default to Chinese when writing the artifact, but preserve technical paper terms in English where needed for precision.
Prefer natural Simplified Chinese descriptions for claims, evidence summaries, and caveats.
