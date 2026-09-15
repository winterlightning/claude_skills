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

## Stick-figure head alignment

When translating a human reference into a stick figure, identify the body line
before placing the head: locate the hip and shoulder/neck junctions, then extend
the torso centerline from the hip through the shoulder toward the head. Place
the head center on this extended axis, beyond the shoulder, so the head follows
the torso's lean. For a bent or curved torso, use the upper torso's direction
at the neck rather than a line through the entire body. Do not use an arm,
raised hand, or the canvas vertical axis as the body axis.

Keep the head close to its own shoulders using the exact detached-head gap
below. For stick figures, establish that gap at the actual upper torso/neck
junction; an arm passing closer to the head does not satisfy this placement
requirement. Do not raise an arm to manufacture the required gap while leaving
the head farther from the torso. Check clearance to the arms separately.
Solve alignment and clearance together; do not slide the head sideways
or farther away just to clear a raised arm or fit the keyshape. Rebalance the
pose within the reference's action if necessary. Only depart from the torso
axis when the reference clearly shows a deliberate neck bend or head offset;
preserve that anatomical relationship, not an accidental floating head.

For example, in `football-player-kicking-ball-sports`, a torso that extends
upward to the right needs its head along that same continuation, not displaced
to the left while the body leans the other way. A correct minimum gap alone
does not establish correct head placement.

Balance head size and torso curvature together with placement. A slightly
larger circular head and a smooth upper torso can preserve the reference's
action while making the head read as part of the figure. Choose proportions
by native-size review; do not impose one head radius on every pose or increase
the visible gap to accommodate an undersized head.

### Python flags for detached stick figures

After building each stick figure, explicitly pair its head and upper torso:

```python
self.add_arc("head-top", (20, 10), (28, 10), radius_x=4)
self.add_arc("head-bottom", (28, 10), (20, 10), radius_x=4)
self.add_contour("head", "head-top", "head-bottom", closed=True)
self.add_line("torso", (24, 22), (24, 32))
self.mark_human_figure(
    "person", head="head", torso="torso", torso_junction="start",
)
```

This is a construction fragment, not a complete keyshape-fitting icon. Use one
unique figure ID per person. `head` identifies the head outline primitive or
contour; `torso` identifies the actual upper torso line, arc, or Bezier primitive,
never an arm or a whole body contour. For a segmented torso, flag the segment
next to the neck. `torso_junction` selects that primitive's `start` or `end`
endpoint at the neck, so later validation can recover the upper torso direction.

The model retains these flags in `draw().human_figures` and the JSON graph's
`human_figures` records, with exact targets `centerline_gap=8` and `ink_gap=4`.
The centerline gap is measured from the **head outline**, not its center point:
in this example, `22 - (10 + 4) = 8`, leaving `8 - 2 - 2 = 4` visible units.
These are authoring targets for future validation/repair, not measured results.
Flags do not move geometry, waive MIC, or create a `connect` relationship.
Continue checking the actual spacing and alignment described here. Do not use
these detached-head flags for avatars with touching head/body ink.

## Head-to-body gap

For the avatar skill within `solo`, the current rule is **head ink touching body
ink, with zero visible gap**. Read `authoring.avatar.head_body_ink_gap` in the
profile contract and the derived constants in the solo base. Tangent contact
between two 4-unit strokes has 4 units between centerlines. Declare a scoped
`connect` for the actually touching paths; other MIC and hole checks remain.
Face/jaw outlines use circular arcs with equal radii, never oval or flattened
face geometry. Hair/headwear can retain their identifying outlines. The avatar
rule supersedes the detached layout in user.svg and the generic rule below.

A standalone portrait bust in another subject category (for example, a deity
wearing a helmet) can declare `human_construction = "bust"` on its Python
class. This identifies the same touching-ink construction without changing its
subject category. Curved shoulder contact is accepted only when a circular jaw
and shoulder arc have aligned vertical extrema exactly 4u apart on centerlines,
and their actual paths have a direct scoped `connect`. Analytic support bounds
prove the zero-ink-gap contact; the declaration does not excuse overlap,
offset contact, oval faces, or crowding elsewhere.


For a detached user/person head, including solo stick figures, require **exactly 4 units of visible ink
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

### Approved placement example: approaching-ball player

`football-player-approaching-ball` is the user-approved visual example for
this repair. Inspect its [comparison preview](../../work/approaching-ball-head-alignment/approved-comparison.png)
and [Python geometry](../../model/icons/solo/football_player_approaching_ball_419b465d_04b5_589e_924d_0688dd309d6c.py)
when applying this construction to a similar action pose.

The head center is `(29, 11)`, its centerline radius is `5`, and the actual
torso junction is `(24, 23)`. The curved torso's tangent at that junction
points toward the head. The junction is the nearest torso point to the head:

```text
head center to torso junction = sqrt(5² + 12²) = 13
head outline to torso stroke centerline = 13 - 5 = 8
visible ink gap = 8 - 2 - 2 = 4
```

The head's center point is not the head stroke's centerline. For a circular
head of radius `r`, use `distance(head_center, torso_junction) = r + 8`
only when that junction is the nearest body point; verify that no other torso
or arm segment comes closer. For a curved torso, align with its tangent at
the junction rather than forcing the head, shoulder, and hip onto one line.

This example has visual approval and an exact geometric spacing calculation,
but its diagonal head/body distance still produces an automated `review`
warning. Record both facts separately. An approximate reading such as
`8.00002` is not itself proof of exact clearance; retain the analytical
calculation and nearest-point justification. Visual approval does not change
the checker result or release requirements.

## Review

Record the human reference paths and the shared head/body parameters in the
module. Confirm the actual emitted head-to-body gap (not just a named constant),
then compare the result with the selected reference at native size in both
themes. For stick figures, extend the upper torso axis visually through the
shoulder and check that the head center follows it on the head side; record any
reference-supported neck bend or offset. Check head shape, relative head size,
shoulder/limb construction, and the avatar contact (or detached 4-unit gap at
the actual torso junction for stick figures). A generic MIC pass only proves
a minimum; it does not enforce this exact human spacing rule or visual
consistency. Report visual approval, analytical spacing evidence, and automated
validation status separately.
