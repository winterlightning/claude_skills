# png_to_svg_export — the PNG → SVG vectorizing stage, standalone

Copied out of `pg_app_utility/png_to_svg_new` (plus the two helper modules it
imports from sibling folders) so it can be dropped into another project.

## Run

    pip install -r requirements.txt        # numpy, pillow, matplotlib, cairosvg
    ./process.sh path/to/icon.png          # -> path/to/icon_raw.svg (only file saved)

Or call the binary directly (no Python needed):

    ./png2svg icon.png --svg-dir out/      # one SVG per connected component
    ./png2svg icon.png --snap --svg-dir out/

## What is here

| file | role |
|---|---|
| `png2svg` | the vectorizer. Self-contained C binary, **macOS arm64 only**. Source lives in `svg_extraction_polyline/c/` of the original repo (not on this machine); rebuild for Intel/Linux |
| `holecmp` | optional scorer: `./holecmp icon.png result.svg` prints quality JSON |
| `pre_process_input.py` | flattens transparency onto white, collapses all ink to black |
| `combine_svgs.py` | merges the per-object SVGs, fits them onto 1024×1024, keyshape-snaps |
| `step8/step8_scale_svg.py` | the bbox → uniform scale → center normalization used by combine_svgs |
| `keyshapes/` | stretch-to-fit snap onto the 12 grid shapes (`grid_system/*.svg`) |
| `process.sh` | drives the three steps above per input PNG |
| `docs/` | the original binary usage notes and full-pipeline description |

Input convention the binary expects: opaque black ink on white, ideally
1024×1024 (the desktop app resizes with LANCZOS before calling it).
`pre_process_input.py` handles the colour/transparency part.

## Not included

The original `process.sh` continues into grid snapping
(`snap_icon_to_grid_rewrite`), corner rounding (`corner_rounding`) and QA
overlays (`qa_overlays.py`, `svg_extraction/`). Those are separate
post-processing stages, not the vectorizing itself. See `docs/PROCESS.md`.
