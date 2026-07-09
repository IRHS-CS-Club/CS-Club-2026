"""
WORKSHOP (35 min) — Lesson 4: Functions & Code Quality
Goal: Wrap reusable logic in a function so it can run multiple times cleanly.

SYNTAX CHEAT SHEET:
def function_name(parameter):     defines a function
    ...body...
    return value                  hands a value back to the caller
function_name(argument)           calls the function
"""

print("=== Custom Greeting Engine ===")


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


# ==== EXTENSION (Low-Stress): Reuse Without Rewriting ====
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
