"""high-temperature-thermometer (redraw of the new-pipeline traced SVG).

Plan: VRECT_L, centerline box (8,4)-(40,44); an upright glass thermometer
(Lucide `thermometer` read) with a tall mercury column and two scale ticks.
- glass: one closed contour mirrored about the axis x=19. A semicircular
  cap r9 about (19,13) (apex = keyshape top 4), straight walls x=10 / x=28
  down to y=26, cubic shoulders that continue the bulb circle up to the wall
  ends (a deliberate corner there, as in Lucide and the generated image), and
  a bulb semicircle r11 about (19,33) (apex = bottom 44, left side = 8).
- mercury: one straight line on the axis from just under the cap (y=14) to
  the bulb centre (y=33); its height carries "high temperature".
- ticks: two horizontal marks x=37..40 at y=10 and y=18, right of the upper
  tube; their right ends are the keyshape right extreme 40.
Extremes: left 8 (bulb), right 40 (ticks), top 4 (cap), bottom 44 (bulb).
Metric issues fixed:
- clearance e0/e1 (mercury 2.98 from the tube): the tube is 18 wide on
  centerlines, the axis mercury sits 9 from each wall (an exact 8 to the
  curve-owning glass contour came back as a review warning).
- clearance e0/e2, e0/e3 (ticks 1.97 from the tube): ticks start at x=37,
  9 from the wall x=28 and 9.25 from the cap arc.
- clearance e1/e2, e1/e3 (ticks 4.9 from the mercury): now 18 apart.
- clearance e2/e3 (ticks 4.62 apart): ticks are 8 apart (y=10, y=18).
- hole (bulb interior 3.6 inscribed): the bulb is r11, its open interior is
  far above 6 inscribed; the mercury ends 11 inside the bulb wall.
- keyshape-short-axis (x filled 47%): the tube is widened to 18, the bulb to
  22 and the ticks reach the right edge, so all four extremes lie on the box.
  VRECT_L is used instead of the suggested VRECT_M (second candidate, 0.66 vs
  0.72): on VRECT_M (28 wide) the bulb plus the 9+9 tube clearance leaves no
  room for the ticks at all.
- stroke-width (2.4 traced): authored at stroke 4 with every gap budgeted at
  8+ on centerlines.
Not fully recovered: the image's bulb is ~1.7x the tube width; the 32-wide
box with 9 clearance inside the tube and beside the ticks allows only 22/18,
so the shoulder corner, not the width, separates bulb from tube; the ticks
are short (3 on centerlines).
Lucide: `thermometer` (straight tube, round cap, bulb joined at a corner).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1fa52957-1342-499f-9403-f3293476b96f"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1515-high-temperature-thermometer/"
    "high-temperature-thermometer_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AX = 19                       # shared vertical axis
HALF = 9                      # tube half-width; 9, not 8: an exact 8 to the
                              # curve-owning glass contour comes back as review
CAP_Y = 13                    # cap centre; apex at CAP_Y - HALF = 4
BULB_Y, BULB_R = 33, 11       # bulb centre; apex 44, sides 8 / 30
SHOULDER_Y = 26               # wall end = shoulder corner (~on the r11 bulb)
# Cubic arc handles for the shoulders: 4/3*tan(35deg/4)*r11 along the
# circle tangents at the bulb side (vertical) and at the wall end.
K1, K2X, K2Y = 2.26, 1.29, 1.85
MERCURY_TOP = CAP_Y + 1
TICK_X0, TICK_X1 = AX + HALF + 9, 40
TICK_YS = (10, 18)


class HighTemperatureThermometerRedraw(Solo48):
    icon_id = "high-temperature-thermometer-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ("hot thermometer", "high temperature", "heat")
    keywords = ("thermometer", "temperature", "high", "hot", "heat", "weather", "fever")

    def build(self) -> None:
        left, right = AX - HALF, AX + HALF
        bl, br = AX - BULB_R, AX + BULB_R
        # -- glass: cap, walls, shoulders, bulb (mirrored about AX) ----------
        self.add_line("wall-l", (left, SHOULDER_Y), (left, CAP_Y))
        self.add_arc("cap", (left, CAP_Y), (right, CAP_Y), radius_x=HALF)
        self.add_line("wall-r", (right, CAP_Y), (right, SHOULDER_Y))
        # Shoulders: the bulb circle continued up to the wall ends, a cubic
        # arc of ~35 degrees (the wall ends are not integer points on r11),
        # meeting the straight wall at a deliberate Lucide-style corner.
        self.add_bezier("shoulder-r", (right, SHOULDER_Y),
                        ((right + K2X, SHOULDER_Y + K2Y), (br, BULB_Y - K1), (br, BULB_Y)))
        self.add_arc("bulb", (br, BULB_Y), (bl, BULB_Y), radius_x=BULB_R)
        self.add_bezier("shoulder-l", (bl, BULB_Y),
                        ((bl, BULB_Y - K1), (left - K2X, SHOULDER_Y + K2Y), (left, SHOULDER_Y)))
        self.add_contour("glass", "wall-l", "cap", "wall-r", "shoulder-r",
                         "bulb", "shoulder-l", closed=True)

        # -- mercury column: from under the cap to the bulb centre ------------
        self.add_line("mercury", (AX, MERCURY_TOP), (AX, BULB_Y))

        # -- scale ticks --------------------------------------------------------
        for j, y in enumerate(TICK_YS):
            self.add_line(f"tick-{j}", (TICK_X0, y), (TICK_X1, y))
