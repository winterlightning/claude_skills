"""camera-drone-front (redraw of the new-pipeline traced SVG).

Plan: front view of a camera drone. A rounded body carries a ring lens, and
two T-shaped rotors (mast + horizontal propeller bar) stand on its top corners.
Mirrored about x=24; no useful Lucide drone front view exists, so the body
follows Lucide `camera`/`webcam` construction (rounded rect r4, cardinal-arc
lens) and the rotors are plain T joints.
- body: rounded rectangle (8,14)-(40,42), corner radius 4.
- masts: x=12 and x=36, i.e. the tangent points of the top corner arcs, from
  the body top (y=14) up to the bars (y=6); shared nodes, declared connect.
- rotors: bars 6..18 and 30..42 at y=6, each split at its mast (T joint).
- lens: 4-cardinal-arc ring r5 at (24,28), 9 from the top/bottom walls and
  11 from the side walls (a curve against a wall must clear 9, not exactly 8).
Keyshape: SQUARE, not the suggested HRECT_M. A ring lens (r>=4 to keep its
hole) needs 9 clear on each side, so the body is at least 26 tall, and the
rotor bars need 8 above the body top: 34+ units of height. HRECT_M gives 28,
HRECT_L 32 (tried: lens gap exactly 8 came back `review`). The body is too wide
for the trace's side arms, since outboard masts need 8 from the side walls.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4, every gap budgeted for it.
- keyshape-short-axis: every extreme sits on the SQUARE box (6..42 both axes).
- clearance e0/e3, e1/e4 (rotor bar 2 above the arm post): masts now join the
  bars at a shared node (T joint) instead of stopping just below them.
- clearance e0/e2, e1/e2 (rotor bar 5.8 from the body corner): bars now sit
  8 above the body top on straight runs.
- clearance e2/e5, e3/e5, e4/e5 (lens 1.7-4.5 from body and arms): lens 9
  from every body wall; arm joints no longer sit next to the lens.
- holes at (19.3,23.5), (28.6,23.5) and (23.9,25.9) (0.8-1.5 wide): the
  arm/body/lens slivers are gone; the body interior is open and the lens is
  an r5 ring (small-circle rule).
Not kept: the trace's wide 3:1 proportions and its side arms (see keyshape).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d66af9da-0871-557c-abb0-a240e310287a"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1935-camera-drone-front/camera-drone-front_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                     # mirror axis
L, T, R, B = 8, 14, 40, 42  # body centerline box
CR = 4                      # body corner radius
BAR_Y = 6                   # rotor bars (8 above the body top)
MAST_X = L + CR             # masts rise from the corner tangent points
BAR_HALF = 6                # rotor half-length
LENS_R = 5
LENS_CY = 28


class CameraDroneFrontRedraw(Solo48):
    icon_id = "camera-drone-front-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("drone", "quadcopter", "camera drone")
    keywords = ("drone", "camera", "quadcopter", "uav", "aerial", "propeller", "lens")

    def build(self) -> None:
        ml, mr = MAST_X, 2 * AX - MAST_X
        self.add_line("top", (ml, T), (mr, T))
        self.add_arc("c-tr", (mr, T), (R, T + CR), radius_x=CR, sweep=True)
        self.add_line("right", (R, T + CR), (R, B - CR))
        self.add_arc("c-br", (R, B - CR), (R - CR, B), radius_x=CR, sweep=True)
        self.add_line("bottom", (R - CR, B), (L + CR, B))
        self.add_arc("c-bl", (L + CR, B), (L, B - CR), radius_x=CR, sweep=True)
        self.add_line("left", (L, B - CR), (L, T + CR))
        self.add_arc("c-tl", (L, T + CR), (ml, T), radius_x=CR, sweep=True)
        self.add_contour("body", "top", "c-tr", "right", "c-br", "bottom", "c-bl", "left", "c-tl", closed=True)

        for side, x in (("l", ml), ("r", mr)):
            self.add_line(f"bar-{side}-a", (x - BAR_HALF, BAR_Y), (x, BAR_Y))
            self.add_line(f"bar-{side}-b", (x, BAR_Y), (x + BAR_HALF, BAR_Y))
            self.add_contour(f"rotor-{side}", f"bar-{side}-a", f"bar-{side}-b")
            self.add_line(f"mast-{side}", (x, BAR_Y), (x, T))
            self.relate("connect", f"mast-{side}", f"rotor-{side}")
            self.relate("connect", f"mast-{side}", "body")

        cx, cy, r = AX, LENS_CY, LENS_R
        self.add_arc("lens-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("lens-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("lens-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("lens-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("lens", "lens-1", "lens-2", "lens-3", "lens-4", closed=True)
