# process.sh — PNG → raw SVG → grid-snap → corner-round (+ QA overlays)

The per-icon pipeline runner. Takes one or more input PNGs and drives every
stage, landing all results in `output/<stem>/` next to the script.

```bash
./process.sh input.png [more.png ...]        # full pipeline
RAW_ONLY=1 ./process.sh input.png            # stop after the raw stage (+ QA)
SKIP_QA=1  ./process.sh input.png            # skip the QA overlay stage
```

Each run **purges that stem's prior outputs first** (`__N.svg` parts, raw,
snapped, rounded, metrics, `rounding_work/`) so a re-run with fewer components
never inherits stale parts. A stage failure warns and moves on to the next
PNG; files from the stages that already succeeded are kept.

## Stage 1 — raw extraction (`png2svg` + `combine_svgs.py`)

- `./png2svg <input.png> --svg-dir output/<stem>/` traces the PNG into
  per-object SVGs: `output/<stem>/<stem>__0.svg, __1.svg, …`
  (see `BINARY_USAGE.md` for the binary's flags; the script self-heals a
  missing execute bit on freshly copied binaries).
- `combine_svgs.py` merges the parts into one 1024×1024 SVG →
  `<stem>_raw.svg` (the canonical raw stage) plus `<stem>_final_raw.svg`
  (source-coordinate variant used for precision/recall scoring).

With `RAW_ONLY=1` the script stops here (after QA, unless `SKIP_QA=1`).
That is the batch workflow: `batch_process.sh` runs this raw stage over a
whole directory, then the snap and round stages are (re-)derived separately
by `./resnap.sh` and `./reround.sh`.

## Stage 2 — grid snap (`snap_icon_to_grid_rewrite/snap_to_grid/pipeline.py`)

```
python3 pipeline.py output/<stem>/<stem>_raw.svg --snap --final-only --no-show
```

Slices the icon at its symmetry axis, separates objects, snaps them to the
40×40 grid, mirrors the kept side back, and writes `final.svg`, which is
copied to `output/<stem>/<stem>_snapped.svg`. Notable behavior:

- Full circles and near-full arc curls pass through — snapped uniformly but
  never sliced/mirrored. Zero-length round-cap dots pass through with
  half-cell-snapped centers.
- **Asymmetric icons** (`SYMMETRICAL=FALSE` in the log, `"symmetrical":
  false` in `output/<stem>/meta.json`) pass through **as drawn** by default
  (`--skip-asymmetrical`, default on) — they are parked for a future
  asymmetric-specific algorithm. `--no-skip-asymmetrical` grid-snaps them
  anyway.
- Re-run just this stage over existing raws with `./resnap.sh [stems…]`
  (default sweep = stems with an `approved_pngs/<stem>.png`; asymmetric
  passthroughs are counted `ok-asym` in its summary).

## Stage 3 — corner rounding (`corner_rounding/`)

Runs `detect_symmetry.py` + `round_corners.py` **on the snapped SVG** (the
rounded stage is always derived from snapped — after any resnap, re-run
rounding). Every output path is redirected into
`output/<stem>/rounding_work/` (scratch: `rounded/`, `overlap/`,
`corner_detail.json`, `fit.json`, `symmetry.json`) so the full-dataset JSONs
inside `corner_rounding/` are never clobbered. The result is copied to
`output/<stem>/<stem>_rounded.svg`.

Re-run just this stage with `./reround.sh [stems…]`.

## Stage 4 — QA overlays (`qa_overlays.py`)

Runs on the **raw** SVG only (reusing the `svg_extraction/` producers),
scoring it against the source PNG:

- `<stem>_raw_distance_debug.png` — lowest-distance gate overlay
- `<stem>_raw_holes_area.png` — average-hole-diameter gate overlay
- `<stem>_raw_visual_comparison.png` — side-by-side visual check
- `<stem>_raw.metrics.json` — precision/recall (measured source-space via
  `<stem>_final_raw.svg`) + gate verdicts

`SKIP_QA=1` skips this stage in both full and `RAW_ONLY` runs.

## Output layout

```
output/<stem>/
  <stem>__0.svg, __1.svg, …        per-object SVGs (png2svg)
  <stem>_raw.svg                   combined 1024² raw SVG      (stage 1)
  <stem>_final_raw.svg             source-coordinate combined SVG
  <stem>_snapped.svg               grid-snapped                (stage 2)
  meta.json                        verdict / symmetrical / snap_skipped / axes
  <stem>_rounded.svg               corner-rounded              (stage 3)
  rounding_work/                   rounding scratch
  <stem>_raw_*.png, _raw.metrics.json   QA overlays + gates    (stage 4)
```
