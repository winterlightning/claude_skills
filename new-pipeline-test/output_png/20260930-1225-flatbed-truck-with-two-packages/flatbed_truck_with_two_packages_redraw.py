"""flatbed truck with two packages (redraw of the new-pipeline traced SVG).

Plan: right-facing flatbed truck in side view on HRECT_M (centerline box
(4,10)-(44,38), the metrics' suggestion; the trace is 2.16:1 wide).
- bed: one straight flatbed at BED_Y=28 from the rear extreme x=4 to the cab.
- cab: one closed outline -- back wall on CAB_X=32, roof at the y=10 extreme,
  a 45-degree windshield from SHOULDER (38,10) to NOSE (44,16) and the front
  wall on the x=44 extreme down to the bed line.
- packages: two equal open boxes standing on the bed (the bed is their floor),
  PKG_W=10 wide and PKG_H=10 tall, so each hole is 6x6 inscribed. The rear one
  starts at the bed's rear end; the gap between them is 8 on centerlines. The
  front one leans on the cab back wall (its top meets the wall at a split
  vertex) because 40 units cannot fit box, gap, box, gap and a readable cab.
- wheels: two equal r=5 circles hung tangent under the bed, each split at its
  top apex, which is also a bed/cab vertex (shared node + connect); the bottom
  apexes are the y=38 extreme. Rear wheel under the rear package, front wheel
  under the cab.
Lucide `truck` informed the construction (lower cab with a slanted nose, plain
round wheels on the chassis), redrawn on this grid.

Metric issues fixed:
- stroke-width: redrawn at stroke 4 as 6 parts (bed, cab, two packages, two
  wheels), the stroke budget.
- keyshape-short-axis: the trace filled 66% of the HRECT_M height; the cab roof
  now sits on y=10 and the wheels reach y=38, so all four extremes are on the box.
- clearance e0/e3, e0/e5, e1/e2, e1/e4, e1/e5, e2/e3, e2/e4, e2/e5, e3/e5, e4/e5
  and the seven under-6 holes: they came from packages floating 2 units above
  the bed, wheels cutting into the bed, and a cab window 3 units inside the cab.
  Packages now stand on the bed (shared vertices, connected), the wheels hang
  below it, and every enclosed space is at least 6 inscribed.
Not reproduced: the cab side window (the 12-unit cab cannot keep it 8 from the
roof, back wall and front wall), the bed overhang past the rear package and the
gap between the front package and the cab (both cost width the 40-unit
HRECT_M box does not have).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4375e4d8-018b-56ed-9a8e-e4438dff0be0"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1225-flatbed-truck-with-two-packages/flatbed-truck-with-two-packages_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT, RIGHT, TOP, BOTTOM = 4, 44, 10, 38
WHEEL_R = 5
BED_Y = BOTTOM - 2 * WHEEL_R        # wheels hang tangent below the bed
PKG_W, PKG_H, PKG_GAP = 10, 10, 8
PKG_TOP = BED_Y - PKG_H
REAR_PKG = LEFT
FRONT_PKG = REAR_PKG + PKG_W + PKG_GAP
CAB_X = FRONT_PKG + PKG_W           # front package leans on the cab wall
SHOULDER = (38, TOP)                # windshield top
NOSE = (RIGHT, TOP + RIGHT - 38)    # 45-degree windshield foot
REAR_WHEEL_X, FRONT_WHEEL_X = 11, 38


class FlatbedTruckWithTwoPackagesRedraw(Solo48):
    icon_id = "flatbed-truck-with-two-packages-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/road"
    aliases = ("flatbed truck", "cargo truck", "delivery truck")
    keywords = ("truck", "flatbed", "packages", "boxes", "cargo", "delivery", "shipping", "transport")

    def wheel(self, name, cx):
        top, bottom = (cx, BED_Y), (cx, BOTTOM)
        self.add_arc(f"{name}-front", top, bottom, radius_x=WHEEL_R)
        self.add_arc(f"{name}-back", bottom, top, radius_x=WHEEL_R)
        self.add_contour(name, f"{name}-front", f"{name}-back", closed=True)
        return top

    def build(self) -> None:
        rear = self.wheel("wheel-rear", REAR_WHEEL_X)
        front = self.wheel("wheel-front", FRONT_WHEEL_X)
        rear_foot, rear_back = (REAR_PKG, BED_Y), (REAR_PKG + PKG_W, BED_Y)
        front_foot = (FRONT_PKG, BED_Y)
        self.add_polyline("bed", rear_foot, rear, rear_back, front_foot, (CAB_X, BED_Y))
        self.add_polyline("cab", (CAB_X, BED_Y), front, (RIGHT, BED_Y), NOSE, SHOULDER,
                          (CAB_X, TOP), (CAB_X, PKG_TOP), closed=True)
        self.add_polyline("package-rear", rear_foot, (REAR_PKG, PKG_TOP),
                          (REAR_PKG + PKG_W, PKG_TOP), rear_back)
        self.add_polyline("package-front", front_foot, (FRONT_PKG, PKG_TOP), (CAB_X, PKG_TOP))
        self.relate("connect", "bed", "cab")
        self.relate("connect", "bed", "wheel-rear")
        self.relate("connect", "cab", "wheel-front")
        self.relate("connect", "bed", "package-rear")
        self.relate("connect", "bed", "package-front")
        self.relate("connect", "cab", "package-front")
