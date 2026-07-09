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

# [💡 WHY]: .sort() mutates `scores` directly and gives back nothing (None),
# because Python's convention is "if a method changes the object in place,
# it doesn't ALSO return it."

# [💡 THE FIX #1]: sort first, then print the variable — not the method call.
scores2 = [42, 7, 99, 15]
scores2.sort()
print(f"Fixed (in-place): {scores2}")

# [💡 THE FIX #2]: use sorted(), which RETURNS a new sorted list instead of
# mutating and returning None. Safe to print directly.
scores3 = [42, 7, 99, 15]
print(f"Fixed (sorted()): {sorted(scores3)}")
