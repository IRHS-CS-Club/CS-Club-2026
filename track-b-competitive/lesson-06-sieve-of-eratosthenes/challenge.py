"""
Track B — Lesson 6 Challenge: Primes in Range

Given two integers L and R (L <= R), count how many primes exist in the
inclusive range [L, R]. R can be up to 10^6 -- checking each number in the
range individually with a naive divisor-by-divisor test up to N is too
slow. Build a sieve up to R once, then count.

Input format:
    L R

Output format:
    a single integer: count of primes in [L, R]
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from template_io import read_ints  # noqa: E402


def solve(low: int, high: int) -> int:
    # 📝 TODO: build a Sieve of Eratosthenes up to `high`.
    # 📝 TODO: count how many indices in [low, high] are marked prime.
    pass


def main() -> None:
    low, high = read_ints()
    print(solve(low, high))


if __name__ == "__main__":
    main()
