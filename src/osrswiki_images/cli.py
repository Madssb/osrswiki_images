from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Dict

from .client import search_all


def main() -> None:
    p = argparse.ArgumentParser(
        prog="osrswiki-images",
        description="Resolve OSRS names to wiki/image URLs using search_all().",
    )
    p.add_argument(
        "-i",
        "--input",
        default="-",
        help="Path to JSON array of strings (use '-' for stdin).",
    )
    p.add_argument(
        "-o", "--output", default="-", help="Path to write JSON (use '-' for stdout)."
    )
    p.add_argument(
        "--indent",
        type=int,
        default=2,
        help="JSON indent (default 2; use 0 for compact).",
    )
    args = p.parse_args()

    # read
    data = (
        sys.stdin.read()
        if args.input == "-"
        else open(args.input, "r", encoding="utf-8").read()
    )
    names: Any = json.loads(data)
    if not isinstance(names, list) or (names and not isinstance(names[0], str)):
        raise SystemExit("Input must be a JSON array of strings.")

    # resolve
    out: Dict[str, Dict[str, str]] = {}
    for name in names:
        rec = search_all(name)
        if rec:
            out[name] = rec  # {'wikiUrl','imgUrl'}

    # write
    text = json.dumps(out, ensure_ascii=False, indent=(args.indent or None))
    if args.output == "-":
        sys.stdout.write(text)
    else:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text)
