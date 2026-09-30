"""hand playing yoyo (redraw of the new-pipeline traced SVG).

Plan: VRECT_L (centerline box (8,4)-(40,44)); a cropped stick arm hanging a
yo-yo on its string.
- arm: one polyline, shoulder (8,4) on the x=8 / y=4 corner, 45-degree upper
  arm down to the elbow (18,14), 3:1 forearm up to the hand (30,10).
- string: straight down from the hand to the yo-yo's top apex, sharing the
  hand node with the arm and the apex node with the yo-yo (both connected).
- yo-yo: circle r=10 about (30,34) drawn as two half arcs split at the string
  apex; its bottom apex is the y=44 extreme and its right apex the x=40
  extreme. Axle: a dot at the centre.
Metric issues fixed:
- stroke-width: redrawn at stroke 4 with every gap budgeted for it.
- keyshape-short-axis: parts rebuilt to touch all four VRECT_L extremes.
- clearance e0/e2, e1/e2 and hole (3.8 wide): the axle was a traced dot
  7.6 from the ring; now the ring is r=10 around a dot axle, so the ring
  is 10 from the axle on centerlines and the annulus is 6 wide in ink.
- head-gap: false positive; the "head" e0 is the yo-yo ring and e2 its axle.
  There is no human head in this subject, so no mark_human_figure.
Dropped: the small hollow axle ring of the PNG; a hollow ring needs r>=5 for
its own 6-unit hole and would push the yo-yo to r=15, past the width budget.
Lucide: no useful match (no yo-yo in Lucide); construction follows the
Lucide rule of integer nodes, whole-circle radii and straight strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "28a605e6-a545-47ed-ae21-f45557bb8374"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1521-hand-playing-yoyo/hand-playing-yoyo_raw.svg"
AUTHOR = "claude-opus-5-5"

SHOULDER = (8, 4)
ELBOW = (18, 14)
YOYO_C = (30, 34)
YOYO_R = 10
HAND = (YOYO_C[0], 10)
YOYO_TOP = (YOYO_C[0], YOYO_C[1] - YOYO_R)
YOYO_BOTTOM = (YOYO_C[0], YOYO_C[1] + YOYO_R)


class HandPlayingYoyoRedraw(Solo48):
    icon_id = "hand-playing-yoyo-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "activities/toys"
    aliases = ("yo-yo", "yoyo trick", "playing yoyo")
    keywords = ("yoyo", "yo-yo", "toy", "hand", "string", "play", "game")

    def build(self) -> None:
        self.add_polyline("arm", SHOULDER, ELBOW, HAND)
        self.add_line("string", HAND, YOYO_TOP)
        self.relate("connect", "arm", "string")

        self.add_arc("yoyo-r", YOYO_TOP, YOYO_BOTTOM, radius_x=YOYO_R, radius_y=YOYO_R)
        self.add_arc("yoyo-l", YOYO_BOTTOM, YOYO_TOP, radius_x=YOYO_R, radius_y=YOYO_R)
        self.add_contour("yoyo", "yoyo-r", "yoyo-l", closed=True)
        self.relate("connect", "string", "yoyo")
        self.add_dot("axle", YOYO_C)
