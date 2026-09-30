"""hand-holding-smartphone-component (redraw of the new-pipeline traced SVG).

Plan: VRECT_M, centerline box (10,4)-(38,44).
- phone: one closed contour 12 wide (18..30) and 24 tall (4..28), all four
  corners r4 (Lucide `smartphone` proportions), flat bottom edge.
- thumb: an open run wrapping the phone's lower-right corner, concentric with
  that corner (C=(26,24)) so the band is exactly 8 wide on centerlines: a
  level tip edge leaving the right wall at (30,20) at 90 degrees, an r4 tip
  round to (38,24) (the x=38 extreme), the r12 outer arc about C down to
  (26,36), 8 below the phone bottom, then an r4 bend into the wrist line x=22
  down to (22,44) (the y=44 extreme).
- palm: the fingers sit behind the phone, so the palm edge is one polyline
  (10,44) up to (10,32) (the x=10 extreme) and a 45 degree run that ends on
  the phone's left wall at (18,24), where the wall hands over to its corner.
  The forearm is 12 wide (x=10 to x=22).
Both hand parts share an exact endpoint with the phone and are declared
`connect`.

Metric issues (hand-holding-smartphone-component_metrics.json):
- stroke-width (trace 2.64 after fit): fixed, stroke 4 and every gap between
  non-joined parts budgeted at >= 8 on centerlines.
- keyshape-short-axis (VRECT_M x filled 66%): fixed, the palm reaches x=10
  and the thumb tip x=38, so all four extremes sit on the box.
- clearance e0/e1 (palm edge 4.57 from the phone's lower-left corner): fixed,
  the palm's vertical run stays >= 8 from the phone wall and corner, the
  thumb band is concentric with the phone corner at 8, and the wrist bend is
  8.6 from the phone's lower-left corner.
- narrow-join (palm meets the phone wall at 14.8 deg): fixed, the palm now
  arrives at 45 degrees (135 to the wall above), and the thumb tip leaves the
  wall at 90 degrees instead of a tangent knob.
- loose-join (palm ends 1.05 short of the phone): fixed, exact shared
  endpoint (18,24) with relate('connect').
- no-head (human subject without a head): not applicable, not fixed; the
  subject is a hand holding a phone, with no figure, so no head is drawn and
  no human-figure mark is made.
Lucide `smartphone` informed the phone (rounded rectangle, empty screen);
Lucide has no hand-holding-phone icon, the hand follows the generated image.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "03153fc4-5884-4120-9394-75c1b95598b0"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1254-hand-holding-smartphone-component/hand-holding-smartphone-component_raw.svg"
AUTHOR = "claude-opus-5-5"

# phone
LEFT, RIGHT, TOP = 18, 30, 4
CORNER = 4
# thumb band about C, the phone's lower-right corner centre: inner radius is
# the phone corner, outer radius 8 further out
C = (26, 24)
INNER, OUTER = CORNER, CORNER + 8
TIP_R = 4
WRIST_X, BOTTOM = 22, 44
# palm
PALM_X, PALM_KNEE = 10, 32


class HandHoldingSmartphoneComponentRedraw(Solo48):
    icon_id = "hand-holding-smartphone-component-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("hand holding phone", "holding smartphone", "mobile in hand")
    keywords = ("hand", "phone", "smartphone", "mobile", "device", "hold", "grip", "thumb")

    def build(self) -> None:
        cx, cy = C
        tip_y = cy - TIP_R                                  # 20
        corner_c = (LEFT + CORNER, cy)                      # (22, 24)
        # phone, clockwise from the top edge
        self.add_line("phone-top", (LEFT + CORNER, TOP), (RIGHT - CORNER, TOP))
        self.add_arc("phone-tr", (RIGHT - CORNER, TOP), (RIGHT, TOP + CORNER), radius_x=CORNER)
        self.add_line("phone-right", (RIGHT, TOP + CORNER), (RIGHT, tip_y))
        self.add_line("phone-right-grip", (RIGHT, tip_y), (cx + INNER, cy))
        self.add_arc("phone-br", (cx + INNER, cy), (cx, cy + INNER), radius_x=INNER)
        self.add_line("phone-bottom", (cx, cy + INNER), (corner_c[0], cy + INNER))
        self.add_arc("phone-bl", (corner_c[0], cy + INNER), (LEFT, corner_c[1]), radius_x=CORNER)
        self.add_line("phone-left", (LEFT, corner_c[1]), (LEFT, TOP + CORNER))
        self.add_arc("phone-tl", (LEFT, TOP + CORNER), (LEFT + CORNER, TOP), radius_x=CORNER)
        self.add_contour(
            "phone", "phone-top", "phone-tr", "phone-right", "phone-right-grip",
            "phone-br", "phone-bottom", "phone-bl", "phone-left", "phone-tl", closed=True,
        )

        # thumb wrapping the lower-right corner, then the wrist
        tip_c = (cx + INNER + TIP_R, cy)                    # (34, 24)
        self.add_line("thumb-top", (RIGHT, tip_y), (tip_c[0], tip_y))
        self.add_arc("thumb-tip", (tip_c[0], tip_y), (cx + OUTER, cy), radius_x=TIP_R)
        self.add_arc("thumb-outer", (cx + OUTER, cy), (cx, cy + OUTER), radius_x=OUTER)
        bend = cx - WRIST_X
        self.add_arc("wrist-bend", (cx, cy + OUTER), (WRIST_X, cy + OUTER + bend),
                     radius_x=bend, sweep=False)
        self.add_line("wrist", (WRIST_X, cy + OUTER + bend), (WRIST_X, BOTTOM))
        self.add_contour("thumb", "thumb-top", "thumb-tip", "thumb-outer", "wrist-bend", "wrist")
        self.relate("connect", "thumb", "phone")

        # palm edge behind the phone
        self.add_polyline("palm", (PALM_X, BOTTOM), (PALM_X, PALM_KNEE), (LEFT, corner_c[1]))
        self.relate("connect", "palm", "phone")
