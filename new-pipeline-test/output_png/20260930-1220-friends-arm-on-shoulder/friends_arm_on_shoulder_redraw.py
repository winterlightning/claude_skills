"""friends-arm-on-shoulder (redraw of the new-pipeline traced SVG).

Plan: two head-and-shoulder busts side by side on HRECT_M (centerline box
(4,10)-(44,38)), Lucide `users`-style shoulders, with the left friend's arm
draped down onto the right friend's near shoulder.
- busts: one repeat definition (flat standalone shoulder line split at the neck,
  r5 corner arcs, vertical sides to the bottom extreme y=38), 14 wide, placed at
  axis x=11 / x=37 so the outer sides hit x=4 / x=44 and the inner sides sit
  12 apart. The right friend stands 3 lower (shoulder y=31 vs 28): at equal
  heights the arm merged with the two shoulder lines and the pair read as "mm".
- heads: 4-cardinal-arc r5 circles straight above each neck, outline exactly 8
  above its own shoulder line (4 units of ink); the left head top is y=10.
- arm: one cubic from the 3-4-5 lattice node (16,29) on the left friend's inner
  corner to the node (32,32) on the right friend's inner corner (the hand).
  Both corners are split at those nodes, so the arm shares exact endpoints; it
  leaves and arrives at 2:1 slopes, 63 degrees to each corner arc.
Reference: icon_set/references/human_ref/user.svg (detached head over open
rounded shoulders, 8-unit centerline gap); Lucide `users` / `user` for the
flat-topped rounded shoulder construction.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap was budgeted at stroke 4.
- keyshape-short-axis: extremes sit on the HRECT_M box exactly (left head top
  y=10, bust feet y=38, outer sides x=4 / x=44) instead of stretching the trace.
- clearance e0-e3 / e1-e2 (heads vs shoulders 2.9): each head outline is now
  exactly 8 above its shoulder line (certified detached head gap).
- clearance e0-e4 / e1-e4 (arm vs heads 5.5 / 2.9): the arm stays >= 9.7 from
  both head outlines.
- clearance e2-e3 (bust feet 6.5 apart): the inner sides are 12 apart.
- narrow-join e4-e2 (27 degrees) and loose-join e4-e2 (1.44 short): the hand
  ends on the corner arc's own node at 63 degrees, declared with connect.
- no-head: the heads are true circles, marked with mark_human_figure.
None left unfixed. validate_icon(): valid, no warnings; build_gate: PASS.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fc3c63fc-721e-43dd-a5cf-cb7496abf926"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1220-friends-arm-on-shoulder/"
    "friends-arm-on-shoulder_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HEAD_R = 5                # head centerline radius
HEAD_GAP = 8              # head outline to shoulder line, centerlines (4 ink)
FOOT = 38                 # bottom extreme
HALF = 7                  # half bust width
CORNER = 5                # shoulder corner radius
# One bust definition, two placements: (axis x, shoulder-line y).
BUSTS = {"left": (11, 28), "right": (37, 31)}
DROP = 3                  # arm leave/arrive slope 2:1 (63 degrees to the corner)


def inner_node(n: str) -> tuple[int, int]:
    """3-4-5 lattice point on the inner (friend-facing) shoulder corner."""
    ax, top = BUSTS[n]
    d = +1 if n == "left" else -1
    return (ax + d * (HALF - CORNER + 3), top + CORNER - 4)


class FriendsArmOnShoulderRedraw(Solo48):
    icon_id = "friends-arm-on-shoulder-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people"
    aliases = ("friends", "friendship", "buddies", "arm around shoulder")
    keywords = ("friends", "friendship", "people", "support", "together", "hug", "team")

    def build(self) -> None:
        for n in BUSTS:
            self.bust(n)
        # Arm: out of the left friend's inner shoulder, draped down onto the
        # right friend's inner shoulder (the hand).
        a, b = inner_node("left"), inner_node("right")
        self.add_bezier("arm", a, ((a[0] + 2 * 2, a[1] - 2), (b[0] - 2 * DROP, b[1] - DROP), b))
        self.relate("connect", "arm", "left-shoulder-in")
        self.relate("connect", "arm", "right-shoulder-in")

    def bust(self, n: str) -> None:
        ax, top = BUSTS[n]
        cy, r = top - HEAD_GAP - HEAD_R, HEAD_R
        pts = [(ax - r, cy), (ax, cy - r), (ax + r, cy), (ax, cy + r), (ax - r, cy)]
        for i in range(4):
            self.add_arc(f"{n}-head-{i}", pts[i], pts[i + 1], radius_x=r, sweep=True)
        self.add_contour(f"{n}-head", *(f"{n}-head-{i}" for i in range(4)), closed=True)

        inner = +1 if n == "left" else -1
        for d in (-1, +1):
            s = "in" if d == inner else "out"
            top_end = (ax + d * (HALF - CORNER), top)
            side_top = (ax + d * HALF, top + CORNER)
            sweep = d > 0  # corner runs from the shoulder line down to the side
            self.add_line(f"{n}-top-{s}", (ax, top), top_end)
            self.add_line(f"{n}-side-{s}", side_top, (ax + d * HALF, FOOT))
            if s == "in":
                # Split the corner where the arm attaches so both share the node.
                mid = inner_node(n)
                self.add_arc(f"{n}-corner-in-a", top_end, mid, radius_x=CORNER, sweep=sweep)
                self.add_arc(f"{n}-corner-in-b", mid, side_top, radius_x=CORNER, sweep=sweep)
                parts = (f"{n}-corner-in-a", f"{n}-corner-in-b", f"{n}-side-in")
            else:
                self.add_arc(f"{n}-corner-out", top_end, side_top, radius_x=CORNER, sweep=sweep)
                parts = (f"{n}-corner-out", f"{n}-side-out")
            self.add_contour(f"{n}-shoulder-{s}", *parts)
        self.relate("connect", f"{n}-top-in", f"{n}-top-out")
        self.relate("connect", f"{n}-top-in", f"{n}-shoulder-in")
        self.relate("connect", f"{n}-top-out", f"{n}-shoulder-out")
        self.mark_human_figure(f"friend-{n}", head=f"{n}-head", torso=f"{n}-top-in",
                               torso_junction="start")
