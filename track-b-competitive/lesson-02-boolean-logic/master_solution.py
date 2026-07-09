"""
Track B — Lesson 2: Boolean Logic & Simplifying Conditionals

Gap-Filler: De Morgan's Laws let you push `not` through and/or:
    not (A and B)  ==  (not A) or (not B)
    not (A or B)   ==  (not A) and (not B)
Useful for simplifying "reject if NOT valid" checks into direct accept
checks. Also: `and`/`or` short-circuit — the right side is never evaluated
if the left side already decides the result, which is safe to lean on for
guard clauses (e.g. `lst and lst[0] == target` avoids an IndexError on an
empty list).
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from template_io import read_ints  # noqa: E402


def in_valid_range_demorgan(x: int, low: int, high: int) -> bool:
    """
    Original: reject if (x < low) or (x > high)
    De Morgan: accept if NOT((x < low) or (x > high))
                      == (NOT x < low) AND (NOT x > high)
                      == (x >= low) AND (x <= high)
    """
    return x >= low and x <= high


def first_or_default(values: list[int], target: int, default: int = -1) -> int:
    """Short-circuit guard: `values and ...` skips the index check on []."""
    return values[0] if values and values[0] == target else default


# ---- THE TRAP: chaining comparisons without parentheses ----
# a < b < c is valid Python and means (a < b) and (b < c) — that part is
# fine. The real trap is mixing comparisons with `and`/`or` and assuming
# math-class operator precedence:
#     if not a == b or c == d:      # reads like "not (a==b or c==d)"
#         ...                       # actually means (not (a == b)) or (c == d)
# `not` binds tighter than `or` but looser than `==`, so intent gets lost.
# FIX: always parenthesize explicitly when mixing not/and/or.
def is_valid_pair_fixed(a: int, b: int, c: int, d: int) -> bool:
    return not (a == b or c == d)


def main() -> None:
    x, low, high = read_ints()
    print(in_valid_range_demorgan(x, low, high))


if __name__ == "__main__":
    main()
