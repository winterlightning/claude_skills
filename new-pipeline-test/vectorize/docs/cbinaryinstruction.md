# cbinaryinstruction — running `png2svg` and `holecmp` standalone

Two self-contained command-line binaries, built from this directory
(`svg_extraction_polyline/c/`). Copy the two files anywhere and run them
from there — they read only their command-line arguments, write only
where told, and need no repo files, config, or environment variables.

| Binary | What it does |
|---|---|
| `png2svg` | PNG → SVG vectorization (the C port of the probe_fit → svg_point chain) |
| `holecmp` | Benchmark calculator: scores ANY result SVG against its source PNG (band + hole metrics, one JSON) |

## Requirements

- **macOS on Apple Silicon (arm64) only.** Only system libraries are
  used (`libSystem`, `libc++` — present on every macOS); GEOS is linked
  statically. Nothing to install.
- On Intel/Linux, rebuild instead: `./build.sh` here (GEOS static-lib
  recipe in `docs/BUILD.md`).
- The binaries are gitignored build artifacts — a fresh clone will not
  have them; copy the files themselves or rebuild.

## png2svg

```
./png2svg input.png                  # writes <stem>__N.svg into the CURRENT dir
./png2svg input.png --svg-dir DIR    # writes them into DIR
./png2svg input.png -o out.svg       # one object -> out.svg; N objects -> out.svg.<i>.svg
```

- One SVG per connected component (`<stem>__0.svg`, `<stem>__1.svg`, …).
- Coordinates are source-image pixels; each file carries a data-fitted
  viewBox and real per-stroke widths (`stroke-linecap="round"`).
- Progress line goes to stderr (`input.png: N svg(s)`); exit 0 on success.

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

## Typical standalone session

```bash
mkdir work && cd work
cp /path/to/png2svg /path/to/holecmp .
./png2svg icon.png --svg-dir .
./holecmp icon.png icon__0.svg | python3 -m json.tool
```

Runtime: ~0.05–0.3s per image for png2svg, ~0.2–1s for holecmp
(the band thickness map dominates).
