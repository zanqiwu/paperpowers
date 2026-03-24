---
name: interactive-section-writing
description: Use when the user knows what section they need but does not know how to write it, wants guided questions, or needs a section skeleton grounded in actual evidence
---

# Interactive Section Writing

Help the user write by extracting missing information first, then drafting.

Read `../../references/evidence-rules.md` before writing technical content.

## Core Rule

When evidence is missing, ask for it. Do not fill the gap with confident prose.

## Workflow

1. Identify the target section:
   - title
   - abstract
   - introduction
   - related work
   - method
   - experiments
   - limitations
   - rebuttal
2. Ask one focused question at a time until the section can be written honestly.
3. Build a section skeleton.
4. Draft only after the skeleton and evidence are adequate.
5. Offer one tighter revision pass if needed.

## Section-Specific Guidance

- `Abstract`: problem, gap, method, evidence, result, impact
- `Introduction`: context, gap, stakes, idea, contributions
- `Related work`: clusters, nearest neighbors, distinction
- `Method`: assumptions, setup, components, rationale
- `Experiments`: setup, baselines, metrics, headline findings, interpretation
- `Rebuttal`: acknowledge concern, give evidence, commit to clarification

## Output Format

Return one of these based on readiness:
- `Questions needed first`
- `Section skeleton`
- `Draft paragraph(s)`
- `Revision suggestions`

## Red Flags

- Writing result claims without numbers
- Writing related work without citations
- Writing contributions before the gap is clear
- Asking five questions at once
