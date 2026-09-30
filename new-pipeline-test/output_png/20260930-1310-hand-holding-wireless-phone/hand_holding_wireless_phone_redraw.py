"""hand-holding-wireless-phone (redraw of the new-pipeline traced SVG).

Plan: an upright phone floating above an open palm, broadcasting two signal
arcs. SQUARE, centerline box (6,6)-(42,42).
- phone: closed rounded rectangle x 10..22, y 6..26, corner r 3 (tall 12x20,
  inner opening 8x16 of ink).
- signal: two concentric-looking arcs opening to the right of the phone, as
  Lucide `smartphone-nfc` does: inner r 9 through (31,11)/(31,21) (centre
  ~(23.5,16)), outer r 15 through (39,7)/(39,25) (centre (27,16), apex exactly
  x=42). Both are mirrored about the phone's mid height y=16; the band between
  them is 8.6 at the ends and 9.5 at the apexes.
- arm: one open stroke. A 45-degree forearm (6,42)-(11,37) turns tangentially
  into the horizontal palm y=35, which runs under the phone and ends in a
  short upward curl at (29,32), so the phone sits centred over the hand.
Extremes: x=6 forearm, y=6 phone top, x=42 outer arc apex, y=42 forearm.

Why the layout moved: the trace stacks waves above the phone above the palm.
With 8-unit centerline gaps that stack needs outer arc -> inner arc (8) ->
inner arc sag + gap (>=10) -> phone (>=14) -> gap (8) -> palm -> forearm drop,
well over the 40-unit height of any keyshape, so the waves go beside the phone.

Metric issues (hand-holding-wireless-phone_metrics.json):
- stroke-width (info, trace 2.65): fixed, redrawn at stroke 4 with every gap
  re-budgeted.
- keyshape-short-axis (VRECT_M x filled 85%): fixed by changing keyshape.
  Moving the waves beside the phone makes the subject square (36x36), so
  SQUARE is the exact fit; every extreme sits on the box.
- clearance e0/e1 (outer vs inner wave, 3.25): fixed, the arcs are >= 8.6 apart.
- clearance e0/e2, e1/e2 (waves vs phone, 6.0 / 3.15): fixed, the inner arc's
  ends are 9 right of the phone's right wall.
- clearance e2/e3 (phone vs palm, 3.38): fixed, the phone bottom (y 26) is 9
  above the palm (y 35); at exactly 8 the palm's tangent bend came back as a
  review warning.
- hole [30.0, 9.7] (0.4, the sliver between the merged waves): fixed, the waves
  no longer touch so there is no enclosed sliver.
- hole [30.4, 16.1] (phone opening 4.4): fixed, the opening is 8x16 of ink.
- no-head (warn): not applicable; the subject is a hand only, with no head or
  torso, so there is no human figure to mark.
Reference: Lucide `smartphone-nfc` (phone with arcs radiating to the side) and
`hand-helping` (open palm entering from the lower left). The hand is
deliberately asymmetric.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "67fe58cc-4429-4121-a342-5bd274251e19"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1310-hand-holding-wireless-phone/hand-holding-wireless-phone_raw.svg"
AUTHOR = "claude-opus-5-5"

# Phone: tall rounded rectangle in the upper left.
PH_L, PH_T, PH_R, PH_B, PH_RAD = 10, 6, 22, 26, 3
# Signal arcs to the right of the phone (ends mirrored about y=16).
INNER_END, INNER_R = 31, 9      # (31,11)-(31,21)
INNER_HALF = 5
OUTER_END, OUTER_R = 39, 15     # (39,7)-(39,25), centre (27,16)
OUTER_HALF = 9
MID_Y = (PH_T + PH_B) // 2      # 16
# Arm: forearm at 45 degrees, palm 9 below the phone, curl at the tip.
ARM_START, ARM_BEND = (6, 42), (11, 37)
PALM_Y = PH_B + 9               # 35
PALM_IN, PALM_OUT = (17, PALM_Y), (25, PALM_Y)
TIP = (29, 32)


class HandHoldingWirelessPhoneRedraw(Solo48):
    icon_id = "hand-holding-wireless-phone-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("hand-holding-phone", "wireless-phone-in-hand", "contactless-phone")
    keywords = ("phone", "smartphone", "mobile", "hand", "holding", "wireless", "signal", "nfc", "contactless")

    def build(self) -> None:
        r = PH_RAD
        self.add_line("phone-top", (PH_L + r, PH_T), (PH_R - r, PH_T))
        self.add_arc("phone-tr", (PH_R - r, PH_T), (PH_R, PH_T + r), radius_x=r, sweep=True)
        self.add_line("phone-right", (PH_R, PH_T + r), (PH_R, PH_B - r))
        self.add_arc("phone-br", (PH_R, PH_B - r), (PH_R - r, PH_B), radius_x=r, sweep=True)
        self.add_line("phone-bottom", (PH_R - r, PH_B), (PH_L + r, PH_B))
        self.add_arc("phone-bl", (PH_L + r, PH_B), (PH_L, PH_B - r), radius_x=r, sweep=True)
        self.add_line("phone-left", (PH_L, PH_B - r), (PH_L, PH_T + r))
        self.add_arc("phone-tl", (PH_L, PH_T + r), (PH_L + r, PH_T), radius_x=r, sweep=True)
        self.add_contour("phone", "phone-top", "phone-tr", "phone-right", "phone-br",
                         "phone-bottom", "phone-bl", "phone-left", "phone-tl", closed=True)

        self.add_arc("wave-inner", (INNER_END, MID_Y - INNER_HALF), (INNER_END, MID_Y + INNER_HALF),
                     radius_x=INNER_R, sweep=True)
        self.add_arc("wave-outer", (OUTER_END, MID_Y - OUTER_HALF), (OUTER_END, MID_Y + OUTER_HALF),
                     radius_x=OUTER_R, sweep=True)

        # Arm: forearm -> tangent bend -> palm -> upward curl.
        bx, by = ARM_BEND
        ix, iy = PALM_IN
        ox, oy = PALM_OUT
        tx, ty = TIP
        self.add_line("forearm", ARM_START, ARM_BEND)
        self.add_bezier("wrist", ARM_BEND, ((bx + 2, by - 2), (ix - 3, iy), PALM_IN))
        self.add_line("palm", PALM_IN, PALM_OUT)
        self.add_bezier("fingertip", PALM_OUT, ((ox + 2, oy), (tx - 1, ty + 1.5), TIP))
        self.add_contour("arm", "forearm", "wrist", "palm", "fingertip")
