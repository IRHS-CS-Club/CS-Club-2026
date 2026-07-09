"""
Track B — Lesson 6: Prime Numbers & Eratosthenes' Sieve

Gap-Filler: to find ALL primes up to N, the Sieve of Eratosthenes runs in
O(N log log N) by crossing out multiples of each prime once, instead of
testing every number individually. This is the standard competitive-math
tool whenever a problem needs many primality checks up to a bound N.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from template_io import read_int  # noqa: E402


# ---- THE TRAP: naive primality check scanning all the way to N ----
# def is_prime_slow(n):
#     if n < 2:
#         return False
#     for i in range(2, n):           # BUG: checks every number up to N-1
#         if n % i == 0:
#             return False
#     return True
# FIX: a number n can only have a factor pair (a, b) where a <= sqrt(n), so
# it's enough to check divisors up to sqrt(n) — everything past that is a
# mirror of a factor you'd have already found.
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:  # stop at sqrt(n), not n
        if n % i == 0:
            return False
        i += 1
    return True


def sieve_of_eratosthenes(limit: int) -> list[int]:
    """Returns all primes <= limit in O(limit log log limit)."""
    if limit < 2:
        return []
    is_prime_flags = [True] * (limit + 1)
    is_prime_flags[0] = is_prime_flags[1] = False

    for p in range(2, int(limit**0.5) + 1):
        if is_prime_flags[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime_flags[multiple] = False

    return [n for n, flag in enumerate(is_prime_flags) if flag]


def main() -> None:
    limit = read_int()
    primes = sieve_of_eratosthenes(limit)
    print(primes)
    print(f"Count: {len(primes)}")


if __name__ == "__main__":
    main()
