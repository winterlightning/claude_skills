"""beetle-in-coiled-shell (redraw of the new-pipeline traced SVG).

Plan: a side-view beetle whose back is a coiled shell, on HRECT_M
(centerline box (4,10)-(44,38)).
- shell: the coil *is* the shell. One spiral turning the same way all
  along: outer r13 top arc about A=(31,23) from its rear tip (43,28) over
  the top (31,10) to the front (18,23); a lower arm (circle-like cubics
  about (26.5,23), r~8.5) from (18,23) under the body to (35,23); then the
  inner r4 curl about A back to (27,23). Arms facing each other are 9 apart
  (r13 vs r4) and the curl tip sits 8+ from the lower arm.
- head: a r5 ring about (13,23), tangent to the shell front at (18,23).
- antennae: a V from the head at (10,19), to (4,13) and (13,10), spread 63 deg so
  they stay 8+ apart past the root.
- legs: three short diagonal legs, front and middle from the lower arm,
  rear from the outer arc's tip; feet on y=38, splayed so they stay 8+ apart.
Traced shape: 20260928-1657-beetle-in-coiled-shell/beetle-in-coiled-shell_raw.svg
(read for the subject only; nothing copied from its coordinates).
No useful Lucide match: lucide/snail informed the half-turn-arc spiral
(arcs with alternating centres), rebuilt with 8+ gaps between turns.

Metric issues:
- clearance e0/e4 (front leg 4.1 from the head): fixed, the front leg hangs
  from the shell's lower arm 8.6 from the head.
- clearance e1/e2, e1/e7, e2/e7 (antennae crowd each other and the shell):
  fixed, the antennae share one root on the head's far side and fan away
  from the shell (8+ from it).
- clearance e3/e6, e4/e5 (paired legs 4-5 apart): fixed, four crowded legs
  become three legs with 8+ between attachments and feet.
- clearance e3/e8, e5/e8, e6/e8, e7/e8 and narrow-join e8/e7 (spiral fused
  into the shell at 13.8 deg, legs touching it): fixed, the spiral and the
  shell are one continuous coil, so no separate spiral meets the shell wall.
- holes (5.6 and 4.56 inscribed, need 6): the head ring is r5 (6 inscribed)
  and the shell interior is open to the coil, so no closed pocket remains.
- loose-join e1/e0 (antenna 0.38 short of the head): fixed, the antennae
  start on the head's integer point (10,19) and connect.
- keyshape-short-axis (x fill 96%): fixed, antenna tip on x=4 and shell on
  x=44 reach the HRECT_M box exactly.
- stroke-count (9 strokes, budget 6): reduced to 7 (shell coil, head, two
  antennae, three legs), not 6. Drawing the antennae as one V polyline gives 6,
  but svg_metrics.py then no longer sees the antennae touching the head (it
  checks endpoints only) and reports a false clearance error.
- not fixable in svg_metrics.py: it reports head/shell as 0 apart, but they
  touch on purpose at (18,23), declared connect (validator: valid). The
  script only finds joins at endpoints; this tangent contact is a head
  endpoint meeting the middle of the shell's path.
- stroke-width (info): drawn at stroke 4; all gaps budgeted for 4.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e6e35530-888b-4ddb-ab14-ab2f3f1591c8"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1657-beetle-in-coiled-shell/"
    "beetle-in-coiled-shell_raw.svg"
)
AUTHOR = "claude-opus-5-5"

A = (31, 23)          # coil centre: outer r13 and inner r4 arcs
R_OUT = 13
R_IN = 4
B = (26.5, 23)        # lower arm centre (between the outer and inner turns)
FRONT = (18, 23)      # A - (13, 0): shell front, head tangent point
REAR_TIP = (43, 28)   # A + (12, 5): outer turn's free end
RIGHT = (44, 23)      # A + (13, 0)
ARM_END = (35, 23)    # A + (4, 0): lower arm -> inner curl
CURL_TIP = (27, 23)   # A - (4, 0)
FRONT_HIP = (24, 31)
MID_HIP = (32, 29)
HEAD = (13, 23)
R_HEAD = 5
ANT_ROOT = (10, 19)   # HEAD + (-3, -4)


def arm_segments(knots):
    """Cubics running clockwise-negative (counter-clockwise on screen) about B
    through integer knots, tangent to the circle at every knot."""
    segs = []
    for p, q in zip(knots, knots[1:]):
        ap = math.atan2(p[1] - B[1], p[0] - B[0])
        aq = math.atan2(q[1] - B[1], q[0] - B[0])
        rp = math.hypot(p[0] - B[0], p[1] - B[1])
        rq = math.hypot(q[0] - B[0], q[1] - B[1])
        d = aq - ap
        k = 4 / 3 * math.tan(d / 4)
        c1 = (p[0] - k * rp * math.sin(ap), p[1] + k * rp * math.cos(ap))
        c2 = (q[0] + k * rq * math.sin(aq), q[1] - k * rq * math.cos(aq))
        segs.append((tuple(round(v, 3) for v in c1), tuple(round(v, 3) for v in c2), q))
    return segs


class BeetleInCoiledShellRedraw(Solo48):
    icon_id = "beetle-in-coiled-shell-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/insects"
    aliases = ("shell-beetle", "coiled-shell-bug")
    keywords = ("beetle", "shell", "spiral", "coil", "insect", "bug", "snail")

    def build(self) -> None:
        # Shell coil: rear tip -> right -> over the top -> front -> lower arm -> curl.
        self.add_arc("shell-rear", REAR_TIP, RIGHT, radius_x=R_OUT, sweep=False)
        self.add_arc("shell-top", RIGHT, FRONT, radius_x=R_OUT, sweep=False)
        segs = arm_segments([FRONT, FRONT_HIP, MID_HIP, ARM_END])
        self.add_bezier("shell-arm-front", FRONT, segs[0])
        self.add_bezier("shell-arm-mid", FRONT_HIP, segs[1])
        self.add_bezier("shell-arm-back", MID_HIP, segs[2])
        self.add_arc("shell-curl", ARM_END, CURL_TIP, radius_x=R_IN, sweep=False)
        self.add_contour(
            "shell", "shell-rear", "shell-top", "shell-arm-front",
            "shell-arm-mid", "shell-arm-back", "shell-curl",
        )

        # Head ring, split at the shell tangent point and the antenna root.
        self.add_arc("head-top", FRONT, ANT_ROOT, radius_x=R_HEAD, sweep=False)
        self.add_arc("head-rest", ANT_ROOT, FRONT, radius_x=R_HEAD,
                     large_arc=True, sweep=False)
        self.add_contour("head", "head-top", "head-rest", closed=True)
        self.relate("connect", "head", "shell")

        self.add_line("antenna-front", ANT_ROOT, (4, 13))
        self.add_line("antenna-back", ANT_ROOT, (13, 10))
        self.relate("connect", "antenna-front", "head")
        self.relate("connect", "antenna-back", "head")
        self.relate("connect", "antenna-front", "antenna-back")

        self.add_line("leg-front", FRONT_HIP, (20, 38))
        self.add_line("leg-mid", MID_HIP, (34, 38))
        self.add_line("leg-rear", REAR_TIP, (44, 38))
        for leg in ("leg-front", "leg-mid", "leg-rear"):
            self.relate("connect", leg, "shell")
