"""
WORKSHOP (35 min) — Lesson 7: Comments & Documenting Code
Goal: Rewrite bad "what" comments as good "why" comments.

RULE OF THUMB: if a comment could be deleted and the code still explains
itself just as well, the comment isn't pulling its weight.
"""

print("=== Comment Cleanup ===")

# Below are three lines with BAD comments (they just repeat the code).
# 📝 TODO: replace each comment with a WHY comment, or delete it if the
# code is already self-explanatory without one.

inventory_limit = 20  # sets inventory_limit to 20
# 📝 TODO: rewrite this comment to explain WHY 20 was chosen (make up a reason!)

current_items = 18  # sets current_items to 18
# 📝 TODO: delete this comment entirely — is it needed at all?

if current_items >= inventory_limit:  # checks if current_items >= inventory_limit
    # 📝 TODO: rewrite this comment to explain WHY we check this, not WHAT
    print("Inventory full!")
else:
    print(f"Room for {inventory_limit - current_items} more items.")


# ==== EXTENSION (Low-Stress): The Mystery Code Exchange ====
# Swap this function with a partner AFTER deleting the function's name and
# all its comments below. Can they guess what it does just from reading the
# code itself? If not, the code (not the comments) needs better naming.
#
# 📝 TODO: pick a small function you wrote earlier this term, strip its
# comments, rename it something generic like `mystery_function`, and trade
# with a partner.
def mystery_function(n):
    result = []
    for i in range(2, n):
        if n % i == 0:
            result.append(i)
    return result


print(mystery_function(30))
