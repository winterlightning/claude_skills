"""burger beside drink cup (redraw of the new-pipeline traced SVG).

Plan: HRECT_M (centerline box (4,10)-(44,38)), as suggested. Width budget
40 = burger 20 + gap 8 + cup 12; height budget 28 = bun dome 11 + 9 + 8.
- top bun: one closed contour. A 10x9 half ellipse about (14,19) whose
  apex (14,10) is the y=10 extreme and whose left end sits on the x=4
  extreme; radius-2 corners turn tangentially into the flat base y=21.
  The base sits 9 (not 8) above the filling: the engine cannot certify a
  corner arc at exactly 8, so exact-8 came back `review`.
- filling: straight line y=30 across the full bun width (4..24).
- bottom bun: straight line y=38 (4..24), the y=38 extreme with the cup.
  The trace's closed shallow bottom bun cannot survive: dome 12 + filling
  gap 8 + gap 8 + a closed bun with a 6-unit opening (10) needs 36+ rows,
  the box has 28. A flat slab keeps the three-layer burger read.
- cup: one closed polygon, rim y=18 from x=32 to x=44 (the x=44 extreme),
  walls tapering 2 units to the base 34..42 on y=38; symmetric about x=38.
  The rim is split at the straw node.
- straw: x=38 from the rim up to (38,10), connected to the cup.
No Lucide original was used (lucide `hamburger`/`cup-soda` overlap their
layers at 24px, which cannot hold MIC 8); only the dome-over-lines stacking.
Metric issues:
- stroke-width (trace 2.4): redrawn at stroke 4 on the integer grid.
- keyshape-short-axis (x filled 96%): fixed; buns reach x=4, cup rim x=44,
  straw/dome apex y=10, cup base and bottom bun y=38.
- clearance e0-e2/e3/e4/e5 (cup vs burger 4.96..6.08): fixed; cup wall
  (32,18)-(34,38) is >= 8.3 from the dome and the burger lines.
- clearance e2-e3, e3-e4, e3-e5, e2-e4, e2-e5, e4-e5 (burger layers
  2.5..5.5): fixed; dome base, filling and bottom bun are 9 / 8 apart.
- hole at (8.2,35.7) (0.6, bottom bun sliver): fixed by drawing the bottom
  bun as one line; no closed shallow bun remains.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5d4383cc-7fa3-4af5-b119-dc3b67d08db0"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1658-burger-beside-drink-cup/burger-beside-drink-cup_raw.svg"
AUTHOR = "claude-opus-5-5"

BUN_L, BUN_R = 4, 24
BUN_MID = (BUN_L + BUN_R) // 2
DOME_RX = (BUN_R - BUN_L) // 2
DOME_RY = 9
CORNER_R = 2
DOME_BASE = 21
DOME_SPRING = DOME_BASE - CORNER_R
BOTTOM_Y = 38
FILLING_Y = BOTTOM_Y - 8  # dome base 9 above: its corner arcs cannot certify exactly 8

CUP_MID = 38
RIM_HALF, BASE_HALF = 6, 4
RIM_Y = 18
STRAW_TOP = 10


class BurgerBesideDrinkCupRedraw(Solo48):
    icon_id = "burger-beside-drink-cup-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/fast-food"
    aliases = ("burger and drink", "fast food", "burger and soda", "combo meal")
    keywords = ("burger", "hamburger", "drink", "cup", "soda", "straw", "fast food", "meal")

    def build(self) -> None:
        self._burger()
        self._cup()

    def _burger(self) -> None:
        l, r, m = BUN_L, BUN_R, BUN_MID
        self.add_arc("dome-l", (l, DOME_SPRING), (m, DOME_SPRING - DOME_RY),
                     radius_x=DOME_RX, radius_y=DOME_RY, sweep=True)
        self.add_arc("dome-r", (m, DOME_SPRING - DOME_RY), (r, DOME_SPRING),
                     radius_x=DOME_RX, radius_y=DOME_RY, sweep=True)
        self.add_arc("dome-corner-r", (r, DOME_SPRING), (r - CORNER_R, DOME_BASE),
                     radius_x=CORNER_R, sweep=True)
        self.add_line("dome-base", (r - CORNER_R, DOME_BASE), (l + CORNER_R, DOME_BASE))
        self.add_arc("dome-corner-l", (l + CORNER_R, DOME_BASE), (l, DOME_SPRING),
                     radius_x=CORNER_R, sweep=True)
        self.add_contour("top-bun", "dome-l", "dome-r", "dome-corner-r", "dome-base",
                         "dome-corner-l", closed=True)
        self.add_line("filling", (l, FILLING_Y), (r, FILLING_Y))
        self.add_line("bottom-bun", (l, BOTTOM_Y), (r, BOTTOM_Y))

    def _cup(self) -> None:
        m = CUP_MID
        self.add_polyline(
            "cup",
            (m - RIM_HALF, RIM_Y), (m, RIM_Y), (m + RIM_HALF, RIM_Y),
            (m + BASE_HALF, BOTTOM_Y), (m - BASE_HALF, BOTTOM_Y),
            closed=True,
        )
        self.add_line("straw", (m, RIM_Y), (m, STRAW_TOP))
        self.relate("connect", "straw", "cup")
