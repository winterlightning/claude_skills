"""bell-with-ringing-strokes (redraw of the new-pipeline traced SVG).

Plan: a hollow bell with a flared flat rim, a detached U clapper under the
rim and one ringing stroke each side of the dome, on SQUARE (centerline box
(6,6)-(42,42)), mirrored about x=24.
- bell: one closed contour. Dome = r9 semicircle about (24,16) as two
  quarter arcs (top (24,7), sides (15,16)/(33,16)), short straight sides down
  to y=21, tangent-continuous cubic flares out to the rim corners (9,29) and
  (39,29), flat rim between them.
- ringing strokes: r18 arcs through (6,15) and (9,6) on the left, mirrored
  on the right; their centre (23.97,15.99) is all but the dome's, so they
  stay ~9 from the dome all along. The lower ends set the left/right
  extremes x=6/42 (the arcs stop above their horizontal extreme) and the
  upper ends the top y=6.
- clapper: r4 semicircle about (24,38), ends (20,38)/(28,38) 9 below the rim,
  bottom (24,42) sets the lower extreme.
Traced shape: 20260929-1824-bell-with-ringing-strokes/
bell-with-ringing-strokes_raw.svg (read for the subject only; nothing copied
from its coordinates).
Lucide: lucide/bell-ring informed the construction (dome with straight sides
flaring to a flat rim, ringing arcs outside the dome's shoulders); the
detached U clapper follows the generated image.

Metric issues:
- clearance e0/e2 and e1/e2 (ringing strokes 6.5 from the dome): fixed, the
  strokes are (near-)concentric with the dome and sit ~9 from it.
- clearance e2/e3 (clapper 3.2 below the rim, touching in ink): fixed, the
  clapper ends sit 9 below the rim line.
- hole at [23.7, 38.3] (3.2 inscribed sliver between clapper and rim):
  fixed, the clapper is detached with an open 5-unit ink gap, no enclosed hole.
- stroke-width (info): drawn at stroke 4; all gaps budgeted for 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4a12d6a5-374a-5c49-8bd7-4bf52793db57"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1824-bell-with-ringing-strokes/"
    "bell-with-ringing-strokes_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AX = 24                     # mirror axis
DOME_C = (AX, 16)           # dome and ringing strokes share this centre
DOME_R = 9
RING_R = 18                 # through the lattice points (+-18, -1), (+-15, -10)
SIDE_Y = 21                 # straight sides run from the dome to here
RIM_Y = 29
RIM_HALF = 15               # rim corners at x = 9 / 39
CLAP_C = (AX, 38)
CLAP_R = 4


def _m(x):
    return 2 * AX - x


class BellWithRingingStrokesRedraw(Solo48):
    icon_id = "bell-with-ringing-strokes-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ("alarm-bell-ring", "bell-ring", "ringing-bell")
    keywords = ("bell", "ringing", "ring", "alarm", "notification", "alert", "sound")

    def build(self) -> None:
        cx, cy = DOME_C
        left, right, top = cx - DOME_R, cx + DOME_R, cy - DOME_R
        rim_l, rim_r = AX - RIM_HALF, AX + RIM_HALF

        self.add_arc("dome-left", (left, cy), (cx, top), radius_x=DOME_R)
        self.add_arc("dome-right", (cx, top), (right, cy), radius_x=DOME_R)
        self.add_line("side-right", (right, cy), (right, SIDE_Y))
        self.add_bezier("flare-right", (right, SIDE_Y),
                        ((right, SIDE_Y + 4), (rim_r - 3, RIM_Y - 2), (rim_r, RIM_Y)))
        self.add_line("rim", (rim_r, RIM_Y), (rim_l, RIM_Y))
        self.add_bezier("flare-left", (rim_l, RIM_Y),
                        ((rim_l + 3, RIM_Y - 2), (left, SIDE_Y + 4), (left, SIDE_Y)))
        self.add_line("side-left", (left, SIDE_Y), (left, cy))
        self.add_contour("bell", "dome-left", "dome-right", "side-right", "flare-right",
                         "rim", "flare-left", "side-left", closed=True)

        # ringing strokes, concentric with the dome
        lo, hi = (cx - 18, cy - 1), (cx - 15, cy - 10)
        self.add_arc("ring-left", lo, hi, radius_x=RING_R)
        self.add_arc("ring-right", (_m(hi[0]), hi[1]), (_m(lo[0]), lo[1]), radius_x=RING_R)

        # detached clapper, opening upward
        kx, ky = CLAP_C
        self.add_arc("clapper", (kx + CLAP_R, ky), (kx - CLAP_R, ky), radius_x=CLAP_R)
