"""airplane-right-facing-full-wings (redraw of the new-pipeline traced SVG).

Plan: flat top view of an airliner flying right on HRECT_L (centerline box
(4,8)-(44,40)), one closed hollow silhouette mirrored about the fuselage axis
y=24 with M(x,y) = (x, 48-y).
- fuselage: straight sides on y=20 / y=28 (8 apart, the narrowest outlined
  tube that clears 8 between centerlines); elliptical nose rx6 ry4 about
  (38,24), tangent to both sides, its apex is the x=44 extreme.
- wings: one swept quadrilateral per side, leading edge (33,20)->(22,8),
  flat tip (22,8)-(17,8) on the y=8 / y=40 extremes, trailing edge back to
  the root at (23,20). A 3-unit tip left only a sliver of opening at
  stroke 4, so the tip is 5 wide.
- tailplanes: a small swept fin per side, front edge (14,20)->(8,14) at 45
  degrees, flat top (8,14)-(4,14) on the x=4 extreme, rear edge to the tail
  point (6,24) that leaves the reference's shallow V notch at the tail.
Spacing: the tail point is 8.49 from each fin's front edge and 8.94 from the
fin roots; the fin root is 8.05 from the wing's trailing edge.
Fixed from the trace metrics:
- keyshape-short-axis (warn): the trace filled only 93% of the HRECT_L x
  axis; the redraw is authored to all four extremes (x 4..44, y 8..40).
- stroke-width (info): the trace stroke was 2.46; redrawn at stroke 4, the
  tailplanes are enlarged (6 above the fuselage instead of ~3.5) and the
  tail notch, fin roots and wing roots are re-spaced to keep 8 between
  centerlines.
Lucide `plane` informed the rounded nose and swept wings; the full symmetric
top view follows the generated image.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3297cd8c-f784-4a07-8f3e-82b7e7146b94"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1812-airplane-right-facing-full-wings/airplane-right-facing-full-wings_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS_Y = 24
NOSE_C = (38, AXIS_Y)
NOSE_RX = 6
NOSE_RY = 4
NOSE_A = (38, 20)           # upper side meets the nose
WING_LEAD = (33, 20)        # upper wing roots on y=20
WING_TIP_LEAD = (22, 8)
WING_TIP_TRAIL = (17, 8)
WING_TRAIL = (23, 20)
FIN_ROOT = (14, 20)
FIN_TOP_FRONT = (8, 14)
FIN_TOP_REAR = (4, 14)
TAIL_POINT = (6, AXIS_Y)


def m(p):
    return (p[0], 2 * AXIS_Y - p[1])


class AirplaneRightFacingFullWingsRedraw(Solo48):
    icon_id = "airplane-right-facing-full-wings-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/aircraft"
    aliases = ("airplane", "plane", "airliner", "aeroplane")
    keywords = ("airplane", "plane", "flight", "aircraft", "travel", "airport", "airplane mode")

    def build(self) -> None:
        upper = [
            NOSE_A, WING_LEAD, WING_TIP_LEAD, WING_TIP_TRAIL, WING_TRAIL,
            FIN_ROOT, FIN_TOP_FRONT, FIN_TOP_REAR, TAIL_POINT,
        ]
        pts = upper + [m(p) for p in reversed(upper[:-1])]
        members = []
        for i, (a, b) in enumerate(zip(pts, pts[1:])):
            self.add_line(f"edge-{i + 1}", a, b)
            members.append(f"edge-{i + 1}")
        self.add_arc("nose", m(NOSE_A), NOSE_A, radius_x=NOSE_RX, radius_y=NOSE_RY, sweep=False)
        members.append("nose")
        self.add_contour("silhouette", *members, closed=True)
