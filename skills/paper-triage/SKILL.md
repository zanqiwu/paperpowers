---
name: paper-triage
description: Use when starting any academic-paper conversation, or when the user asks for help on ideas, literature, experiments, figures, draft quality, or revisions
---

# Paper Triage

Route academic-paper work into the right workflow before producing substantial content.

## Use This Skill To Classify The Task

Before doing real work, identify:
- The paper stage: idea, literature review, experiment design, drafting, figure design, review, or revision
- The main artifact available: note, outline, draft, PDF, reviews, code, or experiment logs
- The main blocker: novelty, evidence, writing, structure, figures, or reviewer response

Then use the matching skill:
- Need a senior academic expert to evaluate reasonableness, claims, experiments, and writing direction end-to-end -> `paperpowers:academic-expert`
- Raw or underdefined idea -> `paperpowers:idea-brainstorming`
- Need related work, citations, or paper clustering -> `paperpowers:literature-mapping`
- Need to pressure-test novelty -> `paperpowers:novelty-stress-test`
- Need experiment recommendations or gap analysis -> `paperpowers:experiment-design`
- Need reviewer-style critique of a draft -> `paperpowers:paper-review`
- Need figure choices or figure briefs -> `paperpowers:figure-planning`
- User is stuck writing a section -> `paperpowers:interactive-section-writing`
- Need to respond to feedback and revise -> `paperpowers:revision-loop`

If the request spans multiple stages, handle them in this order:
1. Clarify stage and artifacts
2. Academic-expert diagnosis if the user needs holistic guidance
3. Literature and novelty
4. Experiments and figures
5. Drafting
6. Review and revision

## Non-Negotiables

- Do not invent papers, citations, metrics, datasets, or results.
- Do not claim novelty without comparing against nearest existing work.
- Do not suggest experiments without naming which claim they validate.
- Do not draft result text when results are missing.
- Do not collapse review, writing, and literature work into one vague response.

## Working Style

- If the user is vague, ask one short clarifying question that determines the next skill.
- Prefer artifact-based work over chat-memory-based work.
- If a local draft exists, read it before judging it.
- If the task needs current papers, use the web or an available literature MCP and rely on primary sources.

## Recommended Artifacts

When useful, save outputs under:
- `docs/paperpowers/ideas/`
- `docs/paperpowers/literature/`
- `docs/paperpowers/experiments/`
- `docs/paperpowers/figures/`
- `docs/paperpowers/reviews/`
- `docs/paperpowers/revisions/`

## Output Contract

Start by stating:
- Current stage
- Missing inputs
- Next skill you are using

Then follow that skill exactly.
