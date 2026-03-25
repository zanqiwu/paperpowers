# Zotero MCP

这个目录不再内置本地 Zotero MCP 源码，而是直接接入上游仓库：

- `kujenga/zotero-mcp`
- GitHub: `https://github.com/kujenga/zotero-mcp`

这样做的原因：

- 避免重复维护一份平行实现
- 直接跟随上游工具更新
- 保持 `paperpowers` 仓库聚焦在技能与工作流，而不是重复实现外部 MCP

## 上游工具当前提供的核心能力

根据 `kujenga/zotero-mcp` 当前 README：

- `zotero_search_items`
- `zotero_item_metadata`
- `zotero_item_fulltext`

## 推荐接入方式

### 方式 1：直接用上游已发布包

```json
{
  "mcpServers": {
    "zotero": {
      "command": "uvx",
      "args": [
        "--upgrade",
        "zotero-mcp"
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

### 方式 2：直接 clone 上游 GitHub 仓库后运行

```bash
git clone https://github.com/kujenga/zotero-mcp.git
```

然后在 MCP 配置里指向这个上游仓库目录：

```json
{
  "mcpServers": {
    "zotero": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/zotero-mcp",
        "run",
        "zotero-mcp"
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

## 你如何把 Zotero API 提供给我

你有两种方式。

### 方式 A：本地 Zotero API

1. 打开 Zotero 桌面端
2. 进入 `Settings`
3. 在 `Advanced` 下启用允许其他应用与 Zotero 通信
4. 在 MCP 配置里设置：

```json
"env": {
  "ZOTERO_LOCAL": "true",
  "ZOTERO_API_KEY": "",
  "ZOTERO_LIBRARY_ID": "",
  "ZOTERO_LIBRARY_TYPE": "user"
}
```

### 方式 B：Zotero Web API

你需要提供给 MCP 的是：

- `ZOTERO_API_KEY`
- `ZOTERO_LIBRARY_ID`
- `ZOTERO_LIBRARY_TYPE`

配置示例：

```json
"env": {
  "ZOTERO_LOCAL": "false",
  "ZOTERO_API_KEY": "your_real_key_here",
  "ZOTERO_LIBRARY_ID": "your_library_id_here",
  "ZOTERO_LIBRARY_TYPE": "user"
}
```

## 如何获取 `ZOTERO_API_KEY` 和 `ZOTERO_LIBRARY_ID`

按 Zotero 官方 Web API 文档：

- 非公开库的读取需要 API key
- 用户库请求路径使用 `/users/<userID>`
- group 库请求路径使用 `/groups/<groupID>`

你可以这样准备：

1. 打开 API key 页面：`https://www.zotero.org/settings/keys`
2. 创建一个新的只读 key
3. 记录你的 `userID`
4. 如果你访问的是 group 库，则记录 `groupID`

不要把真实 key 提交进 git 仓库。

## 参考链接

- 上游仓库：`https://github.com/kujenga/zotero-mcp`
- Zotero Web API v3：`https://www.zotero.org/support/dev/web_api/v3/start`
- Zotero Web API basics：`https://www.zotero.org/support/dev/web_api/v3/basics`
