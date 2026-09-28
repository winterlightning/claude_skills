"""arrow turn right (redraw of the new-pipeline traced SVG).

Plan: SQUARE (centerline box (6,6)-(42,42)), after Lucide `corner-up-right`
(a quarter-arc bend into a straight shaft ending in a 90-degree chevron head),
with the generated image's S-shaped tail kept below the bend.
- head: chevron (HEAD_BACK, 6) -> tip (42, SHAFT_Y) -> (HEAD_BACK, 26); the
  arms are 45 degrees and HEAD_ARM long on each axis, so the top arm end is
  the y=6 extreme and the tip is the x=42 extreme.
- body: one contour. Shaft along y=SHAFT_Y from the tip back to the bend;
  quarter arc radius BEND_R about (BEND_X, SHAFT_Y + BEND_R) whose left apex
  (6, 30) is the x=6 extreme; then one symmetric cubic S from that apex
  (leaving straight down, tangent to the arc) to the tail foot (14, 42),
  arriving straight down on the y=42 extreme.
Metric issues:
- keyshape-short-axis (x filled 87%): fixed; the bend apex now sits on x=6
  and the tip on x=42, so all four SQUARE extremes are exact.
- stroke-width (trace 2.4): redrawn at stroke 4 on the integer grid.
- clearance e0-e1 / e0-e2 (6.14 / 6.34 < 8): partly fixed. The arm ends now
  sit 10 units off the shaft (trace ~8.6), so the head opening between each
  arm tip and the shaft is 10 >= 8. Points on a 45-degree arm are only
  d/sqrt(2) from the shaft, so the metric's "beyond 8 units of the joint"
  probe cannot reach 8 on any arrowhead that shares its tip with the shaft;
  that residual is the connected wedge at the shared tip, not a gap between
  distinct parts, and the Solo48 validator certifies it.
The reference's diagonal lower tail was not used; the generated image's S
tail reads better at 48 px and keeps the foot inside the box.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "90bda1dc-4ea8-4d9e-aace-a5784e398b7c"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1637-arrow-turn-right/arrow-turn-right_raw.svg"
AUTHOR = "claude-opus-5-5"

TIP_X = 42
SHAFT_Y = 16
HEAD_ARM = 10
HEAD_BACK = TIP_X - HEAD_ARM
BEND_R = 14
BEND_X = 6 + BEND_R            # shaft meets the arc here
APEX = (6, SHAFT_Y + BEND_R)   # arc's left apex, the x=6 extreme
FOOT = (14, 42)
S_MID_Y = (APEX[1] + FOOT[1]) / 2


class ArrowTurnRightRedraw(Solo48):
    icon_id = "arrow-turn-right-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/arrows"
    aliases = ("turn right arrow", "curved arrow right")
    keywords = ("arrow", "turn", "right", "direction", "navigation", "redirect", "forward")

    def build(self) -> None:
        tip = (TIP_X, SHAFT_Y)
        self.add_polyline("head", (HEAD_BACK, SHAFT_Y - HEAD_ARM), tip,
                          (HEAD_BACK, SHAFT_Y + HEAD_ARM))

        self.add_line("shaft", tip, (BEND_X, SHAFT_Y))
        self.add_arc("bend", (BEND_X, SHAFT_Y), APEX, radius_x=BEND_R, sweep=False)
        self.add_bezier("tail", APEX,
                        ((APEX[0], S_MID_Y), (FOOT[0], S_MID_Y), FOOT))
        self.add_contour("body", "shaft", "bend", "tail")
        self.relate("connect", "head", "body")
