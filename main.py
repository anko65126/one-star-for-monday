"""Entry program for 'One Star for Monday'.

The whole entry is one line, under 180 characters and at most 25 words:
a one-star review of Monday written as though Monday were a restaurant.
The joke is Monday-specific — seated at dawn, cold coffee, and a meeting
that could have been an email — ending with a firm "would not return".
"""

import sys
from pathlib import Path

LINE = "One star. Monday seated me at 6 a.m., served cold coffee and a meeting that could have been an email. Would not return."
# Reads like a real one-star restaurant review: seating, service, and the verdict, all Monday-specific.
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 180, f"line is {len(LINE)} characters, over the 180 limit"
    assert len(LINE.split()) <= 25, f"line is {len(LINE.split())} words, over the 25-word limit"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "line must not be blank"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} characters, {len(LINE.split())} words)")


if __name__ == "__main__":
    main(sys.argv)
