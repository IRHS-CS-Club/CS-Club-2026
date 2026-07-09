"""
HUDDLE DEMO (10 min) — Lesson 2: Conditionals, Inputs, & Outputs
Instructor projects this file and runs it live. No edits needed.
"""

print("=== The Ordering Trap ===")

age = 20  # pretend a 20-year-old typed their age

# 🔥 THE TRAP: checking the LOOSER condition (age > 13) before the
# STRICTER one (age > 19). Once the first `if` matches, Python never even
# looks at the rest — so a 20-year-old gets stuck in the teen branch!
if age > 13:
    rating = "PG-13"
elif age > 19:
    rating = "R"
else:
    rating = "G"

print(f"Age {age} -> rated for: {rating}")
print("Expected R, got PG-13 instead!")

# [💡 WHY]: elif chains stop at the FIRST True condition, top to bottom.
# Fix: check the MOST restrictive / narrowest condition first.
if age > 19:
    rating = "R"
elif age > 13:
    rating = "PG-13"
else:
    rating = "G"

print(f"Fixed order -> rated for: {rating}  <-- correct!")
