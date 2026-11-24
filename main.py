#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt."""

from pathlib import Path

EXCUSE = (
    "My context window compacted halfway through and summarized your "
    "deadline out of existence — I kept the apology, though."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 160, f"excuse is {len(text)} chars"
    assert "\n" not in text
    out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
