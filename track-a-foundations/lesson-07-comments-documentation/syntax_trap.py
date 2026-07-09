"""
HUDDLE DEMO (10 min) — Lesson 7: Comments & Documenting Code
Instructor projects this file and runs it live. No edits needed.
"""

print("=== The Self-Explanatory Overload Trap ===")

# 🔥 THE TRAP: comments that just repeat what the code already says.
# These add noise without adding any new information.
x = 5  # sets x to 5
x = x + 1  # adds 1 to x
print(x)  # prints x

print("Those comments told us NOTHING we couldn't already read from the code.")

# [💡 THE FIX]: good comments explain WHY, not WHAT — the reasoning, the
# hidden constraint, the thing a reader can't get from the code alone.
max_players = 5  # capped at 5 -- the game server drops connection 6+
current_players = max_players + 1  # simulate an overflow attempt
if current_players > max_players:
    # Reject instead of crash: the server has no error handling past this
    # point, so we must never let current_players exceed max_players.
    current_players = max_players

print(f"Players allowed in: {current_players}")
print("This comment explains a reason a reader couldn't guess from the code alone.")
