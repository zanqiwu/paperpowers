# MCP

这个目录用于统一放置 `paperpowers` 相关的 MCP 工具源码，目标是让仓库结构更清晰，也便于后续继续扩展更多 MCP 工具。

## 当前包含

- `mineru-cloud`
  - 用于调用 MinerU Cloud API 解析论文 PDF 和其他远程文档

## 当前与哪些 skills 配合

- `academic-expert`
- `paper-review`
- `literature-mapping`

## 目录约定

- 一个 MCP 工具一个子目录
- 子目录中优先只保留源码和最小运行说明
- 密钥不写入仓库

## MinerU Cloud 运行方式

推荐在 MCP 客户端中把命令指向仓库内源码：

```json
{
  "mcpServers": {
    "mineru-cloud": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/paperpowers/mcp/mineru-cloud",
        "run",
        "mcp-server-mineru-bach"
      ],
      "env": {
        "MINERU_TOKEN": "${MINERU_TOKEN}",
        "MINERU_BASE_URL": "${MINERU_BASE_URL}"
      }
    }
  }
}
```

## 环境变量

- `MINERU_TOKEN`
- `MINERU_BASE_URL`
  - 默认：`https://mineru.net/api/v4`
