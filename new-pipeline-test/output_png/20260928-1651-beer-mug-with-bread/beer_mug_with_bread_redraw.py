"""beer mug with bread (redraw of the new-pipeline traced SVG).

Plan: HRECT_M (centerline box (4,10)-(44,38)), as suggested. The 40-unit
width is the whole budget: bread 12 + gap 8 + mug 12 + handle 8. Handle
after Lucide `beer` (straight arms into a rounded loop); the foam is the mug
outline's own scalloped top instead of Lucide's overlapping cloud, which
would crowd a 12-wide mug and the bread beside it.
- bread: one closed contour. Walls x=5 and x=15 on y=38 with radius-2
  bottom corners; the crust is a mirrored Bezier toast top (squared by
  CRUST_ROUND) that swells one unit past each wall, knots with vertical
  tangents on the x=4 extreme and x=16, crown at (10,20). The inward lip
  where crust meets wall is the slice's crust notch from the image.
- mug: one closed contour. Walls x=24 and x=36 on y=38 (radius-2 corners);
  the foam top is two radius-3 bumps about (27,13) and (33,13) whose apexes
  are the y=10 extreme.
- foam line: y=FOAM_Y (23) across the mug, splitting foam from beer; it
  shares its right node with the handle's top arm.
- handle: arm (36,23)->(40,23), radius-4 bend to the grip x=44 (the x=44
  extreme), radius-4 bend and arm back to (36,33).
Metric issues:
- stroke-width (trace 2.4): redrawn at stroke 4 on the integer grid.
- keyshape-short-axis (y filled 85%): fixed; foam apexes on y=10, both
  bases on y=38, crust swell on x=4, handle grip on x=44.
- clearance e0-e2 (foam vs handle 2.13): fixed; the foam stays inside the
  mug walls and the handle hangs below the foam line.
- clearance e0-e3 / e1-e3 (bread vs foam 6.12, bread vs mug 4.48): fixed;
  bread's widest point x=16 is 8 from the mug wall x=24.
- holes at (30.2,15.5) / (25.4,15.9) (foam bubbles 2.84 / 1.28): fixed by
  dropping the separate foam cloud; the foam band now holds a 6.1 ink
  circle (FOAM_Y is 10 below the bump cusps, not the bare 8).
- hole at (40.5,25.8) (handle 2.8): improved to 4.0 ink (8x10 on
  centerlines), not to 6. A 6-ink handle needs a 10-unit span; taking the
  2 units from the bread or the mug was tried (bread 10 / mug 12 / handle
  10 passed every metric) but at 48 px the 8-wide bread body read as a
  keyhole, so the handle keeps 8. Validator and build gate both pass it.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f7b3cdc5-a4f3-4160-a8d1-71f476dc0fda"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1651-beer-mug-with-bread/beer-mug-with-bread_raw.svg"
AUTHOR = "claude-opus-5-5"

BASE_Y = 38
CORNER_R = 2

BREAD_L, BREAD_R = 5, 15
BREAD_MID = (BREAD_L + BREAD_R) // 2
BREAD_SWELL = 1
BREAD_SHOULDER_Y = 29
BREAD_WIDE_Y = 25
BREAD_TOP = 20
CRUST_ROUND = 0.72  # > 0.5523 squares the crust towards a toast top

MUG_L, MUG_R = 24, 36
BUMP_R = 3
FOAM_TOP = 10
CUSP_Y = FOAM_TOP + BUMP_R
FOAM_Y = CUSP_Y + 10

HANDLE_R = 4
HANDLE_ARM = 4
HANDLE_TOP = FOAM_Y
HANDLE_BOTTOM = HANDLE_TOP + 10


class BeerMugWithBreadRedraw(Solo48):
    icon_id = "beer-mug-with-bread-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/drink"
    aliases = ("beer and bread", "pub food", "beer mug and toast")
    keywords = ("beer", "mug", "bread", "toast", "pub", "bar", "food", "drink", "foam")

    def build(self) -> None:
        self._bread()
        self._mug()
        self._handle()

    def _bread(self) -> None:
        l, r, m = BREAD_L, BREAD_R, BREAD_MID
        wl, wr = l - BREAD_SWELL, r + BREAD_SWELL
        half = m - wl
        k = CRUST_ROUND * half
        self.add_line("bread-wall-r", (r, BREAD_SHOULDER_Y), (r, BASE_Y - CORNER_R))
        self.add_arc("bread-corner-r", (r, BASE_Y - CORNER_R), (r - CORNER_R, BASE_Y),
                     radius_x=CORNER_R, sweep=True)
        self.add_line("bread-base", (r - CORNER_R, BASE_Y), (l + CORNER_R, BASE_Y))
        self.add_arc("bread-corner-l", (l + CORNER_R, BASE_Y), (l, BASE_Y - CORNER_R),
                     radius_x=CORNER_R, sweep=True)
        self.add_line("bread-wall-l", (l, BASE_Y - CORNER_R), (l, BREAD_SHOULDER_Y))
        lip = BREAD_SHOULDER_Y - BREAD_WIDE_Y
        rise = BREAD_WIDE_Y - BREAD_TOP
        ky = CRUST_ROUND * rise
        self.add_bezier(
            "bread-crust", (l, BREAD_SHOULDER_Y),
            ((l, BREAD_SHOULDER_Y - lip * 0.4), (wl, BREAD_WIDE_Y + lip * 0.4), (wl, BREAD_WIDE_Y)),
            ((wl, BREAD_WIDE_Y - ky), (m - k, BREAD_TOP), (m, BREAD_TOP)),
            ((m + k, BREAD_TOP), (wr, BREAD_WIDE_Y - ky), (wr, BREAD_WIDE_Y)),
            ((wr, BREAD_WIDE_Y + lip * 0.4), (r, BREAD_SHOULDER_Y - lip * 0.4), (r, BREAD_SHOULDER_Y)),
        )
        self.add_contour("bread", "bread-wall-r", "bread-corner-r", "bread-base",
                         "bread-corner-l", "bread-wall-l", "bread-crust", closed=True)

    def _mug(self) -> None:
        l, r = MUG_L, MUG_R
        mid = (l + r) // 2
        self.add_line("mug-wall-l", (l, FOAM_Y), (l, BASE_Y - CORNER_R))
        self.add_arc("mug-corner-l", (l, BASE_Y - CORNER_R), (l + CORNER_R, BASE_Y),
                     radius_x=CORNER_R, sweep=False)
        self.add_line("mug-base", (l + CORNER_R, BASE_Y), (r - CORNER_R, BASE_Y))
        self.add_arc("mug-corner-r", (r - CORNER_R, BASE_Y), (r, BASE_Y - CORNER_R),
                     radius_x=CORNER_R, sweep=False)
        self.add_line("mug-wall-r-low", (r, BASE_Y - CORNER_R), (r, HANDLE_BOTTOM))
        self.add_line("mug-wall-r-mid", (r, HANDLE_BOTTOM), (r, FOAM_Y))
        self.add_line("mug-wall-r-up", (r, FOAM_Y), (r, CUSP_Y))
        self.add_arc("foam-bump-r", (r, CUSP_Y), (mid, CUSP_Y), radius_x=BUMP_R, sweep=False)
        self.add_arc("foam-bump-l", (mid, CUSP_Y), (l, CUSP_Y), radius_x=BUMP_R, sweep=False)
        self.add_line("mug-wall-l-up", (l, CUSP_Y), (l, FOAM_Y))
        self.add_contour("mug", "mug-wall-l", "mug-corner-l", "mug-base", "mug-corner-r",
                         "mug-wall-r-low", "mug-wall-r-mid", "mug-wall-r-up", "foam-bump-r",
                         "foam-bump-l", "mug-wall-l-up", closed=True)
        self.add_line("foam-line", (l, FOAM_Y), (r, FOAM_Y))
        self.relate("connect", "foam-line", "mug")

    def _handle(self) -> None:
        x0, x1 = MUG_R, MUG_R + HANDLE_ARM
        x2 = x1 + HANDLE_R
        self.add_line("handle-top", (x0, HANDLE_TOP), (x1, HANDLE_TOP))
        self.add_arc("handle-bend-t", (x1, HANDLE_TOP), (x2, HANDLE_TOP + HANDLE_R),
                     radius_x=HANDLE_R, sweep=True)
        self.add_line("handle-grip", (x2, HANDLE_TOP + HANDLE_R), (x2, HANDLE_BOTTOM - HANDLE_R))
        self.add_arc("handle-bend-b", (x2, HANDLE_BOTTOM - HANDLE_R), (x1, HANDLE_BOTTOM),
                     radius_x=HANDLE_R, sweep=True)
        self.add_line("handle-bottom", (x1, HANDLE_BOTTOM), (x0, HANDLE_BOTTOM))
        self.add_contour("handle", "handle-top", "handle-bend-t", "handle-grip",
                         "handle-bend-b", "handle-bottom")
        self.relate("connect", "handle", "mug")
