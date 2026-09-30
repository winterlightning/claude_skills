"""bottle-opener-with-heart-notched-aperture (redraw of the new-pipeline traced SVG).

Plan: a paddle bottle opener, mirrored about x=24, on VRECT_L (centerline box
(8,4)-(40,44)).
- body: one closed contour. Flat top y=4 between r8 rounded corners, straight
  sides x=8/40 down to y=18, tangent-continuous cubic tapers in to a narrow
  handle (walls x=19/29 from y=35, 10 apart), closed by an r5 semicircle
  about (24,39) whose bottom (24,44) is the lower extreme.
- heart aperture: one closed contour of mirrored cubics inside the head:
  notch (24,15), lobe tops (20,13)/(28,13), then one cubic per side down to
  the point (24,27). The lobe extremes (x ~16.5/31.5) are off-grid on
  purpose so the heart sits 8.5 from the straight sides (an exact 8 against
  a curve comes back `review`); it sits 9 below the top.
- The heart is as large as the head allows so its hole passes the metric's
  6-inscribed floor at stroke 4; that pushes the neck down to y=35, so the
  handle is shorter than in the generated image (deliberate trade).
Traced shape: 20260929-1825-bottle-opener-with-heart-notched-aperture/
bottle-opener-with-heart-notched-aperture_raw.svg (read for the subject only;
nothing copied from its coordinates).
Lucide: lucide/heart informed the aperture (two rounded lobes over a shallow
notch, sides sweeping to a point); no Lucide bottle opener exists, the paddle
follows the generated image.

Keyshape: VRECT_L instead of the suggested VRECT_M. The heart needs ~15 of
width for a passing hole; the 28-wide VRECT_M head would leave it ~6 from each
side. VRECT_L (32 wide) gives the 8.5 gap.

Metric issues:
- clearance e0/e1 (heart 2.98 from the body outline): fixed, >= 8 everywhere, 8.0 where
  the lower heart sides pass the tapers (validator and build gate pass with no warnings).
- hole at [23.9, 11.8] (2.3 sliver between heart and head top): fixed, the
  band above the heart is 9 on centerlines.
- hole at [23.9, 18.8] (heart interior 2.6 wide): fixed, heart hole is now
  6.2 inscribed at stroke 4.
- keyshape-short-axis (x fill 66%): fixed, the head reaches x=8 and x=40.
- stroke-width (info): drawn at stroke 4; all gaps budgeted for 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0b913234-7695-5b92-8cb9-b37fc3a45260"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1825-bottle-opener-with-heart-notched-aperture/"
    "bottle-opener-with-heart-notched-aperture_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AX = 24            # mirror axis
TOP, SIDE = 4, 16  # head top and half width (x = 8 / 40)
CORNER = 8         # head corner radius
SIDE_Y = 18        # straight sides end here
NECK_Y = 35        # taper meets the handle walls here
HANDLE = 5         # handle half width and bottom radius
BOTTOM_C = 39      # centre of the handle's bottom semicircle
HEART_W = 8        # lobe tops at x = 20 / 28
NOTCH, LOBE_TOP, POINT = 15, 13, 27   # heart y levels
LOBE_C1, LOBE_C2 = (33, 13), (33, 20)   # lobe cubic handles (right side)


def _m(p):
    return (2 * AX - p[0], p[1])


class BottleOpenerWithHeartNotchedApertureRedraw(Solo48):
    icon_id = "bottle-opener-with-heart-notched-aperture-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ("beer-opener", "heart-bottle-opener")
    keywords = ("bottle", "opener", "beer", "heart", "love", "bar", "drink")

    def build(self) -> None:
        l, r = AX - SIDE, AX + SIDE
        hl, hr = AX - HANDLE, AX + HANDLE

        # right half, top to bottom, then the mirror back up
        self.add_line("top", (l + CORNER, TOP), (r - CORNER, TOP))
        self.add_arc("corner-right", (r - CORNER, TOP), (r, TOP + CORNER), radius_x=CORNER)
        self.add_line("side-right", (r, TOP + CORNER), (r, SIDE_Y))
        self.add_bezier("taper-right", (r, SIDE_Y), ((r, SIDE_Y + 9), (hr, NECK_Y - 4), (hr, NECK_Y)))
        self.add_line("handle-right", (hr, NECK_Y), (hr, BOTTOM_C))
        self.add_arc("bottom", (hr, BOTTOM_C), (hl, BOTTOM_C), radius_x=HANDLE)
        self.add_line("handle-left", (hl, BOTTOM_C), (hl, NECK_Y))
        self.add_bezier("taper-left", (hl, NECK_Y), ((hl, NECK_Y - 4), (l, SIDE_Y + 9), (l, SIDE_Y)))
        self.add_line("side-left", (l, SIDE_Y), (l, TOP + CORNER))
        self.add_arc("corner-left", (l, TOP + CORNER), (l + CORNER, TOP), radius_x=CORNER)
        self.add_contour("body", "top", "corner-right", "side-right", "taper-right",
                         "handle-right", "bottom", "handle-left", "taper-left",
                         "side-left", "corner-left", closed=True)

        # heart aperture: right half as cubics, left half mirrored. The lobe
        # runs top -> point in one cubic so its side extreme (x ~ 31.5) is
        # off-grid, keeping >8 from the straight head side.
        n, p = (AX, NOTCH), (AX, POINT)
        t = (AX + HEART_W // 2, LOBE_TOP)          # lobe top
        right = (
            ((AX + 1, NOTCH - 1.5), (t[0] - 2, LOBE_TOP), t),
            (LOBE_C1, LOBE_C2, p),
        )
        self.add_bezier("heart-right", n, *right)
        # mirror walks p -> t' -> n: reverse each cubic and flip x
        left = [(_m(c2), _m(c1), _m(k0)) for (c1, c2, _), k0 in zip(reversed(right), (t, n))]
        self.add_bezier("heart-left", p, *left)
        self.add_contour("heart", "heart-right", "heart-left", closed=True)
