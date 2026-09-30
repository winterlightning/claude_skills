"""domed-observatory (redraw of the new-pipeline traced SVG).

Plan: a domed observatory on HRECT_L (centerline box (4,8)-(44,40)), three
parts, as in the generated image:
- dome: two mirrored quarter circles of radius R=16 about the slit walls,
  left centre (20,24) from (4,24) up to (20,8), right centre (28,24) from
  (44,24) up to (28,8). Each half turns 90 degrees at its apex into a
  vertical slit wall that drops to the base top (y=24). The slit between
  x=20 and x=28 is the observing opening, open at the top.
- base: one closed contour, rectangle x 4..44, y 24..40, with the doorway
  cut into the bottom edge as a notch x 20..28, y 32..40. The top edge is
  split at x=20 and x=28 where the slit walls land.
The quarter arcs start on the base corners with a vertical tangent, so the
wall-to-dome silhouette is tangent-continuous on both sides, and the door
sits on the same axis as the slit (mirror axis x=24).
Extremes: x=4 / x=44 (base walls, dome feet), y=8 (dome apexes), y=40
(base bottom), so the HRECT_L fit is exact.
Clearances (centerlines): slit walls 8 apart; door walls 8 apart; door top
8 below the base top; slit walls and door walls are collinear but 8 apart
along y (24 -> 32).

Metric issues:
- stroke-width (info): redrawn at stroke 4, every gap budgeted at 8.
- stroke-count (warn, 9 strokes vs 6): fixed, 3 contours (two dome halves,
  one base).
- keyshape-short-axis (warn, x filled 93%): fixed. The dome feet and base
  walls sit on x=4 and x=44, so all four extremes are on the box.
- clearance e0/e6, e1/e6, e2/e6, e3/e6, e4/e6 (door top vs base top, 3.9):
  fixed, the door top is 8 below the base top line.
- clearance e1/e2, e3/e4, e1/e4, e2/e3, e1/e7, e2/e5, e3/e7, e4/e5 (slit
  6.7-7.8): fixed, the slit walls are 8 apart.
- clearance e1/e3, e2/e4 (0.53): trace artefact (each slit wall was traced
  twice, as an outline pair); rebuilt as one wall per side.
- e8 t-junction noise at the slit foot: the trace's extra slit-bottom stroke
  is dropped; the slit is closed by the base top line.
Lucide construction: no observatory in Lucide; the `warehouse` / `house`
style of a closed base outline with a notched doorway, and quarter-circle
arcs as in `umbrella`-type domes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "af83b2d3-a6c8-48f0-bf59-777e2e438dbf"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1200-domed-observatory/"
    "domed-observatory_raw.svg"
)
AUTHOR = "claude-opus-5-5"

X0, X1 = 4, 44          # HRECT_L centerline x extremes
TOP, BOTTOM = 8, 40     # HRECT_L centerline y extremes
AXIS = 24               # mirror axis
HALF = 4                # half slit / half door width (8 between walls)
EAVE = 24               # base top, dome feet
R = EAVE - TOP          # 16, dome quarter radius
DOOR_TOP = EAVE + 8     # 32


class DomedObservatoryRedraw(Solo48):
    icon_id = "domed-observatory-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/buildings"
    aliases = ("observatory", "astronomical observatory", "telescope dome")
    keywords = ("observatory", "dome", "astronomy", "telescope", "science",
                "building", "stars", "slit")

    def build(self) -> None:
        sl, sr = AXIS - HALF, AXIS + HALF      # slit / door walls, 20 and 28

        # dome: two quarter circles turning into the slit walls
        self.add_arc("dome-l-arc", (X0, EAVE), (sl, TOP), radius_x=R, sweep=True)
        self.add_line("dome-l-wall", (sl, TOP), (sl, EAVE))
        self.add_contour("dome-l", "dome-l-arc", "dome-l-wall")
        self.add_arc("dome-r-arc", (X1, EAVE), (sr, TOP), radius_x=R, sweep=False)
        self.add_line("dome-r-wall", (sr, TOP), (sr, EAVE))
        self.add_contour("dome-r", "dome-r-arc", "dome-r-wall")

        # base: rectangle with the doorway notched into the bottom edge
        self.add_polyline(
            "base",
            (X0, EAVE), (sl, EAVE), (sr, EAVE), (X1, EAVE),
            (X1, BOTTOM), (sr, BOTTOM), (sr, DOOR_TOP),
            (sl, DOOR_TOP), (sl, BOTTOM), (X0, BOTTOM),
            closed=True,
        )
        self.relate("connect", "dome-l", "base")
        self.relate("connect", "dome-r", "base")
