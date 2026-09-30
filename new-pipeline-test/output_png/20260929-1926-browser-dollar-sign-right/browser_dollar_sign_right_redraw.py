"""browser dollar sign right (redraw of the new-pipeline traced SVG).

Plan: a rounded browser window on the left with one header divider, and a
Lucide-style dollar sign standing to its right, HRECT_M keyshape
(centerline box (4,10)-(44,38)).
- window: closed rounded rectangle x 4..26, y 10..38, corner radius 4;
  both side walls are split at y=20 where the header divider meets them
  (declared connects). The header band is 10 tall on centerlines, so its
  opening is 6 ink-free, and the page area below is 18 tall (the header
  band stays in the top third so the frame reads as a browser, not a
  box split in half; a 21x24 window with the header mid-height was tried
  first and rejected on the 48 px render).
- dollar: one contour on axis x=39 -- top terminal (44,14)->(39,14), a
  radius-5 upper lobe bowing left to x=34, a radius-5 lower lobe bowing
  right to x=44 (the two lobes meet tangent-horizontal at (39,24)), and a
  bottom terminal (39,34)->(34,34). The vertical stroke is two 4-unit stubs
  on x=39 (y 10..14 and 34..38) sharing the lobe endpoints, so they carry
  the y=10 / y=38 extremes and the sign reads as `$` without a stroke
  crossing the S waist.
- gap: window wall x=26 to the dollar's left lobe apex / terminal x=34 is 8
  on centerlines (4 ink), certified by validate_icon().
Every arc centre and endpoint is on the integer grid; nothing is copied
from the trace coordinates.

Metric issues:
- error `clearance` e0/e1 (header 4.04 below the window top): fixed, the
  header sits 10 below the top edge (6 ink opening).
- errors `clearance` e0/e5, e0/e6, e1/e3, e1/e5, e1/e6 (window and header
  crowding the dollar): fixed, the dollar starts 8 right of the window wall.
- errors `clearance` e2/e6, e3/e5, e3/e7, e4/e6, e5/e8, e7/e8 and the rest
  (the traced `$` was 9 fragments with the stem crossing the S): fixed by
  rebuilding the sign as one S contour with radius-5 lobes (10 between
  its horizontal runs) plus two end stubs.
- error `hole` (two 0.2 slivers at the window's top corners): fixed, the
  header band opening is a 6-wide clean slot.
- warn `stroke-count` (9 strokes, budget 6): fixed, 5 strokes (window,
  header, dollar S and the two stem stubs).
- warn `keyshape-short-axis` (y filled 66%): fixed, the window and the
  stubs reach y=10 and y=38, the window wall x=4 and the dollar's top terminal / lower lobe
  x=44, so all four HRECT_M extremes are exact.
- info `stroke-width` (trace 2.66, target 4): fixed by construction at
  stroke 4; all distinct-part gaps are >= 8 on centerlines.
Not reproduced: the window's landscape proportion. The subject is 2.16:1
wide but HRECT_M allows 40x28, so the window is 22x28 to leave room for a
readable dollar and the 8-unit gap.
Lucide construction used: `dollar-sign` (horizontal terminals with two
semicircular lobes) and `app-window` (rounded frame with a header rule).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "150d4701-3c3f-45a7-a26d-8c580a891da1"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1926-browser-dollar-sign-right/browser-dollar-sign-right_raw.svg"
AUTHOR = "claude-opus-5-5"

WIN_L, WIN_R, WIN_TOP, WIN_BOTTOM, WIN_RAD, HEADER_Y = 4, 26, 10, 38, 4, 20
DOLLAR_X, LOBE_R, S_TOP, STEM_TOP, STEM_BOTTOM = 39, 5, 14, 10, 38
S_MID, S_BOTTOM = S_TOP + 2 * LOBE_R, S_TOP + 4 * LOBE_R


class BrowserDollarSignRightRedraw(Solo48):
    icon_id = "browser-dollar-sign-right-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/web"
    aliases = ("web payment", "online price", "browser dollar")
    keywords = ("browser", "window", "dollar", "money", "price", "payment", "online", "web")

    def build(self) -> None:
        l, r, t, b, k, h = WIN_L, WIN_R, WIN_TOP, WIN_BOTTOM, WIN_RAD, HEADER_Y
        self.add_line("win-top", (l + k, t), (r - k, t))
        self.add_arc("win-tr", (r - k, t), (r, t + k), radius_x=k, sweep=True)
        self.add_line("win-right-upper", (r, t + k), (r, h))
        self.add_line("win-right-lower", (r, h), (r, b - k))
        self.add_arc("win-br", (r, b - k), (r - k, b), radius_x=k, sweep=True)
        self.add_line("win-bottom", (r - k, b), (l + k, b))
        self.add_arc("win-bl", (l + k, b), (l, b - k), radius_x=k, sweep=True)
        self.add_line("win-left-lower", (l, b - k), (l, h))
        self.add_line("win-left-upper", (l, h), (l, t + k))
        self.add_arc("win-tl", (l, t + k), (l + k, t), radius_x=k, sweep=True)
        self.add_contour("window", "win-top", "win-tr", "win-right-upper", "win-right-lower",
                         "win-br", "win-bottom", "win-bl", "win-left-lower",
                         "win-left-upper", "win-tl", closed=True)
        self.add_line("header", (l, h), (r, h))
        self.relate("connect", "header", "window")

        x, q = DOLLAR_X, LOBE_R
        self.add_line("s-top", (x + q, S_TOP), (x, S_TOP))
        self.add_arc("s-upper-a", (x, S_TOP), (x - q, S_TOP + q), radius_x=q, sweep=False)
        self.add_arc("s-upper-b", (x - q, S_TOP + q), (x, S_MID), radius_x=q, sweep=False)
        self.add_arc("s-lower-a", (x, S_MID), (x + q, S_MID + q), radius_x=q, sweep=True)
        self.add_arc("s-lower-b", (x + q, S_MID + q), (x, S_BOTTOM), radius_x=q, sweep=True)
        self.add_line("s-bottom", (x, S_BOTTOM), (x - q, S_BOTTOM))
        self.add_contour("dollar-s", "s-top", "s-upper-a", "s-upper-b",
                         "s-lower-a", "s-lower-b", "s-bottom")
        self.add_line("stem-top", (x, STEM_TOP), (x, S_TOP))
        self.add_line("stem-bottom", (x, S_BOTTOM), (x, STEM_BOTTOM))
        self.relate("connect", "stem-top", "dollar-s")
        self.relate("connect", "stem-bottom", "dollar-s")
