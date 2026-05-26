#!/usr/bin/env python3
"""Build DICTIONARY.md and QUICK-REFERENCE.md from data/entries.yml.

Single source of truth lives in data/entries.yml. Do not edit the
generated markdown files directly — they will be overwritten.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write(
        "ERROR: PyYAML is required. Install with `pip install pyyaml`.\n"
    )
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "entries.yml"
DICT_OUT = ROOT / "DICTIONARY.md"
QR_OUT = ROOT / "QUICK-REFERENCE.md"

DICT_HEADER = """# Prompt 辭典

可放入 prompt 的關鍵詞，全部從軟體工程、邏輯學、認知科學、語言學、品質保證五大領域借用而來。這本辭典不發明新詞、不收錄 prompt engineering 內部黑話（few-shot、RAG 等），只挑「已經在其他領域有明確定義、可以直接搬進 prompt 當控制詞使用」的術語。每個詞條給五個欄位：來源、權威參考、本義、Prompt 用法、範例，方便 Ctrl-F 翻完直接抄進對話框。

> 本檔由 `data/entries.yml` 經 `scripts/build.py` 自動生成，請勿直接編輯。
"""

QR_HEADER = """# Prompt 辭典速查表

關鍵詞的快速查詢表。點擊任一詞名跳轉到 [DICTIONARY.md](DICTIONARY.md) 對應的詳細詞條。

> 沒看到合用的詞？打開 [DICTIONARY.md](DICTIONARY.md) Ctrl-F 全文搜尋。
>
> 本檔由 `data/entries.yml` 經 `scripts/build.py` 自動生成，請勿直接編輯。
"""

CN_NUMERALS = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]


def load() -> dict:
    return yaml.safe_load(DATA.read_text(encoding="utf-8"))


def resolve_source(entry: dict, categories: dict) -> dict:
    """Return effective source for an entry (entry override or category default)."""
    if "source" in entry and entry["source"]:
        return entry["source"]
    return categories[entry["category"]]["default_source"]


def format_source(src: dict) -> str:
    """Render a source citation as markdown text (with or without link)."""
    name = src["name"]
    url = src.get("url")
    if url:
        return f"[{name}]({url})"
    return name


def group_entries_by_category(data: dict) -> dict[str, list[dict]]:
    """Preserve original entry order; group by category."""
    grouped: dict[str, list[dict]] = {key: [] for key in data["categories"]}
    for entry in data["entries"]:
        grouped[entry["category"]].append(entry)
    return grouped


def ordered_category_keys(data: dict) -> list[str]:
    """Return category keys sorted by their `order` field."""
    return sorted(
        data["categories"].keys(),
        key=lambda k: data["categories"][k]["order"],
    )


def build_dictionary(data: dict) -> str:
    parts: list[str] = [DICT_HEADER, "\n---\n"]
    categories = data["categories"]
    grouped = group_entries_by_category(data)

    for idx, cat_key in enumerate(ordered_category_keys(data)):
        cat_meta = categories[cat_key]
        numeral = CN_NUMERALS[idx] if idx < len(CN_NUMERALS) else str(idx + 1)
        parts.append(f"\n## {numeral}、{cat_meta['name']}\n")

        for entry in grouped[cat_key]:
            src = resolve_source(entry, categories)
            parts.append(f'\n<a id="{entry["slug"]}"></a>')
            parts.append(f"### {entry['term']} / {entry['english']}\n")
            parts.append(f"- **來源**：{entry['origin']}")
            parts.append(f"- **權威參考**：{format_source(src)}")
            parts.append(f"- **本義**：{entry['meaning']}")
            parts.append(f"- **Prompt 用法**：{entry['prompt_usage']}")
            parts.append(f"- **範例**：{entry['example']}\n")

        if idx < len(data["categories"]) - 1:
            parts.append("---\n")

    return "\n".join(parts).rstrip() + "\n"


def build_quick_ref(data: dict) -> str:
    parts: list[str] = [QR_HEADER, "\n---\n"]
    categories = data["categories"]
    grouped = group_entries_by_category(data)

    for idx, cat_key in enumerate(ordered_category_keys(data)):
        cat_meta = categories[cat_key]
        numeral = CN_NUMERALS[idx] if idx < len(CN_NUMERALS) else str(idx + 1)
        parts.append(f"\n## {numeral}、{cat_meta['name']}\n")
        parts.append("| 詞 | Prompt 用法 |")
        parts.append("|---|---|")
        for entry in grouped[cat_key]:
            parts.append(
                f"| [**{entry['term']}**](DICTIONARY.md#{entry['slug']}) "
                f"| {entry['short_usage']} |"
            )
        parts.append("")
        if idx < len(data["categories"]) - 1:
            parts.append("---\n")

    return "\n".join(parts).rstrip() + "\n"


def main() -> int:
    data = load()
    dict_md = build_dictionary(data)
    qr_md = build_quick_ref(data)
    DICT_OUT.write_text(dict_md, encoding="utf-8", newline="\n")
    QR_OUT.write_text(qr_md, encoding="utf-8", newline="\n")
    n = len(data["entries"])
    print(f"OK Built DICTIONARY.md and QUICK-REFERENCE.md ({n} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
