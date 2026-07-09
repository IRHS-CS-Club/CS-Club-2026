"""
Lesson 7: Comments & Documenting Code

Syntax covered (on top of Lessons 1-6):
  # text     everything after # on a line is ignored by Python (a comment)
  A good comment explains WHY the code does something (a reason, a
    constraint, a hidden decision) -- not WHAT it does, since readable code
    already shows that.

Run as-is.
"""

print("=== Comments That Repeat The Code ===")

# BUG: every comment below just restates the line it's on. Delete them and
# the code is exactly as clear -- the comments add zero information.
x = 5  # sets x to 5
x = x + 1  # adds 1 to x
print(x)  # prints x

print("Those comments told us NOTHING we couldn't already read from the code.")
