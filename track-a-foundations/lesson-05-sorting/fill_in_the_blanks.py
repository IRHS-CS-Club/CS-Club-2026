"""
WORKSHOP (35 min) — Lesson 5: Algorithms I — Sorting
Goal: Sort a messy list of arcade scores correctly.

SYNTAX CHEAT SHEET:
my_list.sort()      sorts IN PLACE, returns None
sorted(my_list)      returns a NEW sorted list, leaves original untouched
list[-1]             last element     list[-3:]  last three elements
"""

print("=== Arcade High-Score Board ===")

raw_scores = [340, 12, 9981, 250, 77, 4200, 15]

# ---- TASK: sort the scores from lowest to highest ----
# PSEUDOCODE:
#   sorted_scores = sorted(raw_scores)
# 📝 TODO: use sorted() (NOT .sort()!) so we get a usable return value
sorted_scores = []
print(f"Sorted scores: {sorted_scores}")


# ==== EXTENSION (Low-Stress): High-Score Tracker ====
# Now pull out just the top 3 highest scores from the sorted list.
#
# PSEUDOCODE:
#   top_three = the LAST three items of sorted_scores
#   print them in order from highest to lowest

# 📝 TODO: slice the last 3 items from sorted_scores
top_three = []
# 📝 TODO: reverse top_three so the highest score prints first
print(f"🏆 Top 3 High Scores: {top_three}")
