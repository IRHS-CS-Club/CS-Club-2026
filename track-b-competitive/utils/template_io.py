"""
Reusable I/O helpers for Track B (Competitive Core).

CCC's judge feeds input via stdin but does NOT support reading through
sys.stdin buffering tricks in the way some competitive setups do -- stick to
plain input()/print(). These helpers exist so every lesson parses input the
same way instead of re-deriving split()/map() boilerplate each time.
"""


def read_int() -> int:
    """Read a single integer from its own line."""
    return int(input())


def read_ints() -> list[int]:
    """Read one line of space-separated integers."""
    return list(map(int, input().split()))


def read_int_pair() -> tuple[int, int]:
    """Read exactly two space-separated integers from one line."""
    a, b = read_ints()
    return a, b


def read_str() -> str:
    """Read a single whitespace-trimmed token/line."""
    return input().strip()


def read_strs() -> list[str]:
    """Read one line of space-separated string tokens."""
    return input().split()


def read_int_grid(rows: int) -> list[list[int]]:
    """Read `rows` lines, each a row of space-separated integers."""
    return [read_ints() for _ in range(rows)]
