# COMPETITIVE CORE: Read line with two integers (A and B). Output (A^2) - B.
import sys

def solve():
    # 📝 TODO: Fast token parsing
    tokens = list(map(int, sys.stdin.readline().split()))
    if len(tokens) >= 2:
        print((tokens[0] ** 2) - tokens[1])

if __name__ == "__main__":
    solve()