"""arrow turn right (redraw of the new-pipeline traced SVG).

Plan: SQUARE (centerline box (6,6)-(42,42)), after Lucide `corner-up-right`
(stem, radius-4 quarter bend, straight shaft, 90-degree chevron head), which
is exactly the generated image's construction; Lucide's radius 4 on the 24
grid becomes BEND_R = 8 here.
- body: one contour. Stem up x=STEM_X from the foot (6, 42) (the x=6 and
  y=42 extremes) to (6, SHAFT_Y + BEND_R); quarter arc radius BEND_R about
  (STEM_X + BEND_R, SHAFT_Y + BEND_R), tangent to both lines; shaft along
  y=SHAFT_Y to the tip (42, SHAFT_Y), the x=42 extreme.
- head: chevron (HEAD_BACK, 6) -> tip -> (HEAD_BACK, SHAFT_Y + HEAD_ARM);
  45-degree arms HEAD_ARM long per axis, so the top arm end is the y=6
  extreme. It shares the tip with the shaft (declared connect).
Metric issues:
- stroke-width (trace 2.4): redrawn at stroke 4 on the integer grid.
- keyshape-short-axis (x filled 87%): fixed; stem on x=6, tip on x=42, top
  arm end on y=6, foot on y=42, so all four SQUARE extremes are exact.
- clearance e0-e2 / e1-e2 (6.09 / 6.0 < 8): partly fixed. The arm ends now
  sit HEAD_ARM = 10 units off the shaft (trace ~10), so the head openings are
  10 >= 8. A point on a 45-degree arm at distance d from the shared tip is
  only d/sqrt(2) from the shaft, so the metric's "beyond 8 units of the
  joint" probe reads ~5.7 on every chevron that shares its tip with the
  shaft; that is the connected wedge at the tip, not a gap between distinct
  parts, and the Solo48 validator certifies the shared-endpoint join.
- the trace's 20-degree kink where the stem met the elliptical bend is gone:
  the bend is a true circular quarter arc tangent to stem and shaft.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "90bda1dc-4ea8-4d9e-aace-a5784e398b7c"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1651-arrow-turn-right/arrow-turn-right_raw.svg"
AUTHOR = "claude-opus-5-5"

STEM_X = 6
FOOT_Y = 42
TIP_X = 42
HEAD_ARM = 10
SHAFT_Y = 6 + HEAD_ARM
HEAD_BACK = TIP_X - HEAD_ARM
BEND_R = 8


class ArrowTurnRightRedraw(Solo48):
    icon_id = "arrow-turn-right-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/arrows"
    aliases = ("turn right arrow", "corner up right arrow")
    keywords = ("arrow", "turn", "right", "direction", "navigation", "redirect", "forward")

    def build(self) -> None:
        tip = (TIP_X, SHAFT_Y)
        bend_start = (STEM_X, SHAFT_Y + BEND_R)
        bend_end = (STEM_X + BEND_R, SHAFT_Y)

        self.add_line("stem", (STEM_X, FOOT_Y), bend_start)
        self.add_arc("bend", bend_start, bend_end, radius_x=BEND_R, sweep=True)
        self.add_line("shaft", bend_end, tip)
        self.add_contour("body", "stem", "bend", "shaft")

        self.add_polyline("head", (HEAD_BACK, SHAFT_Y - HEAD_ARM), tip,
                          (HEAD_BACK, SHAFT_Y + HEAD_ARM))
        self.relate("connect", "head", "body")
