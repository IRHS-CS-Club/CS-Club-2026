"""
HUDDLE DEMO (10 min) — Lesson 5: Algorithms I — Sorting
Instructor projects this file and runs it live. No edits needed.
"""

print("=== The Mutating vs Returning Trap ===")

scores = [42, 7, 99, 15]

# 🔥 THE TRAP: .sort() sorts the list IN PLACE and returns None.
# Printing the return value prints... None.
print(f"print(scores.sort()) -> {scores.sort()}")
print("Expected the sorted list, got None instead!")
print(f"But scores itself IS sorted now: {scores}")
