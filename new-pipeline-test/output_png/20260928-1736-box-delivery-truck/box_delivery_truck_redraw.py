"""box-delivery-truck (redraw of the new-pipeline traced SVG).

Plan: side view of a box truck driving right, on HRECT_M (centerline box
(4,10)-(44,38)), built the way Lucide `truck` is: one outline, wheels whose
centres sit on the chassis line, and chassis segments that stop exactly on
each wheel's left / right extreme.
- body: open polyline from the rear corner (4,33) up the rear wall to the
  cargo top y=10 (the top extreme), across to the cargo/cab step at x=26,
  down to the cab roof y=16, along the roof to (38,16), down the sloped
  windshield to (44,24) (the right extreme), down the nose to (44,33) and back
  along the chassis to the front wheel's right extreme (36,33).
- divider: one polyline from the rear wheel's right extreme along the chassis
  to (26,33), then straight up the cargo/cab wall to the roof step (26,16).
- wheels: two equal circles, r=5 (6-unit inner hole), centres (9,33) and
  (31,33) on the chassis line; their bottoms are the y=38 extreme. Each circle
  is split at its left / right extremes so the chassis shares both endpoints.
  The rear wall lands on the rear wheel's left extreme and the cargo/cab wall
  on the front wheel's left extreme, both tangent-continuous (vertical wall
  into the wheel's vertical tangent).
Why the rear wheel is flush with the rear wall: 40 units of width cannot hold
two 10-unit wheels plus five 8-unit gaps (rear wall, wheel, cab wall, wheel,
nose = 44). A short chassis stub behind the rear wheel (the image has one)
leaves the wall 5-6 from the wheel and fails the build gate's internal
spacing, so the wall runs straight into the wheel instead. The chassis stub
in front of the front wheel keeps its full 8.
Proportions: cargo 22 wide, cab 18 (the image's cab is about half the cargo;
the extra cab width is what the 8-unit nose stub costs), roof 6 below the
cargo top, windshield dropping over the front of the cab.

Fixed from the trace metrics:
- stroke-width (info): redrawn at stroke 4 on the 48 grid; every gap is
  budgeted for stroke 4.
- keyshape-short-axis: the trace filled 66% of HRECT_M on y; the body was
  made taller (cargo top y=10, wheel bottoms y=38) so all four extremes sit
  on the box with no stretch.
- clearance e1/e2, e2/e3, e3/e4 (2.5-6 apart): the chassis segments stopped
  just short of the wheels. They now end exactly on the wheel extremes and
  are declared connected, so there is no near-miss left.
- holes at (11.2,30.3) and (36.5,30.3) (1.6 wide): slivers between the
  chassis line and the wheel tops, because the trace ran the line through the
  wheels above their centres. With the centres on the line there are no
  slivers.
- hole at (35.8,22.7) (5.6 wide): the cab interior. The cab is now 18 wide
  with the roof 12 above the front wheel top, well over the 6 floor.
All issues fixed; validate_icon() valid with no warnings, build_gate pass.
Lucide `truck` informed the construction (wheel centres on the chassis line,
chassis broken by the wheels). The cab slope is deliberate asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0070eae2-79f7-4131-b3be-164ea822745d"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1736-box-delivery-truck/box-delivery-truck_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT, RIGHT = 4, 44          # rear wall, nose
TOP, ROOF = 10, 16           # cargo top, cab roof
CHASSIS = 33                 # wheel centres sit on this line
WHEEL_R = 5                  # CHASSIS + WHEEL_R = 38, the bottom extreme
REAR_X = LEFT + WHEEL_R      # the rear wall lands on the rear wheel's left extreme
STEP_X = 26                  # cargo/cab wall
FRONT_X = STEP_X + WHEEL_R   # the wall lands on the front wheel's left extreme
SHIELD = (38, ROOF)          # roof end, top of the windshield
NOSE_TOP = (RIGHT, 24)       # bottom of the windshield


class BoxDeliveryTruckRedraw(Solo48):
    icon_id = "box-delivery-truck-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/vehicles"
    aliases = ("delivery truck", "box truck", "cargo truck", "lorry")
    keywords = ("truck", "delivery", "shipping", "cargo", "van", "logistics", "transport")

    def build(self) -> None:
        self.add_polyline(
            "body",
            (LEFT, CHASSIS), (LEFT, TOP),
            (STEP_X, TOP), (STEP_X, ROOF), SHIELD, NOSE_TOP,
            (RIGHT, CHASSIS), (FRONT_X + WHEEL_R, CHASSIS),
        )
        self.add_polyline(
            "divider",
            (REAR_X + WHEEL_R, CHASSIS), (STEP_X, CHASSIS), (STEP_X, ROOF),
        )
        self.relate("connect", "divider", "body")

        for name, cx in (("rear-wheel", REAR_X), ("front-wheel", FRONT_X)):
            left, right = (cx - WHEEL_R, CHASSIS), (cx + WHEEL_R, CHASSIS)
            self.add_arc(f"{name}-top", left, right, radius_x=WHEEL_R)
            self.add_arc(f"{name}-bottom", right, left, radius_x=WHEEL_R)
            self.add_contour(name, f"{name}-top", f"{name}-bottom", closed=True)
            self.relate("connect", name, "body")
            self.relate("connect", name, "divider")
