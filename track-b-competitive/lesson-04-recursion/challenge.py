"""
Track B — Lesson 4 Challenge: Digital Root

The digital root of a number is found by repeatedly summing its digits
until only one digit remains. E.g. 9875 -> 9+8+7+5=29 -> 2+9=11 -> 1+1=2.

Write `solve(n)` recursively. Think carefully about your base case: what
single-digit input should stop the recursion, and does every recursive
call actually get closer to it?

Input format:
    a single non-negative integer N

Output format:
    a single integer: the digital root of N
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from template_io import read_int  # noqa: E402


def solve(n: int) -> int:
    # 📝 TODO: base case -- what single-digit value of n should stop here?
    # 📝 TODO: recursive case -- sum n's digits, then recurse on that sum.
    pass


def main() -> None:
    n = read_int()
    print(solve(n))


if __name__ == "__main__":
    main()
