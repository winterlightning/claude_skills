"""calendar number seven (redraw of the new-pipeline traced SVG).

Plan: a rounded calendar page with two binding tabs and the numeral 7,
VRECT_L keyshape (centerline box (8,4)-(40,44)), page mirrored about x=24.
- page: closed rounded rectangle x 8..40, y 8..44, corner radius 4; the
  top edge is split at x=16 and x=32 where the bindings cross it.
- bindings: two vertical tabs x=16 / x=32, y 4..12, each split at y=8 on
  the page's top edge; the shared endpoints are declared as contact. The
  tab tops are the y=4 extreme, the page bottom the y=44 extreme and the
  walls the x=8 / x=40 extremes, so the keyshape fit is exact.
- seven: the typeface v2 glyph `digit-7` (icon_set/typeface/glyphs-v2.json,
  centerline bar 7.4 wide, diagonal 5.5 across over 15 down) translated so
  its bar sits on y=20 (8 below the tab ends) and its foot on y=35 (9 above
  the page bottom). SOLO48 nodes must be integers, so its nodes are snapped
  to the nearest grid form: bar (20,20)-(28,20), diagonal to (22,35); the
  glyph's sub-unit corner cubic becomes the round join. The bar centre is
  x=24, the page axis.
Nothing is copied from the trace coordinates.

Metric issues:
- error `clearance` e1/e2, e1/e3 (page vs bindings 0.1 apart): fixed; the
  tabs deliberately cross the page top, so they share the (16,8) / (32,8)
  endpoints and the contact is declared instead of being a near miss.
- error `clearance` e1/e4 (page bottom vs seven 4.85): fixed, 9 apart.
- error `clearance` e0/e2, e0/e3, e0/e4 (header divider too close to the
  tabs and the seven): resolved by dropping the header divider.
- error `hole` (header cell 4.8 wide): resolved with the divider.
- info `stroke-width` (trace 2.77, target 4): drawn at stroke 4.
Not kept: the header divider. The numeral must be the typeface glyph (15
tall, or 20 in v1) and cannot be scaled; divider-to-top needs 10 (6-wide
cell), divider-to-seven 8 and seven-to-bottom 8, i.e. at least 41 of
height below the page top, while the tallest SOLO48 centerline box leaves
36 below a top edge that the bindings cross. The page, tabs and a large 7
still read as a dated calendar leaf.
Lucide construction used: `calendar` (rounded page, two binding lines
crossing its top edge); header omitted for the reason above.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d7201890-607e-4568-916a-e843756d3ef0"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1928-calendar-number-seven/calendar-number-seven_raw.svg"
AUTHOR = "claude-opus-5-5"

PAGE_L, PAGE_R, PAGE_TOP, PAGE_BOTTOM, PAGE_RAD = 8, 40, 8, 44, 4
BIND_XS, BIND_TOP, BIND_BOTTOM = (16, 32), 4, 12
# typeface v2 digit-7: M 5,2 L 12.4325,2 C 12.7061,2 12.8947,2.27438 12.7967,2.52987 L 7.24562,17
SEVEN_BAR_L, SEVEN_BAR_R, SEVEN_TOP, SEVEN_FOOT_X, SEVEN_FOOT_Y = 20, 28, 20, 22, 35


class CalendarNumberSevenRedraw(Solo48):
    icon_id = "calendar-number-seven-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/time"
    aliases = ("calendar 7", "day seven")
    keywords = ("calendar", "date", "day", "seven", "7", "schedule", "number")

    def build(self) -> None:
        l, r, t, b, k = PAGE_L, PAGE_R, PAGE_TOP, PAGE_BOTTOM, PAGE_RAD
        x1, x2 = BIND_XS
        self.add_line("page-top-left", (l + k, t), (x1, t))
        self.add_line("page-top-mid", (x1, t), (x2, t))
        self.add_line("page-top-right", (x2, t), (r - k, t))
        self.add_arc("page-tr", (r - k, t), (r, t + k), radius_x=k, sweep=True)
        self.add_line("page-right", (r, t + k), (r, b - k))
        self.add_arc("page-br", (r, b - k), (r - k, b), radius_x=k, sweep=True)
        self.add_line("page-bottom", (r - k, b), (l + k, b))
        self.add_arc("page-bl", (l + k, b), (l, b - k), radius_x=k, sweep=True)
        self.add_line("page-left", (l, b - k), (l, t + k))
        self.add_arc("page-tl", (l, t + k), (l + k, t), radius_x=k, sweep=True)
        self.add_contour("page", "page-top-left", "page-top-mid", "page-top-right", "page-tr",
                         "page-right", "page-br", "page-bottom", "page-bl", "page-left",
                         "page-tl", closed=True)

        for x in BIND_XS:
            self.add_line(f"binding-{x}-upper", (x, BIND_TOP), (x, t))
            self.add_line(f"binding-{x}-lower", (x, t), (x, BIND_BOTTOM))
            self.add_contour(f"binding-{x}", f"binding-{x}-upper", f"binding-{x}-lower")
            self.relate("connect", "page", f"binding-{x}")

        self.add_polyline("seven", (SEVEN_BAR_L, SEVEN_TOP), (SEVEN_BAR_R, SEVEN_TOP),
                          (SEVEN_FOOT_X, SEVEN_FOOT_Y))
