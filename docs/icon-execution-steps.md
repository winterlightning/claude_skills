# Icon Processing Execution Steps

Follow this runbook whenever one selected SVG reference is traced, simplified, and remade as one Unlimited Shapes icon.

Use [icon-batch-execution-steps.md](icon-batch-execution-steps.md) instead when a
set of references is processed in one execution. That runbook keeps this
per-icon discipline and adds a staged scope boundary, a shared skill read, an
atom-consolidation gate, and a family review.

## Single-icon boundary

- Process exactly one source SVG per execution.
- Do not scan, detect, compare, rank, or remake sibling variants.
- Do not run folder or batch detection as part of this workflow.
- A filename such as `variant 1` is only the selected source's name; it does not authorize inspecting variants 2–4.
- Start a separate execution from Step 1 if the user later selects another SVG.

## Required order

```text
1. Select one source SVG
2. Run shape detection on that SVG only
3. Verify detection JSON + Matplotlib plot
4. Load SKILL.md + required references
5. Send the complete evidence bundle into icon making
6. Map detected elements to maker decisions
7. Reuse or create atoms without overfitting
8. Compose the icon
9. Validate the atomic grid, then spacing, keyshape containment, and visual quality
10. Deliver source, mappings, outputs, and registry changes
```

Do not begin icon composition before steps 1–5 are complete.

## Step 0 — Work from the project root

```bash
cd /Applications/Workspaces/pictographic/unlimited_shapes
python3 -m pip install -r requirements.txt
```

Keep the selected reference file unchanged. Write its detection and icon outputs to a separate output folder.

## Step 1 — Select the source SVG

Record exactly one input path. For example:

```text
test_input/Building - variant 1.svg
```

That file is the complete reference scope for this execution. Ignore every other variant, even when it is stored beside the selected SVG. Do not use sibling variants to improve, correct, compare, or reinterpret the selected source.

## Step 2 — Run shape detection first

```bash
mkdir -p work
python3 core/detect_svg_shapes.py \
  "test_input/Building - variant 1.svg" \
  --output "work/Building - variant 1-shapes.json" \
  --plot "work/Building - variant 1-preflight.png"
```

Do not pass a folder, wildcard, or list of SVGs. Do not run `batch_detect_svg_shapes.py` for an individual icon-making execution.

## Step 3 — Detection checkpoint

Before opening the icon-making skill, verify the three evidence files for the one selected icon exist:

- Original source SVG.
- Matching `*-shapes.json` report.
- Matching `*-preflight.png` Matplotlib plot.

Then inspect:

- `summary.readyForIconMaker`.
- `elements` and their source element IDs.
- `makerPreflight.suggestedAtoms`.
- `makerPreflight.manualReview`.
- Every `specIssues` warning or error.
- The visual labels and geometry in the Matplotlib plot.

`readyForIconMaker: false` does not mean stop permanently. It means the agent must resolve the marked geometry semantically instead of accepting detector suggestions automatically.

If the JSON source name, geometry, or plot does not match the SVG, regenerate both detection artifacts before continuing.

## Step 4 — Load the icon-making skill

Invoke `$unlimited-shapes-icons` when the agent supports named skills. The installed entrypoint for this workspace is:

```text
/Applications/Workspaces/pictographic/unlimited_shapes/.agents/skills/unlimited-shapes-icons/SKILL.md
```

Read `SKILL.md` completely. Then read all required references:

```text
references/icon-style-rules.md
references/detection-to-atom-pipeline.md
references/negative-space-and-topology.md
references/keyfit-validation.md
references/hole-diameter-validation.md
```

Resolve relative reference paths from the skill folder. Do not use an older copied prompt or rely on memory; the skill is the current source of workflow instructions.

## Step 5 — Send the evidence bundle into icon making

The agent receives these paths together:

```text
source SVG:      /absolute/path/to/reference.svg
detection JSON:  /absolute/path/to/reference-shapes.json
preflight plot:  /absolute/path/to/reference-preflight.png
output folder:   /absolute/path/to/icon-output
```

All three evidence paths must refer to the same selected SVG. Do not attach or inspect sibling variants.

Recommended agent request:

```text
Use $unlimited-shapes-icons to remake this icon.

Process only the supplied source SVG. Ignore every sibling or alternate variant.
Read the skill and its required references completely.
Use the supplied SVG, detection JSON, and Matplotlib plot as one evidence bundle.
Create the source-element mapping before composition.
Render the source and map foreground/background, connections, overlaps, and
identity-bearing openings before composition. Record painted-clearance checks;
the 4u centerline rule is a collision floor, not a visual-spacing target.
Render and inspect the current composition at 48u and true-size 24px before
choosing its keyshape. A dominant large circle selects `circle-44`; a dominant
large square selects `square-40`. Do not decide from bounds or a small inset.
Do not overfit an unrelated existing atom. If an essential form has no honest
catalog match, create and integrate a reusable parametric atom following the
detection-to-atom pipeline.

Source SVG: <absolute path>
Detection JSON: <absolute path>
Preflight plot: <absolute path>
Output folder: <absolute path>
```

## Step 6 — Create the source-element mapping

For every identity-bearing element or semantic group, record one decision:

- `existing-atom`
- `new-atom`
- `simplify`
- `omit`
- `merge`
- `manual`

Carry detector element IDs into the editable icon source under `sourceAnalysis.mappings`, or an equivalent project field. Include a short reason for every `new-atom`, `simplify`, `omit`, or `manual` decision.

Also record `sourceAnalysis.relationships` (or equivalent) for connected,
ordinary-distinct, visual-opening, and intentional-overlap pairs. For every
identity-bearing opening, store a `spacingChecks` entry with centerline distance,
painted clearance, minimum painted clearance, and pass/fail status.

Do not compose while an essential feature remains unexplained.

## Step 7 — Reuse or create atoms honestly

Use an existing atom only when it preserves the source feature's topology, shape family, and semantic role.

Create a new atom when the feature is essential and existing atoms would require extreme distortion, unrelated geometry, redundant overlaps, or several atoms to imitate one simple contour. One essential source is enough justification; previous recurrence is not required.

A new atom must be generic and parametric, not a frozen trace or complete icon. It must use allowed lines, arcs, and quadratics—never cubic paths. Integrate the ID across the registry, renderers/validators, generator, atom asset, detector when applicable, documentation, and tests before composing with it.

## Step 8 — Compose the icon

Before declaring the keyshape, render and visually inspect the whole composition
at 48u and true-size 24px. Choose from the dominant outer silhouette: a large
circular/radial body selects `circle-44`, while a large four-sided/cornered body
selects `square-40`. Small internal wheels, buttons, windows, badges, or insets
do not control the decision. Save the visualization and record a short visual
rationale with `keyfitCheck.targetToken`.

Apply the active specification:

- 48×48 design canvas.
- 24×24 ship canvas.
- 1u minor / 4u major grid on the 48×48u canvas.
- Four centered painted keyshapes—the keyshape is the padding boundary: circle Ø44u (2u cardinal padding), square 40×40u (4u per side), portrait 36×44u (6u sides / 2u ends), and landscape 44×36u (2u sides / 6u ends).
- Regular stroke 4u design / 2px ship.
- `currentColor`, no fill, centered stroke, round caps/joins.
- Ordinary radii 4u or 8u.
- Straight-line angles in 15° increments.
- Arcs and quadratics only.
- Minimum 4u centerline distance between ordinary distinct parts; this is only the collision floor.
- Identity-bearing openings and parallel structural gaps prefer 4u painted clearance (8u centerline at Regular) and require at least 3u painted clearance (7u centerline) after true-size review.
- 3u overlap cutout where separation is required.
- Every enclosed negative-space region at least 1u inscribed radius, and every solid junction filled at least 1u deep. Crowding is solved by giving the zone room — enlarge, rebalance, or remove a whole part (R9) — never by pushing parts together until a gap closes.
- Symmetry preferred when the subject is naturally symmetrical.

Simplify the reference where needed, but retain its identity-bearing topology and silhouette.

Treat keyshapes as exact painted padding boundaries: paint must reach all four
cardinals or rectangular edges and stay entirely inside the selected boundary.
Circle paint may not enter the corner regions of its 44×44 bounding box. Never multiply every coordinate in a
completed or flattened SVG to fill a keyshape. Resize or recompose the source atoms, then snap ordinary
axis-aligned and 45-degree endpoints back to whole design units. Fractional
coordinates are reserved for exact rotated/arc junctions or a documented optical
correction, not as residue from bulk scaling.

## Step 9 — Validate

Emit both canonical outputs and run structural and overlap validation first:

```bash
python3 core/emit_icon.py <icon.json> --out-dir <output-folder>
python3 core/validate_icon.py <icon.json> --dir <output-folder>
python3 core/render_overlap_audit.py <icon.json> <overlap-audit.svg>
```

Run the grid gate before spacing, hole, or keyshape validation:

```bash
python3 core/check_svg_grid.py <design-svg-or-folder> \
  --expected design \
  --output-dir <grid-qa-folder>
```

Do not continue while the grid gate reports a wrong canvas, wrong normalized
stroke, cubic geometry, an off-grid straight angle, or fractional ordinary
axis/45-degree line endpoints. Correct the editable atomic composition and
re-emit it; do not round a flattened path blindly.

Then validate the declared keyshape and enclosed negative space on the clean
24px ship SVG:

```bash
python3 core/check_keyfit.py <ship.svg> \
  --expected-editable-dir <editable-json-folder> \
  --output-dir <keyshape-qa-folder>
python3 core/qa_overlays.py <ship.svg> \
  --output-dir <hole-qa-folder> \
  --min-radius-design-u 1
```

Inspect these artifacts together:

1. Original source SVG rendered at a comparable square size.
2. Detection JSON.
3. Matplotlib preflight plot.
4. Source-element and relationship mappings.
5. Painted-clearance measurements for identity-bearing openings.
6. 48-unit design SVG.
7. True-size 24px ship SVG.

Confirm:

- Every essential detector element has a resolved mapping.
- Foreground/background order, connections, contour terminations, and openings match the rendered source or have a documented simplification.
- Every identity-bearing opening has a passing painted-clearance measurement; numeric collision-floor compliance alone is insufficient.
- No atom was overfit to represent a different shape family.
- New atoms satisfy their reusable parametric contract.
- `check_svg_grid.py` passes the design output before the downstream checks run.
- No cubic paths exist in new-grid output.
- Distance, visual-clearance, connection, cutout, angle, radius, symmetry, and canvas-safety rules pass.
- `core/qa_overlays.py` reports no undersized hole and no pinched junction. If a zone failed and was repaired, the repair enlarged the opening, rebalanced the composition, or removed a whole part; nothing was squeezed shut or clipped. See [qa-overlays-guide.md](qa-overlays-guide.md) for operation details and [negative-space-repair-examples.md](negative-space-repair-examples.md) for worked repairs.
- `check_keyfit.py` confirms the same declared keyshape after the repair; paint remains centered, reaches the target cardinals/edges, and never crosses the selected boundary.
- The declared keyshape still agrees with the dominant silhouette in both the saved 48u visualization and the true-size 24px output.
- The subject and every opening are recognizable and optically balanced at the true 24px output size, not only enlarged.

## Step 10 — Deliver

The normal handoff for this one icon contains:

- Editable icon source with `sourceAnalysis` mappings, relationship classifications, and `spacingChecks`.
- 48×48 `-design.svg`.
- 24×24 clean ship `.svg`.
- Detection JSON and Matplotlib preflight plot used for the decision.
- List of intentional simplifications or unresolved exceptions.

When a new atom was created, also include:

- New atom ID and contract.
- Registry implementation.
- Generated atom asset.
- Renderer/validator/detector integration.
- Documentation and passing tests.

The process is complete only when the output can be traced from source element → maker decision → atom instance → final SVG.

End the execution after delivering this icon. Do not automatically continue to another file or variant.

## Stop conditions

Stop and report the blocker instead of guessing when:

- The source SVG and detection report do not correspond.
- A required source, JSON, or plot is missing and cannot be generated.
- The requested output location is unavailable.
- Creating a necessary atom would require prohibited cubic geometry or a whole-icon primitive.
- A user decision would materially change the subject or intended icon meaning.
