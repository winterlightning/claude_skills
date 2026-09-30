"""butternut-squash (redraw of the new-pipeline traced SVG).

Plan: one butternut squash on VRECT_M (centerline box (10,4)-(38,44)),
body mirrored about x=24, stem leaning right.
- body: one closed contour, split at the top apex (24,9) where the stem
  attaches. Each half, top-down: a quarter-circle shoulder r6 about (24,15)
  to a straight neck wall at x=18 / x=30 (neck 12 wide on centerlines, runs
  y=15..19), one long S-cubic flaring from the neck into the bulb with vertical
  tangents at both ends (bulb extremes x=10 / x=38 at y=34), then a
  quarter-ellipse (14 x 10) to the bottom apex (24,44). Every knot is
  tangent-continuous. The straight neck over a low round bulb separates it
  from a pear.
- stem: one short cubic rising from the apex (24,9) and leaning right to
  (27,4), the top extreme; shares the apex knot, declared connect.
Metric issues:
- keyshape-short-axis (VRECT_M x fill 66%): the bulb is widened to 28 on
  centerlines so it reaches x=10 and x=38 exactly; neck widened with it
  to 12 (about the image's neck-to-bulb ratio). All four extremes sit on the box.
  Fixed.
- stroke-width (trace 2.66): drawn at stroke 4; the neck interior stays 8
  wide and the bulb hole is far above the 6 minimum. Fixed.
No useful Lucide match (no local Lucide squash, gourd, pear or pumpkin).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0e2a3b90-793a-5161-aa41-5a7e08f9195c"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1924-butternut-squash-vegetable-batch-010-11/butternut-squash-vegetable-batch-010-11_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
K = 0.5523              # cubic circle constant

APEX = (24, 9)          # body top, stem joins here
SHOULDER_C = (24, 15)   # shoulder circle centre, r6
SHOULDER_R = 6
NECK_X = AXIS - SHOULDER_R   # 18: left neck wall
NECK_END = 19                # straight neck runs y=15..19
BULB_X = 10                  # left bulb extreme
BULB_Y = 34                  # height of the bulb extreme
FLARE_IN = 7.0               # handle leaving the neck downward
FLARE_OUT = 7.0              # handle arriving at the bulb side
BOTTOM = (24, 44)
STEM_TOP = (27, 4)


def mx(p):
    return (2 * AXIS - p[0], p[1])


def left_half():
    """Left half of the body, top-down from APEX, as (c1, c2, knot)."""
    r = SHOULDER_R
    neck = (NECK_X, SHOULDER_C[1])
    rx, ry = AXIS - BULB_X, BOTTOM[1] - BULB_Y
    return [
        ((APEX[0] - K * r, APEX[1]), (neck[0], neck[1] - K * r), neck),
        ((NECK_X, neck[1] + 1.5), (NECK_X, NECK_END - 1.5), (NECK_X, NECK_END)),
        ((NECK_X, NECK_END + FLARE_IN), (BULB_X, BULB_Y - FLARE_OUT), (BULB_X, BULB_Y)),
        ((BULB_X, BULB_Y + K * ry), (AXIS - K * rx, BOTTOM[1]), BOTTOM),
    ]


def reverse(start, segs):
    pts = [start] + [s[2] for s in segs]
    return pts[-1], [(segs[i][1], segs[i][0], pts[i]) for i in range(len(segs) - 1, -1, -1)]


class ButternutSquashRedraw(Solo48):
    icon_id = "butternut-squash-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/vegetables"
    aliases = ("butternut squash", "squash", "gourd")
    keywords = ("butternut", "squash", "gourd", "vegetable", "pumpkin", "autumn", "food", "produce")

    def build(self) -> None:
        left = left_half()
        right = [tuple(mx(p) for p in s) for s in left]
        # Clockwise: apex -> right side -> bottom, then bottom -> left side -> apex.
        self.add_bezier("body-right", APEX, *right)
        _, up = reverse(APEX, left)
        self.add_bezier("body-left", BOTTOM, *up)
        self.add_contour("body", "body-right", "body-left", closed=True)

        self.add_bezier("stem", APEX, ((24, 7), (25, 5), STEM_TOP))
        self.relate("connect", "stem", "body")
