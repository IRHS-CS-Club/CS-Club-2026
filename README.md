# CS-Club-2026

Central code infrastructure and development environments for the 2026-2027 high school Computer Science club.

## Environment

Open this repo in VS Code with the Dev Containers extension (or GitHub Codespaces) to get a consistent Python 3.11 / Debian environment automatically — see `.devcontainer/`.

## Curriculum

Dual-track, 8-lesson curriculum. Each lesson is a 45-minute session: a 10-minute huddle (instructor demo) followed by a 35-minute workshop.

- **`track-a-foundations/`** — Foundational Sprints (6 students). Each lesson has:
  - `syntax_trap.py` — the huddle demo, run as-is to show a common bug live.
  - `fill_in_the_blanks.py` — the scaffolded workshop exercise, with a low-stress extension at the bottom.
- **`track-b-competitive/`** — Competitive Core (2 students), CCC-focused. Each lesson has:
  - `master_solution.py` — a complete, efficient reference solution covering that lesson's algorithmic gap, plus its associated trap.
  - `utils/template_io.py` — shared input-parsing helpers (plain `input()`/`print()` only — no `sys.stdin`, to match CCC's judge).
