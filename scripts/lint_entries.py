#!/usr/bin/env python3
"""Validate data/entries.yml against schemas/entry.schema.json plus extras.

Extra checks beyond the JSON schema:
  - Slugs are unique across entries
  - Each entry.category exists in `categories`
  - Term names are unique
  - last_verified >= added
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write(
        "ERROR: PyYAML is required. Install with `pip install pyyaml`.\n"
    )
    sys.exit(2)

try:
    import jsonschema
    from jsonschema import Draft202012Validator
except ImportError:
    sys.stderr.write(
        "ERROR: jsonschema is required. Install with `pip install jsonschema`.\n"
    )
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "entries.yml"
SCHEMA = ROOT / "schemas" / "entry.schema.json"


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)


def main() -> int:
    data = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    errors: list[str] = []

    # 1. Schema validation
    validator = Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        path = "/".join(str(p) for p in err.path) or "(root)"
        # Try to enrich with the offending entry's term
        ctx = ""
        if (
            err.path
            and len(err.path) >= 2
            and err.path[0] == "entries"
            and isinstance(err.path[1], int)
        ):
            idx = err.path[1]
            try:
                term = data["entries"][idx].get("term", "?")
                ctx = f" (entry #{idx}: {term})"
            except (IndexError, KeyError, TypeError):
                pass
        errors.append(f"schema[{path}]{ctx}: {err.message}")

    if errors:
        for e in errors:
            fail(e)
        return 1

    # Past this point data conforms to schema. Do extra checks.
    categories: dict = data["categories"]
    entries: list = data["entries"]

    # 2. Slug uniqueness
    seen_slugs: dict[str, int] = {}
    for i, e in enumerate(entries):
        slug = e["slug"]
        if slug in seen_slugs:
            errors.append(
                f"duplicate slug '{slug}' at entry #{i} ({e['term']}) "
                f"— first seen at entry #{seen_slugs[slug]}"
            )
        else:
            seen_slugs[slug] = i

    # 3. Category refs valid
    for i, e in enumerate(entries):
        if e["category"] not in categories:
            errors.append(
                f"entry #{i} ({e['term']}): category '{e['category']}' "
                f"not declared in categories"
            )

    # 4. Term uniqueness
    seen_terms: dict[str, int] = {}
    for i, e in enumerate(entries):
        term = e["term"]
        if term in seen_terms:
            errors.append(
                f"duplicate term '{term}' at entry #{i} "
                f"— first seen at entry #{seen_terms[term]}"
            )
        else:
            seen_terms[term] = i

    # 5. last_verified >= added (string ISO date compares OK)
    for i, e in enumerate(entries):
        if e["last_verified"] < e["added"]:
            errors.append(
                f"entry #{i} ({e['term']}): last_verified ({e['last_verified']}) "
                f"is earlier than added ({e['added']})"
            )

    if errors:
        for e in errors:
            fail(e)
        return 1

    print(f"OK Lint passed: {len(entries)} entries, {len(categories)} categories.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
