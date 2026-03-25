# PaperPowers

[English README](./README.en.md)

`PaperPowers` 是一套面向 `Codex` 的学术论文辅助技能包，目标不是“自动替你写论文”，而是把论文工作拆成一套更可靠的流程，让智能体在正确的阶段做正确的事。

它借鉴了 `superpowers` 的工作流思想，但面向的是学术论文场景：idea 打磨、文献检索、创新性判断、实验设计、图表规划、论文审稿式检查、交互式章节写作，以及修订循环。

当前版本重点补强了三层长期能力：

- `project memory`
  - 避免每次重新打开都要从零加载论文状态
- `claim-evidence map`
  - 把 claim、实验、图表和证据缺口稳定映射起来
- `reference pipeline + related-work writing`
  - 先做可核验文献管线，再写 related work

为了避免长期状态文件越写越乱，当前版本也加入了统一模板：

- `docs/paperpowers/templates/current-paper-state.template.md`
- `docs/paperpowers/templates/claim-evidence-map.template.md`

这些模板默认以中文书写，但允许保留必要的论文术语，以兼顾人类可读性和专业精度。

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

## 文献正确性规则

`PaperPowers` 对“搜索论文的正确性”做了额外约束：

- 搜索到论文后，必须先核验标题、作者、年份、venue 或 archive
- 至少阅读摘要，才能把该论文当作关键相关工作
- 如果摘要拿不到，不能把它当作 novelty blocker 或关键证据
- 如果摘要显示论文其实不相关，必须立即停止使用它

## MCP 目录

仓库中的 MCP 工具统一收敛到 `mcp/` 目录，便于后续继续扩展。

当前已包含：

- [mcp/README.md](./mcp/README.md)
- [mcp/mineru-cloud/README.md](./mcp/mineru-cloud/README.md)
- [mcp/zotero/README.md](./mcp/zotero/README.md)

`mineru-cloud` 用于读取和解析论文 PDF，目前主要服务于：

- `academic-expert`
- `paper-review`
- `literature-mapping`

`zotero` 用于访问个人文献库，目前采用“直接接入上游 `kujenga/zotero-mcp`”的方案，不在 `paperpowers` 内维护平行实现。

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
  - Zotero MCP 上游接入说明
