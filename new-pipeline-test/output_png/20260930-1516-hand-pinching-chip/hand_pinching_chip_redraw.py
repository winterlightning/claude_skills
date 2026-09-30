"""hand-pinching-chip (redraw of the new-pipeline traced SVG).

Plan: a side-view hand reaches in from the right. Its index finger (above)
and thumb (below) pinch a small square microchip whose two contact pins
point left. Authored on VRECT_L, centerline box (8,4)-(40,44).
Keyshape: the metrics suggested SQUARE (36 tall), but the pinch axis
stacks finger band 8 + gap 8 + chip 8 + gap 8 + thumb band 8 = 40, so only
a 40-tall box fits the brief's "chip clear of both fingertips". VRECT_L's
32 width still holds the pins, chip, pinch throat and palm.
- index finger: band y 4..12, r4 round tip about (16,8).
- thumb: band y 36..44, r4 round tip about (18,40), 2 behind the index tip.
- throat: the finger underside and thumb top turn through r8 corners about
  (21,20) and (21,28) into a short wall x=29, a round opening like the
  image's. The corners sit 8.06 from the chip corners (exactly 8 on a curve
  comes back `review`, so the throat is 1 to the right).
- back of hand: an r10 knuckle arc about (30,14) from the finger top to the
  right edge x=40, then straight down to the open wrist end (40,44); the
  thumb underside stops at (26,44), so the wrist opens downward at the lower
  right (a long thumb base line made the hand read as a "2").
- chip: an 8x8 square (12,20)-(20,28), exactly 8 from both finger bands.
  An 8-tall chip only has room for two pins 8 apart at its top and bottom
  rows, so the pins are the top and bottom edges carried 4 further left to
  x=8.
The hand outline is standalone primitives chained with connect (not one
contour), so the straight finger/thumb-to-chip gaps of exactly 8 certify as
straight-segment spacing.
Lucide `hand` / `grab` informed the rounded equal-width finger bands and the
single open hand outline; Lucide `cpu` gave the square chip with pins
(reduced to two pins on one side).

Metric issues fixed:
- clearance e0/e1 (hand 2.06 from the chip): the chip is 8 from both finger
  bands and 8.06+ from the throat.
- clearance e0/e2, e0/e3 (fingertips 6.2 / 5.8 from the pins): the pins sit
  on the chip's top and bottom rows, 8.6+ from both round tips.
- clearance e2/e3 (pins 3.75 apart): the pins are 8 apart.
- hole at (12.4,19.2), 4.0 wide: the only enclosed opening is the 8x8 chip.
- keyshape-short-axis: every extreme sits on the VRECT_L box (x 8/40,
  y 4/44). SQUARE could not hold the 40-unit pinch stack (see above).
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8.
- no-head (warn): not applicable; the subject is an isolated hand, not a
  figure, so there is no head or head gap.
validate_icon: valid; build_gate: pass.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7fbc0ada-902f-43f4-bdab-cc7b8ccc1b02"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1516-hand-pinching-chip/hand-pinching-chip_raw.svg"
AUTHOR = "claude-opus-5-5"

TIP_R = 4                      # finger bands are 2 * TIP_R wide
TIP_X = 16                     # index tip centre x (leftmost ink x 12)
THUMB_X = 18                   # thumb tip sits 2 behind the index tip
FINGER_TOP, FINGER_LOW = 4, 12
THUMB_TOP, THUMB_LOW = 36, 44
THROAT_X, THROAT_R = 29, 8     # r8 throat corners about (21,20)/(21,28): 8.06 from the chip corners
KNUCKLE_X, BACK_X = 30, 40     # r10 knuckle arc about (30, 14)
WRIST_BACK_Y = 44
WRIST_LOW_X = 26

CHIP_L, CHIP_R = 12, 20
CHIP_T, CHIP_B = 20, 28        # 8 below the finger, 8 above the thumb
PIN_X = 8


class HandPinchingChipRedraw(Solo48):
    icon_id = "hand-pinching-chip-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "programing"
    aliases = ("chip hold", "hand holding microchip", "pinch chip")
    keywords = ("hand", "pinch", "chip", "microchip", "hardware", "processor", "electronics", "technology")

    def build(self) -> None:
        knuckle_r = BACK_X - KNUCKLE_X
        # -- hand: open outline from the wrist's back edge round to its lower edge
        self.add_line("back", (BACK_X, WRIST_BACK_Y), (BACK_X, FINGER_TOP + knuckle_r))
        self.add_arc("knuckle", (BACK_X, FINGER_TOP + knuckle_r), (KNUCKLE_X, FINGER_TOP),
                     radius_x=knuckle_r, sweep=False)
        self.add_line("finger-top", (KNUCKLE_X, FINGER_TOP), (TIP_X, FINGER_TOP))
        self.add_arc("fingertip", (TIP_X, FINGER_TOP), (TIP_X, FINGER_LOW), radius_x=TIP_R, sweep=False)
        self.add_line("finger-low", (TIP_X, FINGER_LOW), (THROAT_X - THROAT_R, FINGER_LOW))
        self.add_arc("throat-top", (THROAT_X - THROAT_R, FINGER_LOW), (THROAT_X, FINGER_LOW + THROAT_R),
                     radius_x=THROAT_R, sweep=True)
        self.add_line("throat", (THROAT_X, FINGER_LOW + THROAT_R), (THROAT_X, THUMB_TOP - THROAT_R))
        self.add_arc("throat-low", (THROAT_X, THUMB_TOP - THROAT_R), (THROAT_X - THROAT_R, THUMB_TOP),
                     radius_x=THROAT_R, sweep=True)
        self.add_line("thumb-top", (THROAT_X - THROAT_R, THUMB_TOP), (THUMB_X, THUMB_TOP))
        self.add_arc("thumb-tip", (THUMB_X, THUMB_TOP), (THUMB_X, THUMB_LOW), radius_x=TIP_R, sweep=False)
        self.add_line("thumb-low", (THUMB_X, THUMB_LOW), (WRIST_LOW_X, THUMB_LOW))
        chain = ["back", "knuckle", "finger-top", "fingertip", "finger-low", "throat-top",
                 "throat", "throat-low", "thumb-top", "thumb-tip", "thumb-low"]
        for a, b in zip(chain, chain[1:]):
            self.relate("connect", a, b)

        # -- chip: 8x8 square, pins carry its top and bottom rows to the left
        self.add_polyline("chip", (CHIP_L, CHIP_T), (CHIP_R, CHIP_T), (CHIP_R, CHIP_B), (CHIP_L, CHIP_B),
                          closed=True)
        self.add_line("pin-top", (PIN_X, CHIP_T), (CHIP_L, CHIP_T))
        self.add_line("pin-low", (PIN_X, CHIP_B), (CHIP_L, CHIP_B))
        self.relate("connect", "pin-top", "chip")
        self.relate("connect", "pin-low", "chip")
