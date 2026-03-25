# PaperPowers

[简体中文说明](./README.md)

`PaperPowers` is a `Codex` skill pack for academic-paper assistance. Its goal is not to "auto-write papers for you", but to turn paper work into a more reliable workflow so the agent does the right kind of work at the right stage.

It borrows the workflow mindset from `superpowers`, but applies it to academic writing: idea shaping, literature search, novelty evaluation, experiment planning, figure planning, reviewer-style draft inspection, interactive section writing, and revision loops.

## Core Capabilities

- judge the weakest part of a paper like an academic advisor
- enforce metadata verification and abstract-first reading when searching papers
- identify which experiments are necessary versus redundant
- inspect drafts from a reviewer perspective across logic, evidence, experiments, and presentation
- ask targeted questions before drafting a section
- plan figures as communication artifacts, not decoration

## Literature Correctness Rule

`PaperPowers` adds a stricter rule for paper search correctness:

- verify title, authors, year, and venue or archive first
- read at least the abstract before treating a paper as a key comparison
- if the abstract is unavailable, do not use the paper as a novelty blocker or key authority
- if the abstract shows the paper is off-topic, stop using it immediately

## MCP Directory

All MCP tools are grouped under `mcp/`.

Current entries:

- [mcp/README.md](./mcp/README.md)
- [mcp/mineru-cloud/README.md](./mcp/mineru-cloud/README.md)
- [mcp/zotero/README.md](./mcp/zotero/README.md)

`mineru-cloud` is used for PDF reading and structured paper parsing.

The Zotero path now points directly to the upstream project `kujenga/zotero-mcp` instead of maintaining a parallel local implementation inside `paperpowers`.

## Documentation

- [INSTALL.md](./INSTALL.md): installation and integration notes
- [TEST_PROMPTS.md](./TEST_PROMPTS.md): prompts for testing skill triggering
- [mcp/README.md](./mcp/README.md): MCP directory notes
- [mcp/mineru-cloud/README.md](./mcp/mineru-cloud/README.md): MinerU Cloud source notes
- [mcp/zotero/README.md](./mcp/zotero/README.md): Zotero MCP upstream integration notes
