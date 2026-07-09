"""
Lesson 5: Algorithms I — Sorting

Syntax covered (on top of Lessons 1-4):
  sorted(list)                 returns a NEW list, sorted ascending (low to high)
  sorted(list, reverse=True)    sorted descending (high to low)
  list[-1]                      last element    list[-3:]  last three elements

Run as-is.
"""

print("=== Arcade Leaderboard ===")

scores = [42, 891, 7, 340, 99]

leaderboard = sorted(scores)

print(f"Leaderboard (highest first): {leaderboard}")
print("Expected the biggest score first, got the smallest score first!")
