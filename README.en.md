# PaperPowers

[简体中文说明](./README.md)

`PaperPowers` is a `Codex` skill pack for academic-paper assistance. Its goal is not to "auto-write papers for you", but to turn paper work into a more reliable workflow so the agent does the right kind of work at the right stage.

It borrows the workflow mindset from `superpowers`, but applies it to academic writing: idea shaping, literature search, novelty evaluation, experiment planning, figure planning, reviewer-style draft inspection, interactive section writing, and revision loops.

## What Problems It Solves

Many paper-writing assistants fail not because the model is weak, but because the workflow is weak:

- writing an abstract before the idea is clear
- making novelty claims before checking related papers carefully
- running many experiments without mapping them to the core claims
- drawing many figures that do not carry the story
- treating review comments as equal when some are fatal and some are cosmetic

`PaperPowers` is designed to reduce those failure modes.

## Core Capabilities

- judge the weakest part of a paper like an academic advisor
- enforce metadata verification and abstract-first reading when searching papers
- identify which experiments are necessary versus redundant
- inspect drafts from a reviewer perspective across logic, evidence, experiments, and presentation
- ask targeted questions before drafting a section
- plan figures as communication artifacts, not decoration

## Included Skills

### 1. `paper-triage`

Entry skill. Determines the current paper stage and routes the request to the right skill.

### 2. `academic-expert`

The most important skill in the pack. Acts like a long-term academic advisor and senior reviewer, judging whether the paper is reasonable, whether the claims are supported, whether the experiments are sufficient, and what the highest-value next step should be.

### 3. `idea-brainstorming`

Turns a vague research direction into a clearer paper idea brief.

### 4. `literature-mapping`

Finds, filters, clusters, and compares related work to identify the nearest papers.

### 5. `novelty-stress-test`

Applies a skeptical-reviewer lens to test whether the novelty claim is actually defensible.

### 6. `experiment-design`

Works backward from paper claims to required experiments, while identifying missing and redundant experiments.

### 7. `paper-review`

Reviews a draft, section, outline, experiment story, or rebuttal like a serious reviewer.

### 8. `figure-planning`

Plans what figures the paper should contain and what each figure should communicate.

### 9. `interactive-section-writing`

Uses guided questions to gather missing information before drafting a section.

### 10. `revision-loop`

Turns advisor comments, reviewer comments, or self-review findings into a prioritized revision plan.

## Recommended Workflow

For a paper from scratch:

1. `paper-triage`
2. `academic-expert`
3. `idea-brainstorming`
4. `literature-mapping`
5. `novelty-stress-test`
6. `experiment-design`
7. `figure-planning`
8. `interactive-section-writing`
9. `paper-review`
10. `revision-loop`

If you already have a draft, usually start with:

1. `paper-triage`
2. `academic-expert`
3. `paper-review`
4. `revision-loop`

## Design Principles

- evidence before conclusions
- verify paper metadata and read the abstract before using a paper as key prior work
- diagnose before drafting
- separate paper stages before choosing a workflow
- never invent papers, metrics, results, or citations
- every experiment must map to a claim
- every figure must serve the paper story

## Literature Correctness Rule

`PaperPowers` adds a stricter rule for paper search correctness:

- verify title, authors, year, and venue or archive first
- read at least the abstract before treating a paper as a key comparison
- if the abstract is unavailable, do not use the paper as a novelty blocker or key authority
- if the abstract shows the paper is off-topic, stop using it immediately

This rule is enforced through shared evidence rules and applied in:

- `academic-expert`
- `literature-mapping`
- `paper-review`
- `novelty-stress-test`
- `figure-planning`

## MinerU Cloud Integration

`mineru-cloud` is integrated for PDF reading and structured paper parsing.

Integrated skills:

- `academic-expert`
- `paper-review`
- `literature-mapping`

Typical use cases:

- analyze a paper PDF directly
- analyze a draft PDF directly
- extract abstract, method, experiment sections, figure captions, and document structure

The repository also includes a reusable local integration package:

- [integrations/mineru-cloud/README.md](./integrations/mineru-cloud/README.md)
- [integrations/mineru-cloud/.env.example](./integrations/mineru-cloud/.env.example)
- [integrations/mineru-cloud/mcp.example.json](./integrations/mineru-cloud/mcp.example.json)

Important:

- no API key is stored in the repository
- the real `MINERU_TOKEN` must be configured locally
- the included files are templates only

## Repository Structure

```text
paperpowers/
  INSTALL.md
  README.md
  README.en.md
  TEST_PROMPTS.md
  references/
  skills/
```

## Install For Codex

### Windows

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills" | Out-Null
cmd /c mklink /J "$env:USERPROFILE\.agents\skills\paperpowers" "C:\Users\Admin\paperpowers\skills"
```

### macOS / Linux

```bash
mkdir -p ~/.agents/skills
ln -s /path/to/paperpowers/skills ~/.agents/skills/paperpowers
```

Restart `Codex` after installation.

## Example Prompts

- `Please act as an academic expert and tell me what is currently weakest in this paper.`
- `Find the 5 papers closest to this work.`
- `Which experiments are still missing for this paper?`
- `Review this draft like a serious reviewer.`
- `I do not know how to write the abstract. Ask me questions first.`
- `Help me decide which figures this paper actually needs.`

## Documentation

- [INSTALL.md](./INSTALL.md): installation and integration notes
- [TEST_PROMPTS.md](./TEST_PROMPTS.md): prompts for testing skill triggering
- [integrations/mineru-cloud/README.md](./integrations/mineru-cloud/README.md): MinerU Cloud integration notes

## Status

The current version is already usable as a `Codex` skill pack, but it is still a first structured release and can be extended further:

- Zotero / OpenAlex / Semantic Scholar / arXiv integration
- domain-specific expert personas
- scripted artifact generation

If you are building a Codex-based academic-writing assistant centered on an "academic expert + paper workflow" model, this repository can serve as a practical starting point.
