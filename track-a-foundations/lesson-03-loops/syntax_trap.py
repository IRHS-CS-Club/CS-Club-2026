"""
HUDDLE DEMO (10 min) — Lesson 3: Introduction to Loops
Instructor projects this file and runs it live. No edits needed.

NOTE: a REAL infinite loop would freeze the terminal, so this demo adds a
`safety_cap` purely so the file can run to completion during class. The
comments show you exactly what the broken code looks like without it.
"""

print("=== The Infinite Loop Trap ===")

# 🔥 THE TRAP (do NOT run this for real — it never stops):
#
#   count = 0
#   while count < 5:
#       print(count)
#       # forgot: count = count + 1
#
# Since `count` never changes, `count < 5` is True forever, and Python
# just keeps printing 0 forever until you force-quit the program.

print("Simulating the broken loop with a safety cap of 10 prints:")
count = 0
safety_cap = 0
while count < 5 and safety_cap < 10:
    print(f"  count is still: {count}  (never increments!)")
    safety_cap += 1  # this line ONLY exists to stop the demo, not a real fix
print("...and it would keep going forever without the cap. That's a crash.")

# [💡 THE FIX]: always update the loop variable inside the loop body.
print("\nFixed version:")
count = 0
while count < 5:
    print(f"  count is now: {count}")
    count += 1  # <-- this line is what was missing
print("Loop finished cleanly because count eventually reached 5.")
