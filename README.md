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

### 2. `academic-expert`

整套技能里最重要的核心角色。它会以长期学术导师和资深 reviewer 的视角，判断论文内容是否合理、claim 是否成立、实验是否足够、叙事是否偏题，以及下一步最值得投入精力的工作是什么。

### 3. `idea-brainstorming`

把一个模糊的研究想法整理成更清晰的论文 idea brief。

### 4. `literature-mapping`

用于查找、筛选、聚类和比较相关工作，找出与你最接近的论文。

### 5. `novelty-stress-test`

模拟苛刻 reviewer，对你的创新性主张进行压力测试。

### 6. `experiment-design`

从论文 claim 反推所需实验，并识别缺失实验和冗余实验。

### 7. `paper-review`

像正式审稿人一样审查草稿、章节、提纲、实验故事或 rebuttal。

### 8. `figure-planning`

规划论文应该画哪些图，每张图要表达什么，而不是直接生成花哨图示。

### 9. `interactive-section-writing`

当你知道要写哪一节，但不知道怎么写时，先通过提问补足信息，再生成结构或草稿。

### 10. `revision-loop`

把导师、审稿人或自查意见整理成一份有优先级的修订计划。

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

## MCP 目录

仓库中的 MCP 工具现在统一收敛到 `mcp/` 目录，便于后续继续扩展更多工具，而不是把不同集成散落在多个位置。

当前已包含：

- [mcp/README.md](./mcp/README.md)
- [mcp/mineru-cloud/README.md](./mcp/mineru-cloud/README.md)
- [mcp/zotero/README.md](./mcp/zotero/README.md)

`mineru-cloud` 用于读取和解析论文 PDF，目前主要服务于：

- `academic-expert`
- `paper-review`
- `literature-mapping`

`zotero` 用于访问个人文献库，目前优先适合：

- 检索自己已经收藏的论文
- 拉取条目元数据和摘要
- 在写 related work 或引用时回到个人知识库核对

注意：

- API key 不会写入仓库
- 真实 `MINERU_TOKEN` 需要你在本地环境变量中设置
- `mineru-cloud` 的封装源码已经随仓库一起提供，便于你继续维护

## 文档说明

- [INSTALL.md](./INSTALL.md)
  - 安装和集成说明
- [TEST_PROMPTS.md](./TEST_PROMPTS.md)
  - 用于验证 skill 触发的测试提示词
- [README.en.md](./README.en.md)
  - 英文版仓库说明
- [mcp/README.md](./mcp/README.md)
  - MCP 目录说明
- [mcp/mineru-cloud/README.md](./mcp/mineru-cloud/README.md)
  - MinerU Cloud 源码说明
- [mcp/zotero/README.md](./mcp/zotero/README.md)
  - Zotero MCP 源码说明
