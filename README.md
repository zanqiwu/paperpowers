# PaperPowers

[English README](./README.en.md)

`PaperPowers` 是一套面向 `Codex` 的学术论文辅助技能包，目标不是“自动替你写论文”，而是把论文工作拆成一套更可靠的流程，让智能体在正确的阶段做正确的事。

它借鉴了 `superpowers` 的工作流思想，但面向的是学术论文场景：idea 打磨、文献检索、创新性判断、实验设计、图表规划、论文审稿式检查、交互式章节写作，以及修订循环。

## 它解决什么问题

很多论文辅助工具的问题不是“模型不够聪明”，而是：

- 在 idea 还不清楚时就开始写摘要
- 没有认真核验相关论文，就下 novelty 结论
- 实验做了很多，但没有映射到核心 claim
- 论文图很多，但没有真正承担叙事功能
- 修改 review comments 时分不清哪些是致命问题，哪些只是表达问题

`PaperPowers` 的设计目标就是减少这些问题。

## 核心能力

- 像学术导师一样整体判断论文当前最薄弱的环节
- 在搜索相关论文时要求先核验元信息并至少阅读摘要
- 帮你判断哪些实验必须做，哪些实验只是重复劳动
- 用 reviewer 视角检查论文的逻辑、证据、实验和表达
- 在你不会写某一节时，先提问补足信息，再生成结构或草稿
- 帮你规划论文图，而不是直接生成无意义的“框架图”

## 当前包含的 Skills

### 1. `paper-triage`

入口技能。用于判断当前任务属于哪个论文阶段，并把请求路由到合适的 skill。

适合：
- 你不确定现在该先做 idea、文献、实验、写作还是审稿式检查
- 你想让系统先判断“当前最关键的问题是什么”

### 2. `academic-expert`

整套技能里最重要的核心角色。它会以长期学术导师和资深 reviewer 的视角，判断论文内容是否合理、claim 是否成立、实验是否足够、叙事是否偏题，以及下一步最值得投入精力的工作是什么。

适合：
- 希望有一个“学术专家”角色整体把关论文
- 想持续跟踪论文状态，而不是只得到一次性的回答
- 想先判断方向和证据是否站得住，再决定是否继续写

### 3. `idea-brainstorming`

把一个模糊的研究想法整理成更清晰的论文 idea brief。

适合：
- 打磨研究问题
- 梳理贡献点
- 明确主要风险和后续证据需求

### 4. `literature-mapping`

用于查找、筛选、聚类和比较相关工作，找出与你最接近的论文。

适合：
- 写 related work
- 判断 novelty 是否站得住
- 找近期强 baseline

### 5. `novelty-stress-test`

模拟苛刻 reviewer，对你的创新性主张进行压力测试。

适合：
- 判断“这到底算不算论文贡献”
- 提前发现 reviewer 可能会攻击的点
- 缩窄过强或不稳的 claim

### 6. `experiment-design`

从论文 claim 反推所需实验，并识别缺失实验和冗余实验。

适合：
- 设计实验矩阵
- 找出必须补的 ablation / baseline / robustness
- 判断哪些实验重复表达了同一个结论

### 7. `paper-review`

像正式审稿人一样审查草稿、章节、提纲、实验故事或 rebuttal。

适合：
- 检查论文结构和论证是否成立
- 找出技术、证据、实验、公平性、表达等问题
- 在投稿前做严格自查

### 8. `figure-planning`

规划论文应该画哪些图，每张图要表达什么，而不是直接生成花哨图示。

适合：
- 设计 method overview 图
- 规划 qualitative / ablation / efficiency 图
- 明确每张图的目标、元素和 caption 意图

### 9. `interactive-section-writing`

当你知道要写哪一节，但不知道怎么写时，先通过提问补足信息，再生成结构或草稿。

适合：
- abstract 不会写
- introduction 不知道怎么开头
- experiments 不知道怎么解释结果
- rebuttal 不知道怎么回应

### 10. `revision-loop`

把导师、审稿人或自查意见整理成一份有优先级的修订计划。

适合：
- 收到 review comments 后组织修改
- 合并重复问题
- 区分必须修、应该修、可忽略的问题

## 推荐使用顺序

如果你是从零开始准备一篇论文，推荐按这个顺序使用：

1. `paper-triage`
2. `academic-expert`
3. `idea-brainstorming`
4. `literature-mapping`
5. `novelty-stress-test`
6. `experiment-design`
7. `figure-planning`
8. `interactive-section-writing`
9. `paper-review`
10. `revision-loop`

如果你已经有草稿，通常从：

1. `paper-triage`
2. `academic-expert`
3. `paper-review`
4. `revision-loop`

开始更合适。

## 设计原则

- 先证据，再结论
- 先核验论文元信息并阅读摘要，再把它当作相关工作依据
- 先定位问题，再开始写
- 先区分论文阶段，再调用合适流程
- 不虚构论文、结果、指标和引用
- 每个实验都必须对应某个 claim
- 每张图都必须服务于论文叙事

## 文献正确性规则

`PaperPowers` 对“搜索论文的正确性”做了额外约束：

- 搜索到论文后，必须先核验标题、作者、年份、venue 或 archive
- 至少阅读摘要，才能把该论文当作关键相关工作
- 如果摘要拿不到，不能把它当作 novelty blocker 或关键证据
- 如果摘要显示论文其实不相关，必须立即停止使用它

这条规则已经写入共享证据规则，并约束到多个 skill，尤其是：

- `academic-expert`
- `literature-mapping`
- `paper-review`
- `novelty-stress-test`
- `figure-planning`

## MinerU Cloud 集成

当前已经集成 `mineru-cloud`，用于读取和解析论文 PDF。

已接入的 skills：

- `academic-expert`
- `paper-review`
- `literature-mapping`

适用场景：

- 直接分析论文 PDF
- 直接分析草稿 PDF
- 提取摘要、方法、实验段落、图表标题、章节结构

## 目录结构

```text
paperpowers/
  INSTALL.md
  README.md
  TEST_PROMPTS.md
  references/
  skills/
```

## 安装到 Codex

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

## 如何触发

你可以直接说：

- `请你先作为一个学术专家整体判断我这篇论文哪里最不成立`
- `帮我找和这个工作最接近的 5 篇论文`
- `我这篇论文还缺哪些实验`
- `请像 reviewer 一样 review 我的草稿`
- `我不知道 abstract 怎么写，你一步步问我`
- `这篇论文应该画哪几张图`
- `帮我根据 review comments 制定修订计划`

## 文档说明

- [INSTALL.md](./INSTALL.md)
  - 安装和集成说明
- [TEST_PROMPTS.md](./TEST_PROMPTS.md)
  - 用于验证 skill 触发的测试提示词
- [README.en.md](./README.en.md)
  - 英文版仓库说明

## 当前状态

当前版本已经可以作为 `Codex skills` 使用，但仍然是第一版结构化能力，后续还可以继续扩展：

- Zotero / OpenAlex / Semantic Scholar / arXiv 的自动接入
- 针对不同学科领域的专用专家 persona
- 自动生成 artifact 文件的脚本化能力

如果你正在构建一个以“学术专家 + 论文工作流”为核心的 Codex 学术写作助手，这个仓库可以作为一个可直接使用和继续扩展的起点。

## License

本仓库使用 [MIT License](./LICENSE)。
