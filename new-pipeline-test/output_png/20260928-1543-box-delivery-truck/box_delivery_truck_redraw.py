"""box delivery truck (redraw of the new-pipeline traced SVG).

Plan: right-facing box truck in side view on HRECT_M (centerline box
(4,10)-(44,38), the metrics' suggestion; the trace is 2.16:1 wide).
- body: one closed outline -- cargo box top at the y=10 extreme and rear wall
  on x=4, a flat chassis at CHASSIS_Y=28, then the cab: front wall on x=44,
  a 45-degree windshield from NOSE (44,23) to SHOULDER (37,16) and a lower
  roof at y=16 back to the cargo wall.
- wall: the cargo/cab divider at x=28, a straight T from the box top to the
  chassis (roughly the trace's 60/40 box-to-cab split).
- wheels: two equal r=5 circles hung tangent under the chassis, each split at
  its top apex, which is also a chassis vertex (shared node + connect); the
  bottom apexes are the y=38 extreme. The centres, 15 and 33, are 18 apart, so the
  rims are exactly 8 apart on centerlines.
Lucide `truck` informed the construction (box + lower cab + slanted nose,
wheels as plain circles on the chassis), redrawn on this grid.

Metric issues fixed:
- stroke-width / stroke-count: redrawn at stroke 4 as 4 parts (body, wall,
  two wheels) instead of 8 traced strokes.
- keyshape-short-axis: the trace filled 66% of the HRECT_M height; the box is
  raised to y=10 and the wheels reach y=38, so all four extremes sit on the box.
- clearance e1/e3, e1/e4, e1/e5, e1/e7, e2/e3, e2/e4, e2/e6, e4/e5 and the
  five under-6 holes: all came from wheels cutting into the body and a cab
  window line 6 units under the roof. The wheels now hang below the chassis
  (no wall pockets), and the cab window line is dropped (a 28-unit-tall
  HRECT_M cannot fit roof, window and chassis 8 apart plus wheels). Every
  hole is now at least 6 inscribed (the wheels' holes are exactly 6).
- loose-join e4/e6, e5/e6: the nose is a single polyline vertex (44,23).
Not reproduced: the trace's overlap of the wheels with the body bottom (the
redraw has the wheels below the chassis instead), and the cab's side window.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1543-box-delivery-truck/box-delivery-truck_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT, RIGHT, TOP, BOTTOM = 4, 44, 10, 38
WHEEL_R = 5
CHASSIS_Y = BOTTOM - 2 * WHEEL_R    # wheels hang tangent below the chassis
AXLE_Y = BOTTOM - WHEEL_R
REAR_X, FRONT_X = 15, 33
WALL_X = 28                         # cargo box / cab divider
ROOF_Y = 16
SHOULDER = (37, ROOF_Y)             # windshield top
NOSE = (RIGHT, 23)                  # windshield foot


class BoxDeliveryTruckRedraw(Solo48):
    icon_id = "box-delivery-truck-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/road"
    aliases = ("box truck", "delivery truck", "cargo truck")
    keywords = ("truck", "delivery", "box", "cargo", "shipping", "van", "transport")

    def wheel(self, name, cx):
        top, bottom = (cx, CHASSIS_Y), (cx, BOTTOM)
        self.add_arc(f"{name}-front", top, bottom, radius_x=WHEEL_R)
        self.add_arc(f"{name}-back", bottom, top, radius_x=WHEEL_R)
        self.add_contour(name, f"{name}-front", f"{name}-back", closed=True)
        return top

    def build(self) -> None:
        rear = self.wheel("wheel-rear", REAR_X)
        front = self.wheel("wheel-front", FRONT_X)
        self.add_polyline("body", (WALL_X, TOP), (LEFT, TOP), (LEFT, CHASSIS_Y), rear,
                          (WALL_X, CHASSIS_Y), front, (RIGHT, CHASSIS_Y), NOSE, SHOULDER,
                          (WALL_X, ROOF_Y))
        self.add_line("wall", (WALL_X, TOP), (WALL_X, CHASSIS_Y))
        self.relate("connect", "body", "wheel-rear")
        self.relate("connect", "body", "wheel-front")
        self.relate("connect", "body", "wall")
