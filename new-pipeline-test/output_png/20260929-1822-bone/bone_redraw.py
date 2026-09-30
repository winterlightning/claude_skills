"""bone (redraw of the new-pipeline traced SVG).

Plan: a horizontal dog-bone outline on HRECT_M (centerline box (4,10)-(44,38)),
drawn as one closed contour mirrored about x=24 and y=24.
- lobe: a circle of radius 5 about (9,15), with (9,33), (39,15) and (39,33)
  as its mirror images. Its left point sits on x=4 and its top on y=10, so
  the four lobes carry all four keyshape extremes.
- notch: a concave radius-10 arc centred (-3,24) that joins the two lobes on
  each end. It is externally tangent to both lobes at (5,18) and (5,30)
  (3-4-5 triangle), so the waist is smooth and dips in to x=7.
- shaft: two straight lines, y=18 and y=30, from x=17 to x=31. Each line meets
  its lobe through a concave radius-3 fillet centred (17,15), which touches
  the lobe at its right point (14,15) and the shaft at (17,18). Every join
  is tangent-continuous.
Traced shape: 20260929-1822-bone/bone_raw.svg and bone.png (read for the
subject only; nothing copied from its coordinates).
Lucide: lucide/bone informed the construction (round lobe arcs joined by a
small concave notch and a straight shaft). Lucide lays the bone diagonally.
This one stays horizontal to match the generated image.

Metric issues:
- stroke-width (info): drawn at stroke 4; all gaps budgeted for 4.
- keyshape-short-axis (y filled 47%): fixed. The lobes reach y=10 and y=38,
  so the bone fills the full HRECT_M height, and the lobes are rounder and
  taller than in the trace. The shaft is 12 tall on centerlines (the trace
  was about 5.5 once fitted).
- hole (4.33 inscribed, need 6): fixed. The shaft interior is 8 wide between
  the ink edges, and the lobe interiors are 6 across.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "bdd6c205-c49b-4436-8ff7-3c7c0b842d86"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1822-bone/bone_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24          # mirror axis for both x and y
LOBE_R = 5         # lobe circle about (9,15)
NOTCH_R = 10       # concave waist arc about (-3,24)
FILLET_R = 3       # concave lobe-to-shaft fillet about (17,15)
SHAFT_Y = 18       # top shaft line; the bottom one is its mirror (y=30)
SHAFT_X = 17       # where the fillet meets the shaft

# Upper-left quarter, walked from the notch tangent point clockwise to the
# shaft: (end, radius, large_arc, sweep) per arc.
LOBE_START = (5, 18)
QUARTER = (
    ((14, 15), LOBE_R, True, True),       # lobe over the left and top
    ((SHAFT_X, SHAFT_Y), FILLET_R, False, False),  # concave fillet into shaft
)




class BoneRedraw(Solo48):
    icon_id = "bone-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ("dog-bone", "dog-treat")
    keywords = ("bone", "dog", "pet", "treat", "skeleton", "chew")

    def build(self) -> None:
        members = []

        def piece(name, start, end, r, large, sweep):
            if r is None:
                self.add_line(name, start, end)
            else:
                self.add_arc(name, start, end, radius_x=r, large_arc=large, sweep=sweep)
            members.append(name)

        def quarter(tag, mirror_x, mirror_y, reverse):
            """The upper-left quarter mirrored; each mirror and a reversed
            walk flip the arc sweep."""
            def at(p):
                x, y = p
                return (2 * AXIS - x if mirror_x else x, 2 * AXIS - y if mirror_y else y)

            pts = [LOBE_START] + [q[0] for q in QUARTER]
            steps = [(pts[i], pts[i + 1], r, large, sweep)
                     for i, (_, r, large, sweep) in enumerate(QUARTER)]
            if reverse:
                steps = [(b, a, r, large, sweep) for a, b, r, large, sweep in reversed(steps)]
            flip = mirror_x ^ mirror_y ^ reverse
            for i, (a, b, r, large, sweep) in enumerate(steps):
                piece(f"{tag}-{i + 1}", at(a), at(b), r, large, sweep ^ flip)

        shaft_l, shaft_r = (SHAFT_X, SHAFT_Y), (2 * AXIS - SHAFT_X, SHAFT_Y)
        notch = [LOBE_START, (LOBE_START[0], 2 * AXIS - LOBE_START[1])]

        # Clockwise: upper-left lobe, top shaft, right end, bottom shaft, left notch.
        quarter("upper-left", False, False, False)
        piece("shaft-top", shaft_l, shaft_r, None, False, False)
        quarter("upper-right", True, False, True)
        piece("notch-right", (2 * AXIS - notch[0][0], notch[0][1]),
              (2 * AXIS - notch[1][0], notch[1][1]), NOTCH_R, False, False)
        quarter("lower-right", True, True, False)
        piece("shaft-bottom", (shaft_r[0], 2 * AXIS - SHAFT_Y),
              (shaft_l[0], 2 * AXIS - SHAFT_Y), None, False, False)
        quarter("lower-left", False, True, True)
        piece("notch-left", notch[1], notch[0], NOTCH_R, False, False)

        self.add_contour("bone", *members, closed=True)
