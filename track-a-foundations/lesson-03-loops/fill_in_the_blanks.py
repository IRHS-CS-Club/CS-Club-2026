"""
Lesson 3: Introduction to Loops
Goal: Print a countdown using a while loop, without freezing the terminal.
"""

print("=== Rocket Launch Countdown ===")

# ---- TASK: count DOWN from 5 to 1, then print "Liftoff!" ----
# PSEUDOCODE:
#   count = 5
#   while count > 0:
#       print count
#       count = count - 1
#   print "Liftoff!"
count = 5
# 📝 TODO: write the while loop condition
while False:
    print(count)
    # 📝 TODO: don't forget to update count, or this loop never ends!
print("Liftoff!")


# ==== EXTENSION: The Loading Bar ====
# Use a loop + time.sleep() to animate a fake "Loading..." bar.
#
# PSEUDOCODE:
#   for each step from 1 to 20:
#       print a growing bar of "#" characters
#       pause briefly with time.sleep(0.1)
import time

# 📝 TODO: change the range() below to control how many steps the bar has
for step in range(1, 5):
    bar = "#" * step
    print(f"\rLoading: [{bar}]", end="")
    # 📝 TODO: add a short time.sleep() pause here to make it animate
print("\nDone!")
