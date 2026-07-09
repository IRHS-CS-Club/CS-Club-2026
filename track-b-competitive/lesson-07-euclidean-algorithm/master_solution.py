"""
Track B — Lesson 7: Divisibility & The Euclidean Algorithm

Complexity: O(log(min(a, b))).
Gap-Filler: gcd(a, b) == gcd(b, a % b), and gcd(a, 0) == a. Each step at
least halves the smaller number (in the worst case, Fibonacci-adjacent
inputs), giving O(log(min(a, b))) instead of checking every divisor up to
min(a, b).
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from template_io import read_ints  # noqa: E402


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b  # modular transformation -- the core of the algorithm
    return a


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b  # divide before multiplying to avoid overflow risk


# ---- THE TRAP: division by zero on raw competitive input ----
# def gcd_unsafe(a, b):
#     while b:
#         a, b = b, a % b        # fine here -- b starts nonzero by definition
#     return a
#
# lcm(a, 0)                      # BUG: gcd(a, 0) == a, so a // gcd(a, 0) is
#                                 # a // a == 1, seemingly fine... but if
#                                 # BOTH inputs are 0, gcd(0, 0) == 0 and the
#                                 # division `a // gcd(a, b)` crashes with
#                                 # ZeroDivisionError. Competitive inputs
#                                 # sometimes include edge-case zeros.
def lcm_safe(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0  # by convention, lcm involving 0 is defined as 0
    return a // gcd(a, b) * b


def main() -> None:
    a, b = read_ints()
    print(gcd(a, b))
    print(lcm_safe(a, b))


if __name__ == "__main__":
    main()
