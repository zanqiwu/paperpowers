# PaperPowers 安装教程

这份文档面向第一次使用的人，按“从零开始”的方式说明如何安装：

1. `PaperPowers`
2. `mineru-cloud`
3. `Codex` 中的本地 skill 发现

如果你只是想看仓库功能，请先看 [README.md](./README.md)。

## 你最终会得到什么

安装完成后，你会得到：

- 一套可被 `Codex` 发现的本地 skills
- 一个可选的 `mineru-cloud` 集成，用于解析论文 PDF
- 一份仓库内可维护的 `mineru-cloud` MCP 源码
- 一套用于测试触发是否正常的提示词

## 前置条件

在开始前，请确认你具备：

- 已安装 `Codex`
- 已安装 `Git`
- 如果要使用 `mineru-cloud`：
  - 已安装 `uv`
  - 已拥有可用的 `MINERU_TOKEN`

## 第 1 步：获取仓库

### 方式 A：直接 clone

```bash
git clone https://github.com/zanqiwu/paperpowers.git
```

### 方式 B：下载压缩包

直接从 GitHub 下载仓库 zip 并解压到本地。

## 第 2 步：让 Codex 发现 skills

`Codex` 需要发现的是仓库中的 `skills/` 目录，而不是整个仓库根目录。

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

完成后重启 `Codex`。

## 第 3 步：验证 PaperPowers 本体安装

先试最简单的提示词：

- `请你先作为一个学术专家整体判断我这篇论文哪里最不成立`
- `帮我找和这个工作最接近的 5 篇论文`
- `请像 reviewer 一样 review 我的草稿`

更完整的测试提示词见：

- [TEST_PROMPTS.md](./TEST_PROMPTS.md)

## 第 4 步：安装 MinerU Cloud 集成

如果你希望这些 skill 能直接分析 PDF：

- `academic-expert`
- `paper-review`
- `literature-mapping`

那么建议安装 `mineru-cloud`。

### 4.1 查看仓库内集成目录

仓库里已经包含源码和模板：

- [integrations/mineru-cloud/README.md](./integrations/mineru-cloud/README.md)
- [integrations/mineru-cloud/README.en.md](./integrations/mineru-cloud/README.en.md)
- [integrations/mineru-cloud/source/README.md](./integrations/mineru-cloud/source/README.md)
- [integrations/mineru-cloud/.env.example](./integrations/mineru-cloud/.env.example)
- [integrations/mineru-cloud/mcp.example.json](./integrations/mineru-cloud/mcp.example.json)
- [integrations/mineru-cloud/mcp.uvx.example.json](./integrations/mineru-cloud/mcp.uvx.example.json)

### 4.2 设置环境变量

Windows:

```powershell
setx MINERU_TOKEN "your_real_token_here"
setx MINERU_BASE_URL "https://mineru.net/api/v4"
```

macOS / Linux:

```bash
export MINERU_TOKEN="your_real_token_here"
export MINERU_BASE_URL="https://mineru.net/api/v4"
```

### 4.3 配置 MCP

推荐优先使用仓库内源码版本：

- [integrations/mineru-cloud/mcp.example.json](./integrations/mineru-cloud/mcp.example.json)

这个模板使用：

- `uv --directory /path/to/paperpowers/integrations/mineru-cloud/source run mcp-server-mineru-bach`

如果你更希望直接使用已发布包，也可以参考：

- [integrations/mineru-cloud/mcp.uvx.example.json](./integrations/mineru-cloud/mcp.uvx.example.json)

它使用：

- `uvx mcp-server-mineru-bach`

## 第 5 步：验证 MinerU 是否工作

建议用 PDF 场景测试：

- `这是我的论文 PDF 链接。请先解析整篇论文，再像 reviewer 一样指出最严重的问题。`
- `我给你一篇论文 PDF 链接，请先解析摘要、方法和实验部分，再告诉我它和我的工作最相关的点。`

## 常见问题

### 1. Skills 没有生效

- `~/.agents/skills/paperpowers` 或 `%USERPROFILE%\.agents\skills\paperpowers` 是否存在
- 它是否指向 `paperpowers/skills`
- 是否已经重启 `Codex`

### 2. MinerU 无法工作

- `MINERU_TOKEN` 是否已设置
- `uv` 是否可用
- 你的 MCP 客户端配置里是否已加入 `mineru-cloud`

### 3. 真实密钥会不会泄露到仓库

不会，只要你遵守以下规则：

- 不要修改并提交 `.env.example`
- 不要创建并提交带真实 token 的 `.env`
- 用本地环境变量保存真实值
