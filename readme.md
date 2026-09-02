# Unlimited Shapes

Build normal, sub, and container icons from registered parametric atoms. The
machine-readable profile source is
[`core/icon_profiles.json`](core/icon_profiles.json); every profile emits a
canonical design/ship pair through the same Python toolchain.

Visual quality comes before catalog reuse. Existing atoms are reusable
candidates, not limits on the design: when they would make an icon awkward,
unnatural, or less recognizable, add a new generic parametric atom instead of
accepting the weaker icon.

Start at [docs/README.md](docs/README.md), then follow the shared
[icon pipeline](docs/icon-pipeline.md). The single-SVG, batch-SVG, and rework-JSON
documents are thin lane adapters and do not redefine the rules.

```bash
./rework_opus.sh "https://symlib.pictographic.ai/download-wrong-icons-json?cat=Building+Construction"
```

`rework_opus.sh` drives that runbook end to end—stage, detect, remake with
Claude, verify every automated QA gate, then upload—and every stage is idempotent, so
re-running the same command resumes instead of starting over.

## Detect an SVG reference first

Run the dependency-free preflight detector before rebuilding an input icon:

```bash
python3 -m pip install -r requirements.txt
python3 core/detect_svg_shapes.py path/to/input.svg \
  --output path/to/input-shapes.json \
  --plot path/to/input-preflight.png
```

It detects native and path-based lines, point dots, arcs, quadratic and cubic
curves, circles, ellipses, rectangles, rounded rectangles, pills, triangles,
diamonds, arches, polylines, and compound paths. It also proposes atomic candidates
and flags new-grid conflicts. The Matplotlib overlay includes the 1u minor / 4u
major 48-unit grid, detection labels/bounds, and color-coded QA. Final icons use
one centered painted keyshape from their declared profile; the keyshape is the
padding boundary. The detector's 48-unit grid is source-analysis evidence only:
recompose sub and container icons on their declared 32-unit and 64-unit design
canvases instead of treating detector coordinates as an authoring scaffold. Add `--show` for
an interactive window. Use `--strict` in automation; status `3` means the
report needs manual review before icon making.

## Run it

Open `frontend/index.html` directly in a browser — no build step, no server,
no dependencies.

- Drag a shape from the palette onto the canvas (or click it to drop it in the
  center).
- Choose the icon type and its keyshape in the toolbar. Containers also show the
  protected 32×32 clearance slot and the accepted sub keyshape used for previews.
- Move with fixed 1u grid snapping, resize with
  the handles (Shift keeps aspect), rotate with the top handle (15° snap),
  flip, and inspect exact coordinates. Canonical paint is fixed to no fill,
  `currentColor`, and the profile's Regular stroke. Resizing recomputes geometry
  and never scales it.
- Copy/paste (Ctrl/Cmd+C/V), undo (Ctrl/Cmd+Z, up to 100 steps), and duplicate
  (Ctrl/Cmd+D) work from the keyboard or the toolbar buttons.
- Name, type, keyshape, and display preferences persist in localStorage.
- **Export JSON** downloads a canonical-schema geometry scaffold. Complete its
  `sourceAnalysis` mappings and spacing checks before validation and delivery.
  **Preview SVG** is explicitly non-canonical and exists only for visual review.

## Layout

| Folder | Contents |
| --- | --- |
| `frontend/` | Profile-aware editable-JSON composer; `js/icon-profiles.js` is generated from `core/icon_profiles.json` |
| `assets/shapes/` | Standalone SVG files for every shape, generated from the registry |
| `core/` | Python-only geometry, emission, validation, overlap, hole/pinch QA, asset-generation, and regression-test tooling |
| `docs/` | Source hierarchy, canonical pipeline, thin lane adapters, script matrix, and QA guides |
| `backend/` | (reserved, empty for now) |

Start with [docs/README.md](docs/README.md).
