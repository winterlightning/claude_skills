"""corn (redraw of the new-pipeline traced SVG).

Plan: an ear of corn standing upright, mirrored about x=24 on VRECT_M
(centerline box (10,4)-(38,44)).
- cob (one open contour): walls x=18 / x=30 from y=16 to the kernel row at
  y=18, then leaning in by 1 to their feet (19,29)/(29,29) on the husk so the
  wall stays 8 from the husk's outer edge below the leaf tip; closed on top
  by a tangent-continuous dome whose apex sits on the box top (24,4).
- kernel row: one r10 arc (18,18)-(30,18) bowed up 2, sharing both ends with
  the walls; it splits the cob into two kernel cells (about 7 and 8 across).
- husk (one closed contour): two pointed leaves whose tips sit on the box
  sides (10,20)/(38,20). The outer edge is one smooth U from tip to tip
  through the box bottom (24,44); each inner edge runs from its tip through
  the wall foot (19,29)/(29,29) into a smooth cup meeting at (24,32).
- stem: a centre line (24,32)-(24,44) separating the two leaves.
Traced shape: 20260930-1042-corn/corn_raw.svg and corn.png, read for
proportion only (cob about half the husk width, tips at mid height).
No useful Lucide match (Lucide has no corn); construction follows Lucide's
wheat/leaf habits: smooth cubics, pointed tips, mirrored halves.

Metric issues:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted for it.
- stroke-count (warn, 11 strokes): fixed; 5 parts (cob, kernel row, husk,
  stem), under the prompt budget of 6.
- keyshape-short-axis (warn, y 96%): fixed; the dome apex is on y=4, the husk
  bottom on y=44 and the leaf tips on x=10/38, so VRECT_M is filled exactly.
- clearance errors between the cob walls, the kernel lines and the leaves
  (e0/e2, e0/e4, e0/e6, e0/e7, e0/e8, e2/e3, e2/e6, e2/e7, e3/e8, e3/e10,
  e4/e9, e4/e10, e5/e10, e6/e10 ...): fixed; the traced double lines at the
  leaf crossing and the V where the leaves meet are gone, every distinct
  pair is 8 apart or shares a declared endpoint.
- holes 1.3-3.9 wide in the kernel grid and leaves (errors): fixed; every
  enclosed opening is now at least 6.7 across on ink (dome 6.7, lower
  kernel cell 7.3, leaves 6.9).
Not kept: the traced vertical kernel line and the second kernel arc. The tips
on x=10/38 must stay 8 from the walls, so the cob is 12 wide on centerlines;
a centre line would leave 4-wide cells, and a second row leaves the leaves
under 2 across. One bowed row keeps the kernel read.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "dfc9df01-8144-40e0-b66d-be471956d900"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1042-corn/corn_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
WALL_X = 18            # left cob wall; right wall is its mirror
DOME_FOOT_Y = 16       # walls turn into the dome here
ROW_Y = 18             # kernel row attaches to the walls here
ROW_R = 10             # chord 12 -> bowed up 2
TIP = (10, 20)         # left leaf tip
WALL_FOOT = (WALL_X + 1, 29)  # left wall lands on the inner husk edge
CUP = (AXIS, 32)       # inner husk edges meet here
BOTTOM = (AXIS, 44)


def mirror(p):
    return (2 * AXIS - p[0], p[1])


class CornRedraw(Solo48):
    icon_id = "corn-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/vegetables"
    aliases = ("corn", "maize", "corn cob", "ear of corn")
    keywords = ("corn", "maize", "cob", "husk", "vegetable", "grain", "harvest", "farm", "food")

    def build(self) -> None:
        # Cob, walked up the left wall, over the dome and down the right wall.
        self.add_line("wall-l-low", WALL_FOOT, (WALL_X, ROW_Y))
        self.add_line("wall-l-high", (WALL_X, ROW_Y), (WALL_X, DOME_FOOT_Y))
        dome_l = ((WALL_X, 9), (20, 4), (AXIS, 4))
        self.add_bezier(
            "dome", (WALL_X, DOME_FOOT_Y),
            dome_l,
            (mirror(dome_l[1]), mirror(dome_l[0]), mirror((WALL_X, DOME_FOOT_Y))),
        )
        self.add_line("wall-r-high", mirror((WALL_X, DOME_FOOT_Y)), mirror((WALL_X, ROW_Y)))
        self.add_line("wall-r-low", mirror((WALL_X, ROW_Y)), mirror(WALL_FOOT))
        self.add_contour("cob", "wall-l-low", "wall-l-high", "dome", "wall-r-high", "wall-r-low")

        self.add_arc("kernel-row", (WALL_X, ROW_Y), mirror((WALL_X, ROW_Y)), radius_x=ROW_R, sweep=True)
        self.relate("connect", "kernel-row", "cob")

        # Husk: outer U tip to tip, then the inner edges back through the wall feet.
        outer_l = ((10, 34), (14, 44), BOTTOM)
        self.add_bezier(
            "husk-outer", TIP,
            outer_l,
            (mirror(outer_l[1]), mirror(outer_l[0]), mirror(TIP)),
        )
        tip_run = ((12, 24), (16, 27))        # tip -> wall foot
        cup_run = ((22, 31), (22, 32))        # wall foot -> cup, (22,31) continues (16,27)->(19,29)
        self.add_bezier(
            "husk-inner-r", mirror(TIP),
            (mirror(tip_run[0]), mirror(tip_run[1]), mirror(WALL_FOOT)),
            (mirror(cup_run[0]), mirror(cup_run[1]), CUP),
        )
        self.add_bezier(
            "husk-inner-l", CUP,
            (cup_run[1], cup_run[0], WALL_FOOT),
            (tip_run[1], tip_run[0], TIP),
        )
        self.add_contour("husk", "husk-outer", "husk-inner-r", "husk-inner-l", closed=True)

        self.add_line("stem", CUP, BOTTOM)
        self.relate("connect", "stem", "husk")
        self.relate("connect", "cob", "husk")
