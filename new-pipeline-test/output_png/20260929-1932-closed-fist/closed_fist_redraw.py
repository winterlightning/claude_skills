"""closed-fist (redraw of the new-pipeline traced SVG).

Plan: an upright front-view closed fist on SQUARE (centerline box
(6,6)-(42,42)).
- palm outline: one closed contour. Straight finger walls on x 6 / 42, S-curve
  heels (y 31 -> 37) into a 20-wide wrist (x 14..34) down to the bottom y 42.
- four knuckles: one cubic bump each, meeting at shared valley knots on
  y 11 at x 15 / 24 / 33. Heights are staggered as in the image: middle
  (apex y 6, the top extreme), ring 7, index ~8, pinky ~9.
- three knuckle divisions drop from the valleys. The index/middle and
  middle/ring divisions end on the thumb; the ring/pinky one ends free.
- thumb: one open contour folded across the front, from the left wall
  across to an r5 tip centred (21,25), back left as a short under edge
  that ends free.
- finger curl: one cubic from the thumb tip's lower right to the right
  wall, closing the curled ring and pinky fingers.
Lucide: no local hand-fist original was found; the construction follows
Lucide's rules (one-cubic rounded bumps, tangent wall/heel joins, integer
knots, arc centres on the grid).

Metric issues (closed-fist_metrics.json) and how they were handled:
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- keyshape-short-axis (SQUARE x fill 73%): kept SQUARE and widened the fist
  to the full 36 so the knuckle divisions sit 9 apart (x 6/15/24/33/42).
  VRECT_M/VRECT_L only allow a 7 or 8 pitch for four fingers.
- clearance e0/e2, e1/e3, e1/e4, e2/e4 (knuckle arcs and divisions 2-7
  apart): the knuckles are rebuilt as bumps that share valley knots with
  each other and with the divisions, so no two separate parts run closer
  than 8; the free ring/pinky division ends 8.4 from the thumb tip.
- narrow-join e4/e0 (curl meeting the wall at 33 deg): the curl now meets
  the right wall at y 20 at about 40 deg, and the right heel starts at y 31
  so the curl never runs parallel to it within 8 (build-gate internal
  spacing).
- holes at (21.8,9.4), (15.3,14.1), (29.0,19.3) (2.5-3.3 wide): the
  knuckle tops are open bumps, not pinched loops; every enclosed finger
  cell is at least 8 across on centerlines.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "398a358b-6ba9-5507-b8f7-6dfcb7f136d1"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1932-closed-fist/closed-fist_raw.svg"
AUTHOR = "claude-opus-5-5"

L, R, TOP, BOT = 6, 42, 6, 42            # SQUARE centerline box
VALLEY_Y = 11
DIVS = (15, 24, 33)                       # valley / division x, pitch 9
WRIST_L, WRIST_R, WRIST_Y = 14, 34, 37    # wrist sides and heel end
HEEL_Y = 31                               # walls turn into the heels
HEEL_PULL = 3                             # heel S-curve handle length
THUMB_Y = 20                              # thumb top edge
THUMB_WALL_Y = 23                         # thumb top meets the left wall
TIP_C, TIP_R = (21, 25), 5                # thumb tip arc
CURL_WALL_Y = 20                          # curl meets the right wall
CURL_C1, CURL_C2 = (30, 30), (37, 26)


class ClosedFistRedraw(Solo48):
    icon_id = "closed-fist-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/hands"
    aliases = ("fist", "clenched fist", "raised fist", "punch")
    keywords = ("fist", "hand", "punch", "power", "strength", "solidarity", "fight", "knuckles")

    def build(self) -> None:
        v1, v2, v3 = DIVS
        vy = VALLEY_Y
        # Palm outline, clockwise from the bottom-left wrist corner.
        self.add_line("wrist-l", (WRIST_L, BOT), (WRIST_L, WRIST_Y))
        self.add_bezier("heel-l", (WRIST_L, WRIST_Y), ((WRIST_L, WRIST_Y - HEEL_PULL), (L, HEEL_Y + HEEL_PULL), (L, HEEL_Y)))
        self.add_line("wall-l-low", (L, HEEL_Y), (L, THUMB_WALL_Y))
        self.add_line("wall-l-high", (L, THUMB_WALL_Y), (L, 15))
        self.add_bezier("index", (L, 15), ((L, 9), (12.5, 7.5), (v1, vy)))
        self.add_bezier("middle", (v1, vy), ((16, vy - 20 / 3), (23, vy - 20 / 3), (v2, vy)))
        self.add_bezier("ring", (v2, vy), ((25, vy - 16 / 3), (32, vy - 16 / 3), (v3, vy)))
        self.add_bezier("pinky", (v3, vy), ((34, 7.5), (R, 8.5), (R, 16)))
        self.add_line("wall-r-high", (R, 16), (R, CURL_WALL_Y))
        self.add_line("wall-r-low", (R, CURL_WALL_Y), (R, HEEL_Y))
        self.add_bezier("heel-r", (R, HEEL_Y), ((R, HEEL_Y + HEEL_PULL), (WRIST_R, WRIST_Y - HEEL_PULL), (WRIST_R, WRIST_Y)))
        self.add_line("wrist-r", (WRIST_R, WRIST_Y), (WRIST_R, BOT))
        self.add_line("wrist-bottom", (WRIST_R, BOT), (WRIST_L, BOT))
        self.add_contour(
            "outline", "wrist-l", "heel-l", "wall-l-low", "wall-l-high", "index", "middle",
            "ring", "pinky", "wall-r-high", "wall-r-low", "heel-r", "wrist-r", "wrist-bottom",
            closed=True,
        )

        # Thumb: top edge from the left wall, r5 tip, short under edge.
        cx, cy = TIP_C
        self.add_bezier("thumb-top-a", (L, THUMB_WALL_Y), ((9, 21), (12, THUMB_Y), (v1, THUMB_Y)))
        self.add_line("thumb-top-b", (v1, THUMB_Y), (cx, cy - TIP_R))
        self.add_arc("tip-a", (cx, cy - TIP_R), (cx + 3, cy - 4), radius_x=TIP_R, sweep=True)
        self.add_arc("tip-b", (cx + 3, cy - 4), (cx + 4, cy + 3), radius_x=TIP_R, sweep=True)
        self.add_arc("tip-c", (cx + 4, cy + 3), (cx, cy + TIP_R), radius_x=TIP_R, sweep=True)
        self.add_bezier("thumb-under", (cx, cy + TIP_R), ((19, 30), (18, 30.5), (16, 31)))
        self.add_contour("thumb", "thumb-top-a", "thumb-top-b", "tip-a", "tip-b", "tip-c", "thumb-under")
        self.relate("connect", "outline", "thumb")

        # Curled finger bottoms: thumb tip to the right wall.
        self.add_bezier("curl", (cx + 4, cy + 3), (CURL_C1, CURL_C2, (R, CURL_WALL_Y)))
        self.relate("connect", "thumb", "curl")
        self.relate("connect", "outline", "curl")

        # Knuckle divisions.
        self.add_line("div-1", (v1, vy), (v1, THUMB_Y))
        self.add_line("div-2", (v2, vy), (cx + 3, cy - 4))
        self.add_line("div-3", (v3, vy), (v3, 19))
        for d in ("div-1", "div-2", "div-3"):
            self.relate("connect", "outline", d)
        self.relate("connect", "thumb", "div-1")
        self.relate("connect", "thumb", "div-2")
