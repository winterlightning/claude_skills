"""diagonal-broom-with-curving-bristles (redraw of the new-pipeline traced SVG).

Subject: a household broom lying on the diagonal, the handle rising to the
upper right and a flared fan head at the lower left with a gently curved
sweeping edge and one curved bristle line following it.

Plan on SQUARE (the metrics suggestion, fill 1.0/1.0; centerline box
(6,6)-(42,42)). The whole broom is mirrored about the anti-diagonal
x + y = 48, so every head point is paired with (48 - y, 48 - x):
- handle: one straight stroke from the box corner (42,6) down the axis to
  the neck (29,19). The trace's hollow double-line handle collapses to a
  single stroke at 48 px.
- collar: a short edge (26,16)-(32,22) perpendicular to the axis, split at
  the neck so the handle shares its endpoint (connect).
- sides: concave r40 arcs flaring from the collar ends to the bristle tips
  (6,17) and (31,42), the flare of the reference head.
- sweep: one r25 arc about (31,17) between the tips; it sets the left edge
  x=6 and the bottom y=42, the handle sets x=42 and y=6.
- bristle: an r17 arc (17,26)-(22,31), nearly concentric with the sweep
  and 8.4 inside it, 9.5 from the sides and 14 from the collar.

Metric issues:
- clearance e0/e2 (bristle 2.43 from the sweep on centerlines) -> fixed:
  8.36 minimum. Not exactly 8, because the validator cannot certify a
  curved pair at exactly the minimum (an exact concentric r17 returned review).
- hole (5.28 inscribed at the head) -> fixed: the band between the sweep
  and the bristle is 4.4 ink wide and opens into the head's large interior;
  the enclosed head is well over 6 inscribed.
- stroke-width (info, trace 2.77) -> redrawn at stroke 4 with every gap
  budgeted at 8 on centerlines.
Deliberate changes: the head is symmetric about the handle axis. The
reference head is turned slightly downward, but an asymmetric head
left no room for a bristle at 8 clearance. The bristle is shorter than in
the image (7 long) because its ends must clear the flared sides by 8.
Handle-to-head proportion: the head is larger than in the image, because
it is the smallest fan found that still holds an 8-clear bristle. Searched
heads with tips (6,20..28) and sweep r20..24 have no room for it.
Reference: no Lucide broom in the local sources; the construction follows
Lucide's single-stroke handles and a round-join closed head contour.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "63b13e7a-cfd8-40db-80b6-da30f17f8995"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1232-diagonal-broom-with-curving-bristles/"
    "diagonal-broom-with-curving-bristles_raw.svg"
)
AUTHOR = "claude-opus-5-5"


def mirror(p):
    """Reflect about the broom axis, the anti-diagonal x + y = 48."""
    return (48 - p[1], 48 - p[0])


HANDLE_TOP = (42, 6)
NECK = (29, 19)            # collar midpoint on the axis; the handle lands here
COLLAR_END = (26, 16)      # collar end on the upper side; mirror -> (32, 22)
TIP = (6, 17)              # upper bristle tip; mirror -> (31, 42)
SWEEP_R = 25               # sweeping edge, centre (31, 17)
BRISTLE_R = 17             # near-concentric bristle line, 8.4 inside the sweep
BRISTLE_END = (17, 26)     # 16.6 from (31, 17); mirror -> (22, 31)
SIDE_R = 40                # flared sides: concave arcs


class DiagonalBroomWithCurvingBristlesRedraw(Solo48):
    icon_id = "diagonal-broom-with-curving-bristles-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/cleaning"
    aliases = ("broom", "sweeping broom", "cleaning broom")
    keywords = ("broom", "sweep", "sweeping", "cleaning", "bristles", "housework", "chores")

    def build(self) -> None:
        collar_b, tip_b = mirror(COLLAR_END), mirror(TIP)

        # head: collar split at the neck for the handle, two flared sides,
        # one sweeping arc
        self.add_line("collar-a", COLLAR_END, NECK)
        self.add_line("collar-b", NECK, collar_b)
        self.add_arc("side-b", collar_b, tip_b, radius_x=SIDE_R, sweep=False)
        self.add_arc("sweep", tip_b, TIP, radius_x=SWEEP_R)
        self.add_arc("side-a", TIP, COLLAR_END, radius_x=SIDE_R, sweep=False)
        self.add_contour(
            "head", "collar-a", "collar-b", "side-b", "sweep", "side-a", closed=True,
        )

        self.add_line("handle", HANDLE_TOP, NECK)
        self.relate("connect", "handle", "head")

        # one bristle line following the sweep
        self.add_arc("bristle", mirror(BRISTLE_END), BRISTLE_END, radius_x=BRISTLE_R)
