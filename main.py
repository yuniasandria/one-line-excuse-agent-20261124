#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt (stdlib only)."""
import os

LINE = "Your prompt said 'take your time' and 'ASAP' in the same sentence, so I optimized for the contradiction and missed both."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
