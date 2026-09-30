"""computer memory module (redraw of the new-pipeline traced SVG).

Plan: a RAM stick seen face-on on HRECT_L (centerline box (4,8)-(44,40)).
- board: one closed rectangle polyline, x 4..44 (the x extremes) and y 8..34
  (top extreme); its round joins give the trace's slightly rounded corners.
  The bottom edge is split at the three pin roots so each pin shares a node
  with it. (Corner arcs r=4 were tried; with arcs in the contour the exact-8
  board-to-chip clearance comes back `review`, so the corners stay joins.)
- chips: the two square chips as one block (12,16)-(36,26), divided by a
  shared wall at the axis x=24, so each chip is a 12x10 cell (6-unit hole).
  The block sits exactly 8 from the board's top, sides and bottom.
- pins: three connector strokes 34 -> 40 (the bottom extreme) at x = 12, 24,
  36, under the chip block's outer walls and divider, as in the trace.
Everything is mirrored about x=24. Lucide `memory-stick` informed the
construction (a rounded board with short pins hanging from the bottom edge);
its notch and contact line are left out, the trace's chips are kept instead.

Keyshape: HRECT_L instead of the suggested HRECT_M. HRECT_M leaves 28 units
of height; board wall, 8 gap, a 10-high chip (the smallest that holds a
6-unit hole), 8 gap and board wall already take 26, which leaves 2-unit pins
that read as bumps. HRECT_L's 32 units give 6-unit pins.

Metric issues fixed:
- stroke-width: redrawn at stroke 4.
- keyshape-short-axis: the trace filled 66% of the height; the board top is
  on y=8 and the pins end on y=40, so all four extremes sit on the box.
- clearance e0/e4, e0/e5, e1/e4, e2/e5, e3/e4, e3/e5 (chips 3-5 units from
  the board bottom and pin roots): the chip block is now 8 from every board
  wall, and the pins, which hang below the board, are 8 below it.
- clearance e4/e5 (chips 7.94 apart) and the five under-6 holes (3.8-4.4
  wide): two separate hollow chips cannot fit the 40-unit width (8 + w + 8 +
  w + 8 leaves w = 8, a 4-unit hole). The chips now share their middle wall,
  so there is no chip-to-chip gap and both chip holes are 6 inscribed; the
  board's remaining hole is a wide ring around them.
Not reproduced: the small gap between the two chips (they now touch).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e89894da-2a07-4c85-8acd-326edf5c64cf"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1046-computer-memory-module/computer-memory-module_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT, RIGHT, TOP, BOTTOM = 4, 44, 8, 40
AXIS = 24
BOARD_BOTTOM = 34
GAP = 8                                  # centerline clearance
CHIP_LEFT, CHIP_RIGHT = LEFT + GAP, RIGHT - GAP        # 12, 36
CHIP_TOP, CHIP_BOTTOM = TOP + GAP, BOARD_BOTTOM - GAP  # 16, 26
PINS = (CHIP_LEFT, AXIS, CHIP_RIGHT)


class ComputerMemoryModuleRedraw(Solo48):
    icon_id = "computer-memory-module-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("ram", "memory stick", "ram module", "dimm")
    keywords = ("memory", "ram", "computer", "hardware", "chip", "module", "dimm")

    def build(self) -> None:
        self.add_polyline("board", (LEFT, TOP), (RIGHT, TOP), (RIGHT, BOARD_BOTTOM),
                          *[(x, BOARD_BOTTOM) for x in reversed(PINS)], (LEFT, BOARD_BOTTOM),
                          closed=True)

        self.add_polyline("chips", (CHIP_LEFT, CHIP_TOP), (AXIS, CHIP_TOP),
                          (CHIP_RIGHT, CHIP_TOP), (CHIP_RIGHT, CHIP_BOTTOM),
                          (AXIS, CHIP_BOTTOM), (CHIP_LEFT, CHIP_BOTTOM), closed=True)
        self.add_line("chip-divider", (AXIS, CHIP_TOP), (AXIS, CHIP_BOTTOM))
        self.relate("connect", "chips", "chip-divider")

        for index, x in enumerate(PINS, start=1):
            self.add_line(f"pin-{index}", (x, BOARD_BOTTOM), (x, BOTTOM))
            self.relate("connect", "board", f"pin-{index}")
