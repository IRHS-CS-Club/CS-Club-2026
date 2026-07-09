"""
Lesson 4: Functions & Code Quality
Goal: Wrap reusable logic in a function so it can run multiple times cleanly.
"""

print("=== Custom Greeting Engine ===")


# ---- TASK 0: same bug category as the demo, different function ----
def is_old_enough_to_vote(age):
    # 📝 TODO: fix the comparison -- voters need to be AT LEAST 18
    return age <= 18


print(f"21-year-old can vote: {is_old_enough_to_vote(21)}")


# ---- TASK: turn a hardcoded greeting into a reusable function ----
# PSEUDOCODE:
#   function greet(name, is_vip):
#       if is_vip: message = "Welcome back, VIP " + name + "!"
#       else: message = "Hello, " + name + "!"
#       return message

# 📝 TODO: give this function a parameter called `name` and one called `is_vip`
def greet(name, is_vip):
    # 📝 TODO: rebuild the Lesson 2 style if/else here, using the parameters
    if False:
        message = f"Welcome back, VIP {name}!"
    else:
        message = f"Hello, {name}!"
    # 📝 TODO: return message instead of just leaving it local
    pass


# Call it three times with different names — no copy-pasted code needed!
print(greet("Alex", False))
print(greet("Rivera", True))
print(greet("Chen", False))


# ==== EXTENSION: Reuse Without Rewriting ====
# Now that greet() exists, add a NEW parameter for a custom title
# ("Captain", "Doctor", etc.) without touching the print lines below.
#
# PSEUDOCODE:
#   function greet_with_title(name, title):
#       return title + " " + name + ", welcome!"

# 📝 TODO: define greet_with_title(name, title) and return a combined message
def greet_with_title(name, title):
    pass


print(greet_with_title("Rivera", "Captain"))
print(greet_with_title("Chen", "Doctor"))
