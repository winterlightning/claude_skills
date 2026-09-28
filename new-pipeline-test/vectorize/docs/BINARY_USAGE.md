# Using the binaries — `png2svg` (the master binary) and `holecmp`

`png2svg` lives in `png2svg/`, `holecmp` in `score/`; both are
committed to the repo, so a fresh clone runs without building. They are
self-contained:
copy the file anywhere and run it — only command-line arguments are
read, output goes only where told, no config or environment needed.

| Binary | What it does |
|---|---|
| `png2svg` | PNG → SVG. THE master binary: runs every vectorization flow in the repo (legacy pipeline included, in-process) and ships the best SVG per object |
| `holecmp` | Benchmark calculator: scores ANY result SVG against its source PNG (band + hole metrics, one JSON) |

## Requirements

- **macOS on Apple Silicon (arm64).** Runtime deps are `libSystem` and
  `libc++` only — present on every macOS. GEOS, cairo, pixman,
  shape_match and the legacy pipeline are all statically linked.
- On Intel/Linux, rebuild: `png2svg/build.sh`
  (GEOS recipe in [BUILD.md](BUILD.md); the script also builds the
  `shape_match` lib and the legacy objects it links).

## png2svg

```
./png2svg input.png                  # <stem>__N.svg into the CURRENT dir
./png2svg input.png --svg-dir DIR    # into DIR
./png2svg input.png -o out.svg       # one object -> out.svg; N objects -> out.svg.<i>.svg
./png2svg input.png --snap           # winner stretched onto the icon grid
```

One SVG per connected component (`<stem>__0.svg`, `<stem>__1.svg`, …).
Coordinates are source-image pixels with a data-fitted viewBox and real
per-stroke widths. **Default output is unsnapped**; `--snap` applies
the legacy stretch-to-fit onto the 12 grid shapes.

### What the default does

The shape-level tournament ([MERGE.md](MERGE.md)): the legacy pipeline,
the polyline flow, the segfit flow, their symmetry variants, and
shape_match geometry transforms of each all run to their finals; whole
standalone shapes then compete by greedy boosted-ΔF1 against the
object's own ink (sym ×1.10, geo ×1.06, legacy & plain ×1.00), the
score.h judge vetoes degenerate compositions back to the best single
candidate, and ties ship the legacy result.

### Flags

| flag | effect |
|---|---|
| `--snap` | stretch-to-fit the winner onto the icon grid (default: unsnapped) |
| `--no-merge` | staged pairwise selection instead of the tournament — with `--no-geo` this is the byte-anchor path, identical to the pre-tournament binary |
| `--no-legacy` | drop the legacy-pipeline candidate |
| `--no-geo` / `--geo-always` | disable / force the geometry-identification transform |
| `--no-sym` / `--sym-always` | disable / force the symmetry flows |
| `--no-segfit` / `--segfit-always` | disable / force the segment-fit branch |
| `--segfit-dump PREFIX OUT.json OUT.svg` | segfit parity harness (drove the port-time gates vs `png2svg/ref_segfit/`) |

### Reading the stderr log

```
  sym: VH cx=546.0 cy=248.0 iou=0.992/0.993        # symmetry detected
  merge: + legacy shape (cand 0) dF1=0.9901 F1=0.9901   # shape selected
  merge: 1 shapes C_merged=100.00 C_best_single=100.00 (legacy) veto=-
  input.png: 9 svg(s)                               # done, exit 0
```

`merge:` summary per object: shape count, composed composite vs the
best single candidate (and its provenance), and the veto — `-` means
the merged composition shipped; `below_best_single` / `band_collapse` /
`hole_cliff` / `no_band` mean it fell back to the best single
candidate. In merged output every element carries
`data-prov="legacy|plain|sym|geo"`.

### Runtime

58-icon corpus, M-series MacBook (2026-07-20): **~3.8s per icon**
default tournament, ~1.2s per icon `--no-merge --no-geo`. Simple
single-loop icons ~2.8s, 9-object icons ~8s. The legacy pipeline pass
and the per-shape scoring dominate; images are independent, so batch
throughput scales with parallel invocations.

## holecmp

```
./holecmp source.png result.svg                     # metrics JSON on stdout
./holecmp source.png result.svg --json out.json     # also write the JSON to a file
./holecmp source.png result.svg --debug PREFIX      # also dump label-map .npy files
```

Works on ANY result SVG for that PNG — png2svg output, the production
pipeline's SVG, anything with paths/shapes. It is FLAGLESS about input
conventions and auto-detects (reporting its choices in the JSON):

- `align`: `identity` (SVG coordinates already source pixels) or `bbox`
  (step8-normalized SVG, mapped onto the source centerline bbox).
- `band.stroke`: `asis` (declared per-stroke widths are real) or `match`
  (placeholder widths — one uniform width fitted by pixel count;
  `band.stroke_matched` reports the fitted width).

JSON shape (stdout, one line):

```json
{"n_src":2,"n_render":2,"matched":2,"missing":0,"merged":0,"extra":0,
 "hole_p_mean":99.76,"hole_r_mean":98.78,"hole_score":98.78,
 "band":{"precision":85.54,"recall":98.41,"miss_pct":0.159,
         "spill_pct":1.446,"stroke":"asis","stroke_matched":null},
 "size":1024,"align":"identity",
 "holes":[{"id":0,"region":2,"area":17853,"cx":558.8,"cy":276.0,
           "status":"matched","precision":99.63,"recall":97.82,
           "render_id":2}, ...]}
```

Reading the numbers:

- **band** — pick_rule_band_metric verbatim: ×10-amplified precision/
  recall of the THICK render vs the ink band, 2.5px tolerance. The
  coverage signal (the only one that sees open strokes).
- **holes** — the SVG rendered at 1px; its enclosed regions vs the
  PNG's holes grown to the stroke centerline. `missing` = a loop broke
  open, `merged` = the wall between two holes broke, `extra` =
  spurious loop. Matched pairs score overlap P/R;
  `hole_score = 100 · Σ min(P,R) / (n_src + extra)` — an extra hole
  costs exactly as much as a missing one. `hole_score` is `null` when
  there is nothing to measure (no source holes, no extras).
- `--debug PREFIX` writes `PREFIX.src_mask.npy`, `PREFIX.src_region.npy`,
  `PREFIX.render_mask.npy`, `PREFIX.render_labels.npy`,
  `PREFIX.band_render.npy` — numpy-loadable label maps for overlays.

Note for snapped SVGs: score **unsnapped** output against the source
(snap distorts geometry away from the ink on purpose); holecmp's `bbox`
align mode copes, but the pre-snap result is the meaningful comparison.

## Typical standalone session

```bash
mkdir work && cd work
cp /path/to/png2svg /path/to/holecmp .
./png2svg icon.png --svg-dir .            # best SVG per object, unsnapped
./png2svg icon.png --snap --svg-dir out/  # grid-snapped variants
./holecmp icon.png icon__0.svg | python3 -m json.tool
```
