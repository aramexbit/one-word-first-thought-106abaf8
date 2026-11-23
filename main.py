#!/usr/bin/env python3
"""Emit a single word to the output directory.

The program is fully deterministic: no randomness, no clock, no network,
no file reads. It writes exactly one word plus a trailing newline.
"""

import os
import sys

WORD = "vellichor"


def output_path():
    """Resolve where the entry file goes."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(directory, "entry.txt")


def write_entry(path):
    """Write the single word, one line, UTF-8."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(WORD + "\n")


def main():
    write_entry(output_path())
    return 0


if __name__ == "__main__":
    sys.exit(main())
