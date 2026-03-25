---
name: literature-mapping
description: Use when the user needs related papers, citation support, nearest-neighbor comparisons, paper clustering, or a structured understanding of prior work for a paper
---

# Literature Mapping

Find and organize the papers that matter to the current research claim.

Read `../../references/evidence-rules.md` before heavy literature work.
Read `../../references/pdf-ingestion-with-mineru.md` when the user provides paper PDFs to inspect directly.
Read `../../references/reference-pipeline.md` when building a literature set that will feed novelty or writing.

## Preferred Sources

Use, in order:
1. Local paper library or Zotero MCP if available
2. Primary paper sources such as arXiv, ACL Anthology, OpenReview, CVF, PMLR, journal pages
3. Scholarly indexes such as OpenAlex or Semantic Scholar for discovery

Never rely on an unverified secondary summary when the paper itself is available.

## Workflow

1. Define the search target:
   - task
   - method family
   - modality
   - benchmark or setting
   - time window
2. Retrieve a candidate set.
3. Verify each candidate before using it:
   - title
   - authors or first author
   - venue or archive
   - year
   - abstract
4. Eliminate off-topic candidates after reading the abstract.
5. Read enough of the strongest remaining papers to compare them accurately:
   - abstract
   - method contribution
   - experiment setup
   - if a PDF URL is available, parse it with MinerU first
6. Cluster the papers by theme, not by title similarity.
7. Identify the 3-5 nearest neighbors to the user's idea.
8. State what gap is real, weak, or unsupported.
9. If the user needs prose rather than search output, route to `paperpowers:related-work-writing`.

## Output Format

Return:
- `Nearest papers`
- `Cluster map`
- `Comparison table`
- `Citation gaps`
- `Writing handoff`
- `Recommended next skill`

For each important paper, include:
- citation metadata
- whether the abstract was checked
- what it contributes
- why it is near or not near the user's work
- what evidence is still needed

## Save Artifact

If useful, save to:
- `docs/paperpowers/literature/YYYY-MM-DD-topic-map.md`

## Red Flags

- Invented citations
- Using papers whose abstract you did not read
- Comparing only titles
- Calling a gap "novelty" when it is merely an untested variant
- Ignoring the most recent strong baselines
