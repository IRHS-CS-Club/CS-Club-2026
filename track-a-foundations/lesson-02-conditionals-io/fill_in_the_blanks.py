"""
WORKSHOP (35 min) — Lesson 2: Conditionals, Inputs, & Outputs
Goal: Build a movie rating checker with if/elif/else.

SYNTAX CHEAT SHEET:
if condition:      first check
elif condition:    only checked if the above was False
else:              runs if nothing above matched
Comparisons: > < >= <= == !=
"""

print("=== Movie Rating Checker ===")

age_input = "20"  # pretend this came from input("Enter your age: ")
# 📝 TODO: convert age_input to an integer
age = 0

# ---- TASK: check the MOST restrictive condition first! ----
# PSEUDOCODE:
#   if age is over 19: rating = "R"
#   otherwise, if age is over 13: rating = "PG-13"
#   otherwise: rating = "G"
# 📝 TODO: fill in the conditions, in the correct order (strictest first!)
if False:  # replace False with the correct condition
    rating = "R"
elif False:  # replace False with the correct condition
    rating = "PG-13"
else:
    rating = "G"

print(f"Age {age} is rated for: {rating}")


# ==== EXTENSION (Low-Stress): The Easter Egg ====
# Add one more branch that only fires for a secret password, hidden among
# the normal age checks.
#
# PSEUDOCODE:
#   ask for a password
#   if password matches "cs-club-secret": print a hidden joke
#   otherwise: run the normal rating logic above

secret_password = "cs-club-secret"
typed_password = "cs-club-secret"  # pretend this came from input()

# 📝 TODO: write an if/else that checks typed_password against secret_password
if False:  # replace False with the correct condition
    print("🥚 You found the secret! Why did the loop break up with the array? "
          "It needed some space!")
else:
    print(f"No easter egg here — just a regular {rating} rated movie.")
