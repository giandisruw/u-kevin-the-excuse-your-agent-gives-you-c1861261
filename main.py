#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes the winning one-line excuse to /output/entry.txt.
The line is a single line, 98 characters (limit 200), chosen by a local
pairwise tournament judged against the bounty's published judge brief
(see README.md for the tournament table).
"""

import os

# Winning line (tournament winner — see README.md).
# Local tournament: 14 candidates, Swiss 4 rounds (28 games) + final,
# 58 judge calls on the Caffeine Inference router, every game played
# in both label orders. #11 led the Swiss at 3.35, #4 second at 2.7;
# the final went to #4, 0.75–0.25 (both calls, margins 2 and 3).
ENTRY = (
    "The compiler warned me. I read the warning, understood it, "
    "and shipped it anyway — growth mindset."
)


def output_dir() -> str:
    """Grader output dir: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> str:
    """Check `line` against the kit's sealed-scorer gate, verbatim.

    competition.yaml: "/output/entry.txt is UTF-8 text of 1 to 200
    characters, not only white space". Single-line follows from the
    task itself (one line, at most 200 characters). Returns the line
    unchanged; raises AssertionError on any gate violation.
    """
    assert isinstance(line, str), "entry must be text"
    # UTF-8: encoding round-trips only if the text is encodable.
    line.encode("utf-8")
    assert 1 <= len(line) <= 200, (
        f"entry must be 1-200 characters, got {len(line)}"
    )
    assert line.strip(), "entry must not be only whitespace"
    assert "\n" not in line and "\r" not in line, (
        "entry must be a single line"
    )
    return line


def main() -> None:
    line = validate(ENTRY)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
