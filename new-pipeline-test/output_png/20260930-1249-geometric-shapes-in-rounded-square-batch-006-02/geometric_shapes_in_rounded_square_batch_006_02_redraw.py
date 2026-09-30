"""geometric-shapes-in-rounded-square-batch-006-02 (redraw of the new-pipeline traced SVG).

Plan: a rounded-square frame holding a hollow circle in the upper-left and an
upright isosceles triangle in the lower-right. SQUARE, centerline box
(6,6)-(42,42).
- frame: four standalone straight walls on the box edges and four
  quarter arcs of radius R=6 at the corners (Lucide rect rx=2 proportion),
  each joined to its neighbours by `connect`;
  all four extremes sit exactly on the box.
- interior band: every inner part stays >= 8 from the walls, so straight
  inner extremes lie in 14..34 on both axes.
- circle: 4 cardinal quarter arcs, r=4 about (18,18); its left and top
  extremes are at 14 (8 from the walls).
- triangle: base (22,34)-(34,34) on y=34 (8 above the bottom wall), apex
  (28,25) on the base's axis x=28; the right vertex (34,34) is 8 from the
  right wall and 8.2 from the lower-right corner arc.
- circle to triangle: apex and left edge are 12.2 from the circle centre,
  i.e. 8.2 from the circle on centerlines.

Metric issues (geometric-shapes-in-rounded-square-batch-006-02_metrics.json):
- stroke-width (trace 2.77 after fit): fixed, stroke 4 throughout and every
  gap budgeted at 8 on centerlines.
- clearance e0/e1 (frame to circle 4.47): fixed, 8 (circle pulled in to
  x,y >= 14 and shrunk from the trace's ~r6 to r4).
- clearance e0/e2 (frame to triangle 4.07): fixed, 8 (triangle vertices
  kept inside 14..34).
- hole at the triangle (4.4 inscribed): fixed, the triangle's centerline
  incircle radius is 3.2 (inscribed diameter 6.4), and the circle's hole is
  8 on centerlines.
The circle is smaller relative to the triangle than in the generated image:
at stroke 4 inside a 36-unit frame, an r5 circle leaves no triangle that
both clears it by 8 and keeps a 6-wide hole.
Reference: Lucide `shapes` / `image` (rounded rect frame, circle + triangle).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "610733a3-dfd5-42df-9651-d396d039493b"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1249-geometric-shapes-in-rounded-square-batch-006-02/"
    "geometric-shapes-in-rounded-square-batch-006-02_raw.svg"
)
AUTHOR = "claude-opus-5-5"

LO, HI, R = 6, 42, 6                  # frame box and corner radius
CIRCLE_C, CIRCLE_R = (18, 18), 4
TRI_APEX, TRI_BASE_Y, TRI_HALF = (28, 25), 34, 6


class GeometricShapesInRoundedSquareRedraw(Solo48):
    icon_id = "geometric-shapes-in-rounded-square-batch-006-02-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shapes"
    aliases = ("shapes", "geometric shapes")
    keywords = ("shapes", "geometry", "circle", "triangle", "square", "frame")

    def build(self) -> None:
        # frame: walls and corner arcs, clockwise from the top wall
        pts = [
            ((LO + R, LO), (HI - R, LO)), ((HI, LO + R), (HI, HI - R)),
            ((HI - R, HI), (LO + R, HI)), ((LO, HI - R), (LO, LO + R)),
        ]
        # standalone members joined by `connect`, so rings exactly 8 inside certify
        for i, (a, b) in enumerate(pts):
            self.add_line(f"wall-{i + 1}", a, b)
            self.add_arc(f"corner-{i + 1}", b, pts[(i + 1) % 4][0], radius_x=R, sweep=True)
        for i in range(4):
            self.relate("connect", f"wall-{i + 1}", f"corner-{i + 1}")
            self.relate("connect", f"corner-{i + 1}", f"wall-{(i + 1) % 4 + 1}")

        cx, cy = CIRCLE_C
        r = CIRCLE_R
        ring = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
        for i, p in enumerate(ring):
            self.add_arc(f"circle-{i + 1}", p, ring[(i + 1) % 4], radius_x=r, sweep=True)
        self.add_contour("circle", "circle-1", "circle-2", "circle-3", "circle-4", closed=True)

        ax, _ = TRI_APEX
        self.add_polyline(
            "triangle", TRI_APEX, (ax + TRI_HALF, TRI_BASE_Y),
            (ax - TRI_HALF, TRI_BASE_Y), closed=True,
        )
