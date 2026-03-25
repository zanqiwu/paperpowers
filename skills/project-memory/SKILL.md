---
name: project-memory
description: Use when the user wants continuity across sessions, a stable paper-state artifact, or a compact memory of thesis, risks, evidence, and next actions so work does not restart from zero
---

# Project Memory

Create or update a compact project state artifact for an ongoing paper.

Read:
- `../../references/project-memory.md`
- `../../references/evidence-rules.md`
- `../../docs/paperpowers/templates/current-paper-state.template.md`

## When To Use

Use this skill when:
- the user says they do not want to reload the paper every time
- the same paper is being advanced over many sessions
- advisor-style guidance needs continuity
- the current thesis, risks, and backlog keep shifting across turns

## Workflow

1. Identify the current paper stage.
2. Capture the current thesis and contribution statement.
3. Record the strongest evidence and weakest unresolved risk.
4. Record:
   - nearest prior work
   - active experiment backlog
   - writing backlog
   - next 3 actions
5. Update the decision log if a strategic choice changed.
6. Keep the state compact and reload-friendly.
7. Use the shared template unless the user explicitly asks for another format.
8. Default to Chinese for the saved artifact, while preserving necessary paper terms such as `thesis`, `claim`, `ablation`, `related work`, and `venue` when they are clearer than forced translation.
9. Write natural Simplified Chinese notes that a human can keep maintaining, not literal translated fragments.

## Output Format

Return:
- `Current snapshot`
- `Working contribution statement`
- `Top risks`
- `Current evidence status`
- `Active backlog`
- `Next 3 actions`
- `State artifact path`

## Persistence

Preferred artifact:
- `docs/paperpowers/state/current-paper-state.md`

Write it in a concise, human-readable form:
- tables for stable fields
- short bullets for backlog and risks
- one sentence for thesis
- Chinese by default
- prefer concise, natural Chinese phrasing over mixed-language headings unless the English term is genuinely clearer

If another paper-state artifact already exists, update it instead of creating a parallel one.

## Escalation

Route forward when needed:
- holistic diagnosis -> `paperpowers:academic-expert`
- claim support structure -> `paperpowers:claim-evidence-map`
- literature grounding -> `paperpowers:literature-mapping`
- writing a section -> `paperpowers:interactive-section-writing`
