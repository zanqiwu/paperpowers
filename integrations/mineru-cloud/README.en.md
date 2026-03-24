# MinerU Cloud Integration

[简体中文说明](./README.md)

This directory contains an in-repository `mineru-cloud` integration. It includes both configuration templates and the wrapped MCP source code, so `PaperPowers` users can maintain and run it without committing API keys into the repository.

## What This Integration Provides

- an environment-variable template without real secrets
- a generic MCP configuration example
- the wrapped `mineru-cloud` source package
- instructions for setting `MINERU_TOKEN`
- guidance on which `PaperPowers` skills use `mineru-cloud`

## Relevant Skills

These skills currently use `mineru-cloud`:

- `academic-expert`
- `paper-review`
- `literature-mapping`

## Do Not Commit Secrets

Do not commit any real token values.

The repository should only contain template files such as:

- `.env.example`
- `mcp.example.json`
- `mcp.uvx.example.json`

## Dependency Notes

The bundled source package is `mcp-server-mineru-bach`, with the following defaults:

- default API base URL: `https://mineru.net/api/v4`
- required env var: `MINERU_TOKEN`
- optional env vars:
  - `MINERU_BASE_URL`
  - `MINERU_OUTPUT_DIR`
  - `MINERU_TMP_DIR`

## Quick Start

### 1. Prepare environment variables

Use the template:

```text
integrations/mineru-cloud/.env.example
```

### 2. Windows example

```powershell
setx MINERU_TOKEN "your_real_token_here"
setx MINERU_BASE_URL "https://mineru.net/api/v4"
```

### 3. macOS / Linux example

```bash
export MINERU_TOKEN="your_real_token_here"
export MINERU_BASE_URL="https://mineru.net/api/v4"
```

### 4. MCP configuration

Prefer the local-source example:

```text
integrations/mineru-cloud/mcp.example.json
```

If you want to run the published package instead, see:

```text
integrations/mineru-cloud/mcp.uvx.example.json
```

## Directory Contents

- `.env.example`
- `mcp.example.json`
- `mcp.uvx.example.json`
- `source/`
