#!/usr/bin/env python3
"""Verify all source URLs in data/entries.yml return 2xx.

Run by the scheduled GitHub Action once per month. Any failure exits
non-zero so the workflow opens a tracking issue.
"""
from __future__ import annotations

import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
import os
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

TIMEOUT_SECONDS = float(os.getenv("VERIFY_TIMEOUT_SECONDS", "5"))
MAX_RETRIES = int(os.getenv("VERIFY_MAX_RETRIES", "2"))
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


def check_url(url: str) -> tuple[bool, int | str, int]:
    """Return (ok, status_or_error, attempts). Follows redirects."""
    attempts = 0
    for attempt in range(1, MAX_RETRIES + 2):
        attempts = attempt
        req = urllib.request.Request(
            url,
            headers={"User-Agent": USER_AGENT},
            method="GET",
        )
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
                status = resp.status
                return (200 <= status < 400, status, attempts)
        except urllib.error.HTTPError as e:
            if e.code in {429, 500, 502, 503, 504} and attempt <= MAX_RETRIES:
                time.sleep(0.5 * attempt)
                continue
            return (False, e.code, attempts)
        except urllib.error.URLError as e:
            if attempt <= MAX_RETRIES:
                time.sleep(0.5 * attempt)
                continue
            return (False, f"URLError: {e.reason}", attempts)
        except TimeoutError:
            if attempt <= MAX_RETRIES:
                time.sleep(0.5 * attempt)
                continue
            return (False, "Timeout", attempts)
        except Exception as e:  # pragma: no cover  (defensive)
            if attempt <= MAX_RETRIES:
                time.sleep(0.5 * attempt)
                continue
            return (False, f"{type(e).__name__}: {e}", attempts)
    return (False, "Unknown", attempts)


def main() -> int:
    data = load()
    url_to_terms = collect_url_to_refs(data)
    if not url_to_terms:
        print("No URLs to verify.")
        return 0

    broken: list[tuple[str, int | str, list[str]]] = []
    for url in sorted(url_to_terms):
        ok, status, attempts = check_url(url)
        if ok:
            retried = " after retry" if attempts > 1 else ""
            print(f"OK   {url} ({status}){retried}")
        else:
            terms = url_to_terms[url]
            print(
                f"FAIL {url} ({status}; attempts={attempts}) "
                f"[used by: {', '.join(terms)}]"
            )
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
