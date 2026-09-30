"""hand-reaching-for-diamond (redraw of the new-pipeline traced SVG).

Plan: a palm-up hand reaches in from the lower left; a faceted diamond hovers
above the cupped palm at the upper right, as in the generated image. Authored
on SQUARE (the suggested keyshape), centerline box (6,6)-(42,42).
- diamond (Lucide `gem`, without the inner facet lines): flat table y=6 from
  x 29..37, girdle y=14 from x 24..42 drawn as a closed outline plus the
  girdle line, pavilion tip (33,22). Crown height 8 so the table and girdle
  lines keep the 8 centerline gap; the table and crown stay mirrored on x=33.
- arm: upper edge on a 3-4-5 slope from (6,42) to the heel of the palm at
  (18,33); lower edge parallel to it, 8.4 away, from (20,42) up to the wrist.
- palm: one smooth run over the thumb mound (apex (24,25)) down into a flat
  cup y=31 that sits 9 below the diamond tip, then the finger top to (38,31),
  an r4 fingertip about (38,35) reaching the box edge x=42, and the finger
  underside y=39 back to the wrist. Finger top and underside are 8 apart.
The hand is open at the arm, so it encloses no hole.

Metric issues fixed:
- clearance e0/e1 (girdle 5.26 from the table): crown height is now 8.
- clearance e1/e2 (diamond tip 4.4 from the palm): the cup sits 9 below the
  tip and the thumb mound is 8.2 from the pavilion edge.
- hole at (29.8,8.8), 1.4 wide, and hole at (31.9,16.2), 5.49 wide: the crown
  trapezoid (8/18 wide, 8 high) and pavilion triangle (18 wide, 8 high) are the
  only holes, both at least 6 inscribed on centerlines.
- keyshape-short-axis: every extreme sits on the SQUARE box (x 6 at the arm,
  x 42 at the girdle and fingertip, y 6 at the table, y 42 at the arm ends).
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8.
- no-head (warn): not applicable; the subject is a hand and arm only, with no
  figure or head, so no head gap is needed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "bce3f8f6-b015-42a5-94c3-92f3bb3be306"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1528-hand-reaching-for-diamond/hand-reaching-for-diamond_raw.svg"
AUTHOR = "claude-opus-5-5"

GEM_AXIS, GEM_TOP, GIRDLE_Y, GEM_TIP = 33, 6, 14, 22
TABLE_HALF, GIRDLE_HALF = 4, 9
CUP_Y, UNDER_Y, TIP_R = 31, 39, 4       # palm cup, finger underside, fingertip radius
FINGER_X = 38                           # fingertip arc centre x (reaches x=42)
ARM_TOP = ((6, 42), (18, 33))           # upper arm edge, 3-4-5 slope
ARM_LOW = ((20, 42), (24, 39))          # lower arm edge, parallel
MOUND = (23, 26)                        # thumb mound apex
CUP_START = 30


class HandReachingForDiamondRedraw(Solo48):
    icon_id = "hand-reaching-for-diamond-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ("reach for diamond", "gem in hand", "catch diamond")
    keywords = ("hand", "diamond", "gem", "jewel", "reach", "palm", "wealth", "value", "premium")

    def build(self) -> None:
        a = GEM_AXIS
        self.add_polyline(
            "gem",
            (a - TABLE_HALF, GEM_TOP), (a + TABLE_HALF, GEM_TOP), (a + GIRDLE_HALF, GIRDLE_Y),
            (a, GEM_TIP), (a - GIRDLE_HALF, GIRDLE_Y),
            closed=True,
        )
        self.add_line("girdle", (a - GIRDLE_HALF, GIRDLE_Y), (a + GIRDLE_HALF, GIRDLE_Y))
        self.relate("connect", "girdle", "gem-2")
        self.relate("connect", "girdle", "gem-4")

        heel = ARM_TOP[1]
        mx, my = MOUND
        self.add_line("arm-top", *ARM_TOP)
        self.add_bezier(
            "palm",
            heel,
            ((heel[0] + 2, heel[1] - 1.5), (mx - 3, my), MOUND),
            ((mx + 3, my), (CUP_START - 3, CUP_Y), (CUP_START, CUP_Y)),
        )
        self.add_line("finger-top", (CUP_START, CUP_Y), (FINGER_X, CUP_Y))
        self.add_arc("fingertip", (FINGER_X, CUP_Y), (FINGER_X, UNDER_Y), radius_x=TIP_R, sweep=True)
        self.add_line("finger-under", (FINGER_X, UNDER_Y), ARM_LOW[1])
        self.add_line("arm-low", ARM_LOW[1], ARM_LOW[0])
        chain = ["arm-top", "palm", "finger-top", "fingertip", "finger-under", "arm-low"]
        for x, y in zip(chain, chain[1:]):
            self.relate("connect", x, y)
