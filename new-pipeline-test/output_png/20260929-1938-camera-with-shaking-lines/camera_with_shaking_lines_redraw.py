"""camera-with-shaking-lines (redraw of the new-pipeline traced SVG).

Subject: a photo camera being shaken -- a rounded camera body with a raised
viewfinder hump and one large centred lens, with one shake mark on each side.

Plan (mirrored about x=24): HRECT_M as suggested, centerline box (4,10)-(44,38).
Extremes: x=4 / x=44 shake marks, y=10 hump top, y=38 body bottom.
- body: one closed contour, walls x=12 / x=36, top y=14, bottom y=38,
  corner radius 3 (Lucide `camera` rounded body). The hump rises from
  shoulders at 24-/+7 on 45 deg slants to a top edge 24-/+3 at y=10.
- lens: full circle r=3 about the body centre (24,26), 9 clear of both
  walls, the top and the bottom (a curve exactly on 8 comes back `review`).
- shake marks: one mirrored definition, a single vertical stroke per side on
  x=4 / x=44, y 20-32 (centred on the lens), 8 from the straight walls.
References: generated PNG read for the subject only (one mark per side, big
lens); Lucide `camera` (rounded body, trapezoid hump, centred lens) and Lucide
`vibrate` (plain side marks beside a device). No trace coordinates copied.

Width budget: 2 x 8 (mark to wall) + 2 x 9 (curved lens to wall) + 2r = 40,
so r <= 3. An r=4 lens was tried: it sits exactly 8 from the walls and
validates as `review` (mic body/lens), so it was reduced, not squeezed.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted at 8.
- keyshape-short-axis (y fills 85%): fixed; y runs exactly 10 (hump top) to
  38 (body bottom), x exactly 4 to 44 (marks).
- clearance e0/e1 (body vs lens, 3.4): fixed; the lens clears every body
  edge by 9.
- clearance e0/e2, e0/e3 (body vs shake arcs, 4.7): fixed; the marks sit 8
  from the straight walls.
- hole [14.5,31.3] (5.2 inscribed, the body corner beside the lens): fixed;
  the body interior around the lens is 9 wide on every side.
Not kept as drawn: the PNG's large lens (width budget above) and its curved
shake arcs. A curved mark must clear the
wall by 9 along its whole length and would push its ends inside x=4 or narrow
the body to 20, leaving no room for a lens; the straight marks keep the
"shaking" read at 48 px.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f5ada276-7815-4d75-9ba7-b74ca81c7919"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1938-camera-with-shaking-lines/camera-with-shaking-lines_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                      # mirror axis
LENS_Y = 26                  # lens centre / body centre line
LENS_R = 3
WALL = 12                    # left wall; right wall mirrors to 36
TOP, BOTTOM = 14, 38         # body top / bottom edges
CR = 3                       # body corner radius
HUMP_TOP, HUMP_HALF, SHOULDER = 10, 3, 7
SHAKE_X = 4                  # left mark; right mark mirrors to 44
SHAKE_HALF = 6               # mark runs LENS_Y -/+ 6


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

        # Shake marks: one mirrored definition, one stroke per side.
        for side, x in (("l", SHAKE_X), ("r", 2 * AX - SHAKE_X)):
            self.add_line(f"shake-{side}", (x, LENS_Y - SHAKE_HALF), (x, LENS_Y + SHAKE_HALF))
