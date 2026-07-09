"""
Lesson 4: Functions & Code Quality

Syntax covered (on top of Lessons 1-3):
  def name(parameter):     defines a reusable block of code
      ...body...
      return value          hands a value back to whoever called it
  name(argument)             runs the function with a specific input
  A function's internal logic is hidden from the caller -- if the return
    value is wrong, you can't see why without reading the function itself.

Run as-is.
"""

print("=== Ride Eligibility Checker ===")


def is_tall_enough(height_cm):
    # BUG: flipped inequality. Riders need to be AT LEAST 120cm, but this
    # returns True for anyone UNDER 120cm instead.
    return height_cm <= 120


riders = [110, 125, 90, 150]
for height in riders:
    print(f"Height {height}cm -> allowed: {is_tall_enough(height)}")

print("A 150cm rider should be allowed. The function says False instead!")
