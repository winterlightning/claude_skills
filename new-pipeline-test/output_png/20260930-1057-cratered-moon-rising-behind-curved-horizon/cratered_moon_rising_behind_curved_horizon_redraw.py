"""cratered-moon-rising-behind-curved-horizon (redraw of the new-pipeline traced SVG).

Plan: a moon rising over a gently arched horizon, on HRECT_L (centerline box
(4,8)-(44,40)). The metrics suggested HRECT_M, but its 28-unit height cannot
hold a moon with an off-centre crater plus an 8-unit gap to the horizon, so
the taller HRECT_L (the second candidate, also "wide") is used.
- moon: one upper half-circle r16 about (24,24). The apex is the top edge
  y=8; the open ends (8,24) / (40,24) stop 11 above the horizon (centerlines).
- craters: a large hollow crater (full circle r3 about (21,21), up and left
  of centre, as in the reference) and a small crater dot at (31,26), low
  right. Both stay 8+ clear of the moon, the horizon and each other.
- horizon: one arc r40 from (4,40) to (44,40), mirrored about x=24 and sagging
  about 5 at the middle. Its ends are the left, right and bottom edges.
Extremes: x 4 / 44 (horizon ends), y 8 (moon apex) / 40 (horizon ends).

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted for it.
- keyshape-short-axis (warn): fixed by moving to HRECT_L and designing to its
  box (moon apex y=8, horizon ends y=40) instead of stretching the trace.
- clearance e0/e1, e0/e2, e0/e3, e1/e2, e2/e3 (errors): fixed; every pair of
  parts is 8 or more apart on centerlines.
- hole at (18.9, 20.0) (error): not fixed to the 6-wide rule. That hole is the
  large crater. A ring with a 6-wide ink hole needs r5 (14 across in ink).
  With the 8-unit gap to the rim and the horizon, an r5 crater fits only near
  the centre of the r16-r18 moon the box allows. That drawing read as an eye,
  so it was rejected. Two such craters cannot fit at all. The crater is a
  diameter-6 circle instead: validate_icon passes and the build gate exempts
  circles of that size, but the pipeline hole metric still flags its 2-wide
  ink hole. The second crater became a dot so that no second small hole is
  added.
No Lucide moonrise or cratered moon exists. The horizon follows the one-arc
ground line of Lucide `sunrise`/`sunset`, and the half-circle over a line
follows the sun in `sunrise`.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3f691cb5-2291-494c-bb9b-480b4d6be086"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1057-cratered-moon-rising-behind-curved-horizon/cratered-moon-rising-behind-curved-horizon_raw.svg"
AUTHOR = "claude-opus-5-5"

MOON = (24, 24)            # moon centre; the upper half-circle rises above the horizon
MOON_R = 16                # apex y=8 = top edge of the box, ends (8,24) / (40,24)
CRATER = (21, 21)          # large crater, up and left of centre: 8.8 inside the rim
CRATER_R = 3               # diameter-6 circle
SMALL_CRATER = (31, 26)    # crater dot, low right: 8.7 inside the rim, 11.2 from the crater
HORIZON_Y = 40             # horizon ends (4,40) / (44,40) = bottom and side edges of the box
HORIZON_R = 40             # apex about y=34.6, about 9 below the dot


class CrateredMoonRisingBehindCurvedHorizonRedraw(Solo48):
    icon_id = "cratered-moon-rising-behind-curved-horizon-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/weather"
    aliases = ("moonrise", "rising moon", "moon over horizon")
    keywords = ("moon", "moonrise", "crater", "horizon", "night", "astronomy", "lunar", "rising")

    def build(self) -> None:
        mx, my = MOON
        self.add_arc("moon", (mx + MOON_R, my), (mx - MOON_R, my), radius_x=MOON_R, sweep=False)

        cx, cy = CRATER
        top, bottom = (cx, cy - CRATER_R), (cx, cy + CRATER_R)
        self.add_arc("crater-left", top, bottom, radius_x=CRATER_R, sweep=False)
        self.add_arc("crater-right", bottom, top, radius_x=CRATER_R, sweep=False)
        self.add_contour("crater", "crater-left", "crater-right", closed=True)
        self.add_dot("small-crater", SMALL_CRATER)

        self.add_arc("horizon", (44, HORIZON_Y), (4, HORIZON_Y), radius_x=HORIZON_R, sweep=False)
