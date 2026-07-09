"""
Track B — Lesson 2 Challenge: Sensor Validity Checker

A sensor reading (a, b, c) is INVALID if `a` falls outside [low, high] OR
`b` equals `c`. Print True if the reading is VALID, False otherwise.

Don't just write `not (a is out of range or b == c)` directly -- use De
Morgan's Law to rewrite it as a direct ACCEPT condition (an AND of two
positive checks), and make sure every mixed not/and/or is parenthesized
so there's no ambiguity about evaluation order.

Input format:
    low high a b c   (five space-separated integers, one line)

Output format:
    True or False
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from template_io import read_ints  # noqa: E402


def solve(low: int, high: int, a: int, b: int, c: int) -> bool:
    # 📝 TODO: use De Morgan's Law to write this as a direct "is valid"
    # check (an AND of two positive conditions), not a negated OR.
    pass


def main() -> None:
    low, high, a, b, c = read_ints()
    print(solve(low, high, a, b, c))


if __name__ == "__main__":
    main()
