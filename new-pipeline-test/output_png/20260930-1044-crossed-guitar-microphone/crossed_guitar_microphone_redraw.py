"""crossed-guitar-microphone (redraw of the new-pipeline traced SVG).

Plan: an acoustic guitar on the anti-diagonal x + y = 48 (body in the lower
left corner, neck to the upper right) crossed at right angles by a ball
microphone on y = x + 1 (head in the upper left corner, handle to the lower
right, passing behind the neck), on SQUARE (centerline box (6,6)-(42,42)).
- guitar body: one closed, tangent-continuous outline: lower bout circle
  (centre (12.5,35.5), r 6.5, touching x 6 and y 42), upper bout circle
  (r 4.5) on the same axis and two concave waist arcs (r 2.5) tangent to both.
  It starts and ends on the integer neck joint N (20,28), the upper bout apex.
- neck: one straight stroke N -> (39,9), ending in a perpendicular tuning-peg
  bar (36,6)-(42,12) that touches the top and right edges.
- microphone: ball head r 5 about (11,11) (6 inscribed hole, touching x 6 and
  y 6), split at (14,15) where a handle stub leaves it to (17,18). The handle
  crosses the neck at (23.5,24.5) and reappears from (30,31) to (40,41); both
  handle ends are 9.2 from the neck centerline, so the gap reads as "behind".
  The stub/handle line is 0.7 off the head centre (a radius-5 circle has no
  grid point on its 45 degree diagonal); invisible at 48 px.
Lucide: `guitar` (smooth waisted body outline, single-stroke neck joined at
the upper bout) and `mic-vocal` (ball head on a straight diagonal handle).

Metric issues (crossed-guitar-microphone_metrics.json) and how they were
handled:
- stroke-width (info): redrawn at stroke 4, every gap budgeted for it.
- stroke-count (warn, 10 strokes): now 6 strokes in 3 connected groups
  (body+neck+peg bar, head+stub, handle).
- clearance e0/e6, e0/e7, e5/e6, e5/e7, e6/e7 (the double-line mic handle
  and the grille band crowding each other and the guitar): single-stroke
  handle, grille band dropped, handle gap 9.2 on each side of the neck.
- clearance e0/e4 (mic head 7 from the guitar): head is 13.4 from the neck
  and 12.5 from the body on centerlines.
- clearance e0/e8, e7/e8 (lower handle 1.9 from the body): the handle
  restarts 9.2 from the neck and 8.7 from the upper bout.
- clearance e1/e2, e1/e3, e2/e3 (three pegs 2.7-5.5 apart): one peg bar.
- clearance e0/e9, e6/e9 (sound hole 2.6 from the body outline) and the
  sub-6 holes (sound hole 5.7, headstock and mic band slivers): the sound hole
  is dropped -- a hole ring or a dot needs a lower bout of r 8.5+, which does
  not fit between the corner and the mic stub (see below); the headstock is a
  single peg bar; the mic head is r 5 (6 inscribed).
- the hollow double-line neck (1-2 wide inside) is a single stroke.
Not fixable as drawn: the sound hole. With the mic stub 9.2 from the neck,
the upper bout must stay 8 from the stub end (17,18), which caps the body at
lower bout r 6.5; a sound hole dot would need r 8.5 (dot 8.5 from a curve,
ring of at least 6).
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ae731560-756d-4bfe-9aa1-bcd0df250afa"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1044-crossed-guitar-microphone/crossed-guitar-microphone_raw.svg"
AUTHOR = "claude-opus-5-5"

LOWER = (12.5, 35.5)             # lower bout centre, touches x 6 and y 42
LOWER_R = 6.5
NECK_BASE = (20, 28)             # N: upper bout apex on the axis x + y = 48
UPPER_R = 4.5
WAIST_R = 2.5
NECK_END = (39, 9)               # the neck ends in a peg bar
PEG_BAR = ((36, 6), (42, 12))    # perpendicular to the neck, touches y 6 and x 42
MIC_HEAD = (11, 11)              # touches x 6 and y 6
MIC_R = 5
STUB = ((14, 15), (17, 18))      # handle stub on y = x + 1, 9.2 above the neck
HANDLE = ((30, 31), (40, 41))    # behind the neck (crossing 23.5,24.5), 9.2 below

AXIS = (1 / math.sqrt(2), -1 / math.sqrt(2))   # towards the headstock


def _add(p, v, k=1.0):
    return (p[0] + v[0] * k, p[1] + v[1] * k)


def _polar(c, r, a):
    return (c[0] + r * math.cos(a), c[1] + r * math.sin(a))


def _arc(c, r, a0, a1, pieces):
    """Cubic segments for the short circular arc a0 -> a1 (radians, y down)."""
    a1 = a0 + (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
    segs = []
    pieces = max(pieces, math.ceil(abs(a1 - a0) / (math.pi / 2) - 1e-9))
    step = (a1 - a0) / pieces
    k = 4 / 3 * math.tan(step / 4) * r
    for i in range(pieces):
        s, e = a0 + step * i, a0 + step * (i + 1)
        p0, p3 = _polar(c, r, s), _polar(c, r, e)
        c1 = (p0[0] - k * math.sin(s), p0[1] + k * math.cos(s))
        c2 = (p3[0] + k * math.sin(e), p3[1] - k * math.cos(e))
        segs.append((c1, c2, p3))
    return segs


def _body_segments():
    L, R, r, w = LOWER, LOWER_R, UPPER_R, WAIST_R
    d = math.dist(L, NECK_BASE) - r              # centre distance L -> U
    U = _add(L, AXIS, d)
    # waist circle centres, one each side of the axis, tangent to both bouts
    x = ((R + w) ** 2 - (r + w) ** 2 + d * d) / (2 * d)
    y = math.sqrt((R + w) ** 2 - x * x)
    perp = (-AXIS[1], AXIS[0])                   # (1,1)/sqrt2: lower-right side
    ang = lambda p, c: math.atan2(p[1] - c[1], p[0] - c[0])
    top = math.atan2(AXIS[1], AXIS[0])           # -45 deg
    segs = []
    # upper-left side: upper bout from N, waist, lower bout down to the left
    Wl = _add(_add(L, AXIS, x), perp, -y)
    ul = ang(Wl, U)
    segs += _arc(U, r, top, ul, 1)
    segs += _arc(Wl, w, ang(U, Wl), ang(L, Wl), 1)
    ll = ang(Wl, L)
    segs += _arc(L, R, ll, -math.pi, 1)          # to the leftmost point (6,33)
    segs += _arc(L, R, math.pi, math.pi / 2, 1)  # to the bottom point (15,42)
    Wr = _add(_add(L, AXIS, x), perp, y)
    lr = ang(Wr, L)
    segs += _arc(L, R, math.pi / 2, lr, 1)
    segs += _arc(Wr, w, ang(L, Wr), ang(U, Wr), 1)
    ur = ang(Wr, U)
    segs += _arc(U, r, ur, top, 1)
    # the outline closes exactly on the integer neck joint
    c1, c2, _ = segs[-1]
    segs[-1] = (c1, c2, NECK_BASE)
    return segs


class CrossedGuitarMicrophoneRedraw(Solo48):
    icon_id = "crossed-guitar-microphone-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/music"
    aliases = ("guitar and microphone", "live music", "party music", "band")
    keywords = ("guitar", "microphone", "music", "concert", "karaoke", "band", "party", "acoustic")

    def build(self) -> None:
        self.add_bezier("body", NECK_BASE, *_body_segments())
        self.add_contour("guitar-body", "body", closed=True)

        # neck ending in a perpendicular tuning-peg bar (headstock)
        p0, p1 = PEG_BAR
        self.add_line("neck", NECK_BASE, NECK_END)
        self.add_polyline("pegs", p0, NECK_END, p1)
        self.relate("connect", "guitar-body", "neck")
        self.relate("connect", "neck", "pegs")

        # microphone: ball head split where the handle stub leaves it
        hx, hy = MIC_HEAD
        a, _ = STUB
        opposite = (2 * hx - a[0], 2 * hy - a[1])
        self.add_arc("mic-head-a", a, opposite, radius_x=MIC_R)
        self.add_arc("mic-head-b", opposite, a, radius_x=MIC_R)
        self.add_contour("mic-head", "mic-head-a", "mic-head-b", closed=True)
        self.add_line("mic-stub", *STUB)
        self.relate("connect", "mic-head", "mic-stub")
        self.add_line("mic-handle", *HANDLE)
