"""amazon-eventbridge (redraw of the new-pipeline traced SVG).

Plan: event-bus fan-out on HRECT_M (centerline box (4,10)-(44,38)).
- source: one large ring, r8, centre (12,24); its left side is the x=4 extreme.
- targets: two equal r5 rings stacked on a shared axis x=39, centres (39,15)
  and (39,33), mirrored about y=24; their tops/bottoms are the y=10 / y=38
  extremes and their right sides the x=44 extreme. They sit exactly 8 apart
  on centerlines (ink gap 4).
- connector: a level stem from the large ring's right point (20,24) to the
  branch node B=(27,24), then a mirrored Y polyline from B to (35,18) and
  (35,30). Both branch ends lie on the small rings on the radial (-4,+-3)
  direction, so every branch meets its ring square-on, like the generated
  image. Each ring is split at its attachment point so the joins share an
  endpoint and are declared with relate("connect").
No useful Lucide match beyond the ring-and-link construction of `share-2` /
`git-fork`; taken from it only the idea of radial links ending on the rings.

Metric issues fixed:
- stroke-width: redrawn at stroke 4; every gap budgeted at 8 centerline.
- keyshape-short-axis: the large ring now reaches x=4 and the small rings
  x=44, so HRECT_M fills 100% on both axes (the trace filled 95% on x).
- hole at (38.6,14.4) and hole at (38.5,33.5): the small rings grow from
  r4.4 to r5, so each hole is 2*5-4 = 6 inscribed (the minimum); the large
  ring's hole is 12.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "34f87da9-e584-47f7-8fe0-ca66e9aa7da9"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1711-amazon-eventbridge/"
    "amazon-eventbridge_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS_Y = 24
BIG_C, BIG_R = (12, AXIS_Y), 8
SMALL_X, SMALL_R = 39, 5
TOP_C = (SMALL_X, AXIS_Y - 9)
BOTTOM_C = (SMALL_X, AXIS_Y + 9)
NODE = (27, AXIS_Y)
TOP_TIP = (TOP_C[0] - 4, TOP_C[1] + 3)        # on the top ring, radial
BOTTOM_TIP = (BOTTOM_C[0] - 4, BOTTOM_C[1] - 3)  # mirrored


class AmazonEventbridgeRedraw(Solo48):
    icon_id = "amazon-eventbridge-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/cloud"
    aliases = ("eventbridge", "aws eventbridge", "event bus")
    keywords = ("amazon", "aws", "event", "bus", "routing", "fan-out", "cloud", "serverless")

    def ring(self, name, centre, r, *points):
        """Closed clockwise ring through ``points`` (all on the circle)."""
        seq = list(points) + [points[0]]
        members = []
        for i in range(len(points)):
            member = f"{name}-{i + 1}"
            self.add_arc(member, seq[i], seq[i + 1], radius_x=r, sweep=True)
            members.append(member)
        self.add_contour(name, *members, closed=True)

    def build(self) -> None:
        cx, cy, r = *BIG_C, BIG_R
        self.ring("source", BIG_C, r,
                  (cx + r, cy), (cx, cy + r), (cx - r, cy), (cx, cy - r))

        tx, ty, s = *TOP_C, SMALL_R
        self.ring("target-top", TOP_C, s,
                  (tx, ty - s), (tx + s, ty), (tx, ty + s), TOP_TIP, (tx - s, ty))
        bx, by = BOTTOM_C
        self.ring("target-bottom", BOTTOM_C, s,
                  (bx, by - s), (bx + s, by), (bx, by + s), (bx - s, by), BOTTOM_TIP)

        self.add_line("stem", (cx + r, cy), NODE)
        self.add_polyline("fork", TOP_TIP, NODE, BOTTOM_TIP)

        self.relate("connect", "stem", "source")
        self.relate("connect", "stem", "fork")
        self.relate("connect", "fork", "target-top")
        self.relate("connect", "fork", "target-bottom")
