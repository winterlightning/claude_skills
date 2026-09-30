"""hand-drill-fire-log (redraw of the new-pipeline traced SVG).

Subject: a friction hand-drill spindle standing on a log, with a flame
rising beside it.

Plan: SQUARE (centerline box (6,6)-(42,42)), the metrics' suggestion
(score 1.12; HRECT_L 0.92). Extremes: log ends x=6/42, spindle top y=6,
flame tip y=6, log bottom y=42.
- log: closed cylinder outline y=30..42, half-ellipse ends (rx=5, ry=6)
  reaching x=6 and x=42; the top edge is split at the spindle foot.
  A second half-ellipse from the right end's top/bottom points, bulging
  left, closes the cut face (eye 10x12 on centerlines).
- spindle: vertical line x=16 from y=6 down to the log top (T-joint,
  declared connect).
- flame: one closed cubic run: main tip (30,6) leaning left, a V notch at
  (36,12), a right lick tip (40,8), then a round bowl (r=7 about (33,15))
  down to y=22. Tangents are vertical at the bowl extremes so the bowl is
  smooth; the tips and the notch are deliberate corners.
Clearances: flame-to-spindle 10 (x 26 vs 16), flame-to-log 8 (y 22 vs 30).

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4 and every gap budgeted for it.
- keyshape-short-axis (warn): y now spans 6..42, so all four extremes sit on
  the SQUARE box (the trace filled 87% on y).
- clearance e0/e3 6.55, e1/e3 5.49, e2/e3 4.08 (errors): the flame was moved
  up and right. It is now 10 from the spindle and 8 from the log top on
  centerlines (the cut face is 14 away).
- hole 4.53 at the flame (error): the flame bowl is r=7 (ink eye 10 wide),
  and the notch stays shallow so the eye keeps its inscribed width.
- hole 4.6 at the log (error): the log body is 12 tall on centerlines
  (8 ink), no longer pinched by the thin trace.
- hole 1.4 at the right end (error): the cut face is a real half-ellipse
  pair, 10 wide on centerlines, instead of a sliver.
No issue left unfixed. build_gate.py: PASS, 0 errors, 0 warnings.
Lucide `flame` informed the bowl-plus-lick flame and `cylinder` the
half-ellipse ends. The flame is deliberately asymmetric, like the source.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e94edbaf-c94d-4cdc-a976-817dfd2498ef"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1300-hand-drill-fire-log/hand-drill-fire-log_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT, RIGHT, BOTTOM = 6, 42, 42
LOG_T = 30
END_RX, END_RY = 5, 6
SPINDLE_X, SPINDLE_TOP = 16, 6

# Flame bowl: circle-ish of radius FR about (FX, FY).
FX, FY, FR = 33, 15, 7
TIP = (30, 6)          # main tip
NOTCH = (36, 12)       # between main tip and right lick
LICK = (40, 8)         # right lick tip
K = 0.5523


class HandDrillFireLogRedraw(Solo48):
    icon_id = "hand-drill-fire-log-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tool"
    aliases = ("hand drill fire", "friction fire", "fire drill")
    keywords = ("fire", "flame", "log", "wood", "drill", "spindle", "survival", "camping", "bushcraft")

    def build(self) -> None:
        lx, rx = LEFT + END_RX, RIGHT - END_RX
        # Log outline: top (split at spindle), right end, bottom, left end.
        self.add_line("log-top-l", (lx, LOG_T), (SPINDLE_X, LOG_T))
        self.add_line("log-top-r", (SPINDLE_X, LOG_T), (rx, LOG_T))
        self.add_arc("log-end-r", (rx, LOG_T), (rx, BOTTOM), radius_x=END_RX, radius_y=END_RY, sweep=True)
        self.add_line("log-bottom", (rx, BOTTOM), (lx, BOTTOM))
        self.add_arc("log-end-l", (lx, BOTTOM), (lx, LOG_T), radius_x=END_RX, radius_y=END_RY, sweep=True)
        self.add_contour("log", "log-top-l", "log-top-r", "log-end-r", "log-bottom", "log-end-l", closed=True)
        # Cut face: inner half-ellipse bulging left.
        self.add_arc("log-cut", (rx, LOG_T), (rx, BOTTOM), radius_x=END_RX, radius_y=END_RY, sweep=False)
        self.relate("connect", "log-cut", "log")

        self.add_line("spindle", (SPINDLE_X, SPINDLE_TOP), (SPINDLE_X, LOG_T))
        self.relate("connect", "spindle", "log")

        # Flame: tip -> notch -> lick -> right -> bottom -> left -> tip.
        c = K * FR
        right, bottom, left = (FX + FR, FY), (FX, FY + FR), (FX - FR, FY)
        self.add_bezier(
            "flame", TIP,
            ((32.5, 7.5), (35, 9.5), NOTCH),
            ((37, 11), (39.5, 9.5), LICK),
            ((40, 10), (FX + FR, 12.5), right),
            ((FX + FR, FY + c), (FX + c, FY + FR), bottom),
            ((FX - c, FY + FR), (FX - FR, FY + c), left),
            ((FX - FR, 11), (27.5, 8.5), TIP),
        )
        self.add_contour("flame-outline", "flame", closed=True)
