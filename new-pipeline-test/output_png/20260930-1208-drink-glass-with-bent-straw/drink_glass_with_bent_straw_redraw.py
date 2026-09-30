"""drink-glass-with-bent-straw: an open tapered drinking glass with a
single bent straw standing in it (redraw of the new-pipeline traced SVG).

Plan: VRECT_M (centerline box (10,4)-(38,44)), glass mirrored about x=24.
- glass: one open contour, no rim line. Walls taper 1:8 from the rim
  points (10,14) / (38,14) down to (13,38) / (35,38); a cubic corner
  (controls continue the wall direction, then run level) turns each wall
  tangent-continuously into the flat base y=44 between (18,44) and (30,44).
  The rim points are the x extremes and land exactly on x=10/38; the base
  is the bottom extreme y=44.
- straw: one open contour on the axis x=24: a vertical tube from (24,35)
  up to (24,12), a cubic bend (tangent vertical at the start, 2:1 slope at
  the end) to (28,7), then a 2:1 diagonal out to (34,4), which is the top
  extreme y=4. The straw's foot stays 9 above the straight base (the
  glass contour holds curves, so an exact 8 comes back review) and >= 11
  from both walls; its tip is 10.8 from the right rim point.

Keyshape: VRECT_M as suggested; straw tip y=4, base y=44, rim points
x=10/38. Nothing stretched.

Metric issues fixed by the rebuild:
- clearance e0/e1 (4.03, straw foot resting on the glass base): the straw
  now ends at y=35, 9 on centerlines above the base (5 ink).
- keyshape-short-axis (x fill 67%): the glass is widened so its rim
  points reach both x extremes exactly, instead of stretching the trace.
- stroke-width (2.66): drawn at the profile stroke 4, gaps budgeted for it.
Nothing left unfixed.
Lucide: `cup-soda` (tapered cup, straw rising and bending off-axis)
informed the construction; the rim/lid band is dropped as in the source.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b59d74df-f296-42de-9d2c-6b949b2542d4"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1208-drink-glass-with-bent-straw/drink-glass-with-bent-straw_raw.svg"
AUTHOR = "claude-opus-5-5"

CX = 24                 # glass symmetry axis, also the straw tube
RIM = (38, 14)          # right rim point (mirror 10,14)
WALL_LOW = (35, 38)     # end of the straight 1:8 wall (mirror 13,38)
BASE = (30, 44)         # right end of the flat base (mirror 18,44)
STRAW_FOOT = (CX, 35)   # 9 above the base line
BEND_START = (CX, 12)
BEND_END = (28, 7)
STRAW_TIP = (34, 4)     # 2:1 diagonal from BEND_END


def mirror(p):
    return (2 * CX - p[0], p[1])


class DrinkGlassWithBentStrawRedraw(Solo48):
    icon_id = "drink-glass-with-bent-straw-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ("glass with straw", "soft drink", "tumbler with straw")
    keywords = ("drink", "glass", "straw", "beverage", "juice", "soda", "cup")

    def build(self) -> None:
        # Glass, drawn left rim -> base -> right rim.
        self.add_line("wall-left", mirror(RIM), mirror(WALL_LOW))
        self.add_bezier(
            "corner-left", mirror(WALL_LOW),
            ((13.5, 42), (15, 44), mirror(BASE)),
        )
        self.add_line("base", mirror(BASE), BASE)
        self.add_bezier(
            "corner-right", BASE,
            ((33, 44), (34.5, 42), WALL_LOW),
        )
        self.add_line("wall-right", WALL_LOW, RIM)
        self.add_contour(
            "glass", "wall-left", "corner-left", "base", "corner-right", "wall-right",
        )

        # Straw, drawn foot -> bend -> tip.
        self.add_line("straw-tube", STRAW_FOOT, BEND_START)
        self.add_bezier("straw-bend", BEND_START, ((24, 10), (26, 8), BEND_END))
        self.add_line("straw-top", BEND_END, STRAW_TIP)
        self.add_contour("straw", "straw-tube", "straw-bend", "straw-top")
