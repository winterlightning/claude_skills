"""euro financial document: an upright page with a clipped top-right corner
and a Euro sign on it (redraw of the new-pipeline traced SVG).

Plan: VRECT_L (centerline box (8,4)-(40,44)), euro sign mirrored about y=24.
- page: one closed contour on the four box extremes, r=4 rounded corners,
  top-right corner clipped by a 45-degree cut (32,4)-(40,12).
- euro C: one contour of two cubics joined by a straight spine at x=20
  (y 20..28); the cubics leave the spine with a vertical tangent, crown at
  about y=13 and end at tips (31,16)/(31,32), so the C is 9 from the right
  wall and >= 9 from the corner cut and the page top/bottom.
- bars: two collinear polylines at y=20 and y=28 (exactly 8 apart), from
  x=17 through the spine to x=26; each shares its spine vertex with the C and
  is declared with `connect`. The 3-unit stub left of the spine carries the
  Euro identity.

Keyshape: VRECT_L instead of the suggested VRECT_M. VRECT_M's 28-wide box
leaves only 12 between the page walls (8 each side) for a stub + C + tip,
too narrow for a readable Euro; VRECT_L gives 16 (the camera-image-file
redraw hit the same budget).

Metric issues fixed by the rebuild:
- clearance e0/e3, e0/e4 (page vs bars, 5.75): bar stubs sit 9 from the left
  wall (8 was `review` against the rounded page contour).
- clearance e0/e5 (page vs C, 7.33): C tips 9 from the right wall.
- clearance e2/e5 (fold vs C, 5.85): the fold lines are gone; the C tip is
  9.2 from the corner cut.
- clearance e3/e4 (bar vs bar, 3.53): bars are 8 apart on centerlines.
- clearance e3/e5, e4/e5 (bars crossing the C, 0.0): the bars now meet the C
  at shared vertices on its spine and the contact is declared (`connect`).
- hole at (32.3,10.7) (1.13, the fold-flap triangle): the flap is removed;
  the corner is a plain clipped cut.
- keyshape-short-axis (y 96%): page edges sit on x 8/40 and y 4/44, exact.
- stroke-width (2.55): drawn at the profile stroke 4, gaps budgeted for it.
Not kept, with reason:
- the folded flap (inner L under the cut): a right-isosceles flap needs legs
  >= 17 to hold a 6-unit hole at stroke 4, which would eat the page top.
- round C (circle arc): with bars 8 apart a circular C wide enough to clear
  the bars would exceed the 16-wide interior band; the C is a tall cubic
  with a short straight spine instead.
Lucide: `file` (page + clipped corner) and `euro` (C with two left-protruding
bars) informed the construction; the bars are shortened so their ends stay
clear of the crown at stroke 4. A square-corner variant with 4-unit stubs
also passed; the rounded page was kept because it matches the image.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "36b5ce8c-0ffe-4bbc-9abc-5d99e806b0d9"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1152-euro-financial-document-solo/euro-financial-document-solo_raw.svg"
AUTHOR = "claude-opus-5-5"

MID_Y = 24                 # euro sign mirrored about y=24
PAGE = (8, 4, 40, 44)      # centerline box, VRECT_L
CUT = 8                    # clipped corner leg
CORNER = 4                 # rounded page corners
STUB_X = 17                # bar left ends, 9 in from the left wall
SPINE_X = 20               # straight left side of the C
BAR_DY = 4                 # bars at y=20 and y=28, 8 apart
BAR_END_X = 26
TIP = (31, 16)             # upper tip; 9 from the right wall
TIP_CTRL = (28, 12)        # tip leaves up-left, toward the crown
SPINE_CTRL = (20, 12)      # C reaches the spine with a vertical tangent


def mirror(point: tuple[float, float]) -> tuple[float, float]:
    return (point[0], 2 * MID_Y - point[1])


class EuroFinancialDocumentSoloRedraw(Solo48):
    icon_id = "euro-financial-document-solo-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/file"
    aliases = ("euro document", "euro invoice", "euro bill")
    keywords = ("euro", "currency", "document", "invoice", "bill", "finance", "file")

    def build(self) -> None:
        x0, y0, x1, y1 = PAGE
        r = CORNER
        self.add_line("page-top", (x0 + r, y0), (x1 - CUT, y0))
        self.add_line("page-cut", (x1 - CUT, y0), (x1, y0 + CUT))
        self.add_line("page-right", (x1, y0 + CUT), (x1, y1 - r))
        self.add_arc("page-br", (x1, y1 - r), (x1 - r, y1), radius_x=r)
        self.add_line("page-bottom", (x1 - r, y1), (x0 + r, y1))
        self.add_arc("page-bl", (x0 + r, y1), (x0, y1 - r), radius_x=r)
        self.add_line("page-left", (x0, y1 - r), (x0, y0 + r))
        self.add_arc("page-tl", (x0, y0 + r), (x0 + r, y0), radius_x=r)
        self.add_contour(
            "page", "page-top", "page-cut", "page-right", "page-br", "page-bottom",
            "page-bl", "page-left", "page-tl", closed=True,
        )

        top = (SPINE_X, MID_Y - BAR_DY)
        bottom = mirror(top)
        self.add_bezier("euro-upper", TIP, (TIP_CTRL, SPINE_CTRL, top))
        self.add_line("euro-spine", top, bottom)
        self.add_bezier("euro-lower", bottom, (mirror(SPINE_CTRL), mirror(TIP_CTRL), mirror(TIP)))
        self.add_contour("euro", "euro-upper", "euro-spine", "euro-lower")

        for name, y in (("bar-top", MID_Y - BAR_DY), ("bar-bottom", MID_Y + BAR_DY)):
            self.add_polyline(name, (STUB_X, y), (SPINE_X, y), (BAR_END_X, y))
            self.relate("connect", "euro", name)
