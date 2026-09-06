# Hole and Pinch QA Guide

`core/qa_overlays.py` is the canonical rendered-geometry gate for enclosed
negative space and squeezed junctions in Unlimited Shapes native SVGs. Run it
after emission, structural/grid validation, declared-overlap review, and the
distance gate. Inspect its visual and numeric evidence, then run the keyshape
gate and native-size review. The shared acceptance order is
distance → holes/pinches → keyshape; all three must pass on the same final
geometry and resolved profile.

This guide covers operation and interpretation. The binding design rules remain
in [icon-rules.md](icon-rules.md), and repair examples are in
[negative-space-repair-examples.md](negative-space-repair-examples.md).

## What it detects

Per-icon metrics include `svgSha256` and `profileSha256`, binding measurements
to the exact SVG and resolved profile. A source change during measurement fails
verification. Acceptance also requires the recorded configured radius/fill-depth
thresholds to equal profile defaults; diagnostic overrides cannot approve output.

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

Pass only the selected native SVG during a single-icon execution:

```bash
python3 core/qa_overlays.py <ship.svg> \
  --icon-type <profile-name> \
  --output-dir <qa-output-folder>
```

Example:

```bash
python3 core/qa_overlays.py work/building/output/building.svg \
  --output-dir work/building/qa/holes
```

Do not pass the source/reference SVG. The input is the clean emitted native SVG.
The program measures against the selected profile's native canvas with 1u = 1px.
Internal raster supersampling is measurement precision, not another deliverable
or acceptance-review size.

## Authorized batch command

The input may be a flat folder when the user has requested a batch:

```bash
python3 core/qa_overlays.py final-svg/ \
  --icon-type <profile-name> \
  --output-dir qa/hole-detection/
```

Directory input is intentionally flat; the program checks `.svg` files directly
inside that folder and does not recurse. Use one icon type per invocation and
select only one canonical SVG per icon, not aliases or diagnostic copies.
Selected files need unique stems so their output artifacts cannot overwrite one
another.

## Pass rules

- Every enclosed region must meet resolved `validation.minimumEnclosedRadius`
  on the selected native canvas (built-in default 1u = 1px radius).
- A solid junction must meet resolved `validation.minimumSolidFillDepth`
  (built-in default 1u).
- Equality passes.
- An icon with no enclosed background region passes the hole portion.
- Any undersized hole or pinched junction makes the icon fail.
- Processing errors, missing inputs, native-size violations, and incomplete
  results fail closed; a zero hole count on an error row is not a pass.

The report's per-file `status` and failure counts are the QA verdict. Always
inspect `hole-diameters.json`, the per-icon metrics, and the HTML report; do not
use process exit status alone as proof of a visual pass. Exit `0` means every
selected input has a complete passing result and reports were written. Exit `1`
means a measurement, input, processing, or report-writing failure. Exit `2`
means invalid arguments or a selection consisting only of empty folders.

## Measurement model

Authored native icons use their configured `strokeWidth`; 1u equals 1px.
The following measurement example uses the built-in 4px stroke.
For stable raster measurement, the validator narrows paint to a **1u measuring
stroke**. Pulling each painted edge inward by `d` grows a hole's measured radius
by the same `d`, so the validator raises its internal radius threshold by that
amount. With the regular 4u authored stroke, the effective measuring threshold
is 2.5u radius / 5u diameter.

This normalization does not loosen the authored rule. Each hole includes
`equivalent_radius_at_authored_stroke_design_u`, which restates the result on the
authored configured-radius gate.

The same narrowed rendering exposes weak closures. If a junction opens into a
trapped pocket before the required fill depth, it is reported as a pinch with a
`closure_margin_design_u` measurement.

## Outputs

The output folder contains:

| Artifact | Purpose |
| --- | --- |
| `<icon>.metrics.json` | Per-icon measurements/status, or processing-error details when writable |
| `<icon>_holes.png` | Successful processing's painted overlay with numbered holes and red pinch markers |
| `hole-diameters.json` | Aggregate list with one result per selected input, including failures |
| `hole-diameters.csv` | Aggregate tabular measurements |
| `hole-radius-report.html` | Human-readable summary and evidence links |
| `hole_error/README.md` | Points to the current failing run, or records that the current run passed |
| `hole_error/run-<id>/` | Preserved failing-run diagnostics, with one numbered subfolder per failed input |

Failure folders are fresh per run; older evidence is retained, never cleared.
Each numbered folder includes an available SVG reference and, only when
processing succeeded, its overlay and metrics. Processing failures appear as
`status: "fail"` with a nonempty `processingErrors` list; their empty region lists
and zero counts do not certify geometry. A stale flat overlay from an earlier
run is not current evidence—consult the current aggregate and error README.

Use separate QA folders. A QA or error directory containing a selected input is
rejected, and the error directory cannot equal or contain the QA output folder.
The default nested `hole_error/` is allowed. Report paths that would overwrite
selected inputs, including link aliases, are rejected. If safe reports cannot be
written, the run fails and earlier artifacts cannot substitute for current QA.

## How to review a result

1. Open `hole-radius-report.html` and identify every failed icon.
2. Check for `processingErrors` first. Resolve checker/input problems before
   attempting a geometry repair; open `_holes.png` only for the current
   successfully processed result.
3. Match each numbered hole or red pinch marker to the editable elements.
4. Read the per-icon metrics to confirm the measured radius or closure margin.
5. Check the profile's native-size SVG; numeric output does not replace
   visual review.
6. Record the affected elements, measurement, repair, and passing rerun under
   `holeDiameterChecks` or equivalent editable metadata.

## Repair order

Repair the authoritative editable geometry composition, never flattened output
paths or SVG copies under `hole_error/`:

1. Enlarge the opening by growing its enclosure or moving adjacent parts apart.
2. Rebalance the composition so the identity-bearing detail can carry a legal
   opening.
3. Remove a complete non-identity-bearing part when the first two options cannot
   preserve recognition. Record the removal as `omit`.

Do not delete an arbitrary path fragment, clip the problem, or push surrounding
parts together until the opening disappears.

After any repair, regenerate the native SVG and its same-size compatibility
alias, recheck structural/grid and declared-overlap prerequisites, and restart
at distance → holes/pinches → keyshape before native-size review. A hole repair
can change both disconnected spacing and painted bounds, so earlier passes
cannot be carried forward. Diagnose unresolved distance reviews or intended
connections instead of distorting the geometry to force a pass.

## Useful options

```text
--error-dir <folder>                 Override the default hole_error history root.
--icon-type <profile-name>   Select the profile used for normalization.
--samples-per-unit <integer>         Raster supersampling; minimum 4, default 32.
--min-radius-design-u <number>       Hole-radius gate; must be greater than 0.
--min-fill-depth-design-u <number>   Pinch gate; 0 disables pinch detection.
```

Omit threshold overrides during ordinary work so the selected profile's
`minimumEnclosedRadius` and `minimumSolidFillDepth` take effect. Explicit CLI
values are diagnostic overrides; a relaxed result does not replace the configured
delivery gate. Change shared policy through
[profile configuration](profile-configuration.md) only when explicitly requested,
then rerun all three gates and native review for affected icons.

## Blocker handling

If `core/qa_overlays.py` or its rendering dependencies are unavailable, report
the hole/pinch gate as blocked. Do not silently skip it and do not substitute a
detector that has not been validated against this measurement model.
