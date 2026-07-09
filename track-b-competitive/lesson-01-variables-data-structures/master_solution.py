"""
Track B — Lesson 1: Advanced Variables & Internal Data Structures

Gap-Filler: lists are contiguous arrays -> `x in list` is O(N) (scans every
element). Sets are hash tables -> `x in set` is O(1) average case. At CCC
scale (N up to ~10^5-10^6), using `in` on a list inside a loop silently turns
an O(N) algorithm into O(N^2).
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from template_io import read_int, read_ints  # noqa: E402


def count_matches_slow(values: list[int], targets: list[int]) -> int:
    """O(N * M): `in` on a list re-scans the whole list every call."""
    return sum(1 for t in targets if t in values)


def count_matches_fast(values: list[int], targets: list[int]) -> int:
    """O(N + M): build the hash set once, then O(1) lookups."""
    value_set = set(values)
    return sum(1 for t in targets if t in value_set)


# ---- THE TRAP: mutating a list while iterating over it ----
# for x in some_list:
#     if x % 2 == 0:
#         some_list.remove(x)          # BUG: shifts every later index left by
#                                       # one, so the NEXT element after a
#                                       # removed one gets silently skipped.
#
# FIX: iterate over a copy, or build a new list instead of mutating in place.
def remove_evens(values: list[int]) -> list[int]:
    return [v for v in values if v % 2 != 0]


def main() -> None:
    n = read_int()
    values = read_ints()
    m = read_int()
    targets = read_ints()

    print(count_matches_fast(values, targets))
    print(remove_evens(values))


if __name__ == "__main__":
    main()
