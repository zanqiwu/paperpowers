# Project Memory

Use this when the user wants continuity across sessions or when the same paper is discussed repeatedly.

## Purpose

Maintain a compact project state so the agent does not need to reconstruct the paper from scratch every time.

## What To Persist

- project name
- target venue or venue family
- current paper stage
- one-sentence paper thesis
- current contribution statement
- nearest competing papers
- strongest current evidence
- weakest unresolved risk
- must-run experiments
- open writing blockers
- current decision log

## Memory Rules

- Keep memory short enough to reload quickly.
- Persist decisions, not whole conversations.
- Rewrite the state when the paper changes materially.
- Distinguish `accepted working view` from `open question`.
- When prior advice was not followed, record that explicitly instead of silently overwriting history.

## Recommended Artifact

Preferred path:

- `docs/paperpowers/state/current-paper-state.md`

Suggested sections:

1. current snapshot
2. contribution statement
3. top risks
4. evidence status
5. nearest prior work
6. active experiment backlog
7. writing backlog
8. next 3 actions
9. decision log

## Session Start Rule

At the start of substantial work on an existing paper:

1. look for the project state artifact
2. load it before forming a new global judgment
3. update it if the paper has moved

If no state artifact exists and the work is likely to continue over multiple turns, create one.
