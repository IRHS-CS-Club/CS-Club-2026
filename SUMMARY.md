# 2026-07-09T20:30:50.592Z

All refinements are in and verified:

**Track A** — `syntax_trap.py` → `demo.py`, every demo trimmed to stop right after the trap prints its error (no inline fix/explanation left); the fix is now the first thing students do in `fill_in_the_blanks.py` (already the natural first task in most lessons, so I didn't bolt on a redundant "Task 0" where it'd duplicate work — only lesson 1 needed one since its trap was unrelated to the RPG calculator task).

**Track B** — every `master_solution.py` now has a `Complexity: O(...)` line up top and an actual **commented-out** naive/failing approach (not a live function) next to the efficient live solution. New `challenge.py` per lesson: distinct problem statement + `solve()` stub with `# 📝 TODO`, using `template_io.py`, for independent practice after you teach off `master_solution.py`.

**Verification:** `lessons/` and `setup-repo.sh` confirmed gone, all 42 `.py` files `py_compile` clean, every `demo.py` runs standalone, every `master_solution.py` still produces correct sample output, every `challenge.py` runs without crashing (unimplemented `solve()` returns `None` as expected).

Nothing staged or committed yet — let me know when you want that.
