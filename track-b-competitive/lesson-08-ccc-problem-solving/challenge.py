"""
Track B — Lesson 8 Challenge: Longest Increasing Run (Subtasked)

Given a list of N integers, find the length of the longest run of
consecutive elements that are strictly increasing.
E.g. [1, 2, 1, 2, 3, 4, 1] -> longest run is [1, 2, 3, 4], length 4.

Subtask 1 (3/15 points): N <= 10 -- any correct approach earns these
points, even an unoptimized one. Do NOT leave this blank just because
Subtask 2 looks hard.
Subtask 2 (12/15 points): N <= 10^5 -- needs an O(N) single-pass approach.

Strategy reminder: get Subtask 1's points locked in first, THEN worry
about the general O(N) solution.

Input format:
    N
    N space-separated integers

Output format:
    a single integer: length of the longest strictly increasing run
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from template_io import read_int, read_ints  # noqa: E402


def solve(values: list[int]) -> int:
    # 📝 TODO: at minimum, get Subtask 1 (N <= 10) correct with any approach.
    # 📝 TODO: then optimize to a single O(N) pass for Subtask 2.
    pass


def main() -> None:
    n = read_int()
    values = read_ints()
    print(solve(values))


if __name__ == "__main__":
    main()
