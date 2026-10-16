#!/usr/bin/env python3
"""Offline Motion Prompt catalog lookup. Python 3 standard library only."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKS = ["motion", "camera", "ui", "lp", "photo"]

def rows():
    output = []
    for pack in PACKS:
        data = json.loads((ROOT / "upstream" / "packs" / pack / "meta.json").read_text(encoding="utf-8"))
        for index, entry in enumerate(data["elements"]):
            copy = dict(entry)
            copy["pack"] = pack
            copy["id"] = f"{PACKS.index(pack) * 24 + index + 1:03d}"
            output.append(copy)
    return output

def main(args):
    if not args or args[0] not in {"list", "search", "get"}:
        print("Usage: motion_lookup.py list | search <words> | get <id>", file=sys.stderr)
        return 2
    items = rows()
    if args[0] == "list":
        for e in items:
            print(f"#{e['id']} [{e['pack']}] {e['name'].get('en', '')}")
    elif args[0] == "search":
        query = " ".join(args[1:]).casefold()
        for e in items:
            content = " ".join(str(v) for v in e.values()).casefold()
            if query in content:
                print(f"#{e['id']} [{e['pack']}] {e['name'].get('en', '')}")
    else:
        if len(args) < 2:
            return 2
        ident = re.sub(r"\D", "", args[1]).zfill(3)
        e = next((e for e in items if e["id"] == ident), None)
        if e is None:
            print("Unknown ID", file=sys.stderr)
            return 1
        print(json.dumps(e, ensure_ascii=False, indent=2))
        print(f"\nSource: upstream/packs/{e['pack']}/pack.js")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
