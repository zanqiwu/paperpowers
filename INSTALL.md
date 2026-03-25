# PaperPowers 安装教程

这份文档面向第一次使用的人，按“从零开始”的方式说明如何安装：

1. `PaperPowers`
2. `mineru-cloud`
3. `Codex` 中的本地 skill 发现

如果你只是想看仓库功能，请先看 [README.md](./README.md)。

## 第 1 步：获取仓库

```bash
git clone https://github.com/zanqiwu/paperpowers.git
```

## 第 2 步：让 Codex 发现 skills

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

## 第 3 步：配置 MCP

仓库里现在统一使用：

- [mcp/README.md](./mcp/README.md)
- [mcp/mineru-cloud/README.md](./mcp/mineru-cloud/README.md)
- [mcp/zotero/README.md](./mcp/zotero/README.md)

### MinerU Cloud

推荐直接从仓库内源码启动：

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

### Zotero

`zotero` 不使用仓库内源码副本，而是直接接入上游 `kujenga/zotero-mcp`。

具体接法见：

- [mcp/zotero/README.md](./mcp/zotero/README.md)
