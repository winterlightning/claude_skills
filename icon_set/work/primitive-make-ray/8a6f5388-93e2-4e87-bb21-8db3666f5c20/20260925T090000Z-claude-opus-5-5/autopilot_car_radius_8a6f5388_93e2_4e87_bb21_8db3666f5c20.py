"""Autopilot car radius: a car side view inside left and right sensing arcs.

Symbol plan: sensing arcs are one pair mirrored about x=24 on the CIRCLE
radius 20, each spanning +-37 degrees (3-4-5 endpoints). The car stays within
radius 12 inside that span (roof and wheels sit above and below it), so
every car point clears the arcs by >= 8. Car: one closed
body contour (flat underside, rounded shoulders, short hood/deck, half-round
cabin) with two wheel half-circles hanging from the underside, mirrored.
The reference's second (inner) arc on each side is dropped: it would need the
car inside radius 4. Lucide: `car` (body + wheels on the underside line) and
`radio` / `wifi` style concentric arcs.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8a6f5388-93e2-4e87-bb21-8db3666f5c20"
SOURCE_PATH = "icon_set/work/todo-references/auto pilot car radius_8a6f5388-93e2-4e87-bb21-8db3666f5c20.svg"
AUTHOR = "claude-opus-5-5"

C = 24
ARC_R = 20
BASE, SIDE, SHOULDER_R, CABIN_R = 5, 10, 3, 6   # car, relative to C
WHEEL_X, WHEEL_R = 6, 3


class AutopilotCarRadius(Solo48):
    icon_id = "autopilot-car-radius"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/vehicle"
    aliases = ("self-driving car range", "autonomous car sensors", "car radar")
    keywords = ("autopilot", "autonomous", "self-driving", "car", "radius", "sensor", "radar")

    def build(self) -> None:
        def p(x, y):
            return (C + x, C + y)

        self.add_arc("range-left", p(-16, -12), p(-16, 12), radius_x=ARC_R, radius_y=ARC_R, sweep=False)
        self.add_arc("range-right", p(16, -12), p(16, 12), radius_x=ARC_R, radius_y=ARC_R, sweep=True)

        top = BASE - 7                     # shoulder start
        deck = top - SHOULDER_R            # hood / deck height
        wl0, wl1 = -WHEEL_X - WHEEL_R, -WHEEL_X + WHEEL_R
        wr0, wr1 = WHEEL_X - WHEEL_R, WHEEL_X + WHEEL_R
        self.add_line("under-rear", p(-SIDE, BASE), p(wl0, BASE))
        self.add_line("under-rear-wheel", p(wl0, BASE), p(wl1, BASE))
        self.add_line("under-mid", p(wl1, BASE), p(wr0, BASE))
        self.add_line("under-front-wheel", p(wr0, BASE), p(wr1, BASE))
        self.add_line("under-front", p(wr1, BASE), p(SIDE, BASE))
        self.add_line("front", p(SIDE, BASE), p(SIDE, top))
        self.add_arc("front-shoulder", p(SIDE, top), p(SIDE - SHOULDER_R, deck), radius_x=SHOULDER_R, radius_y=SHOULDER_R, sweep=False)
        self.add_line("hood", p(SIDE - SHOULDER_R, deck), p(CABIN_R, deck))
        self.add_arc("cabin", p(CABIN_R, deck), p(-CABIN_R, deck), radius_x=CABIN_R, radius_y=CABIN_R, sweep=False)
        self.add_line("deck", p(-CABIN_R, deck), p(-SIDE + SHOULDER_R, deck))
        self.add_arc("rear-shoulder", p(-SIDE + SHOULDER_R, deck), p(-SIDE, top), radius_x=SHOULDER_R, radius_y=SHOULDER_R, sweep=False)
        self.add_line("rear", p(-SIDE, top), p(-SIDE, BASE))
        self.add_contour(
            "body", "under-rear", "under-rear-wheel", "under-mid", "under-front-wheel",
            "under-front", "front", "front-shoulder", "hood", "cabin", "deck",
            "rear-shoulder", "rear", closed=True,
        )
        self.add_arc("wheel-rear", p(wl0, BASE), p(wl1, BASE), radius_x=WHEEL_R, radius_y=WHEEL_R, sweep=False)
        self.add_arc("wheel-front", p(wr0, BASE), p(wr1, BASE), radius_x=WHEEL_R, radius_y=WHEEL_R, sweep=False)
        self.relate("connect", "wheel-rear", "under-rear", "under-rear-wheel", "under-mid")
        self.relate("connect", "wheel-front", "under-mid", "under-front-wheel", "under-front")
