import os
from typing import Any, Literal

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from pyzotero import zotero


load_dotenv()

mcp = FastMCP("paperpowers-zotero")


def get_zotero_client() -> zotero.Zotero:
    """Create a Zotero client from environment variables."""
    library_id = os.getenv("ZOTERO_LIBRARY_ID")
    library_type = os.getenv("ZOTERO_LIBRARY_TYPE", "user")
    api_key = os.getenv("ZOTERO_API_KEY") or None
    local = os.getenv("ZOTERO_LOCAL", "").strip().lower() in {"1", "true", "yes"}

    if local and not library_id:
        library_id = "0"

    if not local and not all([library_id, api_key]):
        raise ValueError(
            "Missing required environment variables. "
            "Set ZOTERO_LOCAL=true for local mode, or set ZOTERO_LIBRARY_ID and ZOTERO_API_KEY."
        )

    return zotero.Zotero(
        library_id=library_id,
        library_type=library_type,
        api_key=api_key,
        local=local,
    )


def _creator_name(creator: dict[str, Any]) -> str:
    if "firstName" in creator and "lastName" in creator:
        return f"{creator['lastName']}, {creator['firstName']}"
    return creator.get("name", "")


def format_item(item: dict[str, Any]) -> str:
    """Format a Zotero item for LLM-readable output."""
    data = item.get("data", {})
    item_key = item.get("key", "")
    item_type = data.get("itemType", "unknown")

    lines = [
        f"Title: {data.get('title', 'Untitled')}",
        f"Item Key: {item_key}",
        f"Type: {item_type}",
        f"Date: {data.get('date', 'No date')}",
    ]

    creators = [_creator_name(creator) for creator in data.get("creators", [])]
    creators = [name for name in creators if name]
    if creators:
        lines.append("Creators: " + "; ".join(creators))

    if publication := data.get("publicationTitle"):
        lines.append(f"Publication: {publication}")
    if doi := data.get("DOI"):
        lines.append(f"DOI: {doi}")
    if url := data.get("url"):
        lines.append(f"URL: {url}")

    if abstract := data.get("abstractNote"):
        lines.append("")
        lines.append("Abstract:")
        lines.append(abstract)

    tags = [tag.get("tag", "") for tag in data.get("tags", []) if tag.get("tag")]
    if tags:
        lines.append("")
        lines.append("Tags: " + ", ".join(tags))

    return "\n".join(lines)


def get_attachment_details(
    zot: zotero.Zotero,
    item: dict[str, Any],
) -> dict[str, str] | None:
    """Find the most suitable attachment for full-text retrieval."""
    data = item.get("data", {})
    item_type = data.get("itemType")

    if item_type == "attachment":
        return {
            "key": data.get("key", ""),
            "content_type": data.get("contentType", "unknown"),
        }

    try:
        children: Any = zot.children(data.get("key", ""))
    except Exception:
        return None

    ranked: list[tuple[int, str, str]] = []
    for child in children:
        child_data = child.get("data", {})
        if child_data.get("itemType") != "attachment":
            continue

        content_type = child_data.get("contentType", "")
        attachment_key = child_data.get("key", "")
        if not attachment_key:
            continue

        score = 0
        if content_type == "application/pdf":
            score = 3
        elif content_type == "text/html":
            score = 2
        else:
            score = 1

        ranked.append((score, attachment_key, content_type))

    if not ranked:
        return None

    ranked.sort(reverse=True)
    _, attachment_key, content_type = ranked[0]
    return {
        "key": attachment_key,
        "content_type": content_type,
    }


@mcp.tool(
    name="zotero_item_metadata",
    description="Get metadata information about a specific Zotero item by item key.",
)
def zotero_item_metadata(item_key: str) -> str:
    try:
        zot = get_zotero_client()
        item: Any = zot.item(item_key)
        if not item:
            return f"No item found with key: {item_key}"
        return format_item(item)
    except Exception as exc:
        return f"Error retrieving item metadata: {str(exc)}"


@mcp.tool(
    name="zotero_item_fulltext",
    description="Get the full text of a Zotero item, given a parent item key or attachment key.",
)
def zotero_item_fulltext(item_key: str) -> str:
    try:
        zot = get_zotero_client()
        item: Any = zot.item(item_key)
        if not item:
            return f"No item found with key: {item_key}"

        attachment = get_attachment_details(zot, item)
        header = format_item(item)

        if attachment is None:
            return header + "\n\nNo suitable attachment found for full-text extraction."

        full_text_data: Any = zot.fulltext_item(attachment["key"])
        if not full_text_data or "content" not in full_text_data:
            return (
                header
                + f"\n\nAttachment Key: {attachment['key']}"
                + f"\nAttachment Type: {attachment['content_type']}"
                + "\n\nAttachment found, but no extractable full text is available."
            )

        content = full_text_data["content"]
        return (
            header
            + f"\n\nAttachment Key: {attachment['key']}"
            + f"\nAttachment Type: {attachment['content_type']}"
            + "\n\nFull Text:\n"
            + content
        )
    except Exception as exc:
        return f"Error retrieving item full text: {str(exc)}"


@mcp.tool(
    name="zotero_search_items",
    description="Search for items in Zotero by query string, query mode, optional tag, and result limit.",
)
def zotero_search_items(
    query: str,
    qmode: Literal["titleCreatorYear", "everything"] = "titleCreatorYear",
    tag: str | None = None,
    limit: int = 10,
) -> str:
    try:
        zot = get_zotero_client()
        params: dict[str, Any] = {
            "q": query,
            "qmode": qmode,
            "limit": max(1, min(limit, 50)),
        }
        if tag:
            params["tag"] = tag

        zot.add_parameters(**params)
        results: Any = zot.items()

        if not results:
            return "No items found matching your query."

        lines = [
            f"Search Query: {query}",
            f"Result Count: {len(results)}",
            "Use item keys with zotero_item_metadata or zotero_item_fulltext for more details.",
            "",
        ]

        for index, item in enumerate(results, start=1):
            data = item.get("data", {})
            lines.append(f"{index}. {data.get('title', 'Untitled')}")
            lines.append(f"   Key: {item.get('key', '')}")
            lines.append(f"   Type: {data.get('itemType', 'unknown')}")
            if data.get("date"):
                lines.append(f"   Date: {data['date']}")
            creators = [_creator_name(creator) for creator in data.get("creators", [])]
            creators = [name for name in creators if name]
            if creators:
                lines.append(f"   Creators: {'; '.join(creators[:4])}")
            if data.get("abstractNote"):
                abstract = data["abstractNote"].strip().replace("\n", " ")
                if len(abstract) > 240:
                    abstract = abstract[:237] + "..."
                lines.append(f"   Abstract: {abstract}")
            lines.append("")

        return "\n".join(lines).rstrip()
    except Exception as exc:
        return f"Error searching items: {str(exc)}"


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
