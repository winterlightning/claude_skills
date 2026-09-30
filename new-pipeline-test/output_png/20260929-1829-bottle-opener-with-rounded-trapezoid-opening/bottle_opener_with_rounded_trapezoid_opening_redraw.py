"""bottle-opener-with-rounded-trapezoid-opening (redraw of the new-pipeline trace).

Plan: a flat bar bottle opener in one closed outline, with a broad rounded
head over a narrow round-ended handle and a detached trapezoid cap opening,
wide edge up, in the head. It is mirrored about x=24 on VRECT_L (centerline
box (8,4)-(40,44)).
- body: a flat top from (18,4) to (30,4), with r10 corners that reach the
  head sides x=8/40 at y=14. Each side then runs through one cubic that
  leaves vertically, stays wide past the opening and turns in to the handle
  at (19,32)/(29,32), where it arrives vertically. Straight handle sides run
  to y=39, and an r5 semicircle closes the end at y=44. Every join is
  tangent-continuous.
- opening: a closed trapezoid with a top edge from (17,13) to (31,13) and a
  bottom edge from (20,23) to (28,23). Its corners are square on centerline,
  and the round joins paint the rounded corners of the reference.
  Clearances: 9 from the head top and sides, 8.6 from the corner arcs, and
  at least 8 from the tapers.
Traced shape: bottle-opener-with-rounded-trapezoid-opening_raw.svg, read
for the subject only; no coordinates copied.
Lucide: no local bottle-opener match. The construction follows the
generated image (head, taper, handle, trapezoid opening).

Keyshape: VRECT_L instead of the suggested VRECT_M. A 6-wide ink hole
needs a trapezoid about 14 wide at the top and 8 at the bottom on
centerline, which puts the top corners 7 from VRECT_M's x=10/38 walls
(8 required). Re-running svg_metrics on this redraw also suggests VRECT_L.

Metric issues:
- clearance e0/e1 (opening 2.9 from the outline): fixed. The opening is 9
  from the head top and sides, 8.6 from the corners and at least 8 from the
  tapers.
- hole at [22.3, 10.1] (2.0 wide sliver between the opening and the head
  top): fixed. That band is now the solid 9-unit head rim, so no sliver
  remains.
- hole at [23.9, 16.7] (the opening, 3.16 inscribed): fixed. The ink hole
  is 6.0 inscribed; the handle cavity is 7.6.
- keyshape-short-axis (x filled only 65%): fixed. The head spans the full
  box width, x=8..40, and the handle end and head top reach y=4..44.
- stroke-width (info): drawn at stroke 4, with every gap budgeted for 4.
Compromise: the handle is shorter than in the image (straight run y=32..39
plus the r5 end), because the stack of top rim, opening and taper
clearances fixes the neck at y=32 or lower.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7bb85302-0b29-5cf0-a28b-f3dad5fd7fa7"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1829-bottle-opener-with-rounded-trapezoid-opening/"
    "bottle-opener-with-rounded-trapezoid-opening_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AX = 24                     # mirror axis
TOP, BOTTOM = 4, 44         # VRECT_L centerline box (8,4)-(40,44)
HEAD_HALF = 16              # head sides at x = 8 / 40
CORNER_R = 10               # head top corners
SHOULDER_Y = 14             # head sides stay vertical to here
GRIP_HALF = 5               # handle sides at x = 19 / 29
NECK_Y = 32                 # taper reaches the handle here
TIP_R = GRIP_HALF           # semicircular handle end, bottom at y = 44
C1_DY, C2_DY = 18, 2         # taper control reach below the shoulder / above the neck
# trapezoid opening, wide edge on top
OPEN_TOP, OPEN_BOT = 13, 23
OPEN_TOP_HALF, OPEN_BOT_HALF = 7, 4


def _m(x):
    return 2 * AX - x


class BottleOpenerWithRoundedTrapezoidOpeningRedraw(Solo48):
    icon_id = "bottle-opener-with-rounded-trapezoid-opening-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ("beer-opener", "bottle-opener", "cap-lifter")
    keywords = ("bottle", "opener", "beer", "cap", "bar", "drinks")

    def build(self) -> None:
        hl, hr = AX - HEAD_HALF, AX + HEAD_HALF
        gl, gr = AX - GRIP_HALF, AX + GRIP_HALF
        tip_y = BOTTOM - TIP_R

        self.add_line("top", (hl + CORNER_R, TOP), (hr - CORNER_R, TOP))
        self.add_arc("corner-right", (hr - CORNER_R, TOP), (hr, TOP + CORNER_R), radius_x=CORNER_R)
        members = ["top", "corner-right"]
        if SHOULDER_Y > TOP + CORNER_R:
            self.add_line("side-right", (hr, TOP + CORNER_R), (hr, SHOULDER_Y))
            members.append("side-right")
        self.add_bezier("taper-right", (hr, SHOULDER_Y),
                        ((hr, SHOULDER_Y + C1_DY), (gr, NECK_Y - C2_DY), (gr, NECK_Y)))
        self.add_line("grip-right", (gr, NECK_Y), (gr, tip_y))
        self.add_arc("tip", (gr, tip_y), (gl, tip_y), radius_x=TIP_R)
        self.add_line("grip-left", (gl, tip_y), (gl, NECK_Y))
        self.add_bezier("taper-left", (gl, NECK_Y),
                        ((gl, NECK_Y - C2_DY), (hl, SHOULDER_Y + C1_DY), (hl, SHOULDER_Y)))
        members += ["taper-right", "grip-right", "tip", "grip-left", "taper-left"]
        if SHOULDER_Y > TOP + CORNER_R:
            self.add_line("side-left", (hl, SHOULDER_Y), (hl, TOP + CORNER_R))
            members.append("side-left")
        self.add_arc("corner-left", (hl, TOP + CORNER_R), (hl + CORNER_R, TOP), radius_x=CORNER_R)
        members.append("corner-left")
        self.add_contour("body", *members, closed=True)

        # opening: square centerline corners, the round joins paint the rounding
        tl, tr = (AX - OPEN_TOP_HALF, OPEN_TOP), (AX + OPEN_TOP_HALF, OPEN_TOP)
        br, bl = (AX + OPEN_BOT_HALF, OPEN_BOT), (AX - OPEN_BOT_HALF, OPEN_BOT)
        self.add_line("open-top", tl, tr)
        self.add_line("open-right", tr, br)
        self.add_line("open-bottom", br, bl)
        self.add_line("open-left", bl, tl)
        self.add_contour("opening", "open-top", "open-right", "open-bottom", "open-left", closed=True)
