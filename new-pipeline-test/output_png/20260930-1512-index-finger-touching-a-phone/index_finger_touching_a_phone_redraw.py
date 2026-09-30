"""index-finger-touching-a-phone (redraw of the new-pipeline traced SVG).

Plan: an upright phone behind a pointing hand, on VRECT_L (centerline box
(8,4)-(40,44)). The metrics suggested VRECT_M (x fill 85%), but at stroke 4
the hollow finger needs 8 between its walls, and the phone needs 8 clear of
it on each side, so the drawing needs the extra width of VRECT_L.
- phone: open rounded outline (r4 corners): left wall x=8, top y=4, right
  wall x=36. The right wall stops at y=21, above the knuckles, and the bottom
  stops at the bottom-left corner (12,40), where the hand covers the phone.
  Its members are standalone primitives chained with connect, so the
  exact-8 gap to the earpiece certifies. Earpiece: one line at y=12,
  x 18..26, centred on the phone.
- hand: one closed contour. The index finger has walls x=20 / x=28, 8 apart
  (Lucide pointer width), and an r4 tip centred at (24,25) that touches the
  screen's centre. The curled fingers are an r4 and an r2 knuckle bump on a
  y=33 baseline; the cusp between them stays 8 from the finger wall. The
  palm's right side is x=40, and two r6 corners meet a flat base at y=44.
- crease: a short stub continues the finger's right wall below the
  knuckles (connected), so the finger reads apart from the curled fingers.
Lucide pointer / smartphone informed the construction (finger with knuckle
bumps and a stub crease; a rounded phone with an earpiece line). The image's
three curled fingers are reduced to two bumps, because three do not fit 8
spacing in 12 units.

Metric issues fixed:
- clearance e0/e1 (earpiece 3 from the phone top): the earpiece is now 8 below the top.
- clearance e0/e2, e0/e3, e0/e4, e0/e5 (phone crossing the hand): the phone's
  right wall ends 8.6+ above the knuckles, and its bottom ends at the corner,
  8+ clear of the palm.
- clearance e3/e5 (knuckle pieces 3.85 apart): the knuckles are rebuilt as
  bumps in the one hand contour, with a single crease stub.
- loose-join e2/e3, e2/e4, e3/e4: the hand is one closed contour with shared
  endpoints. The stub shares the finger-wall node and is declared connected.
- keyshape-short-axis: every extreme is on the VRECT_L box (x 8/40, y 4/44).
- stroke-width (info): redrawn at stroke 4, with every gap budgeted at 8 or more.
No human head or body, so the head-gap rule does not apply.
validate_icon: valid; build_gate: pass.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3730401c-4d35-4b72-a477-2313ba8f23f7"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1512-index-finger-touching-a-phone/"
    "index-finger-touching-a-phone_raw.svg"
)
AUTHOR = "claude-opus-5-5"

# Phone
PH_L, PH_T, PH_R, PH_B, PH_R4 = 8, 4, 36, 40, 4
PH_RIGHT_END = 21        # right wall stops 12 above the knuckle base
EAR_Y, EAR_HALF = 12, 4
PH_CX = 22               # (8 + 36) / 2

# Hand
FIN_L, FIN_R = 20, 28    # finger walls, 8 apart (Lucide pointer width)
TIP_Y = 25               # tip arc centre y (tip top at 21, 9 below the earpiece)
KNUCKLE_Y = 33
K1, K2 = 36, 40          # r4 + r2 knuckle bumps; the cusp stays 8 from the finger wall
PALM_R = 40
BASE_Y, CORNER = 44, 6
CREASE_END = 36

class IndexFingerTouchingAPhoneRedraw(Solo48):
    icon_id = "index-finger-touching-a-phone-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "mobile"
    aliases = ("tap phone", "touch screen", "phone tap")
    keywords = ("finger", "tap", "touch", "phone", "smartphone", "screen", "hand", "gesture", "mobile")

    def build(self) -> None:
        r = PH_R4
        # Phone: open outline from the bottom-left corner round to the right wall's end.
        self.add_arc("ph-bl", (PH_L + r, PH_B), (PH_L, PH_B - r), radius_x=r, sweep=True)
        self.add_line("ph-left", (PH_L, PH_B - r), (PH_L, PH_T + r))
        self.add_arc("ph-tl", (PH_L, PH_T + r), (PH_L + r, PH_T), radius_x=r, sweep=True)
        self.add_line("ph-top", (PH_L + r, PH_T), (PH_R - r, PH_T))
        self.add_arc("ph-tr", (PH_R - r, PH_T), (PH_R, PH_T + r), radius_x=r, sweep=True)
        self.add_line("ph-right", (PH_R, PH_T + r), (PH_R, PH_RIGHT_END))
        # Standalone members chained by connect, so the straight top-to-earpiece
        # gap certifies at exactly 8 (a mixed arc contour is measured as a curve).
        chain = ["ph-bl", "ph-left", "ph-tl", "ph-top", "ph-tr", "ph-right"]
        for a, b in zip(chain, chain[1:]):
            self.relate("connect", a, b)
        self.add_line("earpiece", (PH_CX - EAR_HALF, EAR_Y), (PH_CX + EAR_HALF, EAR_Y))

        # Hand: clockwise from the finger's left wall top.
        tip_r = (FIN_R - FIN_L) // 2
        self.add_arc("tip", (FIN_L, TIP_Y), (FIN_R, TIP_Y), radius_x=tip_r, sweep=True)
        self.add_line("fin-right", (FIN_R, TIP_Y), (FIN_R, KNUCKLE_Y))
        self.add_arc("knuckle-1", (FIN_R, KNUCKLE_Y), (K1, KNUCKLE_Y), radius_x=(K1 - FIN_R) // 2, sweep=True)
        self.add_arc("knuckle-2", (K1, KNUCKLE_Y), (K2, KNUCKLE_Y), radius_x=(K2 - K1) // 2, sweep=True)
        self.add_line("palm-right", (PALM_R, KNUCKLE_Y), (PALM_R, BASE_Y - CORNER))
        self.add_arc("palm-br", (PALM_R, BASE_Y - CORNER), (PALM_R - CORNER, BASE_Y), radius_x=CORNER, sweep=True)
        self.add_line("palm-base", (PALM_R - CORNER, BASE_Y), (FIN_L + CORNER, BASE_Y))
        self.add_arc("palm-bl", (FIN_L + CORNER, BASE_Y), (FIN_L, BASE_Y - CORNER), radius_x=CORNER, sweep=True)
        self.add_line("fin-left", (FIN_L, BASE_Y - CORNER), (FIN_L, TIP_Y))
        self.add_contour(
            "hand", "tip", "fin-right", "knuckle-1", "knuckle-2", "palm-right",
            "palm-br", "palm-base", "palm-bl", "fin-left", closed=True,
        )
        self.add_line("crease", (FIN_R, KNUCKLE_Y), (FIN_R, CREASE_END))
        self.relate("connect", "crease", "hand")
