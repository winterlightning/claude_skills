"""hand-holding-snake (redraw of the new-pipeline traced SVG).

Subject: an open hand, palm up, with a snake rearing in an S above it.

Plan: SQUARE (centerline box (6,6)-(42,42)).
- snake body: one smooth run from the tail curl at the lower left through two
  stacked half-ellipse bowls (rx 6, ry 4.75, rows y=6 / 15.5 / 25, axis x=18),
  then a flat neck along the top edge y=6 into the head.
- snake head: a closed teardrop that leaves the neck junction J=(26,6), runs
  the top edge to (36.5,6), rounds a r5.5 cap whose apex is the right edge
  x=42, and tapers back from the bottom (y=17) into J at 45 degrees, so it
  reads as a head, not a letter loop. Its eye is 6.7 inscribed.
- hand: one open band of width 8 (the forearm), palm top y=34 and back y=42
  from the left edge x=6; the band bends up about a shared centre (27,28)
  (inner r6, outer r14) into a finger on a 3-4-5 slope, capped by a r4
  semicircle about (38,30) whose apex touches x=42.
Vertical budget: snake 6-25, gap 9, hand 34-42 (curved pairs get 9, not 8).

Keyshape: SQUARE, as suggested by the metrics (fill 1.0 on both axes).
Extremes: left x=6 hand ends, top y=6 snake neck/head, right x=42 head cap and
finger tip, bottom y=42 back of the hand.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap budgeted for it.
- clearance e0/e1 2.87 (error): the snake now clears the hand by 9 on
  centerlines (bowl bottom y=25 over palm y=34; head bottom 17 over the
  finger tip top 26).
- holes 1.84 / 0.8 / 1.4 (errors): the trace's hollow double-walled body made
  sliver holes; the body is now a single stroke (no enclosed area) and the
  only hole is the head's eye, 6 inscribed.
- no-head (warn): not applicable -- the only human part is a hand, there is no
  figure and no head to trace.
Lucide `hand-helping` / `hand-coins` informed the palm band and raised
fingers; the existing solo `coiled-snake` / `curving-snake` the single-stroke
body with a looped head.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "cc4af31b-ad07-4519-9e2a-a3b2ee7e8834"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1258-hand-holding-snake/hand-holding-snake_raw.svg"
AUTHOR = "claude-opus-5-5"

# Snake
AXIS = 18                        # shared x of both bowls
ROW_TOP, ROW_MID, ROW_BOT = 6, 15.5, 25
BOWL_RX = 6
J = (26, 6)                      # neck / head junction
HEAD_CX, HEAD_R = 36.5, 5.5      # cap centre x and radius (apex x = 42)
HEAD_BOT = ROW_TOP + 2 * HEAD_R  # 17
TAIL = (7, 19)
# Hand
PALM_TOP, PALM_BACK, LEFT = 34, 42, 6
BEND = (27, 28)                  # shared centre of the palm bend
R_IN, R_OUT = 6, 14              # band width 8
TIP, TIP_R = (38, 30), 4
K = 0.5523


def arc(c, r, a0, a1):
    """Cubic segments for a circular arc from angle a0 to a1 (radians, y down)."""
    n = max(1, math.ceil(abs(a1 - a0) / (math.pi / 2) - 1e-9))
    step = (a1 - a0) / n
    h = 4 / 3 * math.tan(step / 4) * r
    segs = []
    for i in range(n):
        s, e = a0 + i * step, a0 + (i + 1) * step
        p0 = (c[0] + r * math.cos(s), c[1] + r * math.sin(s))
        p3 = (c[0] + r * math.cos(e), c[1] + r * math.sin(e))
        c1 = (p0[0] - h * math.sin(s), p0[1] + h * math.cos(s))
        c2 = (p3[0] + h * math.sin(e), p3[1] - h * math.cos(e))
        segs.append((c1, c2, p3))
    return segs


def line(a, b):
    return ((a[0] + (b[0] - a[0]) / 3, a[1] + (b[1] - a[1]) / 3),
            (a[0] + 2 * (b[0] - a[0]) / 3, a[1] + 2 * (b[1] - a[1]) / 3), b)


class HandHoldingSnakeRedraw(Solo48):
    icon_id = "hand-holding-snake-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/reptile"
    aliases = ("snake in hand", "holding a snake", "snake handler")
    keywords = ("hand", "snake", "serpent", "reptile", "pet", "handler", "palm")

    def build(self) -> None:
        # Snake body: tail curl -> lower bowl (opens left) -> upper bowl (opens right) -> neck.
        ry = (ROW_MID - ROW_TOP) / 2
        kx, ky = BOWL_RX * K, ry * K
        bot, right = (AXIS, ROW_BOT), (AXIS + BOWL_RX, ROW_MID + ry)
        mid, left, top = (AXIS, ROW_MID), (AXIS - BOWL_RX, ROW_TOP + ry), (AXIS, ROW_TOP)
        self.add_bezier(
            "body", TAIL,
            ((7, 23), (11, ROW_BOT), (13, ROW_BOT)),
            ((15, ROW_BOT), (AXIS - kx + 1, ROW_BOT), bot),
            ((bot[0] + kx, bot[1]), (right[0], right[1] + ky), right),
            ((right[0], right[1] - ky), (mid[0] + kx, mid[1]), mid),
            ((mid[0] - kx, mid[1]), (left[0], left[1] + ky), left),
            ((left[0], left[1] - ky), (top[0] - kx, top[1]), top),
            line(top, J),
        )
        # Head: J -> top edge -> r5.5 cap (apex x=42) -> bottom -> back up into J.
        cap = (HEAD_CX, ROW_TOP + HEAD_R)
        hk = HEAD_R * K
        self.add_bezier(
            "head", J,
            line(J, (HEAD_CX, ROW_TOP)),
            *arc(cap, HEAD_R, -math.pi / 2, math.pi / 2),
            ((HEAD_CX - 5, HEAD_BOT), (J[0] + 4, ROW_TOP + 3), J),
        )
        self.add_contour("head-loop", "head", closed=True)
        self.relate("connect", "body", "head")

        # Hand: palm top -> inner bend -> finger -> r4 tip -> finger back -> outer bend -> back.
        fdir = math.atan2(-0.8, 0.6)           # finger direction, 3-4-5 slope
        n_ang = fdir - math.pi / 2             # normal pointing to the palm side
        in_end = (BEND[0] + R_IN * 0.8, BEND[1] + R_IN * 0.6)
        out_end = (BEND[0] + R_OUT * 0.8, BEND[1] + R_OUT * 0.6)
        tip_in = (TIP[0] + TIP_R * math.cos(n_ang), TIP[1] + TIP_R * math.sin(n_ang))
        tip_out = (TIP[0] - TIP_R * math.cos(n_ang), TIP[1] - TIP_R * math.sin(n_ang))
        a_in = math.atan2(0.6, 0.8)
        self.add_bezier(
            "hand", (LEFT, PALM_TOP),
            line((LEFT, PALM_TOP), (BEND[0], PALM_TOP)),
            *arc(BEND, R_IN, math.pi / 2, a_in),
            line(in_end, tip_in),
            *arc(TIP, TIP_R, n_ang, 0),
            *arc(TIP, TIP_R, 0, n_ang + math.pi),
            line(tip_out, out_end),
            *arc(BEND, R_OUT, a_in, math.pi / 2),
            line((BEND[0], PALM_BACK), (LEFT, PALM_BACK)),
        )
