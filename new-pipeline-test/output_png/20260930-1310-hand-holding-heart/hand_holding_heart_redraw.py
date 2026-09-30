"""hand-holding-heart (redraw of the new-pipeline traced SVG).

Subject: an open, upward-facing hand entering from the lower left, its
cupped palm holding a hollow heart above it.

Plan: SQUARE (centerline box (6,6)-(42,42)), as suggested by the metrics
(score 1.25, exact fill on both axes). Two parts, as in the generated image:
- heart: one closed contour of two mirrored cubic runs about x=27 --
  notch (27,10), lobe tops on y=6, sides on x=17 / x=37 (vertical tangent),
  45-degree V into the tip (27,21). Lucide `heart` construction.
- hand: one open contour -- upper wrist on 45 degrees from (6,36), palm
  top as one S cubic (knuckle hump, dip under the heart tip, rise to the
  fingers), fingertip as an r=5 arc about (37,31) on 3-4-5 knots so both
  joins are tangent (finger points up-right on 4:-3), and the palm
  underside as two cubics that ease into the lower wrist ending on y=42.
  Lucide `hand-heart` informed the open cupped palm; its thumb, separate
  wrist cuff and finger lines were not used (the image has none).
Extremes: x=6 wrist end, x=42 fingertip, y=6 heart lobes, y=42 lower wrist.

Metric issues:
- clearance e0/e1 (4.04 on centerlines): the heart now sits clear of the
  palm -- tip (27,21) to the palm top is 8.9 on centerlines (>= 8).
- stroke-width (trace 2.77 after fitting): redrawn at stroke 4; the palm
  band (upper vs lower edge of the same contour) was re-spaced to >= 9.1
  on centerlines so it stays open at the heavier weight.
- no-head (human subject, no head traced): false positive -- the subject
  is a hand, not a figure; there is no head or torso, so no human figure
  is marked.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "045520ca-f23a-531a-b54e-ce7bc4cbf52e"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1310-hand-holding-heart/hand-holding-heart_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 27                  # heart mirror axis
HEART_TOP = 6
HEART_TIP = 21
HALF = 10                  # heart half-width: sides on x=17 / x=37


def mx(p):
    return (2 * AXIS - p[0], p[1])


class HandHoldingHeartRedraw(Solo48):
    icon_id = "hand-holding-heart-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "romance"
    aliases = ("hand heart", "care", "charity")
    keywords = ("hand", "heart", "holding", "care", "love", "charity", "donation", "support", "kindness")

    def build(self) -> None:
        notch = (AXIS, 10)
        tip = (AXIS, HEART_TIP)
        lobe = (AXIS + 5, HEART_TOP)
        side = (AXIS + HALF, 11)
        right = (
            (AXIS + 1, 8), (AXIS + 3, HEART_TOP), lobe,
            (AXIS + 8, HEART_TOP), (AXIS + HALF, 8), side,
            (AXIS + HALF, 14), (AXIS + 4, 17), tip,
        )
        left = tuple(mx(p) for p in right)
        self.add_bezier("heart-r", notch, right[0:3], right[3:6], right[6:9])
        self.add_bezier(
            "heart-l", tip,
            (left[7], left[6], left[5]),
            (left[4], left[3], left[2]),
            (left[1], left[0], notch),
        )
        self.add_contour("heart", "heart-r", "heart-l", closed=True)

        # hand: one open contour -- upper wrist, palm top, fingertip, palm
        # underside, lower wrist.
        self.add_line("wrist-top", (6, 36), (12, 30))
        self.add_bezier("palm-top", (12, 30), ((16, 26), (22, 36), (34, 27)))
        self.add_arc("fingertip", (34, 27), (40, 35), radius_x=5, sweep=True)
        self.add_bezier(
            "palm-under", (40, 35),
            ((36, 38), (30, 40), (26, 40)),
            ((22, 40), (18, 40), (14, 42)),
        )
        self.add_contour("hand", "wrist-top", "palm-top", "fingertip", "palm-under")
