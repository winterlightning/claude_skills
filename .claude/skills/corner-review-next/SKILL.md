---
name: corner-review-next
description: Take the next 10 corner_processing icons nobody has reviewed yet (status todo in corner_processing/review/status.json), look at each one's SHARP output and decide, corner by corner, whether each corner is sharp or round (meaning and balance, with the corner-review reference examples) - ok, or a proposed round-or-sharp change with its drawing. The AI decides every icon; nothing is left for a human. One rule for every corner (corner-review §2): round only where the object is round; 70 deg and wider stays a plain sharp point; a narrow point stays full unless it runs into ink, fills an opening or reads as a stray spike - then its tip is cut flat, never rounded. Never moves a corner, changes an angle, redraws the input or touches the round output; records locally only, never publishes. Optional arguments - --take N (default 10), --offset K (skip the first K free icons) and --flag NAME. Use when asked to review the next corner icons, continue the corner review, or decide the next batch of round / sharp corners. Hand-authored; edit this file directly.
---

# Corner review — next 10

Each run takes **10 icons that have not been reviewed** and decides each one for the user. The rules, the cases
and the reference examples live in **`.claude/skills/corner-review/SKILL.md`**: read it first, every run (Rules,
§2 how to decide round or sharp, and the images in `.claude/skills/corner-review/examples/`). This skill is only the
procedure for one batch.

**Round or sharp only.** Every decision is which corners of the sharp output are sharp and which are round. The
round plate on the sheet is only a reference; never decide anything for the round output.

"Not reviewed" means status `todo` in `corner_processing/review/status.json` (a `reviewing` claim older than 6 h
counts as free again). Icons an earlier review left for a human (`needs-user`, or a `proposed` "report") count as
not reviewed and come first. Icons already `ok`, `proposed` (round or sharp), `decided` or `applied` are never taken.
Decisions stay local (`review/decisions.jsonl` and the review page); nothing is sent to production.

## 1. Take the batch

```bash
cd /Applications/Workspaces/pictographic/claude_skills
export CORNER_REVIEWER=<your model id>
/opt/homebrew/bin/python3 .claude/skills/corner-review-next/next10.py                       # next 10
/opt/homebrew/bin/python3 .claude/skills/corner-review-next/next10.py --take 5 --offset 20    # 5, after skipping 20
/opt/homebrew/bin/python3 .claude/skills/corner-review-next/next10.py --flag narrow-points    # only one flag
```

Pass on the user's arguments: `--take N` (how many, default 10), `--offset K` (skip the first K free icons in list
order, e.g. so two reviewers working at once start in different places), `--flag NAME`. The offset counts free
icons only, so after a batch is recorded, `--offset 0` is the next untouched icon again.

It claims the icons (`reviewing`, so no parallel reviewer gets them), draws a review sheet per icon and prints the
batch name, each sheet path, the flags, the checks, and the corners changed or kept (read the `sharp:` line). If it says there is
nothing to take, tell the user the todo list is empty and stop.

## 2. Decide every icon: each corner sharp or round

The only decision is **which corners of the sharp output are sharp and which are round** (corner-review §2: meaning,
balance, mirrored corners alike, a point that grows too far, big rounds). Never move a corner, change an angle,
redraw the input, or decide anything about the round output. **Apply corner-review §2 to every corner, steps in order:** (1) round only where a sharp corner would change what the object is
(a book spine, a handbag's soft body, a scroll's curl, a line that bends as a path, cable, smoke or rope) - never
for a name that says rounded, a rounded square, a phone, bottle, cloud or avatar, to hide a spike or to balance; (2) **70° or wider → a plain sharp point**, never cut, never round; (3) under 70°, cut the tip flat
(`--cut`) only when the full point runs into other ink, fills an opening, or reads as a stray spike; (4)
otherwise a full sharp point. Mirrored and repeated corners get one answer. When unsure: sharp.

For each icon, in order:

1. **Look.** Read its sheet PNG (Read tool): the 48 px sharp icon first, then the big sharp plate, against the input.
   Ignore the round plate. Flags are hints only.
2. **Decide**:
   - every corner already right (the handbag example) → `ok`;
   - some corners should change (the book example: spine corners round, fore-edge sharp) → build the drawing and
     record `proposed` with `--decision "round or sharp"`;
   - you cannot tell → decide anyway with the tie-break rules in corner-review §2 (a fused or spiking point
     keeps its sharp corner with the tip cut flat, `--cut`, never round, and only when it touches other ink; a full point whose mirrored partner the keyshape shaved flat is shaved the same way with `--slice`, not
     rounded; otherwise `ok`). Never leave an icon for the user: no needs-user, no report.
3. **Build the drawing** for a proposal (from `corner_processing/`):

```bash
/opt/homebrew/bin/python3 ../.claude/skills/corner-review/round_or_sharp.py \
    review/batches/<batch>/batch.json <icon>.svg --round 8,4 8,44 --sharp 40,4 --cut 24,30 --slice 22,32:42,32
# -> {"paths": {"<path id>": {"old": ..., "new": ...}}, "missing": []}   pass "paths" to --paths
```

   `--round` puts a corner back to the input's own round (at a plain line join, a small round fillet); `--sharp`
   turns a kept-round corner into a point; `--cut X,Y` keeps a join sharp with its point cut flat where the
   input's round join ended (for a point that touches other ink); `--slice X,Y:A,B[:rot|:move]` shaves X,Y flat like its keyshape-cut
   partner A,B. The points are corner apexes as the sheet and `sharp_log` give them, or
   the join point in the path; `missing` must be empty. Look at it before recording: `preview.py` takes the same
   arguments plus an output PNG and draws input · sharp now · proposed.

4. **Record it** (from `corner_processing/`):

```bash
/opt/homebrew/bin/python3 review/record.py <batch> <icon>.svg --status ok --note "<what you saw>"
/opt/homebrew/bin/python3 review/record.py <batch> <icon>.svg --status proposed --decision "round or sharp" \
    --paths '<paths from round_or_sharp.py>' \
    --corners '[{"p":[8,4],"decision":"keep","why":"spine, round"}, {"p":[40,4],"decision":"corner","why":"fore-edge, sharp"}]' \
    --note "<which corners are round, which sharp, why it reads and is balanced>"
```

   In `--corners`, `keep` = round, `corner` = sharp, `cut` = sharp with the tip cut flat. Every icon of the batch gets a record. An icon you cannot
   finish: `python3 review/next_batch.py --release <batch>` puts the rest back to `todo`.

Never edit the input SVGs, the outputs, `core/toggle.py`, `status.json` or `decisions.jsonl` by hand, and never
publish (`core/publish.py` is the user's step).

## 3. Report

Rebuild the review page so it shows the decisions (about 10 s):

```bash
cd corner_processing && /opt/homebrew/bin/python3 reports/make_toggle48_report.py
```

The page is served at http://127.0.0.1:8749/toggle48_report.html (start it with
`python3 reports/serve_report.py --port 8749 --no-open` from `corner_processing/` if nothing answers there; 8748 is
the old folder's server). Filter **AI proposed** lists this batch's changes.

End with a short summary for the user: the batch name, how many `ok` / `proposed`, each `proposed` icon with its decision in a few
words, and how many icons are left
(the script prints it). A kind of problem you met more than once is worth naming, so it can become a case in
corner-review.
