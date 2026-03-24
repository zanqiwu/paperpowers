# PaperPowers 安装说明

本文档说明如何把 `PaperPowers` 安装为 `Codex` 可发现的本地 skills 包。

## 目录说明

当前仓库根目录应类似于：

```text
paperpowers/
  INSTALL.md
  README.md
  TEST_PROMPTS.md
  references/
  skills/
```

`Codex` 需要发现的是 `skills/` 目录，而不是整个仓库根目录。

## Windows 安装

在 PowerShell 中执行：

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills" | Out-Null
cmd /c mklink /J "$env:USERPROFILE\.agents\skills\paperpowers" "C:\Users\Admin\paperpowers\skills"
```

如果你的 `paperpowers` 不在 `C:\Users\Admin\paperpowers`，请把上面的目标路径改成你的实际路径。

完成后重启 `Codex`。

## macOS / Linux 安装

```bash
mkdir -p ~/.agents/skills
ln -s /path/to/paperpowers/skills ~/.agents/skills/paperpowers
```

完成后重启 `Codex`。

## 验证安装

重启 `Codex` 后，可以尝试这些提示词：

- `帮我判断这个论文 idea 是否值得继续做`
- `请像 reviewer 一样检查这篇论文草稿`
- `帮我规划这篇论文应该画哪些图`

如果 skills 正常被发现，Codex 应该会加载相应的 `paperpowers` skill，而不是直接用泛化回答。

## MinerU Cloud 集成位置

`mineru-cloud` 已集成在这些 skill 中：

- `academic-expert`
- `paper-review`
- `literature-mapping`

设计原因：

- 这 3 个 skill 都可能需要直接读取论文 PDF 或草稿 PDF
- 它们需要章节结构、摘要、实验段落、图表标题等结构化内容
- 其他 skill 如 `idea-brainstorming`、`revision-loop` 并不总是依赖 PDF 解析，不应强绑定 MinerU

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

### 3. 想更新这套 skills

如果你直接修改了本地目录，只需要重启 `Codex`。

如果你之后把它放进 git 仓库并通过 `git pull` 更新，同样重启 `Codex` 即可。

## 推荐的下一步

安装完成后，建议先阅读：

- `README.md`
- `TEST_PROMPTS.md`

再开始正式使用。
