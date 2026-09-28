---
name: primitive-fix-thuan
description: Claim a number of disapproved Pictographic solo icons from the shared production fix queue, redraw each one by running $primitive-make-ray on its original reference with the reviewer's feedback, upload the before and after drawings to production and report done. Every claimed icon must be compared with its original and its current drawing and fixed; never asks, never skips. Arguments: count, optional --offset, --disapprove-status and --worker. Generated from the contracts by icon_set/scripts/generate_skills.py; do not edit by hand.
---

# $primitive-fix-thuan — claim, redraw with $primitive-make-ray, upload

Arguments: $ARGUMENTS

This skill does **only the production part** of a fix: claim the icons, hand each one to
$primitive-make-ray, then upload the result and report it. All drawing, validation and
export rules are $primitive-make-ray's; do not author or repair geometry any other way.

Run from the repository containing `icon_set/`. The first number in the arguments is the
**count** of icons to claim (default 1 when none is given). `--offset N` skips that many
claimable icons, `--disapprove-status` keeps one disapproval reason (`bad-stroke`, `meaning`,
`manual-fix-request`, `other`). The **worker name** is passed on every call: take it from
`--worker`, else from `$PICTOGRAPHIC_WORKER`, else use `thuan-mac`.

**Run unattended.** This skill exists to fix the icons reviewers marked wrong, and every
claimed icon **must be fixed**. Do not ask the user anything, do not pause between icons for
confirmation, and do not stop after a blocker: work through every claimed icon to `done`.
Where $primitive-make-ray says to ask or to stop (the `AUTHOR` question, a reported
blocker), do not: `AUTHOR` is the model ID you are running as, and a blocker means another
attempt, as in section 2.

## 1. Claim

```bash
python3 icon_set/scripts/primitive_fix.py start --worker <name> --limit <count> [--offset N] [--disapprove-status R]
```

It claims the icons on production (so no other machine fixes them), creates one fix directory
per icon at `icon_set/work/primitive-fix-thuan/<icon-key>/<run-id>/` with `brief.txt`,
`claim.json`, a `before/` copy of the registered module and the displayed SVG, and
`reference/<concept>_<source-uuid>.svg` (the original reference), uploads the before drawing to
production, and prints one block per icon: the icon key, the **reference** path, the `before/`
folder, the disapproval reason and the reviewer's **feedback**. Exit code 3 means nothing was
claimable: report that and stop.

## 2. Redraw with $primitive-make-ray

For each block, run $primitive-make-ray on its **reference** path and follow that skill
completely. Additions for a fix:

- **Review before drawing, every icon.** Render and open both the **original** (the
  `reference/` SVG) and the **current** drawing (`before/<icon-id>.svg`, the one the reviewer
  rejected). Write down what the current drawing gets wrong against the original and against
  the reviewer's feedback, then draw to correct exactly that. The feedback is the specification
  for the revision. Keep the `icon_id` of the block.
- When the reference line says the reference is the current drawing (no original on
  production), the icon is still fixed: redraw it from that drawing, the `icon_id` and the
  feedback. When it says `none`, redraw from the `icon_id` and the feedback.
- **A failing check is never the end.** When the geometry does not pass, try again: simplify or
  drop secondary detail, merge or enlarge parts, change the keyshape, restyle outlined parts as
  solid or single strokes, reduce counts (fewer letters, rays, teeth) as long as the subject
  still reads. Keep the element the feedback names and the subject's identifying silhouette;
  everything else may give way. Author each attempt as a fresh $primitive-make-ray run.
- This is a revision: author a **fresh** run even when an earlier
  `icon_set/work/primitive-make-ray/<source-uuid>/*/result.json` exists; that skip rule does not
  apply here.

Note the new `RESULT_DIR` it creates.

## 3. Upload and report

When the $primitive-make-ray run is valid with zero warnings:

```bash
python3 icon_set/scripts/primitive_fix.py finish --worker <name> --icon <icon-key> --run <make-ray RESULT_DIR> --outcome done --note "<what changed>"
```

`finish` loads the module from that run, validates it again, writes `after/` (module, SVG,
light/dark previews), `validation.txt` and `result.json` in the fix directory, uploads the after
drawing, module and validation to production, and reports **done**: the revision returns to
Ready for the reviewer. It refuses `done` (exit 2, nothing uploaded or reported) while the model
is invalid or has warnings; go back to section 2 and make another attempt until `finish`
accepts it. Do not report `cannot-fix` from this skill.

## 4. Report

For every claimed icon say the key, what was wrong in the current drawing compared with the
original, what the feedback asked for, what changed, the $primitive-make-ray `RESULT_DIR` and
its SVG, and the validation status.

## Never

- Fix an icon you did not claim, or claim more than the requested count.
- Edit registered modules, build, publish or push; the fix lives in the $primitive-make-ray
  run and is promoted separately.
- Report `done` without `finish`, or change the production status through `/api/reviews`.
- Ask the user a question, stop between icons, or end the run with a claimed icon unfixed.
- Draw without first comparing the original and the current drawing.
- Finish with `--outcome cannot-fix`, or leave a claimed icon without a `done` finish.
