# 2026-07-09T20:40:49.445Z

Done. Summary of what changed across all 8 Track A lessons:

- **Headers**: `demo.py` docstrings are now syntax primers ("Syntax covered on top of Lessons 1-N: ...") for you to teach off at the whiteboard, not event labels. All "HUDDLE DEMO (10 min)", "WORKSHOP (35 min)", and "Low-Stress" fluff removed repo-wide (README included).
- **Traps redesigned to be architectural, not syntax quirks**: lesson 1 (missing parentheses → wrong order of operations), lesson 4 (flipped inequality hidden inside a function), lesson 5 (flipped sort direction, missing `reverse=True`), lesson 8 (AI code with a flipped inequality that runs silently wrong, plus an off-by-one boundary bug in the workshop). Lessons 2 (condition ordering), 3 (missing loop update), and 6 (greedy algorithm choice) were already architectural, so I only retitled/retrimmed them — the bugs themselves are unchanged. Lesson 7 has no runtime bug by nature (it's about comment quality), so it's untouched apart from the header.
- Every `fill_in_the_blanks.py` Task 0 now mirrors whichever bug actually appears in its `demo.py`.

Verified: all files `py_compile` clean, every `demo.py` runs and reproduces its stated wrong output. Nothing staged or committed — say the word when you want it pushed.
