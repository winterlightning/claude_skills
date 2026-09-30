"""dollar: the US dollar currency sign, an S crossed by one vertical stroke
(redraw of the new-pipeline traced SVG).

Plan: VRECT_M (centerline box (10,4)-(38,44)), point-symmetric about (24,24)
(every S point p has a partner 48-p), Lucide `dollar-sign` construction.
- S: one open contour. Top bar (36,10)->(17,10), left bowl = semicircle r=7
  about (17,17) to (17,24), straight middle bar (17,24)->(31,24), right bowl
  = semicircle r=7 about (31,31) to (31,38), bottom bar (31,38)->(12,38).
  Bars leave each bowl on its tangent, so every join is smooth. The bowls
  put the S extremes on x=10 and x=38.
- stem: one vertical polyline x=24 from y=4 to y=44 with vertices at y=10,
  24 and 38, where the S bars (split at x=24) share the same vertices; the
  crossings are square (perpendicular) and declared with `connect`.

Keyshape: VRECT_M as suggested; the stem ends sit on y=4/44 and the bowls on
x=10/38, so all four extremes are exact.

Metric issues fixed by the rebuild:
- keyshape-short-axis (x fill 67%): the S now spans the full 28-wide box
  (x 10..38) instead of stretching the trace.
- clearance e0/e1 (0.03, S and stem overlapping): the stem and S cross at
  shared vertices (24,10), (24,24), (24,38) and the contact is declared, so
  there is no unrelated near-touch left.
- hole at (19.3,16.3) (5.2) and hole at (28.5,31.4) (5.4): the stem splits
  each bowl into a 7x14 centerline cell (e.g. x 17..24 plus the r=7 bowl,
  y 10..24), which is well over 6 inscribed at stroke 4; the other halves
  open to the side.
- stroke-width (2.67): drawn at the profile stroke 4, gaps budgeted for it.
Not kept, with reason:
- the trace's diagonal S spine: a diagonal crossing the stem makes acute
  wedges at (24,24) and tighter holes; the horizontal Lucide middle bar
  crosses square and reads the same at 48 px.
- curled tips: the tips end as straight bars (Lucide), 2 short of the
  opposite extremes so the S stays inside the box.
Lucide: `dollar-sign` (stem + bar/semicircle S) informed the construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2c47b147-c2f7-4c49-8513-824a167aa784"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1158-dollar/dollar_raw.svg"
AUTHOR = "claude-opus-5-5"

CX = 24                    # stem x and symmetry centre (24,24)
STEM = (4, 44)             # stem ends on the VRECT_M box
R = 7                      # bowl radius
TOP_Y = 10                 # top bar; bottom bar at 48 - TOP_Y
BOWL_X = 17                # left bowl centre x; right bowl at 48 - BOWL_X
TIP_X = 36                 # top tip; bottom tip at 48 - TIP_X


def flip(p: tuple[int, int]) -> tuple[int, int]:
    return (48 - p[0], 48 - p[1])


class DollarRedraw(Solo48):
    icon_id = "dollar-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "money"
    aliases = ("dollar sign", "usd", "currency dollar")
    keywords = ("dollar", "currency", "money", "usd", "price", "payment", "finance")

    def build(self) -> None:
        tip = (TIP_X, TOP_Y)
        top_cross = (CX, TOP_Y)
        bowl_top = (BOWL_X, TOP_Y)
        bowl_end = (BOWL_X, CX)
        mid = (CX, CX)
        self.add_line("s-top-1", tip, top_cross)
        self.add_line("s-top-2", top_cross, bowl_top)
        self.add_arc("s-bowl-left", bowl_top, bowl_end, radius_x=R, sweep=False)
        self.add_line("s-mid-1", bowl_end, mid)
        self.add_line("s-mid-2", mid, flip(bowl_end))
        self.add_arc("s-bowl-right", flip(bowl_end), flip(bowl_top), radius_x=R, sweep=True)
        self.add_line("s-bottom-1", flip(bowl_top), flip(top_cross))
        self.add_line("s-bottom-2", flip(top_cross), flip(tip))
        self.add_contour(
            "s", "s-top-1", "s-top-2", "s-bowl-left", "s-mid-1", "s-mid-2",
            "s-bowl-right", "s-bottom-1", "s-bottom-2",
        )

        self.add_polyline(
            "stem", (CX, STEM[0]), top_cross, mid, flip(top_cross), (CX, STEM[1]),
        )
        self.relate("connect", "s", "stem")
