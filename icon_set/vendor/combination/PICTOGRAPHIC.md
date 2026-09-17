# Pictographic integration

Copied from `pg_icon_management/combination` on 2026-09-17. The upstream
provenance is retained in PROVENANCE.md. The `preserve_geometry` flag keeps
explicit fractional placements proportional instead of snapping them.

`icon_set/scripts/combination_experiment.py` calls this engine in an isolated
subprocess. Each request gets a private temporary folder. The engine performs
the existing convex-hull erasure and returns a 64×64 SVG with stroke 4.

The Experiment → Combinations tab uses the 56 available generated pairs in
`icon_set/data/combination-pairs.json`. The file is an artwork snapshot, including
source IDs, SVG documents, their hashes, centerline bounds, and source canvases.
Publishing copies it to `gallery/experiment-combination.json`. No sibling app
or running service is needed. Pair availability does not indicate review approval.

Positions align painted bounds (centerline plus half stroke) to opposite edges:
With the default 2-unit outer padding, bottom-right puts the 48×48 main
canvas and its ink at 2,2; the 32×32 sub canvas is at 30,30 and its ink
ends at 62,62. Buffer clearance defaults to 8 units. Padding can be adjusted
from 0 to 8 units without scaling either component. Remaining presets mirror anchors,
with the unanchored axis centered for the four side positions. Offsets translate
artwork, leaving the component-canvas guides at their preset locations.

Adjustments are saved in browser local storage per pair. Preview/download does
not write final-icon records or approvals. `/api/combination-experiment` uses the
server interpreter, or `PICTOGRAPHIC_COMBINE_PYTHON` if supplied. Runtime libraries
are listed in requirements.txt.

The Combinations tab opens with all default results in a searchable grid.
A single Try combine button above the grid opens the adjustable composer.
Each component can be replaced with an approved SVG or a manual SVG upload.
The approved picker uses the same live review statuses as the Icon tab.
Uploaded SVGs are validated with the existing static-SVG validator and measured
in an isolated process. Square-canvas, stroked SVGs up to 1 MB are supported.
Replacement components remain in browser memory for the session; they do not
change the approved collection. Oversized custom artwork is reduced uniformly
to fit its 48/32 canvas. Build the
persistent preview cache after changing artwork or placement code with:

    python -m icon_set.scripts.build_combination_previews

The builder fingerprints artwork and engine code to reuse unchanged renders.
Gallery publication restores the result SVGs from the cache so ordinary gallery
rebuilds do not discard the grid.
