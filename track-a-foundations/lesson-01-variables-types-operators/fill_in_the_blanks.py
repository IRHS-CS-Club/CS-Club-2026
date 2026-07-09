"""
WORKSHOP (35 min) — Lesson 1: Variables, Types, & Operators
Goal: Build an RPG stat calculator using variables and math operators.

SYNTAX CHEAT SHEET:
Variables: name = value
Operators: + (add)  - (sub)  * (mult)  / (div)  ** (power)
Casting:   int("10") turns a string into a number
"""

print("=== RPG Stat Calculator ===")

# ---- TASK 1: Double the starting gold, then add a 50 bonus ----
# PSEUDOCODE:
#   final_gold = (starting_gold * 2) + 50
starting_gold = 100
# 📝 TODO: Finish the equation below
final_gold = 0
print(f"Final Gold: {final_gold}")

# ---- TASK 2: Square the base radius to get the damage zone area ----
# PSEUDOCODE:
#   damage_zone = base_radius ** 2
base_radius = 4
# 📝 TODO: Finish the equation below using **
damage_zone = 0
print(f"Damage Area: {damage_zone}")

# ---- TASK 3: Convert a player-typed level (string) into a real number ----
# PSEUDOCODE:
#   level_num = int(level_input)
#   next_level = level_num + 1
level_input = "5"  # pretend this came from input()
# 📝 TODO: cast level_input to an int before adding 1
level_num = 0
next_level = 0
print(f"Next Level: {next_level}")


# ==== EXTENSION (Low-Stress): The Secret Message ====
# Multiplying a SPACE by a number creates instant indentation.
# Try building your own terminal art with just * and +.
#
# PSEUDOCODE:
#   padding = " " * 10          (10 spaces)
#   message = padding + "You found a secret!" + padding
#   frame = "*" * 40
#   print frame, then message, then frame again

# 📝 TODO: build `padding` using " " multiplied by a number of your choice
padding = ""
message = padding + "You found a secret!" + padding
# 📝 TODO: build `frame` using "*" multiplied by a number of your choice
frame = ""

print(frame)
print(message)
print(frame)
