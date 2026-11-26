#!/usr/bin/env python3
"""Deadpan forecast for a city that does not exist.

Writes exactly one line (max 160 characters) to /output/entry.txt.
Fully offline and deterministic: no network, no randomness, no secrets.
"""

import os

ENTRY = (
    "In Varnwick, thick mist all morning, lifting by noon to reveal the town "
    "was never actually there; residents are asked to remain calm."
)


def main() -> None:
    line = ENTRY.strip()
    # Self-check: single line, 1-160 characters, not only whitespace.
    # (Gate counts characters; the line is plain ASCII, so bytes == chars.)
    assert 1 <= len(line) <= 160, f"line is {len(line)} chars, must be 1-160"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"
    assert len(line.encode("utf-8")) == len(line), "line must be ASCII-safe UTF-8"
    os.makedirs("/output", exist_ok=True)
    # Write exactly the line, no trailing newline.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
