---
name: related-work-writing
description: Use when the user already has verified related papers and needs them turned into a structured related-work section, citation notes, or grouped comparison bullets without falling into paper-by-paper summaries
---

# Related Work Writing

Turn verified literature into clean related-work prose and citation notes.

Read:
- `../../references/evidence-rules.md`
- `../../references/reference-pipeline.md`

## Preconditions

Only use papers that have:
- verified metadata
- checked abstracts

If the literature set is still weak, go back to:
- `paperpowers:literature-mapping`

## Workflow

1. Start from verified papers, not vague topic names.
2. Cluster papers by method or problem theme.
3. Write one group-level statement per cluster.
4. Position the user's work against the nearest 3-5 papers.
5. Avoid one-paper-one-sentence laundry lists.
6. Flag citation gaps or places where deeper reading is still needed.

## Output Format

Return:
- `Clustered related-work outline`
- `Per-cluster writing bullets`
- `Nearest-neighbor positioning`
- `Citation notes`
- `Draft paragraph(s) if ready`
- `Recommended next skill`

## Persistence

If useful, save to:
- `docs/paperpowers/literature/YYYY-MM-DD-related-work-draft.md`

## Red Flags

- Writing related work from titles only
- Turning the section into a bibliography dump
- Claiming novelty without the nearest-neighbor distinction being explicit
- Mixing background papers with direct competitors
