# PaperPowers 测试提示词

下面这些提示词用于快速验证 `paperpowers` 的 skill 是否能被 `Codex` 正确触发。建议从简单到复杂依次测试。

## 1. 入口分诊

```text
我现在有一篇机器学习论文的初稿，也有一些实验结果，但不确定下一步应该先补实验、改写作还是查相关工作。请先帮我判断当前最关键的问题。
```

预期倾向：
- `paper-triage`

## 2. Idea 打磨

```text
我想做一个面向多模态检索的训练方法，核心想法是用更细粒度的负样本构造提升鲁棒性，但我不确定这是否足够成为一篇论文。请帮我梳理问题、贡献和主要风险。
```

预期倾向：
- `idea-brainstorming`

## 3. 学术专家整体判断

```text
我已经有论文提纲、部分实验结果和一个初版摘要，但我不确定整篇论文是否合理。请你先作为一个学术专家，从问题定义、创新性、实验充分性和叙事结构四个角度整体判断我现在最大的短板。
```

预期倾向：
- `academic-expert`

## 3.1 学术专家长期导师模式

```text
从现在开始请你作为我的长期学术导师来帮助我推进这篇论文。先不要直接润色文字，先判断这篇论文目前最薄弱的环节是什么，并告诉我下一步最值得做的 3 件事。
```

预期倾向：
- `academic-expert`

## 3.2 学术专家切换 persona

```text
请你用 skeptical reviewer 和 experimentalist 两个视角，先整体判断我这篇论文的问题，再告诉我应该先补实验还是先收缩 claim。
```

预期倾向：
- `academic-expert`

## 4. 文献梳理

```text
帮我找和“基于大语言模型的表格问答错误检测”最接近的近两年论文，并按方法路线帮我分组，指出我最需要读的 5 篇。
```

预期倾向：
- `literature-mapping`

## 4.1 通过 PDF 做文献理解

```text
我给你一篇论文 PDF 链接，请先解析这篇论文的摘要、方法和实验部分，再告诉我它和我的工作最相关的点是什么。
```

预期倾向：
- `literature-mapping`
- 使用 `mineru-cloud`

## 5. 创新性压力测试

```text
我现在的方法是在现有 RAG 框架上加入一个置信度驱动的检索重排模块，并增加错误归因分析。请你像一个苛刻 reviewer 一样判断这到底算不算创新。
```

预期倾向：
- `novelty-stress-test`

## 6. 实验设计

```text
我的论文 claim 是方法在低资源设定下更稳、更省算力，而且错误类型更可解释。请根据这些 claim 帮我列出必须做的实验、可选实验，以及哪些实验可能是重复的。
```

预期倾向：
- `experiment-design`

## 7. 审稿式检查

```text
请像正式 reviewer 一样审查我这篇论文的方法和实验部分，优先告诉我致命问题和重要问题，不要先帮我润色。
```

预期倾向：
- `paper-review`

## 7.1 对 PDF 草稿做审稿式检查

```text
这是我的论文 PDF 链接。请先解析整篇论文，再像 reviewer 一样指出最严重的技术问题、实验问题和叙事问题。
```

预期倾向：
- `paper-review`
- 使用 `mineru-cloud`

## 8. 图表规划

```text
这篇论文的核心卖点是方法结构简单、训练代价低、而且在 3 个任务上都有稳定提升。你帮我规划一下正文最该画哪几张图，每张图主要要表达什么。
```

预期倾向：
- `figure-planning`

## 9. 交互式章节写作

```text
我现在完全不知道 introduction 怎么写。你不要直接生成一大段，先一步步问我关键问题，帮我把 introduction 的结构搭起来。
```

预期倾向：
- `interactive-section-writing`

## 10. 修订计划

```text
这是我收到的 review comments：评审认为 novelty 不清楚、baseline 不够强、图 2 看不懂、实验解释不充分。请帮我整理成一份有优先级的修订计划。
```

预期倾向：
- `revision-loop`

## 11. 组合场景

```text
我有一个论文 idea，也写了半页摘要，但我不确定这个方向是否真的新，也不知道后面应该补哪些实验。你先判断我现在该怎么推进。
```

预期倾向：
- 先 `paper-triage`
- 再根据判断进入 `academic-expert`、`idea-brainstorming`、`literature-mapping` 或 `experiment-design`

## 使用建议

- 第一次测试时，优先用不含 skill 名称的自然语言提示词，观察是否会隐式触发对应 skill。
- 第二次测试时，可以显式写出 skill 名称，例如：`Use $paper-review to ...`，验证显式调用是否正常。
- 如果你准备接入文献 MCP，优先测试 `literature-mapping` 和 `novelty-stress-test`。
