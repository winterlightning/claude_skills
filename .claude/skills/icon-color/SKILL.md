---
name: icon-color
description: Create or revise Pictographic color SVG variants from existing line-art icons, using semantic theme colors, black outer outlines, transparent openings, and clean inner junctions. Use for coloring icons, color experiments, or color-specific review feedback across sub, solo, and container families. Hand-authored; edit this file directly.
---

# /icon-color — semantic color variants

Use the user's requested icons, collection, theme, feedback, and output location.
Resolve repository paths from the directory containing `icon_set/`; when loaded
through a personal skill link, resolve the link to find this repository.

Read `icon_set/skills/icon-design/coloring.md` and the exact swatches in
`icon_set/skills/icon-design/color-theme.json` before coloring. These are the
maintained color rules and default theme. An explicit user theme overrides the
default palette; keep the outline, opening, and junction rules unless changed
by the user.

## Scope

Work from existing SVGs and preserve their family, native canvas, stroke width,
caps, joins, subject identity, and source art. Color is a variant of any family,
not a new family. Use vector/code tooling and a reproducible color generator.
Keep the approved outline as the comparison source and save color output
separately; do not change production approvals as part of a color experiment.

This skill may add a minimal silhouette closure or a meaningful color region
under the rules below. It does not require creating a new production primitive
for those color-only additions. For a new icon or substantial anatomical or
structural redesign, use `/icon-making` and the relevant family skill first.

## Workflow

1. **Inspect the drawing.** Render and view the original at native size and a
   larger size. Determine the actual object, material, separate parts, holes,
   and open ends. Use the name as context, not as proof of the depicted geometry.
2. **Plan regions and line ownership.** Identify filled surfaces, transparent
   openings, colored inner details, continuous structural lines, and black
   outer contours. Assign palette tokens by what each part represents. Note
   any closure or creative region and why it helps the subject read clearly.
3. **Generate the color variant.** Preserve original path geometry. Add only
   the necessary declared geometry. Paint fills and inner details behind the
   contours that own their junctions. Black outer outlines render last. Do not
   blindly fill every polygon or use the old stroke hue as a semantic classifier.
4. **Record identity and decisions.** Retain source ID/path, family, native
   canvas, and source hash. Record each part's token, transparent regions,
   added paths, and structural layering decisions. Reuse stable part IDs or
   path identities rather than applying another collection's sample numbers.
5. **Verify and deliver.** Inspect the rendered SVG and PNG at native size and
   enlarged junctions. Check transparent openings on more than one background,
   black border continuity, inner intersections, clipping, and repeated colors.
   Confirm valid SVG, allowed swatches, unchanged source files, and stable
   output on a second run. Show changed samples and refresh the requested
   gallery/downloads, preserving review feedback.

## Existing 500-sample experiment

Read this section only when the request concerns `work/color-review-500/`.

- `semantic_theme.py` owns semantic assignments, transparent fill exceptions,
  and structural stroke layering. Its numeric tables belong only to this
  fixed collection; inspect the target record before editing them.
- `color_geometry.py` declares color-only closures and creative regions.
- `theme.json` is this collection's exported theme. Keep it consistent with the
  maintained theme when applying the default rules; preserve an explicitly
  requested alternative theme.
- `apply_theme.py` updates the current assets, metadata, contact sheets, and
  SVG/PNG archive. Prefer it to a full source rebuild for color feedback.
- `test_outline_layers.py` checks preserved source paths, outline protection,
  openings, creative regions, and known junction regressions. Add a targeted
  render check when fixing a new recurring defect.
- To refresh Experiment, use `icon_set/scripts/experiment_gallery.py` to stage
  into a temporary directory and copy only `experiment-color.json` into
  `icon_set/dist/gallery/`. Preserve the separate fill collection.
- The local color feedback server caches revision hashes at startup. If it is
  running, verify its command and restart that specific server after updating
  assets. Preserve `reviews.sqlite3` and the user's current review page.

Report the changed subjects and visible improvements. Distinguish source-path
preservation and rendering checks from production geometry validation; a color
experiment does not imply production approval.
