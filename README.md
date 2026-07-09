# CS-Club-2026

Central code infrastructure and development environments for the 2026-2027 high school Computer Science club.

## Environment

Open this repo in VS Code with the Dev Containers extension (or GitHub Codespaces) to get a consistent Python 3.11 / Debian environment automatically — see `.devcontainer/`.

## Curriculum

Dual-track, 8-lesson curriculum. Each lesson: instructor demo, then independent work.

- **`track-a-foundations/`** — Foundational Sprints (6 students). Each lesson has:
  - `demo.py` — run as-is; the docstring is a syntax primer for the instructor's whiteboard explanation, and the code stops right after the (architectural, not syntax) bug fires so the fix is taught verbally.
  - `fill_in_the_blanks.py` — the scaffolded exercise (fixing the bug from the demo is usually the first task), with an extension at the bottom.
- **`track-b-competitive/`** — Competitive Core (2 students), CCC-focused. Each lesson has:
  - `master_solution.py` — the instructor's whiteboard teaching aid: the efficient solution, a commented-out naive approach that would fail the judge, and a top-line complexity note.
  - `challenge.py` — a distinct practice problem (problem statement in the docstring, `solve()` stub) for students to attempt independently after the concept is taught.
  - `utils/template_io.py` — shared input-parsing helpers (plain `input()`/`print()` only — no `sys.stdin`, to match CCC's judge).
