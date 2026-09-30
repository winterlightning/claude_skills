"""croissant and coffee (redraw of the new-pipeline traced SVG).

Plan: HRECT_M (centerline box (4,10)-(44,38)), as suggested. The generated
image puts the croissant and cup side by side at 3:1; HRECT_M needs every
extreme on its 40x28 box, so side by side would need a 2.13 stretch on y.
Instead the croissant sits in front of the cup's lower left (the usual
breakfast still life): the cup reaches the top and right edges, the
croissant the left and bottom edges.
- croissant: one closed contour, mirrored about x=CROISSANT_X (18). The
  outer crust is a smooth dome over a flat top (15,21)-(21,21), widest at
  x=4 and x=32 on y=31, curling into pointed tips at (8,38) and (28,38).
  The inner edge is a shallow arch, flat at y=34 between the seams. Each tip
  is a shared node, so the converging edges there are exempt from internal
  spacing.
- seams: two straight segment lines (12,23)-(15,34) and (24,23)-(21,34),
  mirrored and joined to split nodes on the crust and the arch. They cut the
  band into the image's three cells.
- cup: one open contour behind the croissant. Rim y=10 from x=15 to x=34;
  the left wall drops onto the croissant's flat-top node (15,21); the right
  wall ends in a radius-3 corner on the crust node (31,28). The croissant
  hides the rest of the cup's base.
- handle: C-shaped, arms 5 from the wall at y=13 and y=23 and a radius-5
  bend about (39,18) whose apex is the x=44 extreme.
Lucide `croissant` (segmented crescent) informed the seam cells and `coffee`
the rim and loop handle. Lucide's diagonal croissant was not used; the
image's front view was kept.
Metric issues:
- stroke-width (trace 2.64 fitted): redrawn at stroke 4 on the integer grid.
- keyshape-short-axis (y filled 47%): fixed by the overlapping composition.
  Rim on y=10, croissant tips on y=38, croissant side on x=4, handle on x=44.
- clearance e0-e3 (croissant vs cup 2.53): fixed. They meet on shared nodes
  (15,21) and (31,28) and are declared connected.
- holes at (13.7,21.4) 4.2, (7.3,24.2) 1.7 and (20.1,24.2) 1.7: fixed. The
  traced tip curls that made the pinholes are gone. svg_metrics on the
  redraw measures every cell at 5.9-9.6 ink with no hole issue, including
  the handle (5.92; 6 in geometry, the rest is raster rounding).
- clearance e1-e2 (seam vs seam 6.31) and e1-e3 (seam vs cup 5.88): not
  fixed to 8. On the redraw, svg_metrics reports seam ends 6 apart on the
  arch, the left seam node 3.6 from the cup-wall node and the handle 5.4
  from the crust. All are parts joined through the same connected drawing,
  and the build gate's internal-spacing check (not parallel within 30 deg)
  passes them. Moving the seams 8 apart shrank the side cells to 4.9 ink,
  and moving the cup wall off the flat top would narrow the cup, so the
  holes were kept.
Validation: validate_icon() valid, build_gate.py PASS, 0 warnings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "15142e4e-b0bd-491b-8e9e-d5620b4c6f6c"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1053-croissant-and-coffee/croissant-and-coffee_raw.svg"
AUTHOR = "claude-opus-5-5"

CROISSANT_X = 18
CROISSANT_TOP = 21
CROISSANT_SIDE = 14       # half width: x=4 and x=32
CROISSANT_WIDE_Y = 31
TIP_Y = 38
TIP_IN = 10               # tip x offset from the axis: (8,38) and (28,38)
FLAT_HALF = 3             # flat top (15,21)-(21,21)
SEAM_OUT = (6, 23)        # outer seam node offset from the axis
SEAM_IN = (3, 34)         # inner seam node offset
ARCH_TOP = 34
CUP_KNOT = (13, 28)       # crust node the cup's bottom corner lands on

CUP_L, CUP_R = CROISSANT_X - FLAT_HALF, 34
RIM_Y = 10
CUP_CORNER = CUP_R - (CROISSANT_X + CUP_KNOT[0])
HANDLE_TOP, HANDLE_BOTTOM = 13, 23
HANDLE_R = (HANDLE_BOTTOM - HANDLE_TOP) // 2
HANDLE_ARM = 5


def _hermite(knots):
    """Cubic segments through integer knots with given unit-ish tangents."""
    segs = []
    for (p0, t0), (p1, t1) in zip(knots, knots[1:]):
        d = ((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2) ** 0.5 / 3
        n0 = (t0[0] ** 2 + t0[1] ** 2) ** 0.5
        n1 = (t1[0] ** 2 + t1[1] ** 2) ** 0.5
        c1 = (p0[0] + t0[0] / n0 * d, p0[1] + t0[1] / n0 * d)
        c2 = (p1[0] - t1[0] / n1 * d, p1[1] - t1[1] / n1 * d)
        segs.append((c1, c2, p1))
    return segs


class CroissantAndCoffeeRedraw(Solo48):
    icon_id = "croissant-and-coffee-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/drink"
    aliases = ("coffee and croissant", "breakfast", "cafe breakfast")
    keywords = ("croissant", "coffee", "cup", "breakfast", "bakery", "cafe", "pastry", "food", "morning")

    def build(self) -> None:
        self._croissant()
        self._cup()
        self._handle()

    def _croissant(self) -> None:
        cx = CROISSANT_X
        mx = lambda dx, y: (cx + dx, y)  # noqa: E731
        tip_l, tip_r = mx(-TIP_IN, TIP_Y), mx(TIP_IN, TIP_Y)
        side_l, side_r = mx(-CROISSANT_SIDE, CROISSANT_WIDE_Y), mx(CROISSANT_SIDE, CROISSANT_WIDE_Y)
        so_l, so_r = mx(-SEAM_OUT[0], SEAM_OUT[1]), mx(SEAM_OUT[0], SEAM_OUT[1])
        si_l, si_r = mx(-SEAM_IN[0], SEAM_IN[1]), mx(SEAM_IN[0], SEAM_IN[1])
        flat_l, flat_r = mx(-FLAT_HALF, CROISSANT_TOP), mx(FLAT_HALF, CROISSANT_TOP)
        apex = mx(0, ARCH_TOP)
        knot_l, knot_r = mx(-CUP_KNOT[0], CUP_KNOT[1]), mx(CUP_KNOT[0], CUP_KNOT[1])
        KNOT_T = (0.45, 1)
        SEAM_T_L, SEAM_T_R = (1, -0.8), (1, 0.8)
        # outer crust, left tip -> over the top -> right tip (mirrored tangents)
        self.add_bezier("crust-l", tip_l, *_hermite([
            (tip_l, (-1, -2)), (side_l, (0, -1)), (knot_l, (KNOT_T[0], -KNOT_T[1])),
            (so_l, SEAM_T_L)]))
        self.add_bezier("crust-tl", so_l, *_hermite([(so_l, SEAM_T_L), (flat_l, (1, 0))]))
        self.add_line("crust-top", flat_l, flat_r)
        self.add_bezier("crust-tr", flat_r, *_hermite([(flat_r, (1, 0)), (so_r, SEAM_T_R)]))
        self.add_bezier("crust-r-up", so_r, *_hermite([(so_r, SEAM_T_R), (knot_r, KNOT_T)]))
        self.add_bezier("crust-r", knot_r, *_hermite([
            (knot_r, KNOT_T), (side_r, (0, 1)), (tip_r, (-1, 2))]))
        # inner arch, right tip -> left tip
        self.add_bezier("arch-r", tip_r, *_hermite([(tip_r, (-1, -0.7)), (si_r, (-1, -0.1))]))
        self.add_bezier("arch-top", si_r, *_hermite([(si_r, (-1, -0.1)), (apex, (-1, 0)), (si_l, (-1, 0.1))]))
        self.add_bezier("arch-l", si_l, *_hermite([(si_l, (-1, 0.1)), (tip_l, (-1, 0.7))]))
        self.add_contour("croissant", "crust-l", "crust-tl", "crust-top", "crust-tr", "crust-r-up", "crust-r",
                         "arch-r", "arch-top", "arch-l", closed=True)
        self.add_line("seam-l", so_l, si_l)
        self.add_line("seam-r", so_r, si_r)
        self.relate("connect", "seam-l", "croissant")
        self.relate("connect", "seam-r", "croissant")

    def _cup(self) -> None:
        l, r = CUP_L, CUP_R
        bottom = CUP_KNOT[1]
        self.add_line("cup-wall-l", (l, CROISSANT_TOP), (l, RIM_Y))
        self.add_line("cup-rim", (l, RIM_Y), (r, RIM_Y))
        self.add_line("cup-wall-r-up", (r, RIM_Y), (r, HANDLE_TOP))
        self.add_line("cup-wall-r-mid", (r, HANDLE_TOP), (r, HANDLE_BOTTOM))
        self.add_line("cup-wall-r-low", (r, HANDLE_BOTTOM), (r, bottom - CUP_CORNER))
        self.add_arc("cup-corner", (r, bottom - CUP_CORNER), (r - CUP_CORNER, bottom),
                     radius_x=CUP_CORNER, sweep=True)
        self.add_contour("cup", "cup-wall-l", "cup-rim", "cup-wall-r-up", "cup-wall-r-mid",
                         "cup-wall-r-low", "cup-corner")
        self.relate("connect", "cup", "croissant")

    def _handle(self) -> None:
        x0, x1 = CUP_R, CUP_R + HANDLE_ARM
        self.add_line("handle-top", (x0, HANDLE_TOP), (x1, HANDLE_TOP))
        self.add_arc("handle-bend", (x1, HANDLE_TOP), (x1, HANDLE_BOTTOM),
                     radius_x=HANDLE_R, sweep=True)
        self.add_line("handle-bottom", (x1, HANDLE_BOTTOM), (x0, HANDLE_BOTTOM))
        self.add_contour("handle", "handle-top", "handle-bend", "handle-bottom")
        self.relate("connect", "handle", "cup")
