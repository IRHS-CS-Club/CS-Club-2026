"""
WORKSHOP (35 min) — Lesson 6: Algorithms II — Greedy Method
Goal: Use a greedy strategy to pack the most valuable loot into a bag.

SYNTAX CHEAT SHEET:
sorted(list, key=..., reverse=True)   sorts by a custom rule, biggest first
for item in list: ...                 loop over each item
"""

print("=== Loot Bag Packer ===")

# Each item: (name, weight, value)
loot_table = [
    ("Gold Coin Pile", 10, 60),
    ("Ruby", 3, 30),
    ("Ancient Shield", 8, 40),
    ("Health Potion", 1, 5),
    ("Enchanted Sword", 5, 45),
]

max_weight = 15

# ---- TASK: greedily pick items by best value-per-weight until the bag is full ----
# PSEUDOCODE:
#   sort loot_table by (value / weight), highest first
#   bag = empty list
#   current_weight = 0
#   for each item in the sorted loot table:
#       if current_weight + item's weight <= max_weight:
#           add item to bag
#           current_weight += item's weight

# 📝 TODO: sort loot_table using a key of value/weight, biggest ratio first
sorted_loot = loot_table

bag = []
current_weight = 0
for name, weight, value in sorted_loot:
    # 📝 TODO: check if this item still fits under max_weight
    if False:
        bag.append(name)
        # 📝 TODO: update current_weight to include this item
        pass

print(f"Bag contents: {bag}")
print(f"Total weight used: {current_weight}/{max_weight}")


# ==== EXTENSION (Low-Stress): Try Breaking It ====
# Greedy-by-ratio is a heuristic, not a guarantee (just like the Coin Change
# Trap!). Try changing one item's weight or value above and see if the bag
# you get still "feels" like the best possible choice, or if a smarter
# combination could beat it.
