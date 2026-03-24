# PaperPowers

`PaperPowers` 是一套面向 `Codex` 的学术论文辅助技能包。它借鉴了 `superpowers` 的思路，但关注点不是软件开发，而是论文 idea 打磨、文献梳理、创新性审视、实验设计、论文审稿式检查、图表规划和交互式写作。

它的目标不是“自动替你写论文”，而是把论文工作拆成一组更可靠的工作流，让智能体在合适的阶段做合适的事。

## 适用场景

- 你有一个模糊的研究想法，但不知道是否足够新
- 你想找最相关的论文，搞清楚自己和前人工作的差异
- 你不确定现在的实验是否足以支撑论文结论
- 你希望像审稿人一样检查自己的草稿
- 你想规划论文中的图，而不是只让模型“随便画”
- 你卡在某一节写不出来，希望智能体一步步提问引导

## 当前包含的 Skills

### 1. `paper-triage`

入口技能。用于判断当前请求属于哪个论文阶段，并把任务路由到正确的 skill。

适合：
- 还不确定现在应该先做 idea、文献、实验还是写作
- 想让系统先判断你当前最缺什么

### 2. `academic-expert`

这是整套技能里最重要的核心角色。它不是单纯做审稿，也不是单纯帮你润色，而是像一个严肃的学术专家或长期导师一样，持续判断你的论文内容是否合理、claim 是否站得住、实验是否足够、写法是否偏题，以及你下一步最值得投入时间的工作是什么。

适合：
- 希望有一个“学术专家”角色整体把关论文
- 不确定自己的论证、实验和叙事是否成立
- 想让系统像导师一样先判断方向对不对，再决定下一步
- 希望它长期跟踪论文状态，而不是只回答一次

### 3. `idea-brainstorming`

把一个粗糙研究想法整理成更清晰的论文 idea brief。

适合：
- 想打磨研究问题
- 想梳理贡献点
- 想明确风险和后续证据需求

### 4. `literature-mapping`

用于查找、筛选、聚类和比较相关工作，找出与你最接近的论文。

适合：
- 写 related work
- 检查 novelty 是否站得住
- 找近期强 baseline

### 5. `novelty-stress-test`

模拟苛刻 reviewer，对你的创新性主张进行压力测试。

适合：
- 判断“这到底算不算论文贡献”
- 提前发现 reviewer 可能会攻击的点
- 缩窄过强或不稳的 claim

### 6. `experiment-design`

从论文 claim 反推需要哪些实验，并识别冗余实验和缺失实验。

适合：
- 设计实验矩阵
- 找出必须补的 ablation / baseline / robustness
- 判断哪些实验重复表达了同一个结论

### 7. `paper-review`

像正式审稿人一样审查草稿、章节、提纲、实验故事或 rebuttal。

适合：
- 检查论文结构和论证是否成立
- 找出技术、证据、实验、公平性、表达等问题
- 在投稿前做一次严格自查

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
- 收到 review comments 之后组织修改
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

## 目录结构

```text
paperpowers/
  README.md
  references/
    evidence-rules.md
    experiment-checklist.md
    figure-patterns.md
    review-rubric.md
    venue-expectations.md
  skills/
    paper-triage/
      SKILL.md
    academic-expert/
      SKILL.md
    idea-brainstorming/
      SKILL.md
    literature-mapping/
      SKILL.md
    novelty-stress-test/
      SKILL.md
    experiment-design/
      SKILL.md
    paper-review/
      SKILL.md
    figure-planning/
      SKILL.md
    interactive-section-writing/
      SKILL.md
    revision-loop/
      SKILL.md
```

## 安装到 Codex

### Windows

在 PowerShell 中执行：

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills" | Out-Null
cmd /c mklink /J "$env:USERPROFILE\.agents\skills\paperpowers" "C:\Users\Admin\paperpowers\skills"
```

然后重启 `Codex`。

### macOS / Linux

```bash
mkdir -p ~/.agents/skills
ln -s /path/to/paperpowers/skills ~/.agents/skills/paperpowers
```

然后重启 `Codex`。

## 如何触发

你可以直接说：

- `帮我判断这个论文 idea 有没有创新性`
- `请你先作为一个学术专家整体判断我这篇论文哪里最不成立`
- `帮我找和这个工作最接近的 5 篇论文`
- `我这篇论文还缺哪些实验`
- `请像审稿人一样 review 我的草稿`
- `我不知道 abstract 怎么写，你一步步问我`
- `这篇论文应该画哪几张图`
- `帮我根据 review comments 制定修订计划`

## 设计原则

- 先证据，再结论
- 先核验论文元信息并阅读摘要，再把它当作相关工作依据
- 先定位问题，再开始写
- 先区分论文阶段，再调用合适流程
- 不虚构论文、结果、指标和引用
- 每个实验都必须对应某个 claim
- 每张图都必须服务于论文叙事

## 参考文件说明

`references/` 目录中的文件为所有 skill 提供共享约束：

- `evidence-rules.md`
  - 规定文献、引用、实验结果相关的真实性约束
- `experiment-checklist.md`
  - 用于检查实验是否充分、是否重复
- `figure-patterns.md`
  - 用于选择合适的论文图类型
- `review-rubric.md`
  - 用于统一审稿式输出的检查维度
- `venue-expectations.md`
  - 用于按投稿场景校准证据强度和实验完整度
- `academic-personas.md`
  - 用于支持 academic-expert 在导师、审稿人、实验设计者等角色间切换
- `advisor-cycle.md`
  - 用于让 academic-expert 以长期导师方式持续跟踪论文进展
- `pdf-ingestion-with-mineru.md`
  - 用于规定何时使用 MinerU Cloud 解析论文 PDF，以及哪些 skill 应该使用它

## 当前状态

当前版本是第一版技能草稿，重点是把论文工作流结构化，便于后续继续增强。它现在已经可以作为 `Codex skills` 使用，但还没有内置：

- Zotero / OpenAlex / Semantic Scholar / arXiv 的自动接入
- 针对不同学科领域的专用专家 persona
- 自动生成 artifact 文件的脚本化能力

当前已经接入的文档解析能力：

- `mineru-cloud`
  - 已接入到 `academic-expert`、`paper-review`、`literature-mapping`
  - 适用于直接分析论文 PDF、草稿 PDF、章节结构、图表标题和实验内容

这些都可以在下一版继续扩展。
