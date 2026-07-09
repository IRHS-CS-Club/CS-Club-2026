"""
HUDDLE DEMO (10 min) — Lesson 6: Algorithms II — Greedy Method
Instructor projects this file and runs it live. No edits needed.
"""

print("=== The Coin Change Trap ===")


def greedy_coin_count(amount, coins):
    coins = sorted(coins, reverse=True)  # always try the biggest coin first
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count


# Normal coin system: greedy always finds the FEWEST coins.
normal_coins = [25, 10, 5, 1]
print(f"Amount 41 with {normal_coins}: {greedy_coin_count(41, normal_coins)} coins")
print("Greedy gives 25+10+5+1 = 4 coins. That IS the true minimum. Greedy wins!")

# 🔥 THE TRAP: invent a weird coin system where greedy is no longer optimal.
weird_coins = [40, 35, 1]
amount = 70
greedy_result = greedy_coin_count(amount, weird_coins)
print(f"\nAmount {amount} with {weird_coins}: {greedy_result} coins (greedy)")
print("Greedy grabs 40, then has 30 left -> thirty 1-coins = 31 coins total!")
print("But 35 + 35 = 70 using only 2 coins. Greedy MISSED the better answer.")

# [💡 WHY]: greedy only works when the coin system has a special property
# (each coin is "big enough" relative to the others). It's a shortcut, not
# a guarantee — always check whether greedy is provably correct for YOUR
# specific problem before trusting it.
