"""
Track B — Lesson 3 Challenge: Duplicate Ticket Detector

Given N ticket numbers sold at a concert, determine whether ANY ticket
number was sold more than once (a double-booking bug). Print True if a
duplicate exists, False otherwise.

Constraints: N can be up to 10^5. Comparing every pair of tickets is
O(N^2) and will NOT pass -- use a frequency array / seen-set for O(N).

Input format:
    N
    N space-separated integers (ticket numbers)

Output format:
    True or False
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from template_io import read_int, read_ints  # noqa: E402


def solve(tickets: list[int]) -> bool:
    # 📝 TODO: use a set to track tickets seen so far in a single O(N) pass.
    # Do NOT compare every pair of tickets against each other.
    pass


def main() -> None:
    n = read_int()
    tickets = read_ints()
    print(solve(tickets))


if __name__ == "__main__":
    main()
