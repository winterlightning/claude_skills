"""batch-05-ribbon-tie (redraw of the new-pipeline traced SVG): a ribbon bow.

Plan: HRECT_L (centerline box (4,8)-(44,40)), mirrored about x=24.
- knot: 12x12 rounded square (r=2) centred on the axis, x 18..30, y 13..25.
- loops: each leaves the knot's top corner node (20,13), rises to a level apex
  on y=8, turns round a quarter-ellipse pair to its outer end on x=4/44 and
  returns through a level bottom node B=(11,27) to the knot's bottom corner
  node (20,25).
- tails: one closed ribbon per side. The inner edge continues from the
  knot's bottom corner node (the loop ends there too), the outer edge leaves
  the loop's bottom node B, and a slanted end cut joins the tips on y=40/38.
Lucide `gift` informed the knot-and-loops bow, Lucide `award` the ribbon tails.

Metric issues:
- keyshape-short-axis (HRECT_M x fill 96%): fixed by redrawing to exact
  extremes; switched to HRECT_L (fit score 1.16 vs 1.21) because HRECT_M's
  28-unit height cannot hold loops + tails with 8-unit centerline gaps.
- stroke-width 2.55: redrawn at stroke 4 with every gap budgeted for it.
- clearance e0..e4 (tails vs loops, loops vs knot) and narrow-join e1/e3:
  fixed. Every contact is now a shared node (knot corners, loop bottom
  node), the tail inner edge and loop bottom meet the knot at one point, and
  the tail's outer edge leaves the loop at ~63 deg instead of 33 deg.
- holes (3.8 knot, 2.51 tail wedges): fixed. Knot interior is 8 wide, each
  tail band is ~10-11 wide on centerlines, the old wedge holes are gone.
Not kept: the V-notched tail ends. A notch vertex must sit 8 from both tail
edges, which needs a 16-wide band; the 48 budget allows ~11, so the tails end
in a slanted cut instead.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a8df920a-b5e4-42ca-a8cb-d0665fd4de17"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1814-batch-05-ribbon-tie/batch-05-ribbon-tie_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
KNOT_X0, KNOT_Y0, KNOT_Y1, R = 18, 13, 25, 2   # knot x 18..30, y 13..25
TOP = (11, 8)            # loop apex (level)
OUT_X, MID_Y = 4, 17     # loop outer end
BOT = (11, 27)           # loop bottom node, tail outer edge starts here
INNER_TIP = (17, 40)
OUTER_TIP = (5, 38)
K = 0.5523


def mx(p):
    return (2 * AXIS - p[0], p[1])


class Batch05RibbonTieRedraw(Solo48):
    icon_id = "batch-05-ribbon-tie-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/gift"
    aliases = ("ribbon bow", "ribbon tie", "gift bow")
    keywords = ("ribbon", "bow", "tie", "gift", "present", "decoration")

    def build(self) -> None:
        x0, x1 = KNOT_X0, 2 * AXIS - KNOT_X0
        y0, y1 = KNOT_Y0, KNOT_Y1
        # Knot: rounded square, nodes at the line/arc junctions.
        self.add_line("knot-t", (x0 + R, y0), (x1 - R, y0))
        self.add_arc("knot-tr", (x1 - R, y0), (x1, y0 + R), radius_x=R)
        self.add_line("knot-r", (x1, y0 + R), (x1, y1 - R))
        self.add_arc("knot-br", (x1, y1 - R), (x1 - R, y1), radius_x=R)
        self.add_line("knot-b", (x1 - R, y1), (x0 + R, y1))
        self.add_arc("knot-bl", (x0 + R, y1), (x0, y1 - R), radius_x=R)
        self.add_line("knot-l", (x0, y1 - R), (x0, y0 + R))
        self.add_arc("knot-tl", (x0, y0 + R), (x0 + R, y0), radius_x=R)
        self.add_contour("knot", "knot-t", "knot-tr", "knot-r", "knot-br",
                         "knot-b", "knot-bl", "knot-l", "knot-tl", closed=True)

        k_top, k_bot = (x0 + R, y0), (x0 + R, y1)
        rx, ry_t, ry_b = TOP[0] - OUT_X, MID_Y - TOP[1], BOT[1] - MID_Y
        out = (OUT_X, MID_Y)
        loop = [
            ("in-top", k_top, ((17, 10), (14, TOP[1]), TOP)),
            ("out-top", TOP, ((TOP[0] - rx * K, TOP[1]), (OUT_X, MID_Y - ry_t * K), out)),
            ("out-bot", out, ((OUT_X, MID_Y + ry_b * K), (BOT[0] - rx * K, BOT[1]), BOT)),
            ("in-bot", BOT, ((15, BOT[1]), (18, 26.5), k_bot)),
        ]
        for side, f in (("l", lambda p: p), ("r", mx)):
            for name, start, ctrl in loop:
                self.add_bezier(f"loop-{side}-{name}", f(start), *[tuple(f(p) for p in ctrl)])
            self.add_contour(f"loop-{side}", *(f"loop-{side}-{n}" for n, *_ in loop))
            self.add_polyline(f"tail-{side}", f(BOT), f(OUTER_TIP), f(INNER_TIP), f(k_bot))
            self.relate("connect", f"loop-{side}", "knot")
            self.relate("connect", f"tail-{side}", "knot")
            self.relate("connect", f"tail-{side}", f"loop-{side}")
