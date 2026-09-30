"""chess-rook-wide-battlements (redraw of the new-pipeline traced SVG).

Plan: a chess rook on VRECT_M (centerline box (10,4)-(38,44)), as the
metrics suggested (fill 1.0 x 0.96; the redraw reaches y=4 and y=44 exactly).
Everything is mirrored about x=24.
- crown: an open-top cup, walls x=10 / x=38 from y=4 down to r=4 corner
  arcs, closed by the crown floor at y=21 (the tower's top).
- battlements: a rim line at y=10 across the cup and two ticks
  (19,4)-(19,10) / (29,4)-(29,10) above it, splitting the top into three
  wide merlons of 9 / 10 / 9 -- the Lucide chess-rook construction.
- body: one polyline from the crown floor at x=16 / x=32, tapering out to
  x=14 / x=34 at y=36, a 3:4 flare out to the base walls at (10,39) /
  (38,39), and a flat foot at y=44.
Three true notched merlons with two open notches need five bands of 8 on
centerlines (40 wide); VRECT_M allows 28 (VRECT_L 32), so the notches are
drawn as ticks over a rim instead, as Lucide does at 24.

Metric issues (chess-rook-wide-battlements_metrics.json):
- hole [23.9, 11.6] 2.88 wide (error): fixed -- the crown opening under the
  rim is 11 on centerlines (rim y=10, floor y=21), 7 inscribed, and the
  notch slivers are gone.
- keyshape-short-axis (y fill 96%, warn): fixed -- ink touches y=4 and y=44
  and x=10 / x=38 exactly.
- stroke-width (trace 2.55 after fitting, info): redrawn at stroke 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6827ce25-bda1-54bb-bc4b-11e435eb0b3f"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1912-chess-rook-wide-battlements/chess-rook-wide-battlements_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
LEFT, RIGHT = 10, 38                       # crown and base walls
TOP, RIM_Y, FLOOR_Y, FOOT_Y = 4, 10, 21, 44
CORNER_R = 4                               # crown floor corner arcs
TICK_DX = 5                                # ticks at 19 / 29: merlons 9 / 10 / 9
TOWER_TOP_DX, TOWER_FOOT_DX = 8, 10        # tower half-widths at y=21 / y=36
TOWER_FOOT_Y, BASE_Y = 36, 39              # 3:4 flare from x=14 to x=10


def mirror(x: int) -> int:
    return 2 * AXIS - x


class ChessRookWideBattlementsRedraw(Solo48):
    icon_id = "chess-rook-wide-battlements-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    aliases = ("rook", "castle chess piece")
    keywords = ("chess", "rook", "castle", "piece", "strategy", "game", "battlements")

    def build(self) -> None:
        tick_l, tick_r = AXIS - TICK_DX, AXIS + TICK_DX
        top_l, top_r = AXIS - TOWER_TOP_DX, AXIS + TOWER_TOP_DX
        foot_l, foot_r = AXIS - TOWER_FOOT_DX, AXIS + TOWER_FOOT_DX
        arc_y = FLOOR_Y - CORNER_R

        # Crown: open-top cup, split where the rim and tower attach.
        self.add_line("crown-wall-l-top", (LEFT, TOP), (LEFT, RIM_Y))
        self.add_line("crown-wall-l", (LEFT, RIM_Y), (LEFT, arc_y))
        self.add_arc("crown-corner-l", (LEFT, arc_y), (LEFT + CORNER_R, FLOOR_Y),
                     radius_x=CORNER_R, sweep=False)
        self.add_line("crown-floor-l", (LEFT + CORNER_R, FLOOR_Y), (top_l, FLOOR_Y))
        self.add_line("crown-floor", (top_l, FLOOR_Y), (top_r, FLOOR_Y))
        self.add_line("crown-floor-r", (top_r, FLOOR_Y), (RIGHT - CORNER_R, FLOOR_Y))
        self.add_arc("crown-corner-r", (RIGHT - CORNER_R, FLOOR_Y), (RIGHT, arc_y),
                     radius_x=CORNER_R, sweep=False)
        self.add_line("crown-wall-r", (RIGHT, arc_y), (RIGHT, RIM_Y))
        self.add_line("crown-wall-r-top", (RIGHT, RIM_Y), (RIGHT, TOP))
        self.add_contour("crown", "crown-wall-l-top", "crown-wall-l", "crown-corner-l",
                         "crown-floor-l", "crown-floor", "crown-floor-r",
                         "crown-corner-r", "crown-wall-r", "crown-wall-r-top")

        # Battlements: rim across the cup, two ticks marking three merlons.
        self.add_polyline("rim", (LEFT, RIM_Y), (tick_l, RIM_Y), (tick_r, RIM_Y), (RIGHT, RIM_Y))
        self.add_line("tick-l", (tick_l, TOP), (tick_l, RIM_Y))
        self.add_line("tick-r", (tick_r, TOP), (tick_r, RIM_Y))
        self.relate("connect", "rim", "crown")
        self.relate("connect", "tick-l", "rim")
        self.relate("connect", "tick-r", "rim")

        # Body: tapered tower, flared base, flat foot.
        self.add_polyline(
            "body",
            (top_l, FLOOR_Y), (foot_l, TOWER_FOOT_Y), (LEFT, BASE_Y), (LEFT, FOOT_Y),
            (RIGHT, FOOT_Y), (RIGHT, BASE_Y), (foot_r, TOWER_FOOT_Y), (top_r, FLOOR_Y),
        )
        self.relate("connect", "body", "crown")
