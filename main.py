#!/usr/bin/env python3
"""Invent a Word We Need (make.fun).

Coins one new English word — leavxiety — and writes it together with its
one-line definition to /output/entry.txt.

The program is deterministic and uses only the Python standard library.
It reads nothing from the network, the environment, or the filesystem
beyond what it ships, and it writes exactly one file: /output/entry.txt.
"""

import os

# The entry: one invented word plus a single-line definition.
# Total length: 87 characters (well inside the 1-140 gate).
ENTRY = (
    "leavxiety \u2014 the nagging worry, halfway to your destination, "
    "that you left the oven on."
)


def main() -> None:
    """Write the entry to /output/entry.txt, exactly as coined."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
