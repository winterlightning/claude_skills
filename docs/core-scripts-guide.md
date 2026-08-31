# Core scripts: mission and workflow

This guide explains what every Python file in `core/` is responsible for, why the icon system needs it, and when it participates in the workflow. Run commands from the project root unless noted otherwise.

## Workflow map

| Step | Goal | Program | Required? |
|---|---|---|---|
| 1. Inspect reference | Convert source SVG geometry into reviewable evidence | `detect_svg_shapes.py` or `batch_detect_svg_shapes.py` | Required when the reference is SVG and no valid report exists |
| 2. Compose | Build editable icon JSON from registered atoms | `shape_registry.py` and `icon_geometry.py` are imported by authoring tools | Required infrastructure; not run directly |
| 3. Emit | Produce canonical 48-unit and 24-pixel SVGs | `emit_icon.py` | Required |
| 4. Structural validation | Check keyshape containment, canvas, angles, spacing, and emitted SVG properties | `validate_icon.py` | Required |
| 4a. Final grid audit | Detect mixed canvases, wrong stroke normalization, off-15° lines, and avoidable fractional axis/45° placement | `check_svg_grid.py` | Required after emission or any keyshape resize |
| 4b. Recover contaminated scaled outputs | Re-emit a named work set from canonical editable JSON without arbitrary global scaling | `restore_grid_outputs.py` | Use when a flattened keyshape-scaling pass has introduced bulk decimals |
| 5. Topology review | Visualize expanded stroke envelopes for declared nearby pairs | `render_overlap_audit.py` | Required when spacing relationships are declared |
| 6. Final rendered QA | Measure actual painted-keyshape containment, enclosed-hole diameter, and squeezed junctions | `check_keyfit.py` and `core/qa_overlays.py` | Required before delivery |
| 7. Visual review | Inspect 48u design, 24px ship output, keyshape, hole, and overlap evidence | Human/designer review | Required; scripts do not prove recognizability |
| Registry maintenance | Regenerate standalone atom assets after registry changes | `generate_assets.py` | Required only when atoms change |
| Example maintenance | Regenerate JSON-backed example icons | `compose_examples.py` | Required only when examples or rendering change |
| Regression testing | Protect detector, registry, and geometry behavior | `test_detect_svg_shapes.py`, `test_shape_registry.py` | Required after core changes |

## Reference-analysis scripts

### `core/detect_svg_shapes.py`

**Mission:** Analyze one reference SVG before icon composition. It normalizes source elements, classifies likely primitives, identifies specification problems, proposes atomic-shape mappings, and can draw a labeled preflight plot.

**Why it is needed:** SVG markup alone does not explain which contours are meaningful, which elements may map to reusable atoms, or which parts require manual review. The report preserves source evidence so the remake is informed without becoming a literal trace.

**Used at:** Step 1, before choosing atoms or writing icon JSON. Reuse an existing valid report rather than creating conflicting analysis.

**Input:** One SVG reference.

**Outputs:** JSON detection report and, when `--plot` is provided, a labeled image. `--strict` returns exit code 3 when manual review remains.

```bash
python3 core/detect_svg_shapes.py reference.svg \
  --output work/reference-shapes.json \
  --plot work/reference-preflight.png \
  --strict
```

The detector proposes evidence; it does not make the final design decision.

### `core/batch_detect_svg_shapes.py`

**Mission:** Run the same reference analysis recursively across a folder of SVGs and create one combined batch summary.

**Why it is needed:** Large icon families need consistent analysis, resumable output, progress reporting, and a complete list of files that failed or still require review.

**Used at:** Step 1 for batch projects. Use the single-file detector for isolated icons.

**Inputs:** Source SVG directory and output directory.

**Outputs:** Per-file `-shapes.json`, per-file `-preflight.png`, and `batch-summary.json` containing counts, statuses, and failures.

```bash
python3 core/batch_detect_svg_shapes.py references/ work/preflight/ \
  --progress-every 10
```

Use `--overwrite` only when reports are stale or the detector changed.

## Shared geometry modules

### `core/shape_registry.py`

**Mission:** Define the Python-side catalog of reusable parametric atoms and return geometry for a requested width and height.

**Why it is needed:** Emission, validation, asset generation, and tests must use the same atom definitions. Centralizing the formulas prevents each command from interpreting a circle, arch, gable, or other atom differently.

**Used at:** Steps 2–5 and registry maintenance. It is imported by other scripts and is not normally executed directly.

**Change it when:** Adding or correcting a reusable atom. Make the matching browser-registry change in `frontend/js/shapes.js`, regenerate assets, and run all tests.

### `core/icon_geometry.py`

**Mission:** Provide shared mathematical operations: path parsing, primitive-to-path conversion, rigid rotation/flip/translation, arc transformation, absolute path rendering, exact half scaling, and dense centerline sampling.

**Why it is needed:** Output and validation must measure the same resolved geometry. A separate transform or arc implementation in each command could allow the validator to approve a shape different from the one that ships.

**Used at:** Steps 3–5. It is an internal module and is not normally run directly.

**Change it when:** Fixing shared path math or adding a supported path operation. Run the full core test suite and emitter parity checks after any change.

## Output and validation scripts

### `core/emit_icon.py`

**Mission:** Turn editable icon JSON into the two canonical SVG deliverables.

**Why it is needed:** It resolves registered atoms and bakes all rigid transforms into path data. The 24-pixel file is generated by halving every design coordinate and radius, guaranteeing consistent 48→24 scaling.

**Used at:** Step 3 after composition, and again after every geometry correction.

**Input:** Icon JSON with a non-empty `instances` array.

**Outputs:** `<name>-design.svg` on a 48-unit canvas with 4u stroke, and `<name>.svg` on a 24-pixel canvas with 2px stroke.

```bash
python3 core/emit_icon.py work/icon.json --out-dir final_svg/
```

A successful emission does not mean the icon passes validation.

### `core/validate_icon.py`

**Mission:** Apply deterministic structural checks to the editable source and emitted SVG files.

**Why it is needed:** Visual inspection can miss off-grid angles, unsafe painted bounds, invalid centered-keyshape containment, under-spaced centerlines, prohibited cubics, missing outputs, or wrong canvas/stroke attributes.

**Used at:** Step 4 after every emission and again immediately before delivery.

**Inputs:** Icon JSON and its emitted SVG directory.

**Output:** Console report and a nonzero exit code on failure. It does not modify the icon.

```bash
python3 core/validate_icon.py work/icon.json --dir final_svg/
```

If it fails, modify the editable JSON, re-emit both SVGs, and rerun every affected check. Do not patch only the final SVG.

### `core/check_svg_grid.py`

**Mission:** Audit one final SVG or a flat output folder after emission or resizing. It normalizes 24px and 48u files to design units, checks canvas/stroke consistency, rejects cubic or unparsable geometry, verifies every straight segment against the 15° direction grid, and identifies avoidable fractional coordinates on axis-aligned and 45° construction.

**Why it is needed:** A path can remain mathematically straight after resizing while leaving the atomic unit grid. Decimal placements such as `10.8u` or `6.4u` can produce inconsistent pixel alignment even when the line angle is 0°, 45°, or 90°. Exact keyshape matching alone does not detect this.

**Used at:** After emission, after every keyshape resize/recomposition, and before final keyshape/hole QA.

```bash
python3 core/check_svg_grid.py final_svg/ \
  --expected ship \
  --output-dir qa_grid/results/
```

Use `--expected design` for a folder that must contain only 48×48/4u outputs, or `--expected either` when intentionally auditing both sizes. A failure must be corrected in editable atomic source. Never round or scale flattened final paths blindly.

Exact rotated, curved, junction, or optical geometry can require fractions. For
a regenerated set carrying reviewed source reasons, pass its hash-locked
exception manifest:

```bash
python3 core/check_svg_grid.py work_keyshape_scale/grid_repair/final \
  --expected design \
  --exceptions work_keyshape_scale/grid_repair/grid-exceptions.json \
  --output-dir work_keyshape_scale/grid_repair/qa/grid
```

An exception is accepted only while its recorded SHA-256 digest matches the SVG;
editing the file invalidates it. The strict audit remains the default.

### `core/repair_keyshape_targets.py`

**Mission:** Repair this 152-icon work set from editable atomic JSON so every
painted result exactly matches one of the four centered keyshapes. It performs
the broad instance-box resize, then applies named recompositions for grid,
angle, topology, and visual corrections. It emits new 48u and 24px folders; it
never transforms flattened SVG paths.

**Why it is needed:** A generic non-uniform resize can reach the target box but
can also introduce off-grid lines, distort canonical angles, or squeeze a
small opening. The named source-level corrections make the migration
repeatable and reviewable.

The repair chooses square-40, portrait-36x44, or landscape-44x36 from the
undistorted source silhouette. Circle-44 requires an explicit semantic choice
because a rectangular bounding box cannot prove radial containment.

**Used at:** One-time exact-keyshape migration after the pre-repair painted-bounds audit
and before grid, keyshape, hole, and true-size visual QA.

```bash
python3 core/repair_keyshape_targets.py \
  work_keyshape_scale/grid_repair/editable \
  work_keyshape_scale/grid_repair/qa/keyfit_target_44/keyfit-results.json \
  work_keyshape_scale/keyshape_target_repair
```

The output folder must be new. After emission, regenerate the hash-locked grid
exception manifest for deliberately fractional exact-angle geometry and run all
final gates. This script is dataset-specific; do not treat its named overrides
as a general-purpose icon scaler.

### `core/restore_grid_outputs.py`

**Mission:** Rebuild the filenames in a contaminated flat output folder from
their canonical editable JSON sources. It resolves the current source batches,
re-emits exact 48u and half-scale 24px SVGs, copies the editable sources, records
provenance, and creates hash-locked reasons for necessary fractional geometry.

**Why it is needed:** Inverting or rounding a global scale can break joints,
arcs, symmetry, and topology. Re-emission restores the registered atomic
construction and retains only fractions produced deliberately by that source.

**Used at:** Migration/recovery only, before the normal grid, keyshape, hole, and
visual QA gates.

```bash
python3 core/restore_grid_outputs.py work_keyshape_scale/final \
  --output-dir work_keyshape_scale/grid_repair
```

The command refuses to replace an existing repair folder unless `--overwrite`
is explicit. Keep the contaminated folder unchanged until the regenerated set
passes all gates.

### `core/render_svg_contact_sheet.py`

**Mission:** Render every SVG in a flat folder at its true output size and
arrange the results in one labeled family sheet. The optional nearest-neighbor
preview scale makes the actual 24px raster decisions visible without changing
them through smoothing.

**Why it is needed:** Numeric grid, keyshape, spacing, and hole passes do not prove
recognizability, consistent family weight, or clean pixel alignment at launch
size. The contact sheet makes outliers visible in one review surface.

**Used at:** Final true-size visual QA and after a localized geometry repair.

```bash
/opt/homebrew/bin/python3 core/render_svg_contact_sheet.py final_24/ \
  qa/family-24px-contact-sheet.png \
  --true-size 24 --preview-scale 3 --columns 10
```

### `core/render_overlap_audit.py`

**Mission:** Render one expanded-stroke diagnostic panel for each two-instance spacing relationship declared in `sourceAnalysis.spacingChecks`.

**Why it is needed:** Numeric declarations are not trustworthy by themselves. The audit shows actual transformed paths, caps, joins, curves, and rotations with the relationship’s required envelope width, making hidden overlaps and bad connections visible.

**Used at:** Step 5 after structural validation, whenever the icon has connected, ordinary-distinct, visual-opening, or intentional-overlap pairs.

**Input:** Icon JSON with two-instance spacing checks.

**Output:** `<name>-overlap-audit.svg`, or a requested output path.

```bash
python3 core/render_overlap_audit.py work/icon.json work/icon-overlap-audit.svg
```

The generated panel still requires visual inspection. For non-connected pairs, positive-area envelope overlap fails. Connected pairs may share paint only at the intended joint.

### `core/render_icon.py`

**Mission:** Provide a compatibility rendering command for older JSON/example workflows while using the current shared Python geometry.

**Why it is needed:** Existing local example-generation calls may expect one requested output filename instead of the canonical emitter naming convention.

**Used at:** Supporting or legacy workflows, especially through `compose_examples.py`. Do not use it as the normal final-delivery command; use `emit_icon.py`.

```bash
python3 core/render_icon.py assets/icons/example.json assets/icons/example.svg
```

It writes the requested 48-unit SVG plus a `-24.svg` companion. `--distance-check` is retained for command compatibility; canonical spacing decisions belong to `validate_icon.py` and `render_overlap_audit.py`.

## Registry and example maintenance

### `core/generate_assets.py`

**Mission:** Regenerate standalone `assets/shapes/<atom-id>.svg` files from the Python atom registry.

**Why it is needed:** Standalone atom assets are derived files. Regeneration keeps them aligned with tested parametric formulas and avoids hand-edited asset drift.

**Used at:** Registry maintenance after adding or changing an atom, not during every icon build.

```bash
python3 core/generate_assets.py
```

Use `--out-dir` to generate into a temporary comparison folder before replacing maintained assets.

### `core/compose_examples.py`

**Mission:** Regenerate every JSON-backed example under `assets/icons/` through the Python compatibility renderer.

**Why it is needed:** Examples should demonstrate current registry and renderer behavior, not preserve stale SVG geometry.

**Used at:** Example maintenance after registry, renderer, or example JSON changes.

```bash
python3 core/compose_examples.py
```

This rewrites generated example SVGs, so review the resulting asset diff.

## Regression tests

### `core/test_detect_svg_shapes.py`

**Mission:** Verify detector parsing, classifications, warnings, proposed atoms, transforms, and plot generation against representative SVG geometry.

**Why it is needed:** A detector regression can silently produce misleading source evidence for every icon made afterward.

**Used at:** After any change to detection logic, atom detection mappings, or SVG parsing; it is also part of the full core test run.

### `core/test_shape_registry.py`

**Mission:** Verify registry IDs, required atoms, allowed path types, parseability, representative geometry invariants, half-scale rendering, and alignment with the browser registry.

**Why it is needed:** Registry drift can break emission or make the editor and Python tooling disagree about available atoms.

**Used at:** After any change to `shape_registry.py`, `icon_geometry.py`, `frontend/js/shapes.js`, or output behavior.

Run both test modules together:

```bash
python3 -m unittest discover -s core -p 'test_*.py'
```

All tests must pass before installing or shipping core changes.

## Final rendered QA scripts

These remain separate because they raster-measure finished output folders and generate user-facing QA evidence rather than define core vector math. They are stored in this project; run the commands from the project root.

### `core/check_keyfit.py`

**Mission:** Measure finished 24×24 SVG paint against circle-44, square-40, portrait-36x44, or landscape-44x36, including true circle containment, and produce overlays plus an HTML report.

For undeclared audit inputs, `circle-44` is inferred only when rendered paint
contains a dominant large-radius form whose outer radial envelope is nearly
constant. Otherwise, near-equal silhouettes fall back to square, tall to
portrait, and wide to landscape. This is diagnostic triage; final delivery still
requires a visually selected `keyfitCheck.targetToken` declaration.

**Used at:** Step 6 after `validate_icon.py`, for single files or completed folders.

```bash
python3 core/check_keyfit.py final_svg/ \
  --expected-editable-dir work_keyshape_scale/keyshape_target_repair/editable \
  --output-dir qa_keyfit_detection/results/
```

`--expected-editable-dir` makes each editable JSON's
`keyfitCheck.targetToken` authoritative. This is required for completed sets:
without it, an icon that accidentally lands on a different canonical token can
still self-assign that token and report a misleading pass.

**Also run it after any hole or pinch repair, not only after `validate_icon.py`.** A repair can cross the selected boundary or make the artwork miss a required edge/cardinal. Declare the intended keyshape in editable metadata and validate against that declaration afterward.

### `core/qa_overlays.py`

**Mission:** Measure enclosed negative space in finished SVGs against two gates — each region's largest inscribed radius against the 1u design-radius minimum, and each solid junction against the 1u paint-depth minimum. The second gate re-renders the icon with narrowed strokes: a junction that reopens into an enclosed pocket is a *pinch*, held closed only because two parts were squeezed until their paint merged.

**Used at:** Step 6 after keyshape validation and before delivery.

```bash
python3 core/qa_overlays.py final_svg/ \
  --output-dir qa/hole-detection/ \
  --min-radius-design-u 1 \
  --min-fill-depth-design-u 1
```

**Measuring stroke.** The gate rasterizes at a fixed **1u** measuring stroke, not the authored 4u, and raises its threshold to **2.5u radius / 5u diameter** to compensate. Narrowing the paint by `d` per edge grows every enclosed region's largest inscribed circle by exactly `d`, so moving the threshold by the same `d` leaves the verdict identical to the 1u rule while making tight regions measurable. Full operation and interpretation guidance is in [qa-overlays-guide.md](qa-overlays-guide.md#measurement-model).

**Outputs:** per-icon `.metrics.json` and `_holes.png` overlay — undersized holes are colored and numbered, pinched junctions are marked with a red cross — plus `hole-diameters.csv`, `hole-diameters.json`, and `hole-radius-report.html`. Each hole carries both `inscribed_radius_design_u` as measured and `equivalent_radius_at_authored_stroke_design_u` restated on the 1u scale; each pinch reports `closure_margin_design_u`, the paint depth that was holding it shut. Every failing icon is copied to `<output-dir>/hole_error/` with its overlay, metrics, and a README naming each failing zone — a ready-to-work queue, cleared at the start of each run. Pass `--min-fill-depth-design-u 0` to measure holes only.

If either final QA tool fails, repair the specific failing zone in the editable source by working down the R9 ladder — enlarge the opening, rebalance the composition so the crowded detail can carry a legal opening, or remove the whole non-identity-bearing part — then re-emit and rerun structural, overlap, keyshape, hole, pinch, and true-size checks. Record any omission. Never delete an arbitrary path fragment, and never squeeze surrounding parts together until the hole closes: that converts a measured hole into a pinch, and the pinch gate fails it. Re-run `check_keyfit.py` afterwards as well: the repair moved paint, and the declared keyshape is measured from painted bounds. [negative-space-repair-examples.md](negative-space-repair-examples.md) works through one repair of each kind, including the keyshape correction one of them needed.
