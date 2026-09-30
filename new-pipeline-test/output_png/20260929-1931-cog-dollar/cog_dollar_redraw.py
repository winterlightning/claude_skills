"""cog-dollar (redraw of the new-pipeline traced SVG).

Plan: a six-tooth cog with a dollar sign in its hub, on CIRCLE (every
centerline point within radius 20 of (24,24)). The cog and the dollar are
both mirror/point symmetric about (24,24).
- cog: one closed contour. Six teeth at 90/30/330/270/210/150 degrees, as in
  the generated image (one on top, one at the bottom, four diagonal). Each
  tooth has a base 8 wide on the hub (radius ~16.5) and a flat tip at radius
  ~19.9. The four diagonal teeth are the upper-right tooth mirrored about
  both axes. Their 60-degree positions are rounded to integer points, with
  the tooth sides kept parallel. Between the teeth, six valley arcs of radius
  17 bulge outward and join the tooth sides at the tooth-base corners.
- dollar: an open S contour, 18..30 tall and 20..28 wide. A top hook arc of
  r5 ending at (28,20) (a 3-4-5 point) meets two semi-ellipse bowls (rx 4,
  ry 3), which cross at the centre with a horizontal tangent, and a bottom
  hook ends at (20,28) as the point mirror. All joins are tangent-continuous.
- stem: two stubs, (24,15)-(24,18) and (24,30)-(24,33), which share the S
  top/bottom nodes and are declared connected. A full stem through the S
  would split each bowl into openings about 4 wide, so it stops at the S.
Construction: the Lucide settings / circle-dollar-sign pattern (round hub
with flat teeth; stacked-bowl S), and the in-set cog-dollar module's S that
stops at shared nodes with its stem stubs (the idea only, not its numbers).
The local Lucide originals were not opened.

Metric issues (cog-dollar_metrics.json):
- stroke-width (info): redrawn at stroke 4, and every gap is budgeted for it.
- stroke-count (warn, 8 > 6): now 4 strokes (the cog contour, the S
  contour and two stem stubs that join the S), within the budget of 6.
- clearance e0/e4 and e1/e4 (stem 6.36 from the cog): the stem ends at
  y 15 / 33, 8.06 from the nearest tooth-base corners (20,8)/(28,8) and
  (20,40)/(28,40).
- clearance e1/e5 (S 7.97 from the cog): the S hook end (28,20) is 10.6
  from the nearest tooth corner (36,13) and about 11 from the valley arc.
- clearance e4/e5 (stem crossing the S, 0.0): the stem no longer crosses the
  S. The stubs meet it at shared nodes (24,18) and (24,30), declared with
  connect.
- clearance e5/e6 (upper S 2.22 from lower S): the S is one tangent-
  continuous contour through (24,24), so there is no gap between two parts.
- loose-join e0/e1 x2 (1.27 short): the cog is one closed contour, and every
  tooth side shares an exact endpoint with its valley arc.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fa84ff77-a565-4df3-9360-0b7e9c3de772"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1931-cog-dollar/cog-dollar_raw.svg"
AUTHOR = "claude-opus-5-5"

C = 24                          # cog and dollar centre
VALLEY_R = 17                   # valley arc radius (hub corners sit at ~16.5)
# Upper-right quadrant of the cog outline, clockwise from the top tooth's
# right tip, offsets from C. Tooth sides are parallel pairs; bases are 8 wide.
TOP_TIP, TOP_BASE = (4, -19), (4, -16)           # top tooth, right side
DIAG = ((12, -11), (15, -13), (19, -6), (16, -4))  # upper-right tooth: base, tip, tip, base
S_TOP, S_MID, S_BOT = 18, 24, 30                 # S nodes on the stem axis
BOWL_RX, BOWL_RY = 4, 3
HOOK_R = 5                                       # hook arc, 3-4-5 end point
STEM = 3                                         # stub length past the S


class CogDollarRedraw(Solo48):
    icon_id = "cog-dollar-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "money"
    aliases = ("gear dollar", "money settings", "cost settings")
    keywords = ("cog", "gear", "dollar", "money", "finance", "settings", "cost", "billing", "payment")

    def _outline(self):
        """Closed cog node list, clockwise from the top tooth's left tip."""
        quarter = [TOP_TIP, TOP_BASE, *DIAG]          # top-right quadrant, top to right
        right = quarter + [(x, -y) for x, y in reversed(quarter)]   # mirror to the bottom
        full = right + [(-x, y) for x, y in reversed(right)]        # mirror to the left
        return [(C + x, C + y) for x, y in full]

    @staticmethod
    def _is_base(p):
        return (p[0] - C) ** 2 + (p[1] - C) ** 2 < VALLEY_R ** 2

    def build(self) -> None:
        pts = self._outline()
        members = []
        for i, a in enumerate(pts):
            b = pts[(i + 1) % len(pts)]
            name = f"cog-{i:02d}"
            # A segment between two tooth-base corners is a valley arc.
            if self._is_base(a) and self._is_base(b):
                self.add_arc(name, a, b, radius_x=VALLEY_R, sweep=True)
            else:
                self.add_line(name, a, b)
            members.append(name)
        self.add_contour("cog", *members, closed=True)

        top, mid, bot = (C, S_TOP), (C, S_MID), (C, S_BOT)
        hook_end = (C + 4, S_TOP + HOOK_R - 3)                 # (28,20) on the r5 circle
        tail_end = (C - 4, S_BOT - HOOK_R + 3)                 # (20,28), point mirror
        self.add_arc("s-hook", hook_end, top, radius_x=HOOK_R, sweep=False)
        self.add_arc("s-upper", top, mid, radius_x=BOWL_RX, radius_y=BOWL_RY, sweep=False)
        self.add_arc("s-lower", mid, bot, radius_x=BOWL_RX, radius_y=BOWL_RY, sweep=True)
        self.add_arc("s-tail", bot, tail_end, radius_x=HOOK_R, sweep=True)
        self.add_contour("s", "s-hook", "s-upper", "s-lower", "s-tail")

        self.add_line("stem-top", (C, S_TOP - STEM), top)
        self.add_line("stem-bottom", bot, (C, S_BOT + STEM))
        self.relate("connect", "s", "stem-top")
        self.relate("connect", "s", "stem-bottom")
