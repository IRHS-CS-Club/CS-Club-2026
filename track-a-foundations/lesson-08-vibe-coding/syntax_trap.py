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
    print("[💡 WHY]: the AI-generated code used `hp`, but YOUR script uses "
          "`player_hp`. Pasted code doesn't know your variable names unless "
          "you told it, or unless you check the names match before running.")

# [💡 THE FIX]: always read AI-generated code line-by-line before running
# it, and rename its variables to match what you already have.
player_hp = player_hp - 10
print(f"Fixed: player_hp = {player_hp}")

print("\nRule of thumb: never paste code you haven't read.")
