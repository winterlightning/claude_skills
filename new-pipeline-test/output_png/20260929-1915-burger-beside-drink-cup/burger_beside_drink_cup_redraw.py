"""burger-beside-drink-cup (redraw of the new-pipeline traced SVG).

Plan: a burger on the left and a tapered soda cup with a bent straw on the
right, on HRECT_L (centerline box (4,8)-(44,40)).
- x budget 40 = burger 18 + gap 8 + cup 14.
- burger top bun: closed dome, half-ellipse rx 9 ry 10 over a flat base line
  on y=21; its left end is the x=4 extreme.
- burger bottom bun: 18x10 rectangle (y 30-40), flat top, rounded bottom
  corners r4, 9 below the top bun's base; its bottom is the y=40 extreme.
  The gap between the buns reads as the patty layer.
- cup: lid line (30,16)-(44,16) (the x=44 extreme) closing a trapezoid body
  that tapers 3 per side to a flat bottom on y=40, mirrored about x=37.
- straw: rises from the lid centre (split point, declared connect) and bends
  45 degrees up-right to its tip on the y=8 extreme.
Lucide references: hamburger (dome over flat base, rounded bottom bun) and
cup-soda (tapered walls under a lid line, bent straw from the lid centre).

Metric issues (burger-beside-drink-cup_metrics.json) and how they were handled:
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- stroke-count (7 > 6): now 4 strokes (top bun, bottom bun, cup with lid,
  straw); the separate middle seam and the double-walled lid are gone.
- keyshape-short-axis (HRECT_M, x fills 96%): widths rebuilt so the burger
  touches x=4 and the lid x=44 exactly. HRECT_L (second candidate, 1.17 vs
  1.21) is used instead of HRECT_M: two buns with >= 6 openings need 10 + 10
  and the gap between two arc-bearing contours needs 9 (an exact 8 comes back
  review), 29 > HRECT_M's 28-unit band. All four HRECT_L extremes are touched.
- clearance e0/e2, e0/e3, e1/e3 (straw vs lid rim, lid rim double wall):
  the lid is one line, the straw joins it at a shared split point and its tip
  stays 8 above the lid.
- clearance e1/e4, e2/e4, e2/e5, e2/e6, e3/e4 (burger vs cup): >= 8 gap
  between burger (x<=22) and cup (x>=30).
- clearance e4/e5, e5/e6 (bun layers 2.7-5.5 apart): the middle seam is
  dropped and the two buns sit 9 apart on centerlines.
- holes at (14.7,24.3) 4.0 and (8.0,35.9) 0.2: dome and bottom bun are each
  10 tall, giving 6 inscribed openings (re-measured with svg_metrics.py:
  6.0, 6.0 and 8.3 for the cup, no issues); the sliver is gone.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5d4383cc-7fa3-4af5-b119-dc3b67d08db0"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1915-burger-beside-drink-cup/burger-beside-drink-cup_raw.svg"
AUTHOR = "claude-opus-5-5"

# burger
BL, BR = 4, 22              # burger left / right
DOME_BASE, DOME_TOP = 21, 11
BUN_TOP, BUN_BOTTOM, BUN_R = 30, 40, 4
# cup
CL, CR = 30, 44             # lid ends
LID_Y, CUP_BOTTOM, TAPER = 16, 40, 3
AXIS = (CL + CR) // 2       # 37
STRAW_BEND_Y, STRAW_TIP = 12, (41, 8)


class BurgerBesideDrinkCupRedraw(Solo48):
    icon_id = "burger-beside-drink-cup-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("burger and soda", "fast food", "burger combo", "meal")
    keywords = ("burger", "hamburger", "drink", "cup", "soda", "straw", "fast food", "takeaway")

    def build(self) -> None:
        # Top bun: dome over a flat base.
        rx = (BR - BL) // 2
        self.add_arc("dome-arc", (BL, DOME_BASE), (BR, DOME_BASE),
                     radius_x=rx, radius_y=DOME_BASE - DOME_TOP, sweep=True)
        self.add_line("dome-base", (BR, DOME_BASE), (BL, DOME_BASE))
        self.add_contour("top-bun", "dome-arc", "dome-base", closed=True)

        # Bottom bun: flat top, rounded bottom corners.
        r, low = BUN_R, BUN_BOTTOM - BUN_R
        self.add_line("bun-top", (BL, BUN_TOP), (BR, BUN_TOP))
        self.add_line("bun-right", (BR, BUN_TOP), (BR, low))
        self.add_arc("bun-corner-r", (BR, low), (BR - r, BUN_BOTTOM), radius_x=r, sweep=True)
        self.add_line("bun-bottom", (BR - r, BUN_BOTTOM), (BL + r, BUN_BOTTOM))
        self.add_arc("bun-corner-l", (BL + r, BUN_BOTTOM), (BL, low), radius_x=r, sweep=True)
        self.add_line("bun-left", (BL, low), (BL, BUN_TOP))
        self.add_contour("bottom-bun", "bun-top", "bun-right", "bun-corner-r",
                         "bun-bottom", "bun-corner-l", "bun-left", closed=True)

        # Cup: lid split at the straw, tapered body.
        self.add_line("lid-left", (CL, LID_Y), (AXIS, LID_Y))
        self.add_line("lid-right", (AXIS, LID_Y), (CR, LID_Y))
        self.add_line("cup-right", (CR, LID_Y), (CR - TAPER, CUP_BOTTOM))
        self.add_line("cup-bottom", (CR - TAPER, CUP_BOTTOM), (CL + TAPER, CUP_BOTTOM))
        self.add_line("cup-left", (CL + TAPER, CUP_BOTTOM), (CL, LID_Y))
        self.add_contour("cup", "lid-left", "lid-right", "cup-right", "cup-bottom",
                         "cup-left", closed=True)

        self.add_polyline("straw", (AXIS, LID_Y), (AXIS, STRAW_BEND_Y), STRAW_TIP)
        self.relate("connect", "straw", "cup")
