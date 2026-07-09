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

if age > 13:
    rating = "PG-13"
elif age > 19:
    rating = "R"
else:
    rating = "G"

print(f"Age {age} -> rated for: {rating}")
print("Expected R, got PG-13 instead!")
