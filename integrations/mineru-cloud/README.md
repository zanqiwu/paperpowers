# MinerU Cloud Integration

这个目录提供 `mineru-cloud` 的仓库内集成模板，目的是让 `PaperPowers` 用户可以安全地接入论文 PDF 解析能力，而不会把 API key 提交到仓库中。

## 这个集成做了什么

- 提供不含密钥的环境变量模板
- 提供通用 MCP 配置示例
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

真实配置建议保存在本地环境变量或你自己的本地配置文件中。

## 依赖信息

根据 `mcp-server-mineru-bach` 的 PyPI 页面，截至 `2026-03-24`：

- 运行方式：`uvx mcp-server-mineru-bach`
- 必需环境变量：`MINERU_TOKEN`
- 可选环境变量：`MINERU_BASE_URL`

来源：
- https://pypi.org/project/mcp-server-mineru-bach/

## 快速开始

### 1. 准备环境变量

复制模板：

```text
integrations/mineru-cloud/.env.example
```

你可以把真实值设置到系统环境变量中，而不是改模板文件。

### 2. Windows 设置示例

PowerShell：

```powershell
setx MINERU_TOKEN "your_real_token_here"
setx MINERU_BASE_URL "https://api.mineru.net/v1"
```

设置后重开终端。

### 3. macOS / Linux 设置示例

```bash
export MINERU_TOKEN="your_real_token_here"
export MINERU_BASE_URL="https://api.mineru.net/v1"
```

如果想持久化，可以写入 `~/.bashrc`、`~/.zshrc` 或其他 shell 配置文件。

### 4. MCP 配置

参考：

```text
integrations/mineru-cloud/mcp.example.json
```

这是一个通用 MCP 配置样例。不同客户端的 MCP 配置路径和加载方式可能不同，你需要把其中的内容合并到你自己的客户端配置里。

## 目录说明

- `.env.example`
  - 环境变量模板，不含真实密钥
- `mcp.example.json`
  - 通用 MCP 配置示例

## 推荐做法

- 用系统环境变量保存 `MINERU_TOKEN`
- 不要在仓库里创建带真实密钥的 `.env`
- 如果你需要本地文件存储密钥，创建一个不提交到 git 的本地配置文件

## 与 PaperPowers 的关系

`PaperPowers` 的 skill 层只声明对 `mineru-cloud` 的依赖，不在 skill 文件中写死 API key。

这样做的原因是：

- 避免泄露密钥
- 保持仓库可公开上传
- 让不同用户可以用自己的 MinerU 账号和 token
