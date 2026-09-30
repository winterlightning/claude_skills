"""clock-with-clockwise-return-arrow (redraw of the new-pipeline traced SVG).

Plan: a clock face whose rim is a clockwise return arrow, on CIRCLE (every
centerline point within radius 20 of (24,24), touching it at the rim's left
apex). The arrowhead sits outside the rim on the right, so the clock centre
moves 3 left of the canvas centre to keep the chevron inside the envelope.
- rim: one open contour of three r17 arcs on centre (21,24), clockwise from
  the lower-right end (36,32) (a 8-15-17 point) through the left apex (4,24)
  and the top apex (21,7) to the tip (38,24) at 3 o'clock, where the tangent
  points straight down.
- arrowhead: a 90-degree chevron (34,20)-(38,24)-(42,20) sharing the rim tip,
  arms 4 long so the outer arm stays inside radius 20 (it reaches 18.4).
- hands: one polyline, 12 o'clock hand (21,24)-(21,16) and 3 o'clock hand
  (21,24)-(27,24), joined at the clock centre.
Lucide construction: rotate-cw / history (open circle arc ending in a
chevron whose apex is the arc end, tangent-vertical at the tip); the in-set
counterclockwise-refresh-arrow uses the same chevron-on-apex join.

Metric issues (clock-with-clockwise-return-arrow_metrics.json):
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- clearance e0/e2 (arrowhead 6.26 from the 3 o'clock hand): the hand now
  ends at (27,24), 8.06 from the inner chevron arm end (34,20) and 11 from
  the tip.
- clearance e1/e2 (12 o'clock hand 7.3 below the rim): the hand now stops
  at y 16, 9 below the rim top (y 7), the margin a curve needs to certify.
- junction e1/e0 (0.08 near miss): the chevron and rim share the exact
  endpoint (38,24) and the contact is declared.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4ae0f802-0947-49ab-948b-a13314a05022"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1928-clock-with-clockwise-return-arrow/clock-with-clockwise-return-arrow_raw.svg"
AUTHOR = "claude-opus-5-5"

CX, CY, R = 21, 24, 17          # clock centre and rim radius
END = (CX + 15, CY + 8)         # rim start, 8-15-17 point below 3 o'clock
TIP = (CX + R, CY)              # rim end = arrow tip at 3 o'clock
ARM = 4                         # chevron arm run and rise
HOUR_TOP = CY - 8               # 12 o'clock hand end, 9 below the rim
MINUTE_END = CX + 6             # 3 o'clock hand end


class ClockWithClockwiseReturnArrowRedraw(Solo48):
    icon_id = "clock-with-clockwise-return-arrow-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "time/clock"
    aliases = ("clock redo", "time forward", "clockwise history")
    keywords = ("clock", "time", "clockwise", "arrow", "redo", "refresh", "rotate", "forward", "history")

    def build(self) -> None:
        left, top = (CX - R, CY), (CX, CY - R)
        self.add_arc("rim-low", END, left, radius_x=R, sweep=True)
        self.add_arc("rim-high", left, top, radius_x=R, sweep=True)
        self.add_arc("rim-turn", top, TIP, radius_x=R, sweep=True)
        self.add_contour("rim", "rim-low", "rim-high", "rim-turn")

        tx, ty = TIP
        self.add_polyline("head", (tx - ARM, ty - ARM), TIP, (tx + ARM, ty - ARM))
        self.relate("connect", "rim", "head")

        self.add_polyline("hands", (CX, HOUR_TOP), (CX, CY), (MINUTE_END, CY))
