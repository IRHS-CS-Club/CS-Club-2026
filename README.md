# CS-Club-2026

Central code infrastructure and development environments for the 2026-2027 high school Computer Science club.

## Environment

Open this repo in VS Code with the Dev Containers extension (or GitHub Codespaces) to get a consistent Python 3.11 / Debian environment automatically — see `.devcontainer/`.

## Curriculum

Dual-track, 8-lesson curriculum. Each lesson is a 45-minute session: a 10-minute huddle (instructor demo) followed by a 35-minute workshop.

- **`track-a-foundations/`** — Foundational Sprints (6 students). Each lesson has:
  - `demo.py` — the huddle demo, run as-is; stops right after the trap fires so the instructor can walk through the fix verbally.
  - `fill_in_the_blanks.py` — the scaffolded workshop exercise (fixing the trap is usually the first task), with a low-stress extension at the bottom.
- **`track-b-competitive/`** — Competitive Core (2 students), CCC-focused. Each lesson has:
  - `master_solution.py` — the instructor's whiteboard teaching aid: the efficient solution, a commented-out naive approach that would fail the judge, and a top-line complexity note.
  - `challenge.py` — a distinct practice problem (problem statement in the docstring, `solve()` stub) for students to attempt independently after the concept is taught.
  - `utils/template_io.py` — shared input-parsing helpers (plain `input()`/`print()` only — no `sys.stdin`, to match CCC's judge).
