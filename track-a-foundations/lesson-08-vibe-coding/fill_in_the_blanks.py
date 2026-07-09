"""
Lesson 8: Vibe Coding Tips & Tricks
Goal: Practice checking AI-generated code against the actual requirement.
"""

print("=== AI Code Checkpoint ===")

# ---- TASK 0: same bug category as the demo, different function ----
def bonus_xp_eligible(player_level):
    # 📝 TODO: fix the comparison -- bonus XP is for level 20 and ABOVE
    return player_level < 20


print(f"Level 25 gets bonus XP: {bonus_xp_eligible(25)}")


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
