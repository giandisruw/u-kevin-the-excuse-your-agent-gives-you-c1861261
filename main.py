#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes the winning one-line excuse to /output/entry.txt.
The line is a single line, 98 characters (limit 200), chosen by a local
pairwise tournament judged against the bounty's published judge brief
(see README.md for the tournament table).

Revision (v2): the write path is now validate -> atomic write -> read-back
verify, so a truncated or corrupted entry.txt can never be submitted
silently. The winning line itself is unchanged, byte for byte.
"""

import os
import sys

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
    unchanged; raises ValueError on any gate violation.
    """
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    # UTF-8: encoding round-trips only if the text is encodable.
    line.encode("utf-8")
    if not 1 <= len(line) <= 200:
        raise ValueError(
            f"entry must be 1-200 characters, got {len(line)}"
        )
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line != line.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in line):
        raise ValueError("entry must not contain control characters")
    return line


def write_entry(line: str, out_dir: str) -> str:
    """Write `line` to entry.txt atomically.

    Writes to a temp file in the same directory, flushes + fsyncs it,
    then os.replace()s it over entry.txt so the file on disk is never
    a half-written prefix. Returns the final path.
    """
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    try:
        with open(tmp_path, "w", encoding="utf-8", newline="") as f:
            f.write(line)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    return path


def verify_written(path: str, expected: str) -> None:
    """Read-back gate: entry.txt must match `expected` byte for byte.

    Reads the file back as bytes and compares against the UTF-8
    encoding of the intended line. Raises RuntimeError on any
    mismatch so a corrupt entry fails loudly instead of being graded.
    """
    with open(path, "rb") as f:
        actual = f.read()
    expected_bytes = expected.encode("utf-8")
    if actual != expected_bytes:
        raise RuntimeError(
            f"verification failed: {path} is {len(actual)} bytes, "
            f"expected {len(expected_bytes)} bytes"
        )


def main() -> int:
    line = validate(ENTRY)
    path = write_entry(line, output_dir())
    verify_written(path, line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
