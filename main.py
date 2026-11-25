"""Roast Your Fridge — round 2 entry.

Writes exactly one roast line to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt when the variable is unset).

Fully deterministic: the line is a constant in this file. No network,
no randomness, no clock, no input from the environment other than the
output directory path.
"""

import os
import sys

# The chosen line (122 characters). Crisper drawer: a detail every fridge
# owner recognises, twisted into witness protection, with the payoff —
# "refuse to come out and testify" — landing in the last few words.
LINE = (
    "My crisper drawer is where vegetables go to file for witness "
    "protection \u2014 even the carrots refuse to come out and testify."
)

MIN_LENGTH = 1
MAX_LENGTH = 140


def main() -> int:
    if not (MIN_LENGTH <= len(LINE) <= MAX_LENGTH):
        sys.stderr.write(
            "entry line is %d characters, outside %d-%d\n"
            % (len(LINE), MIN_LENGTH, MAX_LENGTH)
        )
        return 1
    if "\n" in LINE or "\r" in LINE:
        sys.stderr.write("entry line must be a single line\n")
        return 1
    if not LINE.strip():
        sys.stderr.write("entry line must not be only whitespace\n")
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)

    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
