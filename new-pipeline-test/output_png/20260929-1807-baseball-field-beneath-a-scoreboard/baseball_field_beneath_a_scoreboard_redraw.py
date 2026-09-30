"""baseball-field-beneath-a-scoreboard (redraw of the new-pipeline traced SVG):
a baseball field fan with its infield diamond, under a scoreboard.

Plan: mirrored about x=24 on VRECT_L (centerline box (8,4)-(40,44)). The
vertical chain is the budget: scoreboard 10 + gap 9 + gap 8 + infield 13 = 40.
- scoreboard: sharp-cornered rectangle x 12..36, y 4..14 (10 tall, so the
  inside opening is 6 inscribed); its top is the y=4 extreme.
- field: one closed contour. Home plate (24,44) is the y=44 extreme; the foul
  lines run at 45 degrees through first/third base (32,36)/(16,36) to the
  fence corners (40,28)/(8,28), the x=8/x=40 extremes. The outfield fence is
  two r25 arcs (centres (23,48)/(25,48)) joined tangentially by a 2-unit
  straight centre-field run at y=23.
- infield: the diamond shares home plate and both bases with the foul lines,
  so only its upper sides are drawn (first -> second (24,31) -> third),
  connected at the bases.
Gaps: scoreboard -> fence is 9 (the fence contour has arcs, and an exact 8
against it comes back review); second base -> the straight fence run is 8.
Openings measured by library_qa: scoreboard 6.0, outfield 6.55, infield 5.94
(6.03 on paper; the build gate passes it, svg_metrics marks it ok). Moving the
bases out to (15,35)/(33,35) raises the infield to 6.27 but drops the
outfield to 5.75, so the 45-degree square-ish diamond was kept.
No useful Lucide match (Lucide has no baseball field); the scoreboard follows
Lucide's rect construction.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted for it.
- clearance e0/e3 (scoreboard vs field, 3.99): now 9 on centerlines.
- clearance e1/e3, e2/e3 (posts vs field, 2.4): the posts are dropped. With
  the scoreboard 9 above the fence there is no length left for them, and
  posts standing on the fence would enclose an opening only 4-5 tall.
- clearance e3/e4 (field vs floating diamond, 4.07): the diamond now shares
  home plate and the bases with the foul lines, as on a real field, so no gap
  is needed there; second base sits 8 below the fence.
- hole 2.2 (scoreboard inside): scoreboard 10 tall -> 6 inscribed.
- holes 1.2 / 1.2 (between posts, scoreboard and field): posts removed.
- hole 3.88 (inside the diamond): infield opening 5.94 raster / 6.03 exact.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0a9ee5d8-3550-452a-b859-653ff3a8c18e"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1807-baseball-field-beneath-a-scoreboard/baseball-field-beneath-a-scoreboard_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                      # mirror axis
BOARD = (12, 4, 36, 14)      # scoreboard x0, y0, x1, y1
HOME = (AX, 44)
SECOND = (AX, 31)
BASE_DX, BASE_Y = 8, 36      # first/third base on the 45-degree foul lines
CORNER_DX, CORNER_Y = 16, 28  # fence corners (foul-line ends)
FENCE_Y = 23                 # straight centre-field run
FENCE_HALF = 1               # half length of that run
SHOULDER_R = 25              # tangent fence arcs, centres (AX+-1, 48)


class BaseballFieldBeneathAScoreboardRedraw(Solo48):
    icon_id = "baseball-field-beneath-a-scoreboard-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/sports"
    aliases = ("baseball stadium", "ballpark", "baseball diamond")
    keywords = ("baseball", "field", "diamond", "scoreboard", "stadium", "ballpark", "sports")

    def build(self) -> None:
        x0, y0, x1, y1 = BOARD
        self.add_polyline("scoreboard", (x0, y0), (x1, y0), (x1, y1), (x0, y1), closed=True)

        left_corner = (AX - CORNER_DX, CORNER_Y)
        right_corner = (AX + CORNER_DX, CORNER_Y)
        third = (AX - BASE_DX, BASE_Y)
        first = (AX + BASE_DX, BASE_Y)
        fence_l = (AX - FENCE_HALF, FENCE_Y)
        fence_r = (AX + FENCE_HALF, FENCE_Y)

        self.add_arc("fence-left", left_corner, fence_l, radius_x=SHOULDER_R, sweep=True)
        self.add_line("fence-top", fence_l, fence_r)
        self.add_arc("fence-right", fence_r, right_corner, radius_x=SHOULDER_R, sweep=True)
        self.add_line("foul-right-outer", right_corner, first)
        self.add_line("foul-right-inner", first, HOME)
        self.add_line("foul-left-inner", HOME, third)
        self.add_line("foul-left-outer", third, left_corner)
        self.add_contour(
            "field",
            "fence-left", "fence-top", "fence-right",
            "foul-right-outer", "foul-right-inner", "foul-left-inner", "foul-left-outer",
            closed=True,
        )

        self.add_polyline("infield", first, SECOND, third)
        self.relate("connect", "infield", "field")
