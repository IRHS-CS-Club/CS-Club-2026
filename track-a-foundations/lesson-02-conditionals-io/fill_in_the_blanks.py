"""
Lesson 2: Conditionals, Inputs, & Outputs
Goal: Build a speed camera fine calculator with if/elif/else.
"""

print("=== Speed Camera Fine Calculator ===")

over_limit_input = "35"  # pretend this came from input("km/h over the limit: ")
# 📝 TODO: convert over_limit_input to an integer
over_limit = 0

# ---- TASK: check the MOST restrictive condition first! ----
# PSEUDOCODE:
#   if over_limit is over 30: fine = "Severe"
#   otherwise, if over_limit is over 10: fine = "Moderate"
#   otherwise: fine = "Warning"
# 📝 TODO: fill in the conditions, in the correct order (strictest first!)
if False:  # replace False with the correct condition
    fine = "Severe"
elif False:  # replace False with the correct condition
    fine = "Moderate"
else:
    fine = "Warning"

print(f"{over_limit} km/h over the limit -> {fine}")


# ==== EXTENSION: The Easter Egg ====
# Add one more branch that only fires for a secret password, hidden among
# the normal checks.
#
# PSEUDOCODE:
#   ask for a password
#   if password matches "cs-club-secret": print a hidden joke
#   otherwise: run the normal fine logic above

secret_password = "cs-club-secret"
typed_password = "cs-club-secret"  # pretend this came from input()

# 📝 TODO: write an if/else that checks typed_password against secret_password
if False:  # replace False with the correct condition
    print("🥚 You found the secret! Why did the loop break up with the array? "
          "It needed some space!")
else:
    print(f"No easter egg here — just a regular {fine} fine.")
