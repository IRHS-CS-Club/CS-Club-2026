"""
Lesson 8: Vibe Coding Tips & Tricks

Syntax covered (on top of Lessons 1-7):
  AI-generated code can run without crashing and still be WRONG -- reading
    every condition and comparison it writes is not optional, since a
    flipped inequality won't throw an error, it'll just quietly return
    the wrong answer.

Run as-is.
"""

print("=== Free Shipping Checker ===")


def qualifies_for_free_shipping(cart_total):
    return cart_total < 50


orders = [30, 50, 75, 12]
for total in orders:
    print(f"Order ${total} -> free shipping: {qualifies_for_free_shipping(total)}")

print("A $75 order should qualify. The function says False instead!")
