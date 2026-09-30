"""browser-yuan-sign-solo (redraw of the new-pipeline traced SVG).

Plan: a rounded browser window with a joined toolbar divider and a centred
two-bar yuan sign, mirrored about x = 24.
- window: one closed rounded-rect contour (8,4)-(40,44), corner r = 4, with
  its side walls split at y = 12 where the divider attaches.
- divider: (8,12)-(40,12), sharing both endpoints with the walls, declared
  with relate("connect").
- yuan: fork (19,20) -> (24,25) -> (29,20) (45 degree arms); stem
  (24,25) -> (24,35) split at the upper bar and ending on the lower bar;
  bars y = 27 and y = 35, x 18..30, each split at x = 24 so the crossings
  are shared points. Arm tips sit 8 below the divider, the lower bar 9
  above the bottom wall, the bar ends 10 from the side walls, and the two
  bars are 8 apart. The stem stops on the lower bar: a foot at y = 36 sits
  exactly 8 from the bottom wall (validator `review`), and a 1-unit foot
  at 35 with bars at 26/34 read as a blob at 48 px, so the tail was dropped.

Keyshape: VRECT_L, not the suggested SQUARE. SQUARE gives 36 on centerlines:
frame 6, divider 14, arm tips 22, stem foot at most 34 = 12 for the whole
glyph, which cannot hold the fork plus two bars 8 apart. VRECT_L gives 40
tall (16 for the glyph) at 32 wide, which still clears the side walls.
Lucide `app-window` informed the frame-plus-header construction and Lucide
`japanese-yen` the fork / stem / two-bar yuan.

Metric issues (browser-yuan-sign-solo_metrics.json):
- stroke-width (info, 2.77 fitted): redrawn at stroke 4, every gap budgeted
  for 4.
- clearance e0/e1 6.96 (divider to window top): fixed, divider is 8 below
  the top wall.
- clearance e0/e2 4.62 (divider to yuan arms): fixed, arm tips 8 below.
- clearance e1/e2 5.17 (stem foot to bottom wall): fixed, the stem ends on
  the lower bar, 9 above the bottom wall.
- clearance e2/e3 0.02 and e2/e4 0.09 (bars on the stem): these are the
  intended crossings; the bars and stem now share the crossing points and
  are declared connected.
- clearance e3/e4 4.08 (bar to bar): fixed, bars are 8 apart.
- hole at [9.4,9.4] 3.0 wide (toolbar sliver): fixed, the toolbar band is
  8 tall on centerlines (4 of clear ink).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f3a40f08-7124-46f5-9ed2-b85ee4e25e73"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1936-browser-yuan-sign-solo/browser-yuan-sign-solo_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24

# window
LEFT, TOP, RIGHT, BOTTOM = 8, 4, 40, 44
CORNER_R = 4
HEADER_Y = 12

# yuan
ARM_TIP = (19, 20)
FORK = (AXIS, 25)
BAR_YS = (27, 35)
BAR_HALF = 6
STEM_FOOT = (AXIS, BAR_YS[-1])  # the stem ends on the lower bar


def mx(x: int) -> int:
    return 2 * AXIS - x


class BrowserYuanSignSoloRedraw(Solo48):
    icon_id = "browser-yuan-sign-solo-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "money/browser"
    aliases = ("browser yuan", "web yuan", "online payment yuan", "browser yen")
    keywords = ("browser", "window", "web", "yuan", "yen", "currency",
                "money", "payment", "online", "shop")

    def build(self) -> None:
        r = CORNER_R
        self.add_line("w-top", (LEFT + r, TOP), (RIGHT - r, TOP))
        self.add_arc("w-tr", (RIGHT - r, TOP), (RIGHT, TOP + r), radius_x=r, sweep=True)
        self.add_line("w-ru", (RIGHT, TOP + r), (RIGHT, HEADER_Y))
        self.add_line("w-rl", (RIGHT, HEADER_Y), (RIGHT, BOTTOM - r))
        self.add_arc("w-br", (RIGHT, BOTTOM - r), (RIGHT - r, BOTTOM), radius_x=r, sweep=True)
        self.add_line("w-bottom", (RIGHT - r, BOTTOM), (LEFT + r, BOTTOM))
        self.add_arc("w-bl", (LEFT + r, BOTTOM), (LEFT, BOTTOM - r), radius_x=r, sweep=True)
        self.add_line("w-ll", (LEFT, BOTTOM - r), (LEFT, HEADER_Y))
        self.add_line("w-lu", (LEFT, HEADER_Y), (LEFT, TOP + r))
        self.add_arc("w-tl", (LEFT, TOP + r), (LEFT + r, TOP), radius_x=r, sweep=True)
        self.add_contour("window", "w-top", "w-tr", "w-ru", "w-rl", "w-br",
                         "w-bottom", "w-bl", "w-ll", "w-lu", "w-tl", closed=True)

        self.add_line("divider", (LEFT, HEADER_Y), (RIGHT, HEADER_Y))
        self.relate("connect", "window", "divider")

        self.add_polyline("fork", ARM_TIP, FORK, (mx(ARM_TIP[0]), ARM_TIP[1]))
        self.add_polyline("stem", FORK, *((AXIS, y) for y in BAR_YS))
        self.relate("connect", "fork", "stem")
        for i, y in enumerate(BAR_YS, 1):
            name = f"bar-{i}"
            self.add_polyline(name, (AXIS - BAR_HALF, y), (AXIS, y), (AXIS + BAR_HALF, y))
            self.relate("connect", "stem", name)
