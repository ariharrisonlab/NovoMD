"""Print the CHANGELOG section for a version, for the publish workflow.

Usage: python scripts/release_notes.py v1.5.2   (leading 'v' optional)
"""

from __future__ import annotations

import re
import sys


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: release_notes.py <version>", file=sys.stderr)
        return 2

    version = sys.argv[1].lstrip("v")
    text = open("CHANGELOG.md", encoding="utf-8").read()
    match = re.search(rf"^## \[{re.escape(version)}\][^\n]*\n(.*?)(?=^## \[)", text, re.S | re.M)
    body = match.group(1).strip() if match else "See CHANGELOG.md."
    print(f"{body}\n\n`pip install novomd=={version}`")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
