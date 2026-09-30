"""hand-with-round-wrist-ornament (redraw of the new-pipeline traced SVG).

Plan: an upright open hand, palm facing out, with a hollow round ornament
hanging below the closed wrist, on VRECT_L (centerline box (8,4)-(40,44)).
- hand: one closed contour. Three fingers of Lucide `hand` width (r4 tops =
  8 between centerlines, the finger tubes of Lucide's hand at 2x) with a
  staggered skyline (index top 6, middle top 4, ring top 7); the ring's
  right wall x=40 is the right extreme. Two divider lines drop from the
  finger valleys into the palm and stop 9 above the wrist.
- thumb: a r5 knuckle cap on the 3-4-5 points of centre (13,18), leaving
  the index wall at the crotch (16,14) and returning on a 45-degree outer
  edge to the wrist; its leftmost point x=8 is the left extreme.
- wrist: the hand is closed by a flat wrist line y=25 with a r4 heel corner.
- ornament: a r5 circle (hole 6 ink) on the middle-finger axis x=28, top 9
  below the wrist line, bottom y=44 the bottom extreme.
The generated image has four fingers; at stroke 4 four 8-unit fingers plus a
thumb need 40 across, more than the 32 of VRECT_L, so the hand keeps three
fingers and a short thumb.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4, every gap budgeted at stroke 4.
- keyshape-short-axis: switched VRECT_M -> VRECT_L (the hand needs 32 across);
  all four extremes sit on the VRECT_L box exactly.
- clearance e0-e1 / e0-e2 (finger walls 3.2 apart): fingers are 8 wide on
  centerlines with one shared divider per valley.
- clearance e2-e3 (wrist vs ornament 2.0): the circle top is 9 below the wrist.
- hole 3.21 (ornament): the circle is r5, a 6-unit inscribed hole.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a053cd16-d4e9-4fa2-8cbc-8e8c60de043b"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1539-hand-with-round-wrist-ornament/"
    "hand-with-round-wrist-ornament_raw.svg"
)
AUTHOR = "claude-opus-5-5"

FINGER_R = 4                         # finger tip radius: 8-wide fingers
INDEX, MIDDLE, RING = 20, 28, 36     # finger axes x
INDEX_Y, MIDDLE_Y, RING_Y = 10, 8, 11  # finger tip centres y
DIVIDER_END = 16                     # divider lines stop here
WRIST = 25                           # wrist line y
HEEL_R = 4                           # right heel corner radius
THUMB_C = (13, 18)                   # thumb cap centre (r5, 3-4-5 ends)
THUMB_R = 5
ORN_C = (28, 39)                     # ornament centre, on the middle axis
ORN_R = 5


class HandWithRoundWristOrnamentRedraw(Solo48):
    icon_id = "hand-with-round-wrist-ornament-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures"
    aliases = ("hand with charm", "raised hand with bead", "palm with pendant")
    keywords = ("hand", "palm", "wrist", "ornament", "charm", "bead", "bracelet", "jewelry")

    def build(self) -> None:
        r = FINGER_R
        left, right = INDEX - r, RING + r
        tx, ty = THUMB_C
        crotch = (tx + 3, ty - 4)          # on the index wall x=16
        thumb_out = (tx - 4, ty + 3)
        heel = right - HEEL_R
        wrist_l = (thumb_out[0] + WRIST - thumb_out[1], WRIST)  # 45-degree edge

        self.add_line("index-wall", crotch, (left, INDEX_Y))
        self.add_arc("index-tip", (left, INDEX_Y), (INDEX + r, INDEX_Y), radius_x=r)
        self.add_line("middle-stem", (INDEX + r, INDEX_Y), (MIDDLE - r, MIDDLE_Y))
        self.add_arc("middle-tip", (MIDDLE - r, MIDDLE_Y), (MIDDLE + r, MIDDLE_Y), radius_x=r)
        self.add_line("ring-stem", (MIDDLE + r, MIDDLE_Y), (RING - r, RING_Y))
        self.add_arc("ring-tip", (RING - r, RING_Y), (right, RING_Y), radius_x=r)
        self.add_line("palm-wall", (right, RING_Y), (right, WRIST - HEEL_R))
        self.add_arc("heel", (right, WRIST - HEEL_R), (heel, WRIST), radius_x=HEEL_R)
        self.add_line("wrist", (heel, WRIST), wrist_l)
        self.add_line("thumb-edge", wrist_l, thumb_out)
        self.add_arc("thumb-tip", thumb_out, crotch, radius_x=THUMB_R)
        self.add_contour(
            "hand", "index-wall", "index-tip", "middle-stem", "middle-tip",
            "ring-stem", "ring-tip", "palm-wall", "heel", "wrist",
            "thumb-edge", "thumb-tip", closed=True,
        )

        # Finger dividers drop from the two valleys into the palm.
        self.add_line("divider-1", (INDEX + r, INDEX_Y), (INDEX + r, DIVIDER_END))
        self.add_line("divider-2", (RING - r, RING_Y), (RING - r, DIVIDER_END))
        self.relate("connect", "hand", "divider-1")
        self.relate("connect", "hand", "divider-2")

        # Ornament: a hollow circle hanging below the wrist.
        ox, oy = ORN_C
        self.add_arc("orn-top", (ox - ORN_R, oy), (ox + ORN_R, oy), radius_x=ORN_R)
        self.add_arc("orn-bottom", (ox + ORN_R, oy), (ox - ORN_R, oy), radius_x=ORN_R)
        self.add_contour("ornament", "orn-top", "orn-bottom", closed=True)
