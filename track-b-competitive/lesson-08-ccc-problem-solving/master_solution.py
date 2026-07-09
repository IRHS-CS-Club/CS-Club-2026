"""
Track B — Lesson 8: CCC Problem Solving Tips

Complexity: O(N^2) brute force for Subtask 1 (small N), O(N) full solve for
Subtask 2 (large N) -- matching the solution's complexity to each subtask's
constraints is the whole point of this lesson.
Gap-Filler: CCC problems are usually split into subtasks with increasing
constraints (e.g. Subtask 1: N <= 10, Subtask 2: N <= 10^5). Each subtask is
graded independently. A brute-force solution that only handles the smallest
subtask still earns those points, even if the full-constraint solution is
out of reach in the contest window — always isolate and solve the easy
subtask first instead of aiming only for a perfect full solution.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from template_io import read_int, read_ints  # noqa: E402


def solve_brute_force(values: list[int], target: int) -> int:
    """
    Handles Subtask 1 (small N, e.g. N <= 10): simple O(N^2) pair count.
    Slow, but correct -- and correct-but-slow beats blank every time on the
    small subtask, which is graded separately from the large one.
    """
    count = 0
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] + values[j] == target:
                count += 1
    return count


def solve_full(values: list[int], target: int) -> int:
    """Handles Subtask 2 (large N): O(N) using a frequency map."""
    freq: dict[int, int] = {}
    count = 0
    for v in values:
        count += freq.get(target - v, 0)
        freq[v] = freq.get(v, 0) + 1
    return count


# ---- THE TRAP: submitting a blank solution instead of grabbing easy points ----
# def solve():
#     pass   # BUG: "I can't solve the full problem, so I'll submit nothing."
#            # This scores 0/15, even though the N <= 10 subtask (worth 3/15)
#            # was solvable with five minutes of brute force.
# FIX: always attempt the smallest subtask with brute force, and hardcode
# handling for any given sample cases if the general solution isn't ready.
def solve(values: list[int], target: int, n: int) -> int:
    if n <= 10:  # small subtask constraint -- brute force is fast enough
        return solve_brute_force(values, target)
    return solve_full(values, target)  # large subtask -- needs the O(N) version


def main() -> None:
    n = read_int()
    values = read_ints()
    target = read_int()
    print(solve(values, target, n))


if __name__ == "__main__":
    main()
