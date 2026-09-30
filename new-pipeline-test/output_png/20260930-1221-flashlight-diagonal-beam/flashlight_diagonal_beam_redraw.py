"""flashlight-diagonal-beam: a handheld flashlight lying on the diagonal,
rounded handle end at the lower left, flared head at the upper right, with
three separate light rays fanning out beyond the lens (redraw of the
new-pipeline traced SVG).

Plan: SQUARE (centerline box (6,6)-(42,42)). The whole drawing is mirrored
about the flashlight axis x+y=48, which runs from the handle cap (11,37)
through the lens centre F=(24,24) toward the top-right corner.
- body: one closed hollow outline. Handle edges on x+y=41 and x+y=55
  (9.9 apart), end cap r5 about (11,37) joined at the 3-4-5 lattice points
  (7,34) / (14,41); the cap touches left 6 and bottom 42. At the neck
  (15,26) / (22,33) the edges flare straight out to the lens corners
  (18,18) / (30,30); the lens is the straight face x=y between them.
- rays: one fan about F. The side rays are vertical (24,12)-(24,6) and
  horizontal (36,24)-(42,24), mirror images of each other; the middle ray
  (32,16)-(36,12) lies on the axis. The side rays reach top 6 and right 42.
  Ray roots sit 8.49 from the lens corners and 8.94 from each other; the
  rays diverge, so those roots are the closest points.

Metric issues fixed by the rebuild:
- clearance e0/e1 (4.49), e1/e3 (4.5): rays re-spaced into a 45-degree
  fan whose roots are 8.94 apart on centerlines (4.94 ink).
- clearance e0/e2 (1.76), e1/e2 (1.91), e2/e3 (2.11): the trace's rays
  started almost on the head; every ray now starts at least 8.49 from
  the body outline.
- stroke-width (2.77): drawn at the profile stroke 4 with gaps budgeted
  for it.
Nothing left unfixed. Trade-offs: to fit three rays at clearance 8 in the
corner, the fan is wider (vertical / diagonal / horizontal) than the
trace's narrow fan, and the head is a little smaller relative to the
handle. The rounded corners of the traced head are carried by round joins.
Lucide: `flashlight` (straight flared head on a tube) informed the head
construction; the rounded tube end follows the repo's 45-degree r5 3-4-5
cap recipe used in the diagonal toothbrush redraw.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "09bf5bce-937c-5250-b9be-605725935c95"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1221-flashlight-diagonal-beam/flashlight-diagonal-beam_raw.svg"
AUTHOR = "claude-opus-5-5"

CAP_R = 5
CAP_C = (11, 37)             # handle end cap centre, on the axis x+y=48


def mirror(p):
    """Reflect about the flashlight axis x+y=48."""
    return (48 - p[1], 48 - p[0])


UPPER_TAIL = (7, 34)         # x+y=41, 3-4-5 from CAP_C
UPPER_NECK = (15, 26)        # x+y=41, x-y=-11
LENS_UPPER = (18, 18)        # lens face x=y
LOWER_TAIL = mirror(UPPER_TAIL)   # (14,41)
LOWER_NECK = mirror(UPPER_NECK)   # (22,33)
LENS_LOWER = mirror(LENS_UPPER)   # (30,30)

SIDE_RAY = ((24, 12), (24, 6))    # upper ray; the lower ray is its mirror
MID_RAY = ((32, 16), (36, 12))    # on the axis


class FlashlightDiagonalBeamRedraw(Solo48):
    icon_id = "flashlight-diagonal-beam-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ("flashlight", "torch", "flashlight beam")
    keywords = ("flashlight", "torch", "light", "beam", "lamp", "outdoors", "camping", "dark")

    def build(self) -> None:
        # Body, clockwise from the handle end along the upper edge.
        self.add_line("handle-upper", UPPER_TAIL, UPPER_NECK)
        self.add_line("flare-upper", UPPER_NECK, LENS_UPPER)
        self.add_line("lens", LENS_UPPER, LENS_LOWER)
        self.add_line("flare-lower", LENS_LOWER, LOWER_NECK)
        self.add_line("handle-lower", LOWER_NECK, LOWER_TAIL)
        self.add_arc("handle-cap", LOWER_TAIL, UPPER_TAIL, radius_x=CAP_R, sweep=True)
        self.add_contour(
            "body", "handle-upper", "flare-upper", "lens", "flare-lower",
            "handle-lower", "handle-cap", closed=True,
        )

        # Light rays fanned about the lens centre.
        self.add_line("ray-upper", *SIDE_RAY)
        self.add_line("ray-middle", *MID_RAY)
        self.add_line("ray-lower", *(mirror(p) for p in SIDE_RAY))
