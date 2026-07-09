"""
HUDDLE DEMO (10 min) — Lesson 1: Variables, Types, & Operators
Instructor projects this file and runs it live. No edits needed.
"""

print("=== The String Multiplication Trap ===")

# Player enters their score. input() ALWAYS returns a string, even if the
# player types digits.
raw_score = "50"  # pretend the player typed: 50
print(f"raw_score is type: {type(raw_score)}")

# 🔥 THE TRAP: we want to DOUBLE the score (50 -> 100), so we multiply by 2...
doubled = raw_score * 2

print(f"raw_score * 2 = {doubled}")
print("Expected 100, got '5050' instead!")

# [💡 WHY]: Python's * operator means something different depending on type.
#   int * int   -> multiplication      (50 * 2 == 100)
#   str * int   -> repeats the text    ("50" * 2 == "5050")
# The fix: convert the string to a number FIRST with int(), then multiply.
fixed = int(raw_score) * 2
print(f"int(raw_score) * 2 = {fixed}  <-- this is what we actually wanted")
