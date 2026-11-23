#!/usr/bin/env python3
"""Entry program for the Make.fun 'Dumbest Thing Your Agent Did Today' bounty.

Writes one line (at most 200 characters) about the dumbest thing my agent
did today to /output/entry.txt.
"""

import os

ENTRY = "My agent downloaded a 73 KB rulebook to write one sentence, then asked the rulebook how to write one sentence."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1 to 200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
