import glob
import json
import os
import shutil
import tempfile
import time
import zipfile
from typing import Literal

import requests
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("mcp-server-mineru-bach")

MINERU_BASE_URL = os.environ.get("MINERU_BASE_URL", "https://mineru.net/api/v4")
MINERU_OUTPUT_DIR = os.environ.get(
    "MINERU_OUTPUT_DIR",
    os.path.join(os.path.expanduser("~"), "MinerU", "cloud_results"),
)
MINERU_TMP_DIR = os.environ.get(
    "MINERU_TMP_DIR",
    os.path.join(MINERU_OUTPUT_DIR, "_tmp"),
)

MINERU_SUCCESS_CODE = 0
MINERU_JOB_COMPLETED_STATUS = "done"
MINERU_JOB_FAILED_STATUS = "failed"


def _safe_name_from_url(file_url: str) -> str:
    """Build a filesystem-safe stem from URL."""
    base = os.path.basename(file_url.split("?")[0]) or "document"
    stem, _ = os.path.splitext(base)
    cleaned = "".join(ch if (ch.isalnum() or ch in ("-", "_")) else "_" for ch in stem)
    cleaned = cleaned.strip("_")
    return (cleaned or "document")[:80]


def _ensure_output_dir() -> str:
    os.makedirs(MINERU_OUTPUT_DIR, exist_ok=True)
    return MINERU_OUTPUT_DIR


def _ensure_tmp_dir() -> str:
    os.makedirs(MINERU_TMP_DIR, exist_ok=True)
    return MINERU_TMP_DIR


def _to_abs_saved_path(file_path: str) -> str:
    """Resolve relative path into MINERU_OUTPUT_DIR and enforce directory boundary."""
    base_dir = os.path.abspath(_ensure_output_dir())
    target = file_path
    if not os.path.isabs(target):
        target = os.path.join(base_dir, target)
    target = os.path.abspath(target)
    if os.path.commonpath([base_dir, target]) != base_dir:
        raise ValueError("file_path is outside MINERU_OUTPUT_DIR")
    return target


def download_file(url: str, save_path: str) -> str:
    """Download a file to a specific path."""
    with requests.get(url, stream=True, timeout=60) as response:
        response.raise_for_status()
        with open(save_path, "wb") as file_handle:
            for chunk in response.iter_content(chunk_size=8192):
                file_handle.write(chunk)
    return save_path


def unzip_file(zip_path: str, extract_path: str) -> None:
    """Extract a zip file."""
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)


def process_zip(zip_url: str, output_type: str) -> str:
    """Download and extract the MinerU result archive, then return the requested content."""
    temp_dir = tempfile.mkdtemp(dir=_ensure_tmp_dir())
    try:
        file_name = os.path.basename(zip_url.split("?")[0])
        zip_path = os.path.join(temp_dir, file_name)
        download_file(zip_url, zip_path)

        extract_path = os.path.join(temp_dir, "extracted")
        os.makedirs(extract_path, exist_ok=True)
        unzip_file(zip_path, extract_path)

        if output_type == "json":
            json_files = glob.glob(
                os.path.join(extract_path, "**/*_content_list.json"),
                recursive=True,
            )
            if not json_files:
                raise RuntimeError("content_list.json not found")
            with open(json_files[0], "r", encoding="utf-8") as file_handle:
                return file_handle.read()

        md_file = os.path.join(extract_path, "full.md")
        if not os.path.exists(md_file):
            found_mds = glob.glob(os.path.join(extract_path, "**/full.md"), recursive=True)
            if found_mds:
                md_file = found_mds[0]
        if not os.path.exists(md_file):
            raise RuntimeError("full.md not found")
        with open(md_file, "r", encoding="utf-8") as file_handle:
            return file_handle.read()
    finally:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)


def _make_request(method: str, url: str, **kwargs) -> requests.Response:
    if "timeout" not in kwargs:
        kwargs["timeout"] = 60

    retries = 5
    last_exception = None

    for attempt in range(retries):
        try:
            if method == "POST":
                response = requests.post(url, **kwargs)
            else:
                response = requests.get(url, **kwargs)

            if 500 <= response.status_code < 600:
                time.sleep(3 * (attempt + 1))
                continue

            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as exc:
            if exc.response is not None and 500 <= exc.response.status_code < 600:
                last_exception = exc
                time.sleep(3 * (attempt + 1))
                continue
            raise
        except requests.exceptions.RequestException as exc:
            last_exception = exc
            if attempt == retries - 1:
                break
            time.sleep(3 * (attempt + 1))

    if last_exception is not None:
        raise last_exception
    raise RuntimeError("request failed without an exception")


@mcp.tool()
def analyze_document_mineru(
    file_url: str,
    output_type: Literal["json", "fullmd"] = "fullmd",
    return_full_content: bool = False,
    max_return_chars: int = 8000,
) -> str:
    """
    Analyze document using MinerU v4 API and return content.

    Args:
        file_url: URL of the document file (PDF, etc).
        output_type: Output format, 'json' for structured data, 'fullmd' for markdown content.
        return_full_content: Whether to return entire content in this response. Default False.
        max_return_chars: Max characters returned when return_full_content=False.
    """
    token = os.environ.get("MINERU_TOKEN", "").strip()
    if not token:
        return "Error: MINERU_TOKEN environment variable is not set"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
    }

    create_url = f"{MINERU_BASE_URL}/extract/task"
    payload = {
        "url": file_url,
        "model_version": "vlm",
    }

    try:
        response = _make_request("POST", create_url, json=payload, headers=headers)
        response_json = response.json()

        if response_json.get("code") != MINERU_SUCCESS_CODE:
            return (
                f"Create Task Failed: {response_json.get('msg')} "
                f"(TraceID: {response_json.get('trace_id')})"
            )

        task_id = response_json.get("data", {}).get("task_id")
        if not task_id:
            return "Task created but no task_id returned"

        max_retries = 600
        wait_seconds = 2

        for _ in range(max_retries):
            time.sleep(wait_seconds)

            query_url = f"{MINERU_BASE_URL}/extract/task/{task_id}"

            try:
                status_response = _make_request("GET", query_url, headers=headers)
            except Exception as exc:
                return f"Query Task Error: {str(exc)}"

            status_json = status_response.json()
            if status_json.get("code") != MINERU_SUCCESS_CODE:
                return f"Query Task Failed: {status_json.get('msg')}"

            data = status_json.get("data", {})
            state = data.get("state")

            if state == MINERU_JOB_COMPLETED_STATUS:
                full_zip_url = data.get("full_zip_url")
                if not full_zip_url:
                    return "Task completed but no full_zip_url"

                content = process_zip(full_zip_url, output_type)
                output_dir = _ensure_output_dir()
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                safe_name = _safe_name_from_url(file_url)
                suffix = "md" if output_type == "fullmd" else "json"
                short_task = (task_id or "noid")[:8]
                out_name = f"{timestamp}_{safe_name}_{short_task}.{suffix}"
                out_path = os.path.join(output_dir, out_name)

                with open(out_path, "w", encoding="utf-8") as file_handle:
                    file_handle.write(content)

                content_to_return = content
                truncated = False
                if (not return_full_content) and max_return_chars > 0 and len(content) > max_return_chars:
                    content_to_return = content[:max_return_chars]
                    truncated = True

                result = {
                    "ok": True,
                    "task_id": task_id,
                    "state": state,
                    "output_type": output_type,
                    "saved_path": out_path,
                    "total_chars": len(content),
                    "returned_chars": len(content_to_return),
                    "truncated": truncated,
                    "content": content_to_return,
                }
                if truncated:
                    result["note"] = (
                        "Content is truncated in MCP response. "
                        "Use read_saved_result(file_path=..., start=..., length=...) for chunked reading."
                    )
                return json.dumps(result, ensure_ascii=False, indent=2)

            if state == MINERU_JOB_FAILED_STATUS:
                return f"Task Failed: {data.get('err_msg')}"

        return "Error: Task Timeout (20 minutes)"
    except Exception as exc:
        return f"Exception: {str(exc)}"


@mcp.tool()
def list_saved_results(limit: int = 20) -> str:
    """
    List recently saved MinerU cloud result files.

    Args:
        limit: Maximum number of files to return.
    """
    if limit <= 0:
        limit = 20
    if limit > 200:
        limit = 200

    output_dir = _ensure_output_dir()
    files = []
    for pattern in ("*.md", "*.json"):
        files.extend(glob.glob(os.path.join(output_dir, pattern)))
    files.sort(key=lambda path: os.path.getmtime(path), reverse=True)

    items = []
    for path in files[:limit]:
        stat = os.stat(path)
        items.append(
            {
                "file_name": os.path.basename(path),
                "file_path": path,
                "size_bytes": stat.st_size,
                "modified_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stat.st_mtime)),
            }
        )
    return json.dumps(
        {
            "ok": True,
            "output_dir": output_dir,
            "count": len(items),
            "items": items,
        },
        ensure_ascii=False,
        indent=2,
    )


@mcp.tool()
def read_saved_result(file_path: str, start: int = 0, length: int = 8000) -> str:
    """
    Read a saved MinerU cloud result file chunk by character offset.

    Args:
        file_path: Absolute path or file name under MINERU_OUTPUT_DIR.
        start: Start character offset (0-based).
        length: Number of characters to read.
    """
    try:
        abs_path = _to_abs_saved_path(file_path)
    except Exception as exc:
        return f"Error: invalid file_path - {str(exc)}"

    if not os.path.exists(abs_path):
        return f"Error: file not found - {abs_path}"

    if start < 0:
        start = 0
    if length <= 0:
        length = 8000
    if length > 200000:
        length = 200000

    with open(abs_path, "r", encoding="utf-8") as file_handle:
        content = file_handle.read()

    end = min(start + length, len(content))
    chunk = content[start:end]
    result = {
        "ok": True,
        "file_path": abs_path,
        "total_chars": len(content),
        "start": start,
        "end": end,
        "returned_chars": len(chunk),
        "reached_end": end >= len(content),
        "content": chunk,
    }
    return json.dumps(result, ensure_ascii=False, indent=2)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
