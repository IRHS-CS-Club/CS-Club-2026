"""
Track B — Lesson 3: Time Complexity & Efficient Looping

Complexity: O(N) — a seen-set replaces the nested loop.
Gap-Filler: judges allow roughly 10^8 simple operations per second. An
O(N^2) algorithm on N = 10^5 is ~10^10 operations -> guaranteed TLE. The fix
is almost always trading a nested loop for a frequency array / hash map that
turns an O(N) inner lookup into O(1).
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from template_io import read_int, read_ints  # noqa: E402


# ---- NAIVE APPROACH (commented out -- this is what fails the judge) ----
# def has_pair_with_sum_naive(values: list[int], target: int) -> bool:
#     for i in range(len(values)):
#         for j in range(len(values)):
#             if i != j and values[i] + values[j] == target:
#                 return True
#     return False
# WHY IT FAILS: O(N^2). At N = 10^5 this is ~10^10 comparisons -- Time Limit
# Exceeded on any judge that enforces the ~10^8 ops/sec budget.


def has_pair_with_sum(values: list[int], target: int) -> bool:
    """O(N): frequency/seen-set replaces the inner loop entirely."""
    seen: set[int] = set()
    for v in values:
        if target - v in seen:
            return True
        seen.add(v)
    return False


def frequency_array(values: list[int], max_value: int) -> list[int]:
    """
    O(N + max_value): counts occurrences without ever comparing every pair
    of elements. Classic replacement for nested "count how many equal X"
    loops.
    """
    freq = [0] * (max_value + 1)
    for v in values:
        freq[v] += 1
    return freq


def main() -> None:
    n = read_int()
    values = read_ints()
    target = read_int()

    print(has_pair_with_sum(values, target))
    print(frequency_array(values, max(values) if values else 0))


if __name__ == "__main__":
    main()
