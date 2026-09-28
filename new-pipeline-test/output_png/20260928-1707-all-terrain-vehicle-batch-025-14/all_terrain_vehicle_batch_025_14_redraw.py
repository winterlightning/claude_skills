"""all-terrain-vehicle-batch-025-14 (redraw of the new-pipeline traced PNG).

Plan: a side-view ATV on HRECT_M (centerline box (4,10)-(44,38)), mirrored
about x=24 except the handlebar, which marks the front.
- wheels: two r=6 rings on the axle line y=32; the rear owns x=4, the
  front owns x=44, both own the bottom y=38.
- body: one polyline. Flat fenders at y=17 (9 above each wheel top) drop on
  45-degree diagonals into a footwell floor at y=22 between the wheels.
- handlebar: a stem rising back from the front fender corner to a short grip
  that owns the top y=10; it joins the body at that corner.

Metric issues fixed:
- stroke-width: redrawn at stroke 4 with every gap re-budgeted for it.
- stroke-count: 7 traced strokes -> 4 parts (2 wheels, body, handlebar).
- keyshape-short-axis: the y axis now reaches both HRECT_M extremes
  (grip y=10, tyres y=38).
- clearance e0-e2/e0-e3/e0-e4/e0-e5/e0-e6/e1-e2/e1-e4/e2-e3/e2-e4/e3-e5/e4-e6:
  fenders sit 9 above the tyres, the footwell floor clears both wheels by
  more than 8, the grip sits 12 above the floor; wheel hubs (e5, e6) and the
  seat (e2) were dropped because no 8-unit band exists for them.
- hole (13.2,27.3) and (39.3,25.2): those slivers between the fender tips,
  seat and body are gone; the only holes are the wheel eyes (8 across).
Dropped: the seat, the wheel hubs and the fender tip hooks - each needs an
8-unit gap that the 28-unit height cannot give.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b4068396-30fc-5e9b-8eca-c9272d55decc"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1707-all-terrain-vehicle-batch-025-14/"
    "all-terrain-vehicle-batch-025-14_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
AXLE_Y = 32
WHEEL_R = 6
WHEEL_DX = 14                 # wheel centres at AXIS -/+ 14 -> x=10 and x=38
FENDER_Y = 17
FLOOR_Y = 22
FENDER_IN = 9                 # fender corner at AXIS -/+ 9
FLOOR_IN = 4                  # floor ends at AXIS -/+ 4 (45-degree drop of 5)
LEFT, RIGHT = 4, 44
GRIP = ((25, 10), (30, 10))


class AllTerrainVehicleBatch02514Redraw(Solo48):
    icon_id = "all-terrain-vehicle-batch-025-14-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport"
    aliases = ("atv", "quad bike", "four wheeler")
    keywords = ("all terrain vehicle", "atv", "quad", "off road", "vehicle")

    def build(self) -> None:
        for tag, cx in (("rear", AXIS - WHEEL_DX), ("front", AXIS + WHEEL_DX)):
            self.add_arc(f"{tag}-top", (cx - WHEEL_R, AXLE_Y), (cx + WHEEL_R, AXLE_Y),
                         radius_x=WHEEL_R)
            self.add_arc(f"{tag}-bot", (cx + WHEEL_R, AXLE_Y), (cx - WHEEL_R, AXLE_Y),
                         radius_x=WHEEL_R)
            self.add_contour(f"{tag}-wheel", f"{tag}-top", f"{tag}-bot", closed=True)

        front_corner = (AXIS + FENDER_IN, FENDER_Y)
        self.add_polyline(
            "body",
            (LEFT, FENDER_Y),
            (AXIS - FENDER_IN, FENDER_Y),
            (AXIS - FLOOR_IN, FLOOR_Y),
            (AXIS + FLOOR_IN, FLOOR_Y),
            front_corner,
            (RIGHT, FENDER_Y),
        )

        self.add_polyline("handlebar", GRIP[0], GRIP[1], front_corner)
        self.relate("connect", "handlebar", "body")
