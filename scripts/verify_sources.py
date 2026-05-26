#!/usr/bin/env python3
"""Verify all source URLs in data/entries.yml return 2xx.

Run by the scheduled GitHub Action once per month. Any failure exits
non-zero so the workflow opens a tracking issue.
"""
from __future__ import annotations

import sys
import urllib.error
import urllib.request
from collections import defaultdict
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

TIMEOUT_SECONDS = 5
USER_AGENT = (
    "prompt-lexicon-zh-verify/1.0 (+https://github.com/jasonhan/prompt-lexicon-zh)"
)


def load() -> dict:
    return yaml.safe_load(DATA.read_text(encoding="utf-8"))


def collect_url_to_refs(data: dict) -> dict[str, list[str]]:
    """Map URL -> sorted unique list of entry terms that reference it.

    Category defaults contribute the term of every entry that uses them.
    Per-entry source overrides contribute only that entry.
    """
    categories = data["categories"]
    url_to_terms: dict[str, list[str]] = defaultdict(list)

    for entry in data["entries"]:
        if "source" in entry and entry["source"]:
            src = entry["source"]
        else:
            src = categories[entry["category"]]["default_source"]
        url = src.get("url")
        if url:
            url_to_terms[url].append(entry["term"])

    # Deduplicate and sort
    return {u: sorted(set(terms)) for u, terms in url_to_terms.items()}


def check_url(url: str) -> tuple[bool, int | str]:
    """Return (ok, status_or_error). Follows redirects via default opener."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            status = resp.status
            return (200 <= status < 400, status)
    except urllib.error.HTTPError as e:
        return (False, e.code)
    except urllib.error.URLError as e:
        return (False, f"URLError: {e.reason}")
    except TimeoutError:
        return (False, "Timeout")
    except Exception as e:  # pragma: no cover  (defensive)
        return (False, f"{type(e).__name__}: {e}")


def main() -> int:
    data = load()
    url_to_terms = collect_url_to_refs(data)
    if not url_to_terms:
        print("No URLs to verify.")
        return 0

    broken: list[tuple[str, int | str, list[str]]] = []
    for url in sorted(url_to_terms):
        ok, status = check_url(url)
        if ok:
            print(f"OK   {url} ({status})")
        else:
            terms = url_to_terms[url]
            print(f"FAIL {url} ({status}) [used by: {', '.join(terms)}]")
            broken.append((url, status, terms))

    if broken:
        print()
        print(f"{len(broken)} broken URL(s) detected:")
        for url, status, terms in broken:
            print(f"  - {url} ({status}) used by: {', '.join(terms)}")
        return 1

    print()
    print(f"All {len(url_to_terms)} URL(s) reachable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
