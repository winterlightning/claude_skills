"""browser-yuan-sign-solo (redraw of the new-pipeline traced SVG).

Plan: a rounded browser window with a toolbar divider and a centred two-bar
yuan sign, mirrored about x=24, on VRECT_L (centerline box (8,4)-(40,44)).
- frame: r4 rounded rectangle split into top / left / right contours and a
  standalone bottom line, all joined by `connect` (the standalone bottom lets
  the exact 8-unit gap to the stem tip certify).
- header: toolbar divider at y=12, 8 below the top edge.
- yuan: fork tips (17,20)/(31,20), 8 below the header, meeting at (24,26);
  bar 1 crosses at the fork junction (as in the trace), bar 2 at y=34, and the
  stem runs on to y=36, 8 above the bottom edge. Bars are 14 wide, 10 clear of
  the side walls.
Keyshape: metrics suggested SQUARE (the trace is square), but on SQUARE the
header costs 8 on each side, leaving 12 units for a sign that needs 16 (fork +
8 between bars + stem tail); the SQUARE candidate validated only as a squashed
sign whose fork merged into the bars. VRECT_L, as in the library's other
browser currency icons, gives the 16.
Lucide construction: `panels-top-left` (window + header) and `japanese-yen`
(fork, stem, two bars), rebuilt on this grid.

Metric issues fixed:
- clearance e0/e1 (header 6.66 from the top edge): header moved to 8 below.
- clearance e0/e2, e0/e3 (fork 4.9 under the header): fork tips 8 below it.
- clearance e1/e2 (stem 4.7 above the bottom edge): stem ends 8 above it.
- clearance e2/e4, e2/e5 (bars crossing the stem): the bars now share the
  stem's nodes and are declared connected.
- clearance e3/e5, e4/e5 (bars 3.8 apart, fork 4.9 above bar 2): bars are 8
  apart and bar 1 sits on the fork junction.
- hole 2.8 inscribed at (9.6,9.3) (the corner pocket above the header): the
  header band is now 8 tall, so the pocket is gone.
- loose-join e3/e4 (fork arm 1.08 short of bar 1): bar 1 passes through the
  exact fork junction node and is declared connected to the fork.
- stroke-width (trace 2.77): drawn at stroke 4 with gaps sized for it.
Not fixed: none. The frame-to-header T-junctions from the trace are kept as
connected contacts.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f3a40f08-7124-46f5-9ed2-b85ee4e25e73"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1747-browser-yuan-sign-solo/"
    "browser-yuan-sign-solo_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
LEFT, TOP, RIGHT, BOTTOM = 8, 4, 40, 44
CORNER_R = 4
HEADER_Y = 12
FORK_TOP = 20
FORK_DX = 7      # fork tips at AXIS -/+ 7
JUNCTION_Y = 26  # fork meets the stem; bar 1 crosses here
BAR2_Y = 34
STEM_END = 36
BAR_DX = 7       # bars span AXIS -/+ 7


class BrowserYuanSignSoloRedraw(Solo48):
    icon_id = "browser-yuan-sign-solo-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/finance"
    aliases = ("browser-yuan", "web-payment-yuan")
    keywords = ("browser", "window", "web", "yuan", "yen", "currency", "money", "payment", "cny")

    def build(self) -> None:
        l, t, r, b, R = LEFT, TOP, RIGHT, BOTTOM, CORNER_R
        self.add_line("left-up", (l, HEADER_Y), (l, t + R))
        self.add_arc("corner-tl", (l, t + R), (l + R, t), radius_x=R, sweep=True)
        self.add_line("top", (l + R, t), (r - R, t))
        self.add_arc("corner-tr", (r - R, t), (r, t + R), radius_x=R, sweep=True)
        self.add_line("right-up", (r, t + R), (r, HEADER_Y))
        self.add_contour("frame-top", "left-up", "corner-tl", "top", "corner-tr", "right-up")

        self.add_line("right-wall", (r, HEADER_Y), (r, b - R))
        self.add_arc("corner-br", (r, b - R), (r - R, b), radius_x=R, sweep=True)
        self.add_contour("frame-right", "right-wall", "corner-br")
        self.add_line("frame-bottom", (r - R, b), (l + R, b))
        self.add_arc("corner-bl", (l + R, b), (l, b - R), radius_x=R, sweep=True)
        self.add_line("left-wall", (l, b - R), (l, HEADER_Y))
        self.add_contour("frame-left", "corner-bl", "left-wall")

        self.add_line("header", (l, HEADER_Y), (r, HEADER_Y))
        for side in ("frame-right", "frame-left"):
            for other in ("frame-top", "frame-bottom", "header"):
                self.relate("connect", side, other)
        self.relate("connect", "frame-top", "header")

        junction = (AXIS, JUNCTION_Y)
        self.add_polyline(
            "fork", (AXIS - FORK_DX, FORK_TOP), junction, (AXIS + FORK_DX, FORK_TOP)
        )
        self.add_polyline("stem", junction, (AXIS, BAR2_Y), (AXIS, STEM_END))
        self.relate("connect", "fork", "stem")
        for name, y in (("bar-1", JUNCTION_Y), ("bar-2", BAR2_Y)):
            self.add_polyline(name, (AXIS - BAR_DX, y), (AXIS, y), (AXIS + BAR_DX, y))
            self.relate("connect", name, "stem")
        self.relate("connect", "bar-1", "fork")
