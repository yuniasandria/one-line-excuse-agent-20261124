#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt (stdlib only)."""
import os

# The entry is a single line (120 chars). The line is assembled from
# two parts so the constant is easy to read and review in pieces.
PART_A = "Your prompt said 'take your time' and 'ASAP' in the same "
PART_B = "sentence, so I optimized for the contradiction and missed both."
LINE = PART_A + PART_B

def main():
    # Guard: the entry must stay exactly one line of 120 chars.
    assert "\n" not in LINE and len(LINE) == 120
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
