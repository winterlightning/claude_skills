"""All-terrain vehicle, front view (redraw of the new-pipeline traced SVG).

Subject: a quad bike seen head-on -- a U-shaped handlebar on top, a trapezoid
hood (narrow top, wide bottom) below it, and two upright tires on the outer
walls. No tread, grips or interior detail, as in the generated PNG.

Plan: SQUARE (centerline box (6,6)-(42,42)), mirrored about x=24.
- handlebar: one open contour -- grip lines at y=6 from the walls (x=6 / 42)
  to x=12 / 36, S-cubic risers dropping to y=10 (horizontal tangents at both
  ends), and a flat bar (18,10)-(30,10) that is also the hood's top edge.
- hood: open contour (30,10) -> (37,20) -> (11,20) -> (18,10) hung from the bar
  ends; relate("connect", handlebar, hood). Together they close a hole
  10 tall on centerlines (6 inscribed).
- tires: rounded rectangles 10 x 14 (x 6..16 and 32..42, y 28..42), r3
  corners, reaching the left, right and bottom box edges. The hood bottom is
  exactly 8 above the tire tops (straight-to-straight), so the hood may
  overhang the tires like fenders.
Lucide: no ATV/quad in the local set; the construction follows the
generated PNG. The side-view ATV modules already in solo/ were not useful.

Metric issues:
- stroke-width (trace 2.55 after fitting): fixed, redrawn at stroke 4 on the
  integer grid.
- keyshape-short-axis (HRECT_M, x fill 96%): resolved by using SQUARE instead.
  The stack needs 36 units of height: grips to bar 4, hood hole 10, gap 8,
  tires 14. HRECT_M gives only 28 and HRECT_L 32, which would squash the
  tires to a 10 x 10 square (or 6 tall with a separate handlebar). All four
  SQUARE extremes are touched exactly: grips at y=6, walls at x=6/42, tire
  bottoms at y=42.
- clearance e0-e1 (handlebar to hood, 2.78): fixed by joining the handlebar
  to the hood: the bar's bottom run is the hood's top edge (declared connect).
  A separate handlebar needs 8 more units of height, which no keyshape has.
- clearance e1-e2 / e1-e3 (hood to tires, 2.25 / 2.24): fixed. The hood now
  sits fully above the tires, exactly 8 above them.
- holes (hood 4.4, tires 3.6 inscribed): fixed. The hood hole is 10 tall and
  the tires are 10 wide on centerlines, so every hole is at least 6 inscribed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b4068396-30fc-5e9b-8eca-c9272d55decc"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1823-all-terrain-vehicle-batch-025-14/all-terrain-vehicle-batch-025-14_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
LEFT, RIGHT, TOP, BOTTOM = 6, 42, 6, 42   # SQUARE centerline box
GRIP_END = 12          # grips run LEFT..GRIP_END (mirrored)
HOOD_TOP = 10          # riser drop: grips at TOP, hood top edge (bar bottom) here
HOOD_TOP_HALF = 6      # hood top edge AXIS +- 5
HOOD_BOTTOM = 20
HOOD_BOTTOM_HALF = 13  # hood bottom edge AXIS +- 10
TIRE_W = 10
TIRE_TOP = 28
TIRE_R = 3


class AllTerrainVehicleBatch02514Redraw(Solo48):
    icon_id = "all-terrain-vehicle-batch-025-14-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport"
    aliases = ("atv", "quad bike", "four wheeler")
    keywords = ("all", "terrain", "vehicle", "atv", "quad", "off-road", "handlebar")

    def build(self) -> None:
        # handlebar: grips + S risers + flat bar whose bottom is the hood's top edge
        tl, tr = AXIS - HOOD_TOP_HALF, AXIS + HOOD_TOP_HALF
        mid_l = (GRIP_END + tl) / 2
        mid_r = 48 - mid_l
        self.add_line("grip-left", (LEFT, TOP), (GRIP_END, TOP))
        self.add_bezier("riser-left", (GRIP_END, TOP), ((mid_l, TOP), (mid_l, HOOD_TOP), (tl, HOOD_TOP)))
        self.add_line("bar", (tl, HOOD_TOP), (tr, HOOD_TOP))
        self.add_bezier("riser-right", (tr, HOOD_TOP), ((mid_r, HOOD_TOP), (mid_r, TOP), (48 - GRIP_END, TOP)))
        self.add_line("grip-right", (48 - GRIP_END, TOP), (RIGHT, TOP))
        self.add_contour("handlebar", "grip-left", "riser-left", "bar", "riser-right", "grip-right")

        # hood: trapezoid below the bar, wider at the bottom
        bl, br = AXIS - HOOD_BOTTOM_HALF, AXIS + HOOD_BOTTOM_HALF
        self.add_line("hood-right", (tr, HOOD_TOP), (br, HOOD_BOTTOM))
        self.add_line("hood-bottom", (br, HOOD_BOTTOM), (bl, HOOD_BOTTOM))
        self.add_line("hood-left", (bl, HOOD_BOTTOM), (tl, HOOD_TOP))
        self.add_contour("hood", "hood-right", "hood-bottom", "hood-left")
        self.relate("connect", "handlebar", "hood")

        # tires: mirrored rounded rectangles on the outer walls
        r = TIRE_R
        for name, x0 in (("tire-left", LEFT), ("tire-right", RIGHT - TIRE_W)):
            x1, y0, y1 = x0 + TIRE_W, TIRE_TOP, BOTTOM
            self.add_line(f"{name}-top", (x0 + r, y0), (x1 - r, y0))
            self.add_arc(f"{name}-tr", (x1 - r, y0), (x1, y0 + r), radius_x=r)
            self.add_line(f"{name}-right", (x1, y0 + r), (x1, y1 - r))
            self.add_arc(f"{name}-br", (x1, y1 - r), (x1 - r, y1), radius_x=r)
            self.add_line(f"{name}-bottom", (x1 - r, y1), (x0 + r, y1))
            self.add_arc(f"{name}-bl", (x0 + r, y1), (x0, y1 - r), radius_x=r)
            self.add_line(f"{name}-left", (x0, y1 - r), (x0, y0 + r))
            self.add_arc(f"{name}-tl", (x0, y0 + r), (x0 + r, y0), radius_x=r)
            self.add_contour(name, *(f"{name}-{p}" for p in ("top", "tr", "right", "br", "bottom", "bl", "left", "tl")), closed=True)
