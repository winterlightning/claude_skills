"""box-delivery-truck (redraw of the new-pipeline traced SVG).

Plan: flat side view of a box truck, HRECT_M keyshape (centerline box
(4,10)-(44,38)), built in the Lucide `truck` manner: the wheels sit on the
body's bottom line, which stops at each wheel's left and right points.
- body: one open contour. Tall cargo box on the left (top y=10, rear wall
  x=4, corner radius 3), a stepped-down cab roof at y=16 from the box's
  right wall (x=30) to x=38, a 3:4 sloped windshield to (44,24), the cab
  front wall down to y=32, and the bottom line on y=35 with radius-3
  corners.
- wheels: two full circles, radius 3, centred on the bottom line at x=16
  and x=32 (mirrored about x=24). Each is split at its side points so the
  bottom-line pieces share those endpoints; the contact is declared.
- middle bottom line (19,35)-(29,35) joins the two wheels.
Every arc centre and endpoint is on the integer grid; nothing is copied
from the trace coordinates.

Metric issues:
- error `clearance` e0/e2 (front wheel 2.72 from the cargo box's lower
  divider wall): fixed by dropping the divider below the cab roof. The box
  and cab still read through the stepped roofline; a full-height divider
  cannot fit, because two wheels, two outer walls and a divider need five
  8-unit gaps (at least 50 units) inside a 40-unit width.
- error `clearance` e2/e3 and e3/e4 (6.56, wheels against the bottom
  line and walls): fixed. The bottom line now ends on each wheel's side
  point (a declared shared endpoint), and every wall stands 9 from the
  nearest wheel ring.
- error `hole` x2 (2.53-wide slivers beside the wheels): fixed. The
  slivers came from wheels crowding the corners; with 9-unit spacing no
  sliver closes. Wheels are diameter-6 full circles, the exempt ring size
  (a ring with a 6-wide opening would need radius 5, which is too big for
  two wheels plus spacing).
- warn `keyshape-short-axis` (y filled 84%): fixed. Box top y=10, wheel
  bottoms y=38, rear wall x=4 and cab front x=44 hit all four extremes.
- info `stroke-width` (trace 2.64, target 4): fixed by construction at
  stroke 4 with 8-unit centreline spacing.
Lucide construction used: `truck` (box outline whose bottom line breaks
at circle wheels centred on it).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0070eae2-79f7-4131-b3be-164ea822745d"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1924-box-delivery-truck/box-delivery-truck_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT, RIGHT, TOP, FLOOR = 4, 44, 10, 35
CORNER = 3
BOX_RIGHT, CAB_ROOF = 30, 16
SHIELD_TOP_X, SHIELD_BOTTOM_Y = 38, 24
WHEEL_R = 3
WHEELS = (("rear", 16), ("front", 32))


class BoxDeliveryTruckRedraw(Solo48):
    icon_id = "box-delivery-truck-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/vehicles"
    aliases = ("box truck", "delivery truck", "lorry")
    keywords = ("truck", "delivery", "shipping", "cargo", "lorry", "van", "transport")

    def build(self) -> None:
        l, r, t, f, k = LEFT, RIGHT, TOP, FLOOR, CORNER
        (_, rear_x), (_, front_x) = WHEELS
        w = WHEEL_R
        self.add_line("body-floor-rear", (rear_x - w, f), (l + k, f))
        self.add_arc("body-bl", (l + k, f), (l, f - k), radius_x=k, sweep=True)
        self.add_line("body-rear", (l, f - k), (l, t + k))
        self.add_arc("body-tl", (l, t + k), (l + k, t), radius_x=k, sweep=True)
        self.add_line("body-top", (l + k, t), (BOX_RIGHT - k, t))
        self.add_arc("body-tr", (BOX_RIGHT - k, t), (BOX_RIGHT, t + k), radius_x=k, sweep=True)
        self.add_line("body-step", (BOX_RIGHT, t + k), (BOX_RIGHT, CAB_ROOF))
        self.add_line("body-roof", (BOX_RIGHT, CAB_ROOF), (SHIELD_TOP_X, CAB_ROOF))
        self.add_line("body-shield", (SHIELD_TOP_X, CAB_ROOF), (r, SHIELD_BOTTOM_Y))
        self.add_line("body-front", (r, SHIELD_BOTTOM_Y), (r, f - k))
        self.add_arc("body-br", (r, f - k), (r - k, f), radius_x=k, sweep=True)
        self.add_line("body-floor-front", (r - k, f), (front_x + w, f))
        self.add_contour("body", "body-floor-rear", "body-bl", "body-rear", "body-tl",
                         "body-top", "body-tr", "body-step", "body-roof", "body-shield",
                         "body-front", "body-br", "body-floor-front")

        self.add_line("floor-mid", (rear_x + w, f), (front_x - w, f))

        for name, cx in WHEELS:
            self.add_arc(f"{name}-upper", (cx - w, f), (cx + w, f), radius_x=w, sweep=True)
            self.add_arc(f"{name}-lower", (cx + w, f), (cx - w, f), radius_x=w, sweep=True)
            self.add_contour(f"{name}-wheel", f"{name}-upper", f"{name}-lower", closed=True)
            self.add_anchor(f"{name}-axle", (cx, f))

        self.relate("connect", "body", "rear-wheel")
        self.relate("connect", "body", "front-wheel")
        self.relate("connect", "floor-mid", "rear-wheel")
        self.relate("connect", "floor-mid", "front-wheel")
