"""camera-with-shaking-lines (redraw of the new-pipeline traced SVG).

Subject: a photo camera being shaken -- a rounded camera body with a raised
viewfinder hump and a centred lens, with two short shake marks on each side.

Plan (mirrored about x=24): HRECT_M, centerline box (4,10)-(44,38).
Extremes: x=4 / x=44 shake marks, y=10 hump top, y=38 body bottom.
- body: one closed contour, walls x=12 / x=36, top y=14, bottom y=38,
  corner radius 3 (Lucide `camera` rounded body). The hump rises from
  shoulders at x=24-/+7 on 45 deg slants to a top edge 24-/+3 at y=10.
- lens: full circle r=3 about (24,26) -> 9 clear of both walls, the top and
  the bottom (a curve exactly on 8 comes back `review`).
- shake marks: one repeat definition, vertical dashes on x=4 and x=44, y 16-22
  and 30-36 (mirrored about the body centre y=26); 8 from the walls
  (straight-straight, certified) and 8 apart end to end.
HRECT_M kept as suggested (score 0.91): with the hump the drawing is 28 tall
and fills the short axis exactly.
References: generated PNG read for the subject only; Lucide `camera` (rounded
body, trapezoid hump, centred lens) and Lucide `vibrate` (plain side marks
beside a device). No coordinates copied from the trace.

Width budget (why the lens is small and the marks are straight):
lens diameter 2r + 2 x 9 (lens to wall, curved) + 2 x 8 (wall to mark) must
fit in 40, so r <= 3; the r=3 circle is the exempt small full circle.
Curved marks like the PNG's would need 9 from the wall and stick out past
x=4, so the marks are straight dashes.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4, every gap budgeted at 8 (9 for
  curves).
- keyshape-short-axis (y fills 66%): y runs exactly 10 (hump) to 38 (body),
  x exactly 4 to 44 (marks); no stretch needed.
- clearance e0/e1, e0/e2, e0/e4, e0/e5 (body vs marks, 3.4-4.2): marks sit
  8 from the straight walls.
- clearance e1/e4, e2/e5 (upper vs lower mark, 3.4): marks are 8 apart.
- clearance e0/e3 (body vs lens, 2.4): lens clears every body edge by 9.
- hole [14.6,22.3] (4.8 inscribed): the body interior is 24 x 24.
Not fixed as drawn: the PNG's large lens and curved shake arcs do not fit
the 40-wide budget (see above); both were reduced, not squeezed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f5ada276-7815-4d75-9ba7-b74ca81c7919"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1728-camera-with-shaking-lines/camera-with-shaking-lines_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                      # mirror axis
LENS_Y = 26                  # lens centre / body centre line
LENS_R = 3
WALL = 12                    # left wall; right wall mirrors to 36
TOP, BOTTOM = 14, 38         # body top / bottom edges
CR = 3                       # body corner radius
HUMP_TOP, HUMP_HALF, SHOULDER = 10, 3, 7
SHAKE_X = 4                  # left mark; right mark mirrors to 44
SHAKES = ((16, 22), (30, 36))


class CameraWithShakingLinesRedraw(Solo48):
    icon_id = "camera-with-shaking-lines-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("camera shake", "shaking camera", "camera vibration")
    keywords = ("camera", "shake", "vibration", "photo", "blur", "motion", "device")

    def build(self) -> None:
        left, right = WALL, 2 * AX - WALL

        # Body with the viewfinder hump, one closed contour.
        self.add_line("left", (left, BOTTOM - CR), (left, TOP + CR))
        self.add_arc("tl", (left, TOP + CR), (left + CR, TOP), radius_x=CR, sweep=True)
        self.add_line("shoulder-l", (left + CR, TOP), (AX - SHOULDER, TOP))
        self.add_line("hump-l", (AX - SHOULDER, TOP), (AX - HUMP_HALF, HUMP_TOP))
        self.add_line("hump-top", (AX - HUMP_HALF, HUMP_TOP), (AX + HUMP_HALF, HUMP_TOP))
        self.add_line("hump-r", (AX + HUMP_HALF, HUMP_TOP), (AX + SHOULDER, TOP))
        self.add_line("shoulder-r", (AX + SHOULDER, TOP), (right - CR, TOP))
        self.add_arc("tr", (right - CR, TOP), (right, TOP + CR), radius_x=CR, sweep=True)
        self.add_line("right", (right, TOP + CR), (right, BOTTOM - CR))
        self.add_arc("br", (right, BOTTOM - CR), (right - CR, BOTTOM), radius_x=CR, sweep=True)
        self.add_line("bottom", (right - CR, BOTTOM), (left + CR, BOTTOM))
        self.add_arc("bl", (left + CR, BOTTOM), (left, BOTTOM - CR), radius_x=CR, sweep=True)
        self.add_contour(
            "body", "left", "tl", "shoulder-l", "hump-l", "hump-top", "hump-r",
            "shoulder-r", "tr", "right", "br", "bottom", "bl", closed=True,
        )

        # Lens: full circle on the body centre.
        self.add_arc("lens-top", (AX - LENS_R, LENS_Y), (AX + LENS_R, LENS_Y), radius_x=LENS_R, sweep=True)
        self.add_arc("lens-bottom", (AX + LENS_R, LENS_Y), (AX - LENS_R, LENS_Y), radius_x=LENS_R, sweep=True)
        self.add_contour("lens", "lens-top", "lens-bottom", closed=True)

        # Shake marks: one mirrored definition, two dashes per side.
        for index, (y0, y1) in enumerate(SHAKES):
            self.add_line(f"shake-l{index}", (SHAKE_X, y0), (SHAKE_X, y1))
            self.add_line(f"shake-r{index}", (2 * AX - SHAKE_X, y0), (2 * AX - SHAKE_X, y1))
