# Hole and Pinch QA Guide

`core/qa_overlays.py` is the canonical rendered-geometry gate for enclosed
negative space and squeezed junctions in Unlimited Shapes ship SVGs. Run it
after emission, structural/grid validation, overlap review, and keyshape
validation, then inspect its visual and numeric evidence before delivery.

This guide covers operation and interpretation. The binding design rules remain
in [icon-rules.md](icon-rules.md), and repair examples are in
[negative-space-repair-examples.md](negative-space-repair-examples.md).

## What it detects

The validator rasterizes each finished SVG and reports:

- **Undersized enclosed holes:** background regions surrounded by paint whose
  largest inscribed radius is below the minimum.
- **Pinched junctions:** regions that appear solid only because nearby strokes
  were pushed together with too little paint depth.

These are related legibility failures. A hole cannot be “fixed” by squeezing it
closed; that converts it into a pinch and still fails the gate.

## Requirements

Run from the workspace root with the dependencies in `requirements.txt`
installed. The validator uses CairoSVG, OpenCV, NumPy, and Pillow.

```bash
python3 -m pip install -r requirements.txt
```

## Single-icon command

Pass only the selected ship SVG during a single-icon execution:

```bash
python3 core/qa_overlays.py <ship.svg> \
  --output-dir <qa-output-folder> \
  --min-radius-design-u 1 \
  --min-fill-depth-design-u 1
```

Example:

```bash
python3 core/qa_overlays.py work/building/output/building.svg \
  --output-dir work/building/qa/holes \
  --min-radius-design-u 1 \
  --min-fill-depth-design-u 1
```

Do not pass the source/reference SVG. The input is the clean emitted 24×24 ship
SVG. The program normalizes measurements to the 48u design canvas.

## Authorized batch command

The input may be a flat folder when the user has requested a batch:

```bash
python3 core/qa_overlays.py final-svg/ \
  --output-dir qa/hole-detection/ \
  --min-radius-design-u 1 \
  --min-fill-depth-design-u 1
```

Directory input is intentionally flat; the program checks `.svg` files directly
inside that folder and does not recurse.

## Pass rules

- Every enclosed region needs an inscribed radius of at least **1u** on the
  48×48 design canvas, equivalent to a 2u design diameter or 1px ship diameter.
- A solid junction must remain filled at least **1u** deep.
- Equality passes.
- An icon with no enclosed background region passes the hole portion.
- Any undersized hole or pinched junction makes the icon fail.

The report's per-file `status` and failure counts are the QA verdict. Always
inspect `hole-diameters.json`, the per-icon metrics, and the HTML report; do not
use process exit status alone as proof of a visual pass.

## Measurement model

Authored ship icons use a 2px stroke, equivalent to 4u on the design canvas.
For stable raster measurement, the validator narrows paint to a **1u measuring
stroke**. Pulling each painted edge inward by `d` grows a hole's measured radius
by the same `d`, so the validator raises its internal radius threshold by that
amount. With the regular 4u authored stroke, the effective measuring threshold
is 2.5u radius / 5u diameter.

This normalization does not loosen the authored rule. Each hole includes
`equivalent_radius_at_authored_stroke_design_u`, which restates the result on the
original 1u-radius design gate.

The same narrowed rendering exposes weak closures. If a junction opens into a
trapped pocket before the required fill depth, it is reported as a pinch with a
`closure_margin_design_u` measurement.

## Outputs

The output folder contains:

| Artifact | Purpose |
| --- | --- |
| `<icon>.metrics.json` | Per-icon holes, pinches, measurements, thresholds, and status |
| `<icon>_holes.png` | Painted overlay with numbered holes and red pinch markers |
| `hole-diameters.json` | Aggregate machine-readable results |
| `hole-diameters.csv` | Aggregate tabular measurements |
| `hole-radius-report.html` | Human-readable summary and evidence links |
| `hole_error/` | Current failing SVGs, overlays, metrics, and repair README |

The validator clears the files it owns in `hole_error/` before each run, so that
folder acts as the current repair queue rather than an accumulated history.

## How to review a result

1. Open `hole-radius-report.html` and identify every failed icon.
2. Open its `_holes.png` overlay.
3. Match each numbered hole or red pinch marker to the editable atom instances.
4. Read the per-icon metrics to confirm the measured radius or closure margin.
5. Check the true-size 24px SVG; numeric output does not replace visual review.
6. Record the affected instances, measurement, repair, and passing rerun under
   `holeDiameterChecks` or equivalent editable metadata.

## Repair order

Repair the editable atomic composition, never the flattened ship paths:

1. Enlarge the opening by growing its enclosure or moving adjacent parts apart.
2. Rebalance the composition so the identity-bearing detail can carry a legal
   opening.
3. Remove a complete non-identity-bearing part when the first two options cannot
   preserve recognition. Record the removal as `omit`.

Do not delete an arbitrary path fragment, clip the problem, or push surrounding
parts together until the opening disappears.

After any repair, regenerate the design and ship SVGs and rerun structural,
grid, overlap, keyshape, hole/pinch, and true-size checks. Keyshape validation
must be repeated because changing local paint can move the overall painted
bounds.

## Useful options

```text
--error-dir <folder>                 Override the default hole_error queue.
--samples-per-unit <integer>         Raster supersampling; minimum 4, default 32.
--min-radius-design-u <number>       Hole-radius gate; must be greater than 0.
--min-fill-depth-design-u <number>   Pinch gate; 0 disables pinch detection.
```

Keep the canonical values at `1` unless an explicitly authorized diagnostic run
requires otherwise. A relaxed diagnostic result does not replace the canonical
delivery gate.

## Blocker handling

If `core/qa_overlays.py` or its rendering dependencies are unavailable, report
the hole/pinch gate as blocked. Do not silently skip it and do not substitute a
detector that has not been validated against this measurement model.
