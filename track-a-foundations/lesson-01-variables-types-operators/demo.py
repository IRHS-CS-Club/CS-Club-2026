"""
Lesson 1: Variables, Types, & Operators

Syntax covered:
  name = value              creates a variable
  print(f"text {name}")     prints text with a variable's value inserted
  + - * / **                add, subtract, multiply, divide, power
  Order of operations: * and ** happen BEFORE + and -, left to right.
    Use parentheses to force a different grouping: (a + b) * c

Run as-is.
"""

print("=== RPG Damage Calculator ===")

base_damage = 10
crit_bonus = 5
crit_multiplier = 2

# BUG: intent is (base_damage + crit_bonus) * crit_multiplier -- add the
# crit bonus, THEN double the total for a critical hit. Without the
# parentheses, Python multiplies crit_bonus by crit_multiplier first
# (order of operations), so the bonus never gets the multiplier applied
# to the sum the way the formula intended.
total_damage = base_damage + crit_bonus * crit_multiplier

print(f"Total damage: {total_damage}")
print("Expected 30, got 20 instead!")
