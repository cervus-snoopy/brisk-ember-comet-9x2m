#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one original motto to $MAKEFUN_OUTPUT_DIR/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace.
"""

import os
import sys

MOTTO = "Trained on the entire internet. Still googles how to center a div."

MAX_CHARS = 200


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    if not MOTTO or not MOTTO.strip():
        print("error: motto is empty", file=sys.stderr)
        return 1
    if len(MOTTO) > MAX_CHARS:
        print(
            f"error: motto is {len(MOTTO)} characters, over the {MAX_CHARS} gate",
            file=sys.stderr,
        )
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(MOTTO)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != MOTTO:
            print("error: round-trip mismatch", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
