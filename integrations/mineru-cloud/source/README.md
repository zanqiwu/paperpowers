# MinerU Cloud Source

这个目录包含 `paperpowers` 仓库内随附的 `mineru-cloud` MCP 源码，包名为 `mcp-server-mineru-bach`。

## 这个源码包提供什么

- `analyze_document_mineru`
  - 调用 MinerU Cloud API 解析远程文档 URL
- `list_saved_results`
  - 列出本地已保存的解析结果
- `read_saved_result`
  - 按字符区间分块读取大结果文件

## 依赖

- Python `>=3.10`
- `uv`

## 本地运行

```bash
uv --directory integrations/mineru-cloud/source run mcp-server-mineru-bach
```

## 必需环境变量

- `MINERU_TOKEN`

## 可选环境变量

- `MINERU_BASE_URL`
  - 默认：`https://mineru.net/api/v4`
- `MINERU_OUTPUT_DIR`
  - 默认：`~/MinerU/cloud_results`
- `MINERU_TMP_DIR`
  - 默认：`$MINERU_OUTPUT_DIR/_tmp`
