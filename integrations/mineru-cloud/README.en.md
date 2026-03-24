# MinerU Cloud Integration

[简体中文说明](./README.md)

This directory contains a reusable in-repository integration package for `mineru-cloud`, so `PaperPowers` users can safely enable paper PDF parsing without committing API keys into the repository.

## What This Integration Provides

- an environment-variable template without real secrets
- a generic MCP configuration example
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

Real configuration should live in local environment variables or in your own local untracked config files.

## Dependency Notes

Based on the `mcp-server-mineru-bach` PyPI page, as checked on `2026-03-24`:

- launcher: `uvx mcp-server-mineru-bach`
- required env var: `MINERU_TOKEN`
- optional env var: `MINERU_BASE_URL`

Source:
- https://pypi.org/project/mcp-server-mineru-bach/

## Quick Start

### 1. Prepare environment variables

Use the template:

```text
integrations/mineru-cloud/.env.example
```

You can keep the real values in system environment variables instead of editing the template file.

### 2. Windows example

PowerShell:

```powershell
setx MINERU_TOKEN "your_real_token_here"
setx MINERU_BASE_URL "https://api.mineru.net/v1"
```

Reopen your terminal after setting them.

### 3. macOS / Linux example

```bash
export MINERU_TOKEN="your_real_token_here"
export MINERU_BASE_URL="https://api.mineru.net/v1"
```

If you want persistence, add them to:

- `~/.bashrc`
- `~/.zshrc`
- or your preferred shell config

### 4. MCP configuration

See:

```text
integrations/mineru-cloud/mcp.example.json
```

This is a generic MCP example. Different clients may use different config paths and loading conventions, so you should merge the `mineru-cloud` block into your own client config.

## Directory Contents

- `.env.example`
  - environment template, no real secret
- `mcp.example.json`
  - generic MCP configuration example

## Recommended Practice

- store `MINERU_TOKEN` in system environment variables
- do not create a tracked `.env` with real secrets
- if you need local file-based config, keep it untracked

## How It Relates To PaperPowers

`PaperPowers` only declares `mineru-cloud` as a dependency at the skill layer. It does not hardcode API keys into skill files.

That keeps the repository:

- safer for public publishing
- reusable across users
- easier to configure with each user's own MinerU account and token
