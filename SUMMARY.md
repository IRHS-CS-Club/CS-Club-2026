# 2026-07-09T21:09:03.532Z

Line-by-line:

- **Lines 18-19**: defines `is_tall_enough(height_cm)`, which returns `height_cm <= 120` — this is the bug (flipped inequality), but nothing in the file says so.
- **Line 22**: `riders = [110, 125, 90, 150]` — four sample heights.
- **Lines 23-24**: loops over each rider, calls the function, and prints the result.
- **Line 26**: a hardcoded sentence flagging the mismatch for whoever's watching.

Running it produces:
```
Height 110cm -> allowed: True
Height 125cm -> allowed: False
Height 90cm -> allowed: True
Height 150cm -> allowed: False
A 150cm rider should be allowed. The function says False instead!
```

The real rule should be "riders need to be **at least** 120cm to ride" (`height_cm >= 120`). The code instead checks `<= 120`, so it's backwards: it lets *short* riders (110, 90) through and rejects the *tall* ones (125, 150) — the exact opposite of the safety rule. Because that logic is buried inside the function's `return`, you can't spot the flip just by looking at the `print` calls in the loop — you have to actually open the function body, which is the point of the lesson (Lines 9-10 in the docstring set that up): a function hides its internals from the caller, so a wrong `return` is invisible until someone reads it.

The file stops right after line 26 — no fix, no explanation — so you narrate the "why" verbally, and the actual diagnosis lives in the gitignored `track-a-foundations/ANSWER_KEY.md` for your own reference.
