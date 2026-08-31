# Unlimited Shapes

Build icons by composing pre-built, consistent shape primitives. The current
specification uses a 48×48 design canvas and a half-scale 24×24 ship canvas.

> The browser editor uses the 48u design canvas and displays one selectable
> centered keyshape guide. See `docs/icon-rules.md` before creating output.

For the complete detect → load skill → map → remake → validate workflow, follow
[docs/icon-execution-steps.md](docs/icon-execution-steps.md).
For the usual two-file handoff—this runbook plus one supplied SVG—use
[docs/README-svg-input-processing.md](docs/README-svg-input-processing.md).

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
one centered painted keyshape: circle Ø44u, square 40×40u, portrait 36×44u, or
landscape 44×36u; the keyshape is the padding boundary. Add `--show` for
an interactive window. Use `--strict` in automation; status `3` means the
report needs manual review before icon making.

## Run it

Open `frontend/index.html` directly in a browser — no build step, no server,
no dependencies.

- Drag a shape from the palette onto the canvas (or click it to drop it in the
  center).
- Choose Circle, Square, Portrait, or Landscape in the toolbar to display the
  non-shipping painted keyshape guide.
- Move with fixed 1u grid snapping, resize with
  the handles (Shift keeps aspect), rotate with the top handle (15° snap),
  flip, and restyle stroke (and optional fill) in the properties panel. Shapes
  are stroke outlines with a **constant stroke width** — resizing recomputes
  the geometry, never scales it.
- Copy/paste (Ctrl/Cmd+C/V), undo (Ctrl/Cmd+Z, up to 100 steps), and duplicate
  (Ctrl/Cmd+D) work from the keyboard or the toolbar buttons.
- Preferences (selected keyshape guide and last-used design stroke width)
  persist in the browser's localStorage.
- **Export SVG** downloads the composed icon as a clean standalone `icon.svg`.

## Layout

| Folder | Contents |
| --- | --- |
| `frontend/` | The editor: `index.html`, `css/style.css`, `js/shapes.js` (browser-side registry paired with `core/shape_registry.py`), `js/app.js` |
| `assets/shapes/` | Standalone SVG files for every shape, generated from the registry |
| `core/` | Python-only geometry, emission, validation, overlap, hole/pinch QA, asset-generation, and regression-test tooling |
| `docs/` | `icon-execution-steps.md` — required end-to-end runbook; `atomic-shapes.md` — primitive contract; `icon-rules.md` — numbered design rules; `icon-authoring-guide.md` — authoring reference |
| `backend/` | (reserved, empty for now) |

Start with `docs/atomic-shapes.md` (the primitives) and `docs/icon-rules.md`
(how icons are made from them).
