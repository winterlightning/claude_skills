"""diagonal-chalk-stick-with-mark (redraw of the new-pipeline traced SVG).

Plan: a chalk stick lying on a 4:3 diagonal (lower left to upper right) and
one separate curved chalk mark below and to the right, on SQUARE
(centerline box (6,6)-(42,42)). Two parts:
- stick: a capsule of half-width 5 whose axis runs from A=(11,29) to
  B=(35,11) on the direction (4,-3). The perpendicular (3,4) has length 5, so
  both long sides are integer lines 10 apart: (8,25)->(32,7) and
  (38,15)->(14,33). The far end is a semicircle (r 5) about B; the near end
  is a full circle (r 5) about A, whose inner half (through (15,26)) is the
  visible end face of the stick and shares both tangent points with the
  outline (declared connect).
- mark: one arc r 25 about (22,17) from its lowest point (22,42) up to
  (42,32): a short smile-shaped stroke, 12 from the stick's lower side and
  12 from the end-face circle.
Extremes: left x=6 and bottom y=34 of the end circle, top y=6 and right
x=40 of the far cap; the mark reaches bottom y=42 and right x=42, so all
four SQUARE extremes sit on the box.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted at 8.
- keyshape-short-axis (warn, y filled 87%): fixed. The stick sits higher
  and the mark bottoms out at y=42, so x and y both span 6..42.
- hole at [34.9, 13.6] (error, 5.38 wide): fixed. The stick body is 10
  wide on centerlines, so its interior is 6 inscribed; the far end is a
  round cap instead of the traced pinched arc.
- hole at [9.4, 34.1] (error, 1.44 wide): fixed. The end face is a full
  r 5 circle, inscribed 6, instead of the traced sliver ellipse.
Lucide construction: no chalk icon; the capsule-with-end-face follows the
`cylinder` / `pill` construction (tangent lines on a round end), laid on a
3-4-5 diagonal so every node is an integer point.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d68116b9-c9af-4353-a796-1e8f052913d8"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1159-diagonal-chalk-stick-with-mark/"
    "diagonal-chalk-stick-with-mark_raw.svg"
)
AUTHOR = "claude-opus-5-5"

R = 5                     # stick half-width = end radius
AX, AY = 11, 29           # near end (end face) centre
BX, BY = 35, 11           # far end centre; A->B = 6 * (4,-3)
PX, PY = 3, 4             # perpendicular offset of length R
NEAR_UP = (AX - PX, AY - PY)    # (8,25)
NEAR_LO = (AX + PX, AY + PY)    # (14,33)
FAR_UP = (BX - PX, BY - PY)     # (32,7)
FAR_LO = (BX + PX, BY + PY)     # (38,15)
MARK_R = 25
MARK_START = (22, 42)           # lowest point of the arc about (22,17)
MARK_END = (42, 32)


class DiagonalChalkStickWithMarkRedraw(Solo48):
    icon_id = "diagonal-chalk-stick-with-mark-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/education"
    aliases = ("chalk", "chalk stick", "chalk with mark")
    keywords = ("chalk", "stick", "blackboard", "chalkboard", "school",
                "teacher", "write", "draw", "mark", "classroom")

    def build(self) -> None:
        # stick outline: upper side, far cap, lower side, outer half of end
        self.add_line("side-top", NEAR_UP, FAR_UP)
        self.add_arc("cap", FAR_UP, FAR_LO, radius_x=R, sweep=True)
        self.add_line("side-bottom", FAR_LO, NEAR_LO)
        self.add_arc("end-outer", NEAR_LO, NEAR_UP, radius_x=R, sweep=True)
        self.add_contour("stick", "side-top", "cap", "side-bottom",
                         "end-outer", closed=True)

        # visible end face: inner half of the end circle
        self.add_arc("end-face", NEAR_LO, NEAR_UP, radius_x=R, sweep=False)
        self.relate("connect", "end-face", "stick")

        # chalk mark
        self.add_arc("mark", MARK_START, MARK_END, radius_x=MARK_R, sweep=False)
