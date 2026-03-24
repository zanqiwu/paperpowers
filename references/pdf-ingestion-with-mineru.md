# PDF Ingestion With MinerU

Use MinerU Cloud when the user provides a paper PDF URL and you need structured access to the document.

## When To Use

Use MinerU if you need to inspect:
- a full paper PDF
- a draft PDF
- figure captions or table captions
- section headings
- method and experiment details

Typical PaperPowers skills that should use it:
- `academic-expert`
- `paper-review`
- `literature-mapping`

Usually do not use it for:
- pure idea brainstorming
- revision planning without document reading
- writing help when the user already pasted the needed text

## What To Extract

Prefer:
- section structure
- abstract
- introduction
- method summary
- experiment setup
- results discussion
- figure captions
- table captions

## Tool Preference

If available, use MinerU Cloud document parsing before manual PDF guessing.

Preferred pattern:
1. Parse the PDF into markdown or structured output
2. Read only the parts needed for the current question
3. Cite that the judgment is based on parsed PDF content

## Cautions

- Do not claim parsing is perfect
- If equations, tables, or layouts seem ambiguous, say so
- Do not treat parsed text as ground truth if extraction is obviously broken
- If the PDF is not accessible by URL, ask the user for text, a reachable file URL, or another artifact
