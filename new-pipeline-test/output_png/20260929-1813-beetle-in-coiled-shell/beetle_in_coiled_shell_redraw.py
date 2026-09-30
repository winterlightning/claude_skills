"""beetle-in-coiled-shell (redraw of the new-pipeline traced SVG).

Plan: a side-view bug carrying a coiled shell, facing right, on HRECT_L
(centerline box (4,8)-(44,40)).
- shell: the coil *is* the shell, one spiral turning clockwise on screen all
  the way in. Outer r13 about A=(17,21) from the rear tip (5,26) up the back
  (4,21), over the top (17,8) to the front (30,21); a lower arm (circle-like
  cubics about B=(21.5,21), r 8.5..9.6) from the front under the body through
  the two hips back to (13,21); then the inner r4 curl about A over the top
  to (21,21). Facing turns are 9 apart (r13 vs r4 on top; curl tip 8 from
  the arm's centre line only at B, same contour).
- head: a r5 ring about H=(35,21), tangent to the shell front at (30,21)
  (the trace's oval head; r5 keeps its hole at 6).
- antennae: a V from the head's far side (38,17) = H+(3,-4) to (35,8) and
  (44,11); 8.4+ apart beyond 8 of the root, 8.2+ from the shell.
- legs: two L-shaped legs like the image (shin + forward foot): rear from hip
  (15,28) to heel (13,40), toe (17,40); front from hip (24,30) to heel
  (26,40), toe (30,40).
Extremes: x 4 (shell back) / 44 (antenna tip), y 8 (shell top, antenna tip)
/ 40 (feet).

Keyshape: HRECT_L, not the suggested SQUARE. Metrics give SQUARE fill
x 1.0 / y 0.86 and HRECT_L x 0.93 / y 1.0; at stroke 4 the subject needs
shell 26 + head 10 + antenna spread, 40 wide, which SQUARE's 36 cannot hold,
and the 32 height takes the shell plus short bent legs.

Metric issues:
- stroke-width (info): drawn at stroke 4; every gap budgeted for it.
- stroke-count (12, budget 6): now 6 (shell coil, head, two antennae, two
  legs); the trace's split leg segments and doubled head/shell outlines are
  single strokes.
- keyshape-short-axis (SQUARE y fill 86%): fixed by HRECT_L; all four
  extremes lie on its box exactly.
- clearance e0/e7, e1/e7, e2/e7, e3/e7, e5/e7, e6/e7, e7/e8.. (the spiral
  crowding the shell wall, head and legs 1.5-7.9 apart): fixed, spiral and
  shell are one coil, turns 9 apart, curl 9 from the head.
- clearance e1/e2, e1/e5 (antennae 2.6 apart and 6.5 from the shell): fixed,
  the antennae share a root on the head's far side and fan out, 8.4+ apart
  beyond 8 of the root (tips 9.5), 8.2+ from the shell.
- clearance e3/e9, e3/e11, e4/e11, e5/e8, e5/e9, e5/e11, e6/e8.. (leg
  segments and the shell bottom 2.6-7.8 apart): fixed, each leg is one
  shin + foot polyline hanging from the lower arm, legs 8.8+ apart.
- holes 4.56 / 1.34 / 3.16 inscribed (need 6): the head ring is r5 (6
  inscribed); the shell interior is open to the coil, so no small pockets.
- not fixable in svg_metrics.py: re-run on this redraw it reports shell and
  head 0 apart. They touch on purpose (tangent at (30,21), declared connect,
  validator valid); the script only finds joins at path endpoints, and here
  the head's endpoint meets the middle of the shell path.
Lucide: snail informed the nested-arc spiral shell (arcs about alternating
centres) and the tangent head; rebuilt with 9-unit turn spacing.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e6e35530-888b-4ddb-ab14-ab2f3f1591c8"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1813-beetle-in-coiled-shell/"
    "beetle-in-coiled-shell_raw.svg"
)
AUTHOR = "claude-opus-5-5"

A = (17, 21)          # coil centre: outer r13 and inner r4 arcs
R_OUT = 13
R_IN = 4
B = (21.5, 21)        # lower arm centre (A shifted 4.5 towards the front)
REAR_TIP = (5, 26)    # A + (-12, 5): outer turn's free end
BACK = (4, 21)        # A - (13, 0)
FRONT = (30, 21)      # A + (13, 0): shell front, head tangent point
ARM_END = (13, 21)    # A - (4, 0): lower arm -> inner curl
CURL_TIP = (21, 21)   # A + (4, 0)
FRONT_HIP = (24, 30)
REAR_HIP = (15, 28)
HEAD = (35, 21)
R_HEAD = 5
ANT_ROOT = (38, 17)   # HEAD + (3, -4), the side away from the shell
GROUND = 40


def arm_segments(knots):
    """Cubics running clockwise on screen about B through integer knots,
    tangent to the local circle at every knot."""
    segs = []
    for p, q in zip(knots, knots[1:]):
        ap = math.atan2(p[1] - B[1], p[0] - B[0])
        aq = math.atan2(q[1] - B[1], q[0] - B[0])
        if aq < ap:
            aq += 2 * math.pi
        rp = math.hypot(p[0] - B[0], p[1] - B[1])
        rq = math.hypot(q[0] - B[0], q[1] - B[1])
        k = 4 / 3 * math.tan((aq - ap) / 4)
        c1 = (p[0] - k * rp * math.sin(ap), p[1] + k * rp * math.cos(ap))
        c2 = (q[0] + k * rq * math.sin(aq), q[1] - k * rq * math.cos(aq))
        segs.append((tuple(round(v, 3) for v in c1), tuple(round(v, 3) for v in c2), q))
    return segs


class BeetleInCoiledShellRedraw(Solo48):
    icon_id = "beetle-in-coiled-shell-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/insects"
    aliases = ("shell-beetle", "coiled-shell-bug")
    keywords = ("beetle", "shell", "spiral", "coil", "insect", "bug", "snail")

    def build(self) -> None:
        # Shell coil: rear tip -> back -> over the top -> front -> lower arm -> curl.
        self.add_arc("shell-rear", REAR_TIP, BACK, radius_x=R_OUT, sweep=True)
        self.add_arc("shell-top", BACK, FRONT, radius_x=R_OUT, sweep=True)
        segs = arm_segments([FRONT, FRONT_HIP, REAR_HIP, ARM_END])
        self.add_bezier("shell-arm-front", FRONT, segs[0])
        self.add_bezier("shell-arm-mid", FRONT_HIP, segs[1])
        self.add_bezier("shell-arm-back", REAR_HIP, segs[2])
        self.add_arc("shell-curl", ARM_END, CURL_TIP, radius_x=R_IN, sweep=True)
        self.add_contour(
            "shell", "shell-rear", "shell-top", "shell-arm-front",
            "shell-arm-mid", "shell-arm-back", "shell-curl",
        )

        # Head ring, split at the shell tangent point and the antenna root.
        self.add_arc("head-top", FRONT, ANT_ROOT, radius_x=R_HEAD, sweep=True)
        self.add_arc("head-rest", ANT_ROOT, FRONT, radius_x=R_HEAD,
                     large_arc=True, sweep=True)
        self.add_contour("head", "head-top", "head-rest", closed=True)
        self.relate("connect", "head", "shell")

        self.add_line("antenna-rear", ANT_ROOT, (35, 8))
        self.add_line("antenna-front", ANT_ROOT, (44, 11))
        self.relate("connect", "antenna-rear", "head")
        self.relate("connect", "antenna-front", "head")
        self.relate("connect", "antenna-rear", "antenna-front")

        # Legs: shin down to the heel, foot forward.
        self.add_polyline("leg-rear", REAR_HIP, (13, GROUND), (17, GROUND))
        self.add_polyline("leg-front", FRONT_HIP, (26, GROUND), (30, GROUND))
        for leg in ("leg-rear", "leg-front"):
            self.relate("connect", leg, "shell")
