"""
WORKSHOP (35 min) — Lesson 8: Vibe Coding Tips & Tricks
Goal: Practice checking AI-generated code before trusting it.

RULE OF THUMB: read every line an AI gives you, and confirm every variable
name it uses actually matches a name YOU already defined.
"""

print("=== AI Code Checkpoint ===")

# Your existing variables (pretend you wrote these earlier):
quest_name = "Dragon's Lair"
quest_reward = 250

# Below is a snippet an AI "generated" when asked to print a quest summary.
# It's using variable names that DON'T all match yours.
#
#   print(f"Quest: {quest_title} pays {quest_reward} gold")
#
# 📝 TODO: find the mismatched variable name above and fix it so this line
# would actually run without a NameError
quest_title = quest_name  # <-- one way to bridge the mismatch safely
print(f"Quest: {quest_title} pays {quest_reward} gold")


# ==== EXTENSION (Low-Stress): The Prompt Engineer ====
# Write a "debugging prompt" you could give an AI assistant that FORCES it
# to match your existing code style. A good prompt gives explicit rules,
# not just a vague request.
#
# 📝 TODO: fill in a prompt template with at least 3 explicit rules
my_debugging_prompt = """
Act as a debugging assistant for my Python code. Rules:
1. Only use variable names that already appear in my code below.
2. ... (add a second rule)
3. ... (add a third rule)

My code:
<paste your code here>
"""

print("My custom debugging prompt:")
print(my_debugging_prompt)
