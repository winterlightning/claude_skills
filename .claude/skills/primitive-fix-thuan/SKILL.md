---
name: primitive-fix-thuan
argument-hint: <count> [--offset N] [--disapprove-status bad-stroke|meaning|manual-fix-request|other] [--worker name]
description: Claim a number of disapproved Pictographic solo icons from the shared production fix queue, redraw each one by running /primitive-make-ray on its original reference with the reviewer's feedback, upload the before and after drawings to production and report done or cannot-fix. Arguments: count, optional --offset, --disapprove-status and --worker. Generated from the contracts by icon_set/scripts/generate_skills.py; do not edit by hand.
---

# /primitive-fix-thuan — claim, redraw with /primitive-make-ray, upload

Arguments: $ARGUMENTS

This skill does **only the production part** of a fix: claim the icons, hand each one to
/primitive-make-ray, then upload the result and report it. All drawing, validation and
export rules are /primitive-make-ray's; do not author or repair geometry any other way.

Run from the repository containing `icon_set/`. The first number in the arguments is the
**count** of icons to claim (required; ask when it is missing). `--offset N` skips that many
claimable icons, `--disapprove-status` keeps one disapproval reason (`bad-stroke`, `meaning`,
`manual-fix-request`, `other`). The **worker name** identifies your machine on every call and is
**required**: take it from `--worker`, else from `$PICTOGRAPHIC_WORKER`; if neither is set, ask
the user for it (for example `thuan-mac`) before claiming anything. Never invent one from the
hostname, and never reuse a name you saw in the queue; the scripts refuse to run without it.

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

## 2. Redraw with /primitive-make-ray

For each block, run /primitive-make-ray on its **reference** path and follow that skill
completely. Two additions for a fix:

- The reviewer's feedback is the specification for the revision, and `before/<icon-id>.svg` is
  the drawing they rejected; look at both before drawing. Keep the `icon_id` of the block.
- This is a revision: author a **fresh** run even when an earlier
  `icon_set/work/primitive-make-ray/<source-uuid>/*/result.json` exists; that skip rule does not
  apply here.

Note the new `RESULT_DIR` it creates. A block whose reference line says `none` cannot go through
/primitive-make-ray: finish it as cannot-fix.

## 3. Upload and report

When the /primitive-make-ray run is valid with zero warnings:

```bash
python3 icon_set/scripts/primitive_fix.py finish --worker <name> --icon <icon-key> --run <make-ray RESULT_DIR> --outcome done --note "<what changed>"
```

`finish` loads the module from that run, validates it again, writes `after/` (module, SVG,
light/dark previews), `validation.txt` and `result.json` in the fix directory, uploads the after
drawing, module and validation to production, and reports **done**: the revision returns to
Ready for the reviewer. It refuses `done` (exit 2, nothing uploaded or reported) while the model
is invalid or has warnings; go back to /primitive-make-ray. When no meaning-preserving drawing
can pass, report instead (add `--run` when a run exists so its attempt is uploaded):

```bash
python3 icon_set/scripts/primitive_fix.py finish --worker <name> --icon <icon-key> [--run <make-ray RESULT_DIR>] --outcome cannot-fix --note "<the blocking check and element>"
```

The icon stays **Disapproved** with your worker name and note; reviewers find it with the Cannot
fix filter.

## 4. Report

For every claimed icon say the key, what the feedback asked for, the /primitive-make-ray
`RESULT_DIR` and its SVG, the validation status, and the outcome reported (done or cannot-fix).

## Never

- Fix an icon you did not claim, or claim more than the requested count.
- Edit registered modules, build, publish or push; the fix lives in the /primitive-make-ray
  run and is promoted separately.
- Report `done` without `finish`, or change the production status through `/api/reviews`.
- Leave a claimed icon without a `finish` call (done or cannot-fix).
