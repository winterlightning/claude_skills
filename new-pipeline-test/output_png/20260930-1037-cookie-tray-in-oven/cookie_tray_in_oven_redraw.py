"""cookie-tray-in-oven (redraw of the new-pipeline traced SVG).

Plan: oven front on SQUARE (centerline box (6,6)-(42,42)), mirrored about x=24.
- oven: one closed contour, rounded rectangle (6,6)-(42,42), corner r=6.
  Every extreme sits on the SQUARE box, fixing keyshape-short-axis (the trace
  only filled 87% of y).
- handle: straight bar (16,15)-(32,15), 9 below the top wall. Exactly 8
  against the curved oven contour came back `review`, so it gets 9.
- cookies: three stroke dots on one row y=23, x=16/24/32 (8 apart, 10 from
  the side walls, 8 below the handle).
- tray: shallow open contour with r=2 rounded corners rising to lips at
  (15,31)/(33,31), floor y=33 (9 from the oven walls). Lip tips are 8.06
  from the outer cookies.
Every distinct part is at least 8 apart on centerlines, which fixes all seven
clearance errors (e0-e1, e0-e2, e0-e3, e0-e4, e2-e3, e2-e4, e3-e4). No part
touches another, so the trace's three sliver holes (tray against cookies and
wall) cannot occur.
Changed from the trace: the two ring cookies became dots. At stroke 4, the
oven's inner band is 14..34 (20 wide). Two rings need r>=5 for a 6-unit hole
and 8 between them, which is 28 wide, so no ring pair fits. The tall U tray
sides became short rounded lips for the same reason. No useful Lucide match
was found (Lucide has no oven); the rounded outline follows the Lucide
microwave body.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "41472ab4-d5b7-4320-9072-c062ba84ab5d"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1037-cookie-tray-in-oven/"
    "cookie-tray-in-oven_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
LO, HI = 6, 42          # SQUARE centerline box
CORNER = 6
HANDLE_Y, HANDLE_HALF = 15, 8
COOKIE_Y, COOKIE_STEP = 23, 8
TRAY_Y, TRAY_HALF, TRAY_R = 33, 9, 2


def mx(p):
    return (2 * AXIS - p[0], p[1])


class CookieTrayInOvenRedraw(Solo48):
    icon_id = "cookie-tray-in-oven-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/baking"
    aliases = ("baking cookies", "oven with cookies", "cookie sheet")
    keywords = ("oven", "cookie", "cookies", "baking", "tray", "bake", "kitchen", "dessert")

    def build(self) -> None:
        a, b, c = LO, HI, CORNER
        # Oven body, clockwise from the top-left corner.
        self.add_line("top", (a + c, a), (b - c, a))
        self.add_arc("c-tr", (b - c, a), (b, a + c), radius_x=c)
        self.add_line("right", (b, a + c), (b, b - c))
        self.add_arc("c-br", (b, b - c), (b - c, b), radius_x=c)
        self.add_line("bottom", (b - c, b), (a + c, b))
        self.add_arc("c-bl", (a + c, b), (a, b - c), radius_x=c)
        self.add_line("left", (a, b - c), (a, a + c))
        self.add_arc("c-tl", (a, a + c), (a + c, a), radius_x=c)
        self.add_contour("oven", "top", "c-tr", "right", "c-br",
                         "bottom", "c-bl", "left", "c-tl", closed=True)

        self.add_line("handle", (AXIS - HANDLE_HALF, HANDLE_Y), (AXIS + HANDLE_HALF, HANDLE_Y))

        for i, dx in enumerate((-COOKIE_STEP, 0, COOKIE_STEP)):
            self.add_dot(f"cookie-{i + 1}", (AXIS + dx, COOKIE_Y))

        lip = (AXIS - TRAY_HALF, TRAY_Y - TRAY_R)
        floor = (AXIS - TRAY_HALF + TRAY_R, TRAY_Y)
        self.add_arc("tray-l", lip, floor, radius_x=TRAY_R, sweep=False)
        self.add_line("tray-floor", floor, mx(floor))
        self.add_arc("tray-r", mx(floor), mx(lip), radius_x=TRAY_R, sweep=False)
        self.add_contour("tray", "tray-l", "tray-floor", "tray-r")
