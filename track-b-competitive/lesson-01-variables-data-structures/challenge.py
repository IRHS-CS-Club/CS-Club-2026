"""
Track B — Lesson 1 Challenge: Banned Username Filter

You're given a list of N banned usernames, followed by M login attempts.
For each login attempt, determine whether it matches a banned username.
Print the number of login attempts that ARE banned.

Constraints: N, M can be up to 10^5 -- an O(N * M) scan will NOT pass.
Use the List vs Set gap-filler from the lesson: build a set once, then check
membership in O(1) per attempt.

Input format:
    N
    N space-separated banned usernames
    M
    M space-separated login attempt usernames

Output format:
    a single integer: how many attempts were banned
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from template_io import read_int, read_strs  # noqa: E402


def solve(banned: list[str], attempts: list[str]) -> int:
    # 📝 TODO: build a set from `banned` for O(1) membership checks, then
    # count how many entries in `attempts` are present in that set.
    pass


def main() -> None:
    n = read_int()
    banned = read_strs()
    m = read_int()
    attempts = read_strs()

    print(solve(banned, attempts))


if __name__ == "__main__":
    main()
