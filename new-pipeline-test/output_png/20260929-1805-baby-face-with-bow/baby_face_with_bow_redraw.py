"""baby-face-with-bow (redraw of the new-pipeline traced SVG).

Plan: a round baby head with two short vertical eyes and a small smile, and a
two-loop hair bow on top, on VRECT_L (centerline box (8,4)-(40,44)).
- head: one closed contour, a circle of radius 16 about (24,28) built from
  quarter-circle cubics, touching the box at left (8,28), right (40,28) and
  bottom (24,44). It carries two extra knots, (16,14) and (32,14), where the
  bow loops tuck in.
- bow: two mirrored teardrop loops leave the knot (24,12) on top of the head,
  rise to the top extreme (y=4), round over at x=8 / x=40, and run back under
  themselves to tuck behind the head at (16,14) / (32,14). The short head arc
  closes each loop, so the bow reads as tied on the head, pinched at the
  centre. (A first draft tucked lower, at (11,19); it read as bear ears. The
  tuck points sit on the circle to 0.12, so the head keeps its round side and
  stays 8 from the eyes.)
- face: eyes are vertical strokes at x=19 and x=29 (y 22-25); the smile is an
  arc of radius 5 about (24,30) from (20,33) to (28,33), bottoming at (24,35).
Mirrored about x=24 throughout.

Fixed from the trace metrics:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted for it.
- keyshape-short-axis (warn): the head is widened to the full 32-unit box, so
  x=8 and x=40 are both reached exactly; no stretch needed.
- clearance e0/e1 (1.61) and e0/e2, e1/e2 (2.6-2.7): the traced bow loops
  crossed at the knot and nearly touched the head. The loops now share the
  knot and their tuck points with the head and are declared connected.
- clearance e2/e5, e3/e5, e4/e5 (5.0-6.8): the smile sat too close to the
  eyes and the chin. It is now >= 8 from the eyes and 9 from the chin.
- holes at (16.1,9.1) and (32.0,9.0) (5.2-5.3 wide): each bow loop is now
  closed by the head arc and swelled to 6.2 inscribed at stroke 4.
Not kept: the white gap under the bow. With a head of radius 16 (needed to fit
the eyes and smile at 8-unit spacing) the bow's lower edges would have to stay
8 from the head, leaving under 8 units of loop height below y=4; the loops
could not hold a 6-unit hole. The bow therefore sits on the head.
Known trade-off: re-measuring this redraw with svg_metrics.py flags each tuck
as a narrow join (34 deg). Steeper tucks (tried at 45-60 deg) shrink the loop
holes to 5.2-5.5, so the 6-unit holes were kept; the build gate passes.
Lucide `baby` informed the face (round head, short eyes, shallow arc smile).
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "724c83b9-dfbc-417a-b236-a8b1fd9f3b71"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1805-baby-face-with-bow/baby-face-with-bow_raw.svg"
AUTHOR = "claude-opus-5-5"

CX, CY, R = 24, 28, 16
KNOT = (24, 12)          # top of the head; both loops leave from here
TUCK = (16, 14)          # left loop tucks behind the head (mirrored on the right)
EYE_X, EYE_TOP, EYE_BOTTOM = 19, 22, 25
SMILE_R, SMILE_Y = 5, 33


def mirror(p):
    return (2 * CX - p[0], p[1])


def arc_segment(p0, p1):
    """One cubic following the head circle from knot p0 to knot p1."""
    a0 = math.atan2(p0[1] - CY, p0[0] - CX)
    a1 = math.atan2(p1[1] - CY, p1[0] - CX)
    d = a1 - a0
    if d > math.pi:
        d -= 2 * math.pi
    if d < -math.pi:
        d += 2 * math.pi
    k = 4 / 3 * math.tan(d / 4) * R
    c1 = (p0[0] - k * math.sin(a0), p0[1] + k * math.cos(a0))
    c2 = (p1[0] + k * math.sin(a1), p1[1] - k * math.cos(a1))
    return (tuple(round(v, 3) for v in c1), tuple(round(v, 3) for v in c2), p1)


def loop_segments(sign):
    """Left loop for sign=1; the right loop mirrors it."""
    def m(p):
        return p if sign == 1 else mirror(p)
    return (
        (m((21, 8)), m((17, 4)), m((13, 4))),      # rise from the knot to the top
        (m((9.5, 4)), m((8, 7)), m((8, 10.5))),    # round over the outer end
        (m((8, 13.5)), m((11, 15)), m(TUCK)),      # run back under the loop and tuck behind the head
    )


class BabyFaceWithBowRedraw(Solo48):
    icon_id = "baby-face-with-bow-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/faces"
    aliases = ("baby girl", "baby with bow", "infant face")
    keywords = ("baby", "infant", "girl", "bow", "ribbon", "face", "child", "newborn", "cute")

    def build(self) -> None:
        left, right = (CX - R, CY), (CX + R, CY)
        bottom = (CX, CY + R)
        knots = [KNOT, TUCK, left, bottom, right, mirror(TUCK), KNOT]
        segments = [arc_segment(a, b) for a, b in zip(knots, knots[1:])]
        self.add_bezier("head-outline", KNOT, *segments)
        self.add_contour("head", "head-outline", closed=True)
        self.add_bezier("bow-left", KNOT, *loop_segments(1))
        self.add_bezier("bow-right", KNOT, *loop_segments(-1))
        for eye_x in (EYE_X, 2 * CX - EYE_X):
            self.add_line(f"eye-{'left' if eye_x < CX else 'right'}",
                          (eye_x, EYE_TOP), (eye_x, EYE_BOTTOM))
        self.add_arc("smile", (CX - 4, SMILE_Y), (CX + 4, SMILE_Y),
                     radius_x=SMILE_R, sweep=False)
        self.relate("connect", "head", "bow-left")
        self.relate("connect", "head", "bow-right")
        self.relate("connect", "bow-left", "bow-right")
