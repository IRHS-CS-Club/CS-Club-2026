"""
Lesson 8: Vibe Coding Tips & Tricks
Goal: Practice checking AI-generated code against the actual requirement.
"""

print("=== AI Code Checkpoint ===")

# ---- TASK 0: Fix the flipped inequality from the demo ----
def qualifies_for_free_shipping(cart_total):
    # 📝 TODO: fix the comparison -- free shipping is for orders $50 and OVER
    return cart_total < 50


print(f"$75 order free shipping: {qualifies_for_free_shipping(75)}")


# ---- TASK: an AI wrote this against the requirement "double the reward
# for quests LEVEL 10 OR HIGHER" -- check it carefully against that wording ----
quest_level = 10
quest_reward = 100

# 📝 TODO: this should be True at quest_level == 10, not just above it.
# Find the off-by-one and fix the comparison.
if quest_level > 10:
    quest_reward = quest_reward * 2

print(f"Level {quest_level} reward: {quest_reward}")


# ==== EXTENSION: The Prompt Engineer ====
# Write a "debugging prompt" you could give an AI assistant that FORCES it
# to double-check boundary conditions (>, >=, <, <=) against the exact
# wording of a requirement. A good prompt gives explicit rules, not just a
# vague request.
#
# 📝 TODO: fill in a prompt template with at least 3 explicit rules
my_debugging_prompt = """
Act as a debugging assistant for my Python code. Rules:
1. Check every >, >=, <, <= against the EXACT wording of the requirement.
2. ... (add a second rule)
3. ... (add a third rule)

My code:
<paste your code here>
"""

print("My custom debugging prompt:")
print(my_debugging_prompt)
