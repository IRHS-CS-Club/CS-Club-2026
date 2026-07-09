"""
Lesson 2: Conditionals, Inputs, & Outputs

Syntax covered (on top of Lesson 1):
  input("prompt")            reads text typed by the user (always a string)
  if condition:               runs a block only if condition is True
  elif condition:              only checked if every condition above it was False
  else:                        runs if nothing above matched
  Comparisons: > < >= <= == !=
  elif/else chains stop at the FIRST True condition, top to bottom --
    everything after it is skipped, even if it would also be True.

Run as-is.
"""

print("=== Movie Rating Checker ===")

age = 20  # pretend a 20-year-old typed their age

# BUG: checking the LOOSER condition (age > 13) before the STRICTER one
# (age > 19). Because elif chains stop at the first True match, a
# 20-year-old satisfies "age > 13" and never reaches the "age > 19" check.
if age > 13:
    rating = "PG-13"
elif age > 19:
    rating = "R"
else:
    rating = "G"

print(f"Age {age} -> rated for: {rating}")
print("Expected R, got PG-13 instead!")
