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

total_damage = base_damage + crit_bonus * crit_multiplier

print(f"Total damage: {total_damage}")
print("Expected 30, got 20 instead!")
