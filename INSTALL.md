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
- 一套用于测试触发是否正常的提示词

## 前置条件

在开始前，请确认你具备：

- 已安装 `Codex`
- 已安装 `Git`
- 如果要使用 `mineru-cloud`：
  - 已安装 `uv`，或至少能运行 `uvx`
  - 已拥有可用的 `MINERU_TOKEN`

## 第 1 步：获取仓库

### 方式 A：直接 clone

```bash
git clone https://github.com/zanqiwu/paperpowers.git
```

### 方式 B：下载压缩包

直接从 GitHub 下载仓库 zip 并解压到本地。

本地目录最终应类似：

```text
paperpowers/
  INSTALL.md
  README.md
  README.en.md
  TEST_PROMPTS.md
  integrations/
  references/
  skills/
```

## 第 2 步：让 Codex 发现 skills

`Codex` 需要发现的是仓库中的 `skills/` 目录，而不是整个仓库根目录。

### Windows

在 PowerShell 中执行：

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills" | Out-Null
cmd /c mklink /J "$env:USERPROFILE\.agents\skills\paperpowers" "C:\Users\Admin\paperpowers\skills"
```

如果你的仓库不在 `C:\Users\Admin\paperpowers`，请把路径改成你自己的实际路径。

### macOS / Linux

```bash
mkdir -p ~/.agents/skills
ln -s /path/to/paperpowers/skills ~/.agents/skills/paperpowers
```

完成后重启 `Codex`。

## 第 3 步：验证 PaperPowers 本体安装

重启 `Codex` 后，先不要测复杂场景，先试最简单的提示词：

- `请你先作为一个学术专家整体判断我这篇论文哪里最不成立`
- `帮我找和这个工作最接近的 5 篇论文`
- `请像 reviewer 一样 review 我的草稿`

如果 skills 正常被发现，Codex 应该会优先走 `paperpowers` 的 workflow，而不是直接泛化回答。

更完整的测试提示词见：

- [TEST_PROMPTS.md](./TEST_PROMPTS.md)

## 第 4 步：安装 MinerU Cloud 集成

如果你不需要直接读取论文 PDF，可以跳过这一节。

如果你希望这些 skill 能直接分析 PDF：

- `academic-expert`
- `paper-review`
- `literature-mapping`

那么建议安装 `mineru-cloud`。

### 4.1 查看本地集成模板

仓库里已经包含模板：

- [integrations/mineru-cloud/README.md](./integrations/mineru-cloud/README.md)
- [integrations/mineru-cloud/README.en.md](./integrations/mineru-cloud/README.en.md)
- [integrations/mineru-cloud/.env.example](./integrations/mineru-cloud/.env.example)
- [integrations/mineru-cloud/mcp.example.json](./integrations/mineru-cloud/mcp.example.json)

### 4.2 准备 MinerU Token

你需要有自己的 `MINERU_TOKEN`。

注意：

- 不要把真实 token 写进仓库
- 不要提交带真实 token 的 `.env`
- 推荐把 token 放到系统环境变量里

### 4.3 Windows 设置环境变量

PowerShell：

```powershell
setx MINERU_TOKEN "your_real_token_here"
setx MINERU_BASE_URL "https://api.mineru.net/v1"
```

设置后关闭并重新打开终端。

### 4.4 macOS / Linux 设置环境变量

```bash
export MINERU_TOKEN="your_real_token_here"
export MINERU_BASE_URL="https://api.mineru.net/v1"
```

如果想持久化，可以写入：

- `~/.bashrc`
- `~/.zshrc`
- 或其他 shell 配置文件

### 4.5 准备 MCP 配置

参考模板：

- [integrations/mineru-cloud/mcp.example.json](./integrations/mineru-cloud/mcp.example.json)

这个文件是通用示例，不同客户端的 MCP 配置文件路径可能不同。你需要把其中的 `mineru-cloud` 配置合并到你自己的客户端配置中。

模板的核心配置逻辑是：

- 使用 `uvx mcp-server-mineru-bach`
- 从环境变量读取：
  - `MINERU_TOKEN`
  - `MINERU_BASE_URL`

## 第 5 步：验证 MinerU 是否工作

完成 MinerU 配置后，建议用 PDF 场景测试：

- `这是我的论文 PDF 链接。请先解析整篇论文，再像 reviewer 一样指出最严重的问题。`
- `我给你一篇论文 PDF 链接，请先解析摘要、方法和实验部分，再告诉我它和我的工作最相关的点。`

如果配置正常，相关 skill 应该会优先用 `mineru-cloud` 解析 PDF，而不是只靠文件名或片段猜测。

## 常见问题

### 1. Skills 没有生效

检查：

- `~/.agents/skills/paperpowers` 或 `%USERPROFILE%\.agents\skills\paperpowers` 是否存在
- 它是否指向 `paperpowers/skills`
- 是否已经重启 `Codex`

### 2. 安装后只看到部分 skill

检查每个 skill 目录下是否都存在：

- `SKILL.md`
- `agents/openai.yaml`
- `assets/icon.svg`

### 3. MinerU 无法工作

先检查：

- `MINERU_TOKEN` 是否已设置
- `uvx` 是否可用
- 你的 MCP 客户端配置里是否已加入 `mineru-cloud`

### 4. 真实密钥会不会泄露到仓库

不会，只要你遵守以下规则：

- 不要修改并提交 `.env.example`
- 不要创建并提交带真实 token 的 `.env`
- 用本地环境变量保存真实值

## 推荐阅读顺序

安装完成后，建议按这个顺序继续：

1. [README.md](./README.md)
2. [TEST_PROMPTS.md](./TEST_PROMPTS.md)
3. [integrations/mineru-cloud/README.md](./integrations/mineru-cloud/README.md)
