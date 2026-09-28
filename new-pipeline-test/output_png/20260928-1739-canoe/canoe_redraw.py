"""canoe (redraw of the new-pipeline traced SVG).

Subject: an open canoe seen from the side: a long shallow hull with pointed,
raised bow and stern, an open top rim (gunwale) and two seat bars inside.

Plan: HRECT_M (centerline box (4,10)-(44,38)), the metrics' suggested
keyshape and the flattest SOLO48 rectangle. Mirrored about x=24.
- hull, one closed contour: the tips (8,10)/(40,10) are the top extremes;
  the outer curve bows out to a vertical tangent at x=4/44 (y=26) and rounds
  into the flat keel y=38 (x 15-33) with horizontal tangents; the gunwale
  falls from each tip in a concave curve that lands horizontally on the rim
  line y=28 (x 18-30). The tips are deliberate corners.
- seats: two splayed bars from the rim (18,28)/(30,28) down to the keel
  ends (15,38)/(33,38), sharing endpoints with the hull (scoped connects).
Proportions: HRECT_M forces a 40x28 centerline box on a 3:1 subject. The
extra height goes into the raised ends (tip rise 18) while the hull stays
shallow (10 deep) with a long keel, so it reads as a boat, not a bowl.
Tried and rejected: a 14-deep hull (read as a bowl) and tips pushed out to
x=6 (gunwale and stem closer than 4 ink near the tips: internal-spacing).
Lucide: no canoe in Lucide; construction follows its "sailboat"/"ship"
hull idea (one closed hull outline, flat keel, rounded bilge).

Metric issues fixed:
- hole x3 (3.61, 3.61, 3.4 inscribed): the hull is 10 deep between rim and
  keel centerlines with the seats 12 apart at the rim, so all three bays
  open to >= 6 inscribed ink (build gate: no hole findings).
- keyshape-short-axis (y 48%): all four HRECT_M extremes are exact
  (tips y=10, keel y=38, bilge x=4/44).
- stroke-width (2.67 trace): redrawn at stroke 4 with gaps budgeted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2f08daf6-071b-5ac7-9717-2239ffbb2925"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1739-canoe/canoe_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
TIP_X, TIP_Y = 8, 10          # left tip; right tip mirrors
BILGE_X, BILGE_Y = 4, 26      # outer vertical tangent
KEEL_Y, KEEL_X = 38, 15       # flat keel from 15 to 33
RIM_Y, RIM_X = 28, 18         # rim line from 18 to 30


def mx(x: float) -> float:
    return 2 * AXIS - x


class CanoeRedraw(Solo48):
    icon_id = "canoe-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/water"
    aliases = ("canoe", "kayak", "rowboat")
    keywords = ("canoe", "boat", "paddle", "river", "lake", "water", "camping", "outdoor")

    def build(self) -> None:
        self.add_bezier(
            "outer-l", (TIP_X, TIP_Y),
            ((5, 15), (BILGE_X, 21), (BILGE_X, BILGE_Y)),
            ((BILGE_X, 33), (8, KEEL_Y), (KEEL_X, KEEL_Y)),
        )
        self.add_line("keel", (KEEL_X, KEEL_Y), (mx(KEEL_X), KEEL_Y))
        self.add_bezier(
            "outer-r", (mx(KEEL_X), KEEL_Y),
            ((mx(8), KEEL_Y), (mx(BILGE_X), 33), (mx(BILGE_X), BILGE_Y)),
            ((mx(BILGE_X), 21), (mx(5), 15), (mx(TIP_X), TIP_Y)),
        )
        self.add_bezier(
            "rim-r", (mx(TIP_X), TIP_Y),
            ((mx(10), 21), (mx(12), RIM_Y), (mx(RIM_X), RIM_Y)),
        )
        self.add_line("rim", (mx(RIM_X), RIM_Y), (RIM_X, RIM_Y))
        self.add_bezier(
            "rim-l", (RIM_X, RIM_Y),
            ((12, RIM_Y), (10, 21), (TIP_X, TIP_Y)),
        )
        self.add_contour("hull", "outer-l", "keel", "outer-r", "rim-r", "rim", "rim-l", closed=True)

        self.add_line("seat-l", (RIM_X, RIM_Y), (KEEL_X, KEEL_Y))
        self.add_line("seat-r", (mx(RIM_X), RIM_Y), (mx(KEEL_X), KEEL_Y))
        self.relate("connect", "seat-l", "hull")
        self.relate("connect", "seat-r", "hull")
