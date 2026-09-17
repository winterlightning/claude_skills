# Provenance — `combination/`

Putting an icon back together out of its symbols' finished SVGs. `app/combine.py` decides *what*
gets combined and *where* each piece goes; everything in here is *how*, and none of it is this
repo's own work.

## Source

Copied 2026-08-14 from `/Applications/Workspaces/pictographic/pg_app_utility/`:

| Here | From | Role |
|---|---|---|
| `icon_combination/` | `icon_combination/` | the engine: SVG geometry → line segments, convex-hull buffering, segment clipping, the SVG writer |
| `box_combine.py` | `desktop/box_combine.py` | places each symbol at its measured box and folds them big-to-small, reusing the engine's erasure and writer |
| `run_combine.py` | *new* | this repo's equivalent of the `POST /api/combination/from-boxes` route in `desktop/server.py` |

`box_combine.py` has since diverged from the utility app's copy, in three areas. Nothing in
`icon_combination/` was touched for any of them — each works on the segments its parser produces,
through its own helpers, and writes back out with its own writer.

**Slicing.** A placement can carry percentages to take off the sides of its drawing before it is
placed — `keep_rect` / `slice_segments` / `slice_to` are new, and `_fold` applies a slice after
`clean_to` and names its work files by position as well as by sid, because one symbol placed
twice can now carry two different slices and a sid-only name would let one overwrite the other.

**Placement.** `_fold` no longer calls `process_state_icon` (the engine's step 2, which scales a
drawing into a box and centres it) for the sub icons. Every symbol goes through `fit_into`
instead, and `_state_data` builds the dict the erasure reads out of the engine's own hull and
buffer helpers round segments that are already placed. That is what lets a box said by hand be
snapped onto the canvas' whole units and stay there — a second fit would put the fractional
centring straight back. For a placement that is not snapped the two routes agree exactly; the
geometry is unchanged.

**Output.** `_fold` carries the bottom layer's segment count through every cut (`_survivors`), so
`write_svg` can hand the writer its two groups — `main-icon-clipped` for the main icon,
`state-icon` for the sub icons that cut it — instead of everything in the first and an empty
second. `MIN_SEGMENT_PER_CANVAS` also holds the erasure's exact-cut threshold to the ratio the
engine's own 1.0 had on the 1024 canvas, so a fold written at 64 is cut as finely as one at 1024
rather than rounded to whole segments.

The utility app in turn took `icon_combination/` verbatim from
`pg_app_processing/combination_jobs/side-combination/`; its own `PROVENANCE.md` is the record of
that hop and of the two edits made there (relative intra-package imports, and an `__init__.py`
that selects matplotlib's `Agg` backend before the submodules load). Both edits are in the files
copied here, so **nothing in `icon_combination/` or `box_combine.py` was modified again** — a
`diff -r` against the utility app should come back empty except for `combine_cli.py`.

`combine_cli.py` and `fit_canvas.py` were not both needed. `fit_canvas.py` is here because
`icon_combination/__init__.py` imports it; `combine_cli.py` is not, because it drives the *side*
combination ("big icon plus a badge"), which this repo never asks for.

## Why it was moved

Execute used to POST to `https://macmini.pictographic.ai/api/combination/from-boxes`. That made
changing how icons combine an edit to another repo on another machine, and left Execute dead
whenever the host was unreachable. It is a local subprocess now.

## What is NOT here: the grid snap

The route this replaces also ran its result through `snap_icon_into_keyshapes/stretch_to_fit.py`,
which stretches an icon onto the nearest of twelve key shapes, and returned that as
`snapped_url`. **That step was deliberately left behind.** So:

- no `combined_snapped.svg` — only `combined.svg`
- no shape label (`shape-square`, `shape-circle`, …) on a Positions row
- a composite's generated final is the unsnapped combine

`run_combine.py` still reports `snapped_file`, `snap_meta` and `snap_error`, always null/empty.
That is the seam: porting the snapper later means filling those three in and copying
`stretch_to_fit.py`, `fit_shapes.py`, `bbox_preview.py` and `grid_system/*.svg` (it also adds
`cairosvg` + `pillow` to the dependency list below). Nothing above `run_combine.py` has to change.

## Re-syncing

```bash
SRC=/Applications/Workspaces/pictographic/pg_app_utility
diff -r -x __pycache__ combination/icon_combination "$SRC/icon_combination"
diff combination/box_combine.py "$SRC/desktop/box_combine.py"   # three areas, see above
```

The first should report only the two files that were deliberately not copied —
`combine_cli.py` and that package's own `PROVENANCE.md`, which records the hop before this one
and is worth reading there. Anything else is a real upstream change. Copy it in as-is — the point of a verbatim port is that
the diff stays readable.

## Dependencies

`numpy`, `scipy` (ConvexHull), `shapely` (buffering / clipping) and `matplotlib` — see
`requirements.txt`. matplotlib is imported at module scope by four of the engine's files and is
only actually drawn on the `show_matplotlib=True` path, which nothing here takes.

They are needed by **this folder only**. `app/` remains stdlib-only, which is why `run_combine.py`
runs in its own interpreter: a missing dependency fails one Execute press with a readable message
instead of stopping the server. Point a different interpreter at it with
`SLOWSYM_COMBINE_PYTHON=/path/to/python3` or `--combine-python`.
