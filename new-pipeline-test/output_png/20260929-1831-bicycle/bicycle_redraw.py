"""bicycle (redraw of the new-pipeline traced SVG).

Plan: side-view diamond-frame bicycle facing right, on HRECT_L (centerline box
(4,8)-(44,40)).
- wheels: two equal 4-arc circles, r5, hubs (9,35) and (39,35); r5 is the
  smallest radius whose 6-unit ink hole passes and whose rim has integer points
  off the axes (3-4-5), used for the stay and fork joints.
- frame: one closed main triangle -- top tube S(15,16)-H(33,16), seat tube and
  down tube meeting at the bottom bracket B(24,31). The tubes mirror each other
  about x=24 (slope 3:5); inradius 5.1, so the opening is 6.2 in ink.
- seat stay S -> rear rim (12,31) and fork H -> front rim (36,31) mirror each
  other (slope 1:5). The frame joins the rims, never the hubs: a spoke to a hub
  closes a wheel's opening at any radius below 10.
- seat post and stem lean back at a shared 1:4 slope to y=8; a flat saddle
  (9..17) sits exactly 8 above the top tube; the handlebar runs forward from
  the stem and hooks down (r3), the hook end 8.6 from the head joint.
- the rear triangle is left open (no chain stay): closing it between the rim,
  seat stay and seat tube gives a 4-unit opening at best.
Lucide `bike` informed the equal round wheels; the generated PNG gave the
diamond frame, rear-leaning seat post and the hooked handlebar.

Metric issues (bicycle_metrics.json):
- clearance errors (12; wheels, frame, saddle and bar fused or crossing in the
  trace): fixed -- touching parts share integer endpoints and are declared
  `connect`; nothing crosses a rim; the bracket clears both rims by 10.5 and the
  down/seat tubes clear them by 9.9.
- holes 2.8 / 3.05 / 3.01 inscribed: fixed -- the wheels are 6 in ink, the main
  triangle is 6.2; the rear triangle is open.
- loose-join e4/e6: fixed -- every joint is an exact shared endpoint.
- keyshape-short-axis (HRECT_M, y filled 67%): fixed by choosing HRECT_L, not
  by stretching. HRECT_M leaves 28 units of height; saddle (8 above the top
  tube) plus a diamond with a 6-unit opening plus the wheels needs 32. All four
  HRECT_L extremes are reached: rear rim x=4, front rim x=44, saddle and bar
  y=8, both rims y=40.
- stroke-count 8 vs 6: fixed -- 2 wheels, frame, saddle + post, stem + bar.
- stroke-width (trace 2.65): redrawn at stroke 4.
Not kept: the hub-to-hub rear triangle and the fork reaching the front hub
(see above) -- the frame ends on the rims instead.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e02193de-f02e-5d27-b1d4-4c69559daeda"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1831-bicycle/bicycle_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
R = 5
WHEEL_Y = 35
REAR_X, FRONT_X = 9, 39                     # mirrored about x=24
TOP_Y = 16                                  # top tube
HALF_TOP = 9
SEAT = (AXIS - HALF_TOP, TOP_Y)             # (15,16)
HEAD = (AXIS + HALF_TOP, TOP_Y)             # (33,16)
BRACKET = (AXIS, 31)
STAY_JOINT = (REAR_X + 3, WHEEL_Y - 4)      # (12,31) on the rear rim
FORK_JOINT = (FRONT_X - 3, WHEEL_Y - 4)     # (36,31) on the front rim
TOP = 8                                     # saddle and bar height
POST_TOP = (SEAT[0] - 2, TOP)               # (13,8), slope 1:4
STEM_TOP = (HEAD[0] - 2, TOP)               # (31,8), slope 1:4
SADDLE = ((POST_TOP[0] - 4, TOP), (POST_TOP[0] + 4, TOP))
BAR_END = (37, TOP)
HOOK_R = 3


class BicycleRedraw(Solo48):
    icon_id = "bicycle-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ("bike", "road bike")
    keywords = ("bicycle", "bike", "cycling", "diamond frame", "transport", "sport")

    def _wheel(self, name: str, cx: int, cy: int, *nodes: tuple[int, int]) -> None:
        """Circle split at the given rim nodes (plus the four cardinals), clockwise."""
        pts = {(cx, cy - R), (cx + R, cy), (cx, cy + R), (cx - R, cy), *nodes}
        ordered = sorted(pts, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
        members = []
        for i, a in enumerate(ordered):
            b = ordered[(i + 1) % len(ordered)]
            pid = f"{name}-{i + 1}"
            self.add_arc(pid, a, b, radius_x=R, sweep=True)
            members.append(pid)
        self.add_contour(name, *members, closed=True)

    def build(self) -> None:
        self._wheel("rear-wheel", REAR_X, WHEEL_Y, STAY_JOINT)
        self._wheel("front-wheel", FRONT_X, WHEEL_Y, FORK_JOINT)

        # Main triangle: top tube, down tube, seat tube.
        self.add_polyline("frame", SEAT, HEAD, BRACKET, closed=True)

        # Seat stay and fork, mirrored, ending on the rims.
        self.add_line("seat-stay", SEAT, STAY_JOINT)
        self.add_line("fork", HEAD, FORK_JOINT)
        self.relate("connect", "seat-stay", "frame")
        self.relate("connect", "seat-stay", "rear-wheel")
        self.relate("connect", "fork", "frame")
        self.relate("connect", "fork", "front-wheel")

        # Seat post and flat saddle.
        self.add_line("seat-post", SEAT, POST_TOP)
        self.add_line("saddle-rear", SADDLE[0], POST_TOP)
        self.add_line("saddle-nose", POST_TOP, SADDLE[1])
        self.add_contour("saddle", "saddle-rear", "saddle-nose")
        self.relate("connect", "seat-post", "frame")
        self.relate("connect", "seat-post", "saddle")

        # Stem and forward handlebar with a downward hook.
        self.add_line("stem", HEAD, STEM_TOP)
        self.add_line("bar", STEM_TOP, BAR_END)
        self.add_arc("bar-hook", BAR_END, (BAR_END[0] + HOOK_R, TOP + HOOK_R),
                     radius_x=HOOK_R, sweep=True)
        self.add_contour("handlebar", "stem", "bar", "bar-hook")
        self.relate("connect", "handlebar", "frame")
