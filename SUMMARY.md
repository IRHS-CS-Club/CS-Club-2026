# 2026-07-09T21:02:46.091Z

Confirmed `ANSWER_KEY.md` is correctly ignored — it doesn't even show up in `git status`, and won't be committed or pushed.

**Summary:**
1. Removed every inline `# BUG: ...` explanation from `demo.py` — the code still runs and shows the wrong output (that's the visible symptom the class investigates together), but the diagnosis is gone from the file itself. All 8 explanations now live in `track-a-foundations/ANSWER_KEY.md`, with exact line-number references, gitignored so it stays local to you and never reaches the repo.
2. Fixed the demo/Task-0 overlap for lessons 1, 2, 4, 5, and 8 — each now uses a different domain, variable names, and numbers than its `demo.py` (team score vs. RPG damage, speed-fine tiers vs. movie rating, voting age vs. ride height, golf vs. arcade leaderboard, bonus XP vs. free shipping), while testing the identical underlying bug pattern. Lessons 3, 6, and 7 were already sufficiently separated, so I left those as-is.

Verified: all files `py_compile` clean, every `demo.py` still reproduces its bug's symptom correctly.

Nothing staged or committed — let me know when you want it pushed.
