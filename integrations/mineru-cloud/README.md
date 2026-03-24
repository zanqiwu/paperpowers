# MinerU Cloud Integration

这个目录提供 `mineru-cloud` 的仓库内集成。这里不仅有配置模板，也已经包含你封装的 MCP 源码，便于继续维护、修改和自行运行，而不会把 API key 提交到仓库中。

## 这个集成做了什么

- 提供不含密钥的环境变量模板
- 提供通用 MCP 配置示例
- 提供仓库内可运行的 `mineru-cloud` 源码包
- 说明如何在本地配置 `MINERU_TOKEN`
- 说明 `PaperPowers` 中哪些 skill 会使用 `mineru-cloud`

## 适用的 Skills

当前这些 skills 会使用 `mineru-cloud`：

- `academic-expert`
- `paper-review`
- `literature-mapping`

## 不要把密钥提交到仓库

不要提交任何真实 token。仓库中只应保留模板文件，例如：

- `.env.example`
- `mcp.example.json`
- `mcp.uvx.example.json`

真实配置建议保存在本地环境变量或你自己的本地配置文件中。

## 依赖信息

当前仓库内包含的源码包名为 `mcp-server-mineru-bach`，默认配置为：

- 默认 API 地址：`https://mineru.net/api/v4`
- 必需环境变量：`MINERU_TOKEN`
- 可选环境变量：
  - `MINERU_BASE_URL`
  - `MINERU_OUTPUT_DIR`
  - `MINERU_TMP_DIR`

## 快速开始

### 1. 准备环境变量

复制或参考模板：

```text
integrations/mineru-cloud/.env.example
```

### 2. Windows 设置示例

```powershell
setx MINERU_TOKEN "your_real_token_here"
setx MINERU_BASE_URL "https://mineru.net/api/v4"
```

### 3. macOS / Linux 设置示例

```bash
export MINERU_TOKEN="your_real_token_here"
export MINERU_BASE_URL="https://mineru.net/api/v4"
```

### 4. MCP 配置

推荐优先参考：

```text
integrations/mineru-cloud/mcp.example.json
```

这是一个“从本仓库源码启动”的 MCP 配置样例。

如果你想走发布包方式，也可以参考：

```text
integrations/mineru-cloud/mcp.uvx.example.json
```

## 目录说明

- `.env.example`
  - 环境变量模板，不含真实密钥
- `mcp.example.json`
  - 从仓库内源码启动的 MCP 配置示例
- `mcp.uvx.example.json`
  - 从已发布包启动的 MCP 配置示例
- `source/`
  - `mineru-cloud` 的 Python 源码包

## 与 PaperPowers 的关系

`PaperPowers` 的 skill 层只声明对 `mineru-cloud` 的依赖，不在 skill 文件中写死 API key。
