"""
HUDDLE DEMO (10 min) — Lesson 4: Functions & Code Quality
Instructor projects this file and runs it live. No edits needed.
"""

print("=== The Scope Confusion Trap ===")


def roll_dice():
    # `result` is a LOCAL variable — it only exists inside this function.
    result = 6
    print(f"Inside the function, result = {result}")


roll_dice()

# 🔥 THE TRAP: trying to use `result` out here, in the main script.
try:
    print(f"Outside the function, result = {result}")
except NameError as e:
    print(f"\n💥 CRASH: {e}")
