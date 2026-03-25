# Zotero MCP

这个目录提供 `paperpowers` 内置的 Zotero MCP 源码，当前参考了 `kujenga/zotero-mcp` 的工具边界，但采用了和本仓库一致的轻量单文件结构。

## 当前提供的工具

- `zotero_search_items`
  - 按查询词搜索 Zotero 条目
- `zotero_item_metadata`
  - 获取指定条目的元数据
- `zotero_item_fulltext`
  - 获取指定条目附件的全文文本

## 配置方式

支持两种模式：

- 本地 Zotero API
- Zotero Web API

### 环境变量

- `ZOTERO_LOCAL`
  - `true/false`，为 `true` 时优先使用本地 Zotero API
- `ZOTERO_API_KEY`
  - Web API 模式需要
- `ZOTERO_LIBRARY_ID`
  - Web API 模式需要
- `ZOTERO_LIBRARY_TYPE`
  - 可选，默认 `user`

## 本地运行

```bash
uv --directory mcp/zotero run python server.py
```

## MCP 配置示例

```json
{
  "mcpServers": {
    "zotero": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/paperpowers/mcp/zotero",
        "run",
        "python",
        "server.py"
      ],
      "env": {
        "ZOTERO_LOCAL": "true",
        "ZOTERO_API_KEY": "",
        "ZOTERO_LIBRARY_ID": "",
        "ZOTERO_LIBRARY_TYPE": "user"
      }
    }
  }
}
```

## 说明

- 本地 API 模式要求 Zotero 桌面端运行，并开启允许其他应用访问
- Web API 模式更稳定，也更适合远程环境
- 全文提取依赖 Zotero 附件全文接口，不保证每个条目都可读
