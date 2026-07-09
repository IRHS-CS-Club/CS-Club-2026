"""
Track B — Lesson 4: Recursion

Gap-Filler: every recursive call pushes a new frame onto the call stack.
Python's default recursion limit is ~1000 frames. A correct recursive
function needs (1) a base case that stops the recursion and (2) each call
to make measurable progress toward that base case.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from template_io import read_int  # noqa: E402


def factorial(n: int) -> int:
    if n <= 1:  # base case — stops the recursion
        return 1
    return n * factorial(n - 1)  # progress: n shrinks toward the base case


def fib_memo(n: int, cache: dict[int, int] | None = None) -> int:
    """Fibonacci with memoization -- avoids the exponential call-tree blowup
    of naive recursive fib by caching subproblem results."""
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:  # base case
        return n
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]


# ---- THE TRAP: an unreachable/missing base case ----
# def countdown_broken(n):
#     print(n)
#     countdown_broken(n - 1)          # BUG: no base case at all, or a base
#                                       # case like `if n == 0: return` that
#                                       # n never actually hits (e.g. n starts
#                                       # negative, or decrements by 2 and
#                                       # skips over 0).
#                                       # Result: RecursionError, stack overflow.
def countdown_fixed(n: int) -> None:
    if n < 0:  # base case reachable from ANY starting n, not just n == 0
        return
    print(n)
    countdown_fixed(n - 1)


def demo_stack_overflow() -> None:
    """Shows what the trap actually looks like, safely caught."""

    def broken(n):
        return broken(n - 1)  # no base case -> recurses forever

    try:
        broken(0)
    except RecursionError as e:
        print(f"Caught the trap: {type(e).__name__} — missing base case")


def main() -> None:
    n = read_int()
    print(factorial(n))
    print(fib_memo(n))
    demo_stack_overflow()


if __name__ == "__main__":
    main()
