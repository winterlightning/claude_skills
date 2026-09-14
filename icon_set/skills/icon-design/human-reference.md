# Shared human construction

For any icon containing a human, inspect the relevant reference in
`icon_set/references/human_ref/` before authoring or repairing its geometry:

- `user.svg`: user/avatar busts — circular outlined head, broad smooth shoulders,
  short rounded sides, and an open bottom. Keep its head-to-shoulder proportions.
- `full_body_ref.png`: full-body people and human actions — circular outlined
  heads, simple round-ended limbs, coherent torso/limb strokes, and minimal
  anatomy. Select the pose closest to the brief and preserve the requested action.

These references take priority over Lucide and older generated human icons for
human anatomy, proportions, and silhouette. Lucide may inform other objects or
construction techniques. Inspect both references when the subject mixes bust
and body construction. The full-body sheet is a style reference, not a request
to combine its four scenes. Render the SVG and view the PNG; filenames alone
are not visual evidence.

Keep the same human vocabulary throughout the set, including people in groups
and scenes. Reuse shared head radii and body parameters for equivalent figures
at the same visual scale. Adapt pose and family geometry deliberately; do not
scale a finished icon between families or copy fractional reference coordinates.

## Head-to-body gap

For `avatar`, read `profiles.AVATAR48.head_body_ink_gap` in
`icon_set/model/contracts/icon-profile.v1.json`; the avatar base exports
`HEAD_BODY_INK_GAP` and derives `HEAD_BODY_CENTERLINE_GAP` by adding the stroke.
It currently matches the shared 4-unit gap below, but can be changed separately.
Use `/icon-avatar` for a standalone 48x48 head-and-body avatar.

For a detached user/person head in other families, require **exactly 4 units of visible ink
clearance** to its own body/shoulders, measured between the nearest painted
edges. With stroke 4 this is **8 units between centerlines**, not 4. For a
frontal bust, derive `body_top = head_cy + head_radius + stroke_width + 4`.
In `user.svg`, the head centerline ends at y=22 and the shoulder centerline
begins at y=30; painted edges are y=24 and y=28.

For tilted/action poses, measure the shortest head-to-body gap rather than
only subtracting vertical coordinates. Preserve true anatomical connections
when the subject calls for a continuous neck; never add a neck or a false
`connect` relationship to bypass the detached-head gap. This rule does not set
spacing between different people or between a head and an unrelated object.

Do not enlarge the gap to 5+ units merely to silence a curved-distance warning.
Use geometry whose exact separation can be certified; if the checker cannot
prove it, report the unresolved check instead of claiming a pass. Keep the
profile, stroke, grid, and all other validation thresholds unchanged.

## Review

Record the human reference paths and the shared head/body parameters in the
module. Confirm the actual emitted head-to-body gap (not just a named constant),
then compare the result with the selected reference at native size in both
themes. Check head shape, relative head size, shoulder/limb construction, and
the compact 4-unit gap. A generic MIC pass only proves a minimum; it does not
enforce this exact human spacing rule or visual consistency.
