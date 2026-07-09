"""
Lesson 3: Introduction to Loops

Syntax covered (on top of Lessons 1-2):
  while condition:      repeats the block as long as condition is True
  for x in range(n):    repeats the block n times, x takes 0, 1, ..., n-1
  A while loop's condition must eventually become False, or it never stops.
    That means something inside the loop body has to change a variable
    the condition depends on.

NOTE: a REAL infinite loop would freeze the terminal, so this demo adds a
`safety_cap` purely so the file can run to completion during class.

Run as-is.
"""

print("=== The Infinite Loop Bug ===")

print("Simulating the broken loop with a safety cap of 10 prints:")
count = 0
safety_cap = 0
while count < 5 and safety_cap < 10:
    print(f"  count is still: {count}  (nothing updates it!)")
    safety_cap += 1  # this line ONLY exists to stop the demo, not a real fix
print("...and it would keep going forever without the cap. That's a crash.")
