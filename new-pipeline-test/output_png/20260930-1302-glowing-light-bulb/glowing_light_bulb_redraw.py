"""glowing-light-bulb (redraw of the new-pipeline traced SVG).

Plan: one closed bulb, one detached base line and three glow rays on VRECT_M
(centerline box (10,4)-(38,44)), mirrored about x=24.
- bulb: a semicircular r10 dome about (24,25) (x 14..34, top y=15), each
  equator end flowing tangent-continuously (vertical tangents at both ends)
  through a cubic S-shoulder into the neck at x=19 / x=29, y=34; r2 corners
  close it on a flat bottom y=36 from x=21 to 27.
- base: one level line y=44, x 19..29 (as wide as the neck), 8 below the
  bulb bottom -- the screw base.
- rays: a vertical top ray (24,4)-(24,7), 8 above the dome apex, and two
  45 deg rays (10,7)-(13,10) / (38,7)-(35,10), whose inner ends are 18.6 from
  the dome centre (8.6 clear of the dome) and 11.4 from the top ray.
Extremes: x 10/38 (diagonal ray tips), y 4 (top ray), y 44 (base line).

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap budgeted for it.
- keyshape-short-axis (y filled 95%): the top ray tip sits on y=4 and the
  base line on y=44, so all four extremes are on the VRECT_M box.
- clearance e0/e3 (top ray 3.6 above the bulb): now 8.
- clearance e1/e3, e2/e3 (diagonal rays 4.7 from the bulb): now 8.6; the rays
  moved up and out to the box corners instead of aiming at the dome.
- clearance e3/e4 (base line 3.5 below the bulb): now 8.
Not fixed / changed on purpose:
- the bulb is smaller relative to the rays than in the image: the 40-unit
  height must hold ray + 8 + bulb + 8 + base, which leaves the bulb 21 tall.
Lucide: `lightbulb` (round dome narrowing through S-shoulders into a neck,
level base lines below) informed the bulb; rays follow Lucide `sun` short
strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "564c9b27-dd9b-48b8-8f61-3945889b688c"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1302-glowing-light-bulb/glowing-light-bulb_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
DOME_Y, DOME_R = 25, 10              # dome centre y and radius (apex y=15)
NECK = 5                             # neck half-width (walls x=19 / 29)
NECK_Y, BOTTOM, CR = 34, 36, 2       # neck corner start, flat bottom, corner radius
BASE_Y = 44                          # screw base line
RAY_TOP, RAY_LEN = 4, 3              # top ray
DIAG = ((10, 7), (13, 10))           # left diagonal ray; the right one mirrors it


def mirror(p):
    return (2 * AXIS - p[0], p[1])


class GlowingLightBulbRedraw(Solo48):
    icon_id = "glowing-light-bulb-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("light bulb on", "idea bulb", "bright idea")
    keywords = ("light bulb", "lightbulb", "glow", "idea", "light", "lamp",
                "bright", "inspiration", "rays")

    def build(self) -> None:
        left, right = AXIS - DOME_R, AXIS + DOME_R          # 14, 34
        nl, nr = AXIS - NECK, AXIS + NECK                   # 19, 29
        mid = (DOME_Y + NECK_Y) / 2

        # Bulb, clockwise from the left equator over the dome.
        self.add_arc("dome", (left, DOME_Y), (right, DOME_Y), radius_x=DOME_R)
        self.add_bezier("shoulder-r", (right, DOME_Y),
                        ((right, mid), (nr, mid + 0.5), (nr, NECK_Y)))
        self.add_arc("corner-r", (nr, NECK_Y), (nr - CR, BOTTOM), radius_x=CR)
        self.add_line("bottom", (nr - CR, BOTTOM), (nl + CR, BOTTOM))
        self.add_arc("corner-l", (nl + CR, BOTTOM), (nl, NECK_Y), radius_x=CR)
        self.add_bezier("shoulder-l", (nl, NECK_Y),
                        ((nl, mid + 0.5), (left, mid), (left, DOME_Y)))
        self.add_contour("bulb", "dome", "shoulder-r", "corner-r", "bottom",
                         "corner-l", "shoulder-l", closed=True)

        # Screw base.
        self.add_line("base", (nl, BASE_Y), (nr, BASE_Y))

        # Glow rays.
        self.add_line("ray-top", (AXIS, RAY_TOP), (AXIS, RAY_TOP + RAY_LEN))
        self.add_line("ray-l", *DIAG)
        self.add_line("ray-r", *map(mirror, DIAG))
