"""airplane-taking-off (redraw of the new-pipeline traced PNG).

Plan: a side-view airliner climbing up-right over a level runway, on
HRECT_M (centerline box (4,10)-(44,38)). Extremes: the fin tip owns x=4, the
nose arc owns x=44, the wing tip and nose top own y=10, the runway owns y=38.
- fuselage: one closed contour. Top edge and belly are parallel 1:2 climbs
  10 apart vertically (8.94 on centerlines). The top edge levels out into an
  r4 nose arc about (40,14); a cubic chin turns back into the belly. The
  belly rounds into the lowest point TAIL_LOW (11,30), exactly 8 above the
  runway.
- fin: a pointed lobe of the same contour. The trailing edge rises from
  TAIL_LOW to the tip (4,16); the leading edge drops to the notch (14,22) on
  the top edge, 8 from TAIL_LOW, so the tail never pinches the tube.
- wing: an open swept triangle (32,13)-(16,10)-(20,19) standing on the top
  edge, connected to the fuselage at both roots; its closed hole has
  centerline inradius 3.34.
- runway: one level line (6,38)-(42,38), inset like the generated image.
Tried a more swept wing (tip at (14,10)); its trailing edge came within
2.9 ink of the fin leading edge (internal-spacing review), so it was dropped.
Lucide `plane-takeoff` informed the climbing side view over a runway line.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4 and every gap re-budgeted for it.
- keyshape-short-axis (warn, y filled 66%): the wing tip and nose top reach
  y=10 and the runway sits on y=38, so HRECT_M fits exactly without
  stretching the plane.
- clearance e1/e2 (5.29 apart, need 8): the tail's lowest point is now
  exactly 8 above the runway on centerlines.
- holes 0.82 / 1.71 / 1.0 / 0.57 wide (need 6): the traced T-junction
  pockets (wing trailing edge crossing into the fuselage, the leading-edge
  stub, the thin fin pocket) are gone. The only holes left are the fuselage
  interior (8.94 tube) and the wing triangle (inradius 3.34).
All metric issues were repaired. validate_icon() is valid and build_gate.py
passes with 0 errors and 0 warnings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "39a4161c-ed3c-5509-8f55-7f29d7d27ec9"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1737-airplane-taking-off/airplane-taking-off_raw.svg"
AUTHOR = "claude-opus-5-5"

# Fuselage sides are parallel 1:2 climbs, 10 apart vertically (8.94 on centerlines):
# top edge y = 29 - x/2, belly y = 39 - x/2.
TOP0 = (14, 22)        # fin notch: top edge meets the fin leading edge
WING_TRAIL = (20, 19)  # wing roots on the top edge
WING_LEAD = (32, 13)
WING_TIP = (16, 10)
NOSE_TOP = (40, 10)    # top edge levels out here; r4 nose arc about (40,14)
NOSE_FRONT = (44, 14)
BELLY_FRONT = (36, 21)
BELLY_REAR = (22, 28)
TAIL_LOW = (11, 30)    # lowest point of the aircraft, 8 above the runway
FIN_TIP = (4, 16)
RUNWAY_Y = 38
RUNWAY = ((6, RUNWAY_Y), (42, RUNWAY_Y))


class AirplaneTakingOffRedraw(Solo48):
    icon_id = "airplane-taking-off-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/aircraft"
    aliases = ("plane taking off", "departure", "flight departure", "takeoff")
    keywords = ("airplane", "plane", "take off", "departure", "airport", "flight", "travel", "runway")

    def build(self) -> None:
        # Fuselage outline, clockwise from the fin notch.
        self.add_line("top-rear", TOP0, WING_TRAIL)
        self.add_line("top-wing", WING_TRAIL, WING_LEAD)
        self.add_bezier("top-nose", WING_LEAD, ((36, 11), (38, 10), NOSE_TOP))
        self.add_arc("nose", NOSE_TOP, NOSE_FRONT, radius_x=4, sweep=True)
        self.add_bezier("chin", NOSE_FRONT, ((44, 17), (40, 19), BELLY_FRONT))
        self.add_line("belly", BELLY_FRONT, BELLY_REAR)
        self.add_bezier("belly-rear", BELLY_REAR, ((19, 29.5), (15, 30), TAIL_LOW))
        self.add_line("fin-trail", TAIL_LOW, FIN_TIP)
        self.add_line("fin-lead", FIN_TIP, TOP0)
        self.add_contour(
            "fuselage", "top-rear", "top-wing", "top-nose", "nose", "chin",
            "belly", "belly-rear", "fin-trail", "fin-lead", closed=True,
        )

        # Swept wing rising from the top edge.
        self.add_line("wing-lead", WING_LEAD, WING_TIP)
        self.add_line("wing-trail", WING_TIP, WING_TRAIL)
        self.add_contour("wing", "wing-lead", "wing-trail")
        self.relate("connect", "wing", "fuselage")

        # Runway.
        self.add_line("runway", *RUNWAY)
