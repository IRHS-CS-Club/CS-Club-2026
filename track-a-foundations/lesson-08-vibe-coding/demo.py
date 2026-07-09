"""
HUDDLE DEMO (10 min) — Lesson 8: Vibe Coding Tips & Tricks
Instructor projects this file and runs it live. No edits needed.
"""

print("=== The Prompt Blindness Trap ===")

# Imagine you already wrote this variable earlier in your script...
player_hp = 100

# 🔥 THE TRAP: you asked an AI "write code to reduce hp by 10 and print it"
# and pasted the answer in WITHOUT checking it matches your existing
# variable name. The AI guessed a plausible name, but guessed wrong.
try:
    exec("hp = hp - 10\nprint(hp)")
except NameError as e:
    print(f"💥 CRASH: {e}")
