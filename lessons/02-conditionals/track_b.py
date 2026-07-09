# COMPETITIVE CORE: Read 3 integers (triangle sides). Output Equilateral, Isosceles, or Scalene.
import sys

def solve():
    # 📝 TODO: Short-circuit conditional matrix
    sides = list(map(int, sys.stdin.readline().split()))
    if len(sides) < 3: return
    a, b, c = sides[0], sides[1], sides[2]
    
    if a == b == c: print("Equilateral")
    elif a == b or b == c or a == c: print("Isosceles")
    else: print("Scalene")

if __name__ == "__main__":
    solve()