"""arrow turning left with dashed tail (redraw of the new-pipeline traced SVG).

Plan: a turn-left arrow on VRECT_L (centerline box (8,4)-(40,44)), built like
Lucide `corner-up-left` (open 45-degree chevron on a horizontal shaft that
rounds a quarter arc into a vertical riser), with the riser broken into a
solid run and two short dashes below it.
- head: open chevron, tip on the x=8 extreme at (8, SHAFT_Y); its upper arm
  ends on the y=4 extreme. HEAD = 8 so each arm end sits 8 from the shaft.
- body: one contour upper arm -> tip -> shaft -> arc (radius R, centre on the
  grid) -> solid riser on the x=40 extreme; the lower arm is a separate line
  sharing the tip endpoint, declared with relate("connect").
- tail: two equal dashes of DASH on x=40, separated from the riser and from
  each other by GAP = 9 on centerlines; the last one ends on the y=44 extreme.
  GAP is 9, not 8: the riser shares a contour with the corner arc, and the
  engine cannot certify a curved contour sitting exactly on the 8 minimum
  (it came back `review`); both gaps use 9 so the dash rhythm stays even.
Keyshape: the metrics suggested SQUARE, but the trace only fills 73% of its x
axis (stretch 1.36); VRECT_L needs only a 1.09 stretch and its 40-unit height
is what the riser + two dashes need at an 8-unit gap, so VRECT_L is used.

Metric issues fixed:
- clearance e0/e1 and e0/e2 (chevron arms 5.9-6.0 from the shaft): arms are
  now 8 long on each axis, so their free ends sit exactly 8 from the shaft.
- clearance e0/e4 (riser 3.9 from first dash) and e4/e5 (dashes 4.1 apart):
  gaps are now 9 on centerlines (5 of ink).
- keyshape-short-axis: every extreme sits on the VRECT_L box.
- stroke-width: redrawn at stroke 4 with the gaps budgeted for it.
- loose-join e0/e1/e2 vs e3: e3 was a zero-length trace artefact at the tip;
  dropped, and the arms share the exact tip endpoint with the shaft.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0e26bfd0-c84a-5afd-af45-9efcb51b9f95"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1818-arrow-turning-left-with-dashed-tail/arrow-turning-left-with-dashed-tail_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT, TOP, RIGHT, BOTTOM = 8, 4, 40, 44
HEAD = 8                      # chevron arm run on each axis
SHAFT_Y = TOP + HEAD          # 12
TIP = (LEFT, SHAFT_Y)
R = 6                         # corner radius, centre (RIGHT - R, SHAFT_Y + R)
GAP = 9                       # centerline gap between riser and dashes (8 + 1: see below)
DASH = 2
DASH2 = (BOTTOM - DASH, BOTTOM)
DASH1 = (DASH2[0] - GAP - DASH, DASH2[0] - GAP)
RISER_END = DASH1[0] - GAP    # 22


class ArrowTurningLeftWithDashedTailRedraw(Solo48):
    icon_id = "arrow-turning-left-with-dashed-tail-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol/arrow"
    aliases = ("turn left arrow", "corner up left dashed")
    keywords = ("arrow", "turn", "left", "dashed", "route", "corner", "direction")

    def build(self) -> None:
        self.add_line("arm-top", (LEFT + HEAD, TOP), TIP)
        self.add_line("shaft", TIP, (RIGHT - R, SHAFT_Y))
        self.add_arc("corner", (RIGHT - R, SHAFT_Y), (RIGHT, SHAFT_Y + R), radius_x=R)
        self.add_line("riser", (RIGHT, SHAFT_Y + R), (RIGHT, RISER_END))
        self.add_contour("body", "arm-top", "shaft", "corner", "riser")
        self.add_line("arm-bottom", TIP, (LEFT + HEAD, SHAFT_Y + HEAD))
        self.relate("connect", "arm-bottom", "body")

        self.add_line("dash-1", (RIGHT, DASH1[0]), (RIGHT, DASH1[1]))
        self.add_line("dash-2", (RIGHT, DASH2[0]), (RIGHT, DASH2[1]))
