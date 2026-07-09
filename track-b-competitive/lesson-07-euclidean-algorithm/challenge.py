"""
Track B — Lesson 7 Challenge: Fraction Reducer

Given a fraction numerator/denominator, reduce it to lowest terms using the
Euclidean algorithm for GCD. Print the reduced fraction as "num/den".

Watch out for the zero-denominator edge case raw competitive input can
throw at you -- don't let a division by zero crash your program.

Input format:
    numerator denominator

Output format:
    the reduced fraction, formatted as "num/den"
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from template_io import read_ints  # noqa: E402


def solve(numerator: int, denominator: int) -> str:
    # 📝 TODO: compute gcd(numerator, denominator) using the modulo-based
    # Euclidean algorithm, then divide both numerator and denominator by it.
    # 📝 TODO: handle denominator == 0 without crashing.
    pass


def main() -> None:
    numerator, denominator = read_ints()
    print(solve(numerator, denominator))


if __name__ == "__main__":
    main()
