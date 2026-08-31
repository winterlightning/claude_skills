# Unlimited Shapes icon system

This folder is the human-readable entry point for designing, reviewing, and shipping Unlimited Shapes icons. The system uses a 48-unit design canvas and emits exact half-scale 24-pixel SVGs. All geometry and QA programs in `core/` are Python so the math can be inspected, tested, and reused without a JavaScript runtime.

## Start here

1. Read [icon-rules.md](icon-rules.md) for the binding visual and numeric rules.
2. Read [icon-authoring-guide.md](icon-authoring-guide.md) for composition decisions and common failure modes.
3. Follow [icon-execution-steps.md](icon-execution-steps.md) for one icon or [icon-batch-execution-steps.md](icon-batch-execution-steps.md) for a family.
   If your usual handoff is the runbook plus one supplied SVG, use [README-svg-input-processing.md](README-svg-input-processing.md) as the concise operator guide and request template.
4. Use [atomic-shapes.md](atomic-shapes.md) to choose registered primitives before adding a new one.
5. Use [core-scripts-guide.md](core-scripts-guide.md) to understand which program runs at each workflow step, what it protects, and what it produces.
6. Read [negative-space-repair-examples.md](negative-space-repair-examples.md) before repairing a failed hole or pinch — four worked cases, one per repair option, plus the sizing math.
7. Use [qa-overlays-guide.md](qa-overlays-guide.md) to run and interpret the canonical `core/qa_overlays.py` hole-and-pinch gate.

## Core rules at a glance

- Design on `48×48`; ship on `24×24` at exactly half scale.
- Use a `4u` design stroke and `2px` shipping stroke, with round caps and joins.
- Use a 1u minor / 4u major grid and one centered painted keyshape: circle Ø44u, square 40×40u, portrait 36×44u, or landscape 44×36u. The keyshape is the padding boundary.
- Prefer whole design units and straight angles on the 15-degree grid.
- Paint must reach all four cardinals or rectangular edges and remain inside the selected boundary; circle paint may not enter the corner regions of its 44×44 bounding box. Resize/recompose editable atomic instances and resnap ordinary coordinates—never scale flattened SVG paths.
- Use only registered atomic shapes. New atoms must be genuinely reusable and documented.
- Keep distinct centerlines at least `4u` apart unless a measured relationship explicitly declares a connection or intentional overlap.
- A negative-space hole must have at least a `1u` inscribed radius (`2u` diameter), and a solid junction must be filled at least `1u` deep — a junction held closed by less paint is a squeeze, and fails the same way.
- Repair a failing zone by giving it room, in this order: enlarge the opening, rebalance the composition so the crowded detail is big enough to carry a legal opening, or remove the whole part when it is not identity-bearing. Record the omission and revalidate. Never push parts together to close a hole, and never delete an arbitrary path fragment. See R9 in [icon-rules.md](icon-rules.md).
- Any repair must keep the same declared keyshape, stay centered, reach its target extents, and remain inside its boundary. Re-run `check_keyfit.py` after every hole or pinch repair because every repair moves paint.
- When keyshape containment fails, first reposition or resize. A complete low-priority SVG element or atom instance may be removed only when identity and visual quality remain intact. Never clip or delete an arbitrary path fragment.

## Python commands

Run these from the project root:

```bash
python3 core/emit_icon.py path/to/icon.json
python3 core/validate_icon.py path/to/icon.json
python3 core/render_overlap_audit.py path/to/icon.json
python3 core/detect_svg_shapes.py path/to/icon.svg
python3 core/generate_assets.py
python3 core/compose_examples.py
python3 -m unittest discover -s core -p 'test_*.py'
```

The emitter writes `<name>-design.svg` and `<name>.svg`. The validator checks canvas safety, declared centered-keyshape containment, angle discipline, pair spacing, and emitted SVG properties. Visual review at true 24-pixel size remains mandatory after numeric checks pass.

For the mission, timing, inputs, outputs, and failure meaning of every script, see [Core scripts: mission and workflow](core-scripts-guide.md).

## Source layout

- `core/shape_registry.py` — Python atomic-shape registry.
- `core/icon_geometry.py` — shared path parsing, transforms, rendering, and sampling math.
- `core/emit_icon.py` — canonical 48-unit and 24-pixel SVG output.
- `core/validate_icon.py` — numeric and keyshape validation.
- `core/render_overlap_audit.py` — negative-space envelope panels.
- `core/qa_overlays.py` — rendered enclosed-hole and pinched-junction QA.
- `core/detect_svg_shapes.py` and `core/batch_detect_svg_shapes.py` — source/reference detection evidence.
- `core/test_*.py` — executable regression tests.

Do not add shell, JavaScript, or other executable scripts to `core/`. Supporting non-code data belongs in a clearly named data or reference folder.
