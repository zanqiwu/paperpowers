# MCP

这个目录用于统一放置 `paperpowers` 相关的 MCP 工具说明与源码。

## 当前包含

- `mineru-cloud`
  - 用于调用 MinerU Cloud API 解析论文 PDF
  - 仓库内直接保留源码
- `zotero`
  - 直接接入上游 `kujenga/zotero-mcp`
  - 本仓库只保留接入说明，不维护本地副本

## 当前与哪些 skills 配合

- `academic-expert`
- `paper-review`
- `literature-mapping`

## MinerU Cloud 运行方式

```json
{
  "mcpServers": {
    "mineru-cloud": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/paperpowers/mcp/mineru-cloud",
        "run",
        "python",
        "server.py"
      ],
      "env": {
        "MINERU_TOKEN": "${MINERU_TOKEN}",
        "MINERU_BASE_URL": "${MINERU_BASE_URL}"
      }
    }
  }
}
```
