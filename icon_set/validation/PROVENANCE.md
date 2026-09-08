# Rendered hole and pinch measurement

`hole_geometry.py` vendors the measurement and overlay functions from
`/Applications/Workspaces/pictographic/claude_skills/core/qa_overlays.py`.
Source SHA-256: `e0695ce9a2d62f51c1b30746b7f24e61e364578eac5e5f48e6fde69c6579bcef`.

The functions from `_number` through `save_overlay` retain the source measurement
algorithm except for the background-connectivity correction documented below. Legacy CLI, profile imports, and report writing are excluded. The new
`library_qa.py` adapter supplies this project's native canvas and contract rules,
records hashes, and saves artifacts only when requested. No runtime dependency on
`claude_skills` remains. The source folder is unchanged.

The method narrows a 4-unit authored stroke to a 1-unit measuring stroke and
adds the 1.5-unit retreat to the minimum hole radius. Reports show both measured
and equivalent authored-stroke diameters. Raster supersampling is 32 samples per
unit. Hole measurements are raster approximations, not exact vector proofs.
Pinch checking follows the source's adjusted fill-depth calculation.

Spacing continues to use this project's existing `stroke_distance.py` engine,
including explicit composition ownership and declared-contact exemptions. Debug
component coloring and nearest-pair markers follow the source
`core/check_svg_spacing.py` overlay convention.

## User-approved small circles

The adapter applies the project's explicit 4×4 / 6×6 centerline-circle exception
after the unchanged measurement functions. Only complete circular regions qualify;
raw measurements and the pre-exception verdict remain in JSON. The HTML marks
accepted exceptions. This policy is in `negative-space.v1.json` and does not
modify the source algorithm or exempt spacing and pinch failures.

## Diagonal background connectivity correction

Enclosed background and pinch-pocket labeling use eight-connected neighbours
(edges and corners). The source used four-connected neighbours, which split off
single raster samples at sharp diagonal tips as extra holes. The airplane then
reported three holes at 32 samples/unit and four at 64, although it has two.
Eight-connectivity reports two at 16, 32, and 64 samples/unit. No minimum-area
filter is used: a genuinely isolated one-pixel hole is still measured. Existing
hole-diameter thresholds and the small-circle exception are unchanged. The
contract's measurement revision stamps reports with this corrected method.
