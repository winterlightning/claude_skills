"""Bowling pins row: three identical bowling pins, the middle one in front.

Plan (symbols before coordinates)
- One pin definition (``pin_side``) repeated three times: a radius-5 head
  circle, a narrow neck, a belly, a hip and a flat foot. All knots are
  integer, and the head is split only at its 3-4-5 grid points. The body is
  tangent-continuous cubics. Left and right sides mirror about each pin axis.
- Front pin on x = 24, top y = 9, drawn as one closed outline with a collar
  across its neck.
- Rear pins are the same pin, 9 out and 3 up because they stand behind. The
  front pin hides their inner half, so each rear outline runs from the head
  crossing over the head, down the outer side, and along its base into the
  front pin's hip. The rear head's inner side point (20,11) is the front
  head's (-4,-3) grid point, so the crossing is an exact shared knot. Each
  rear collar runs from the outer neck to the front head's (-4,+3) grid
  point. All four contacts are shared endpoints declared with ``connect``.
- Keyshape SQUARE, envelope exact: rear bellies at x 6/42, rear head tops at
  y 6, front base at y 42.

Metric issues
- keyshape-short-axis (HRECT_L filled only 93% on x): fixed by changing the
  keyshape to SQUARE. HRECT_L gives 40x32 on centerlines, which forces
  squat 24-wide bellies for three pins. SQUARE (candidate score 0.86, scale
  0.99) allows 36-tall pins with 18-wide bellies.
- clearance e2/e5 and e5/e6 (neighbouring pins 2.5 apart): fixed. Three
  separate pins cannot fit: 3 x 14 wide + 2 x 8 gaps is more than any
  SOLO48 width. They are now an overlapping row with exact junctions and
  no near-misses.
- clearance e0/e1, e3/e4, e7/e8 (double collar lines 2.6 apart) and the
  three 2.4-wide collar holes: fixed with one collar line per pin, which
  also removes the band hole.
- stroke-count (9, budget 6): fixed. 6 strokes: front outline, front
  collar, and two rear outlines with their collars.
- stroke-width (trace 2.47): informational. Redrawn at stroke 4; the
  clearances above were planned at 8 centerline units.

Deliberate simplification: the source shows the pins side by side without
overlap. The occlusion is the only change to the subject, forced by the
width budget. validate_icon(): valid, 0 warnings. build_gate: pass.
Lucide: no local bowling-pin match, so none was used. Construction follows
Lucide circle-plus-cubic bottle profiles.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d972c303-2754-4efe-82ae-c0b2f535370b"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1729-bowling-pins-row/bowling-pins-row_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24          # front pin axis
PITCH = 9          # rear pins sit at AXIS -/+ PITCH ...
RISE = 3           # ... and RISE higher, because they stand behind
FRONT_TOP = 9      # front head top; rear head tops at FRONT_TOP - RISE
HEAD_R = 5         # head circle, centre TOP + HEAD_R
NECK = 3           # neck half-width at TOP + 11, where the collar sits
BELLY = 9          # belly half-width at TOP + 23
HIP = 8            # hip half-width at TOP + 30; the rear bases end here
FOOT = 6           # foot half-width at TOP + 33, the base


def pin_side(cx, top, s):
    """One side of a pin, s = -1 left / +1 right, walked from head to foot.

    Returns the knots and the (kind, start, end-or-cubics) pieces. The head
    is three arcs of the radius-5 circle through its 3-4-5 grid points; the
    body is tangent-continuous cubics, vertical at neck and belly.
    """
    x = lambda d: cx + s * d
    hc = top + HEAD_R
    k = {
        "top": (cx, top),
        "upper": (x(4), hc - 3),
        "side": (x(HEAD_R), hc),
        "lower": (x(4), hc + 3),
        "neck": (x(NECK), top + 11),
        "belly": (x(BELLY), top + 23),
        "hip": (x(HIP), top + 30),
        "foot": (x(FOOT), top + 33),
    }
    pieces = [
        ("head-1", "arc", k["top"], k["upper"]),
        ("head-2", "arc", k["upper"], k["side"]),
        ("head-3", "arc", k["side"], k["lower"]),
        ("neck", "bz", k["lower"], (((x(3.25), top + 9), (x(NECK), top + 10), k["neck"]),)),
        ("body", "bz", k["neck"], (
            ((x(NECK), top + 15), (x(BELLY), top + 17), k["belly"]),
            ((x(BELLY), top + 26), (x(8.5), top + 28.5), k["hip"]),
        )),
        ("foot", "bz", k["hip"], (((x(7.5), top + 31.5), (x(7), top + 32), k["foot"]),)),
    ]
    return k, pieces


def reverse(start, segs):
    """The same cubic chain walked from its last knot back to ``start``."""
    knots = [start] + [k for _, _, k in segs]
    return knots[-1], tuple((c2, c1, knots[i]) for i, (c1, c2, _) in reversed(list(enumerate(segs))))


class BowlingPinsRowRedraw(Solo48):
    icon_id = "bowling-pins-row-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("bowling pins", "skittles", "ten pin")
    keywords = ("bowling", "pins", "skittles", "sport", "game", "alley", "strike")

    def piece(self, name, kind, start, end, *, ccw, flip=False):
        """Author one pin piece; ``flip`` walks it the other way."""
        if kind == "arc":
            if flip:
                start, end, ccw = end, start, not ccw
            self.add_arc(name, start, end, radius_x=HEAD_R, sweep=not ccw)
        else:
            if flip:
                start, end = reverse(start, end)
            self.add_bezier(name, start, *end)
        return name

    def build(self) -> None:
        # Front pin: one closed outline, left side down, base, right side up.
        kl, left = pin_side(AXIS, FRONT_TOP, -1)
        kr, right = pin_side(AXIS, FRONT_TOP, 1)
        down = [self.piece(f"front-{p[0]}-l", *p[1:], ccw=True) for p in left]
        self.add_line("front-base", kl["foot"], kr["foot"])
        up = [self.piece(f"front-{p[0]}-r", *p[1:], ccw=False, flip=True) for p in reversed(right)]
        self.add_contour("front", *down, "front-base", *up, closed=True)
        self.add_line("front-collar", kl["neck"], kr["neck"])
        self.relate("connect", "front", "front-collar")

        # Rear pins: the same pin, PITCH out and RISE up. The front pin hides
        # their inner half, so each is drawn from the head crossing (its inner
        # head side = the front head's upper grid point), over the head, down
        # the outer side, and along its base into the front pin's hip. Its
        # collar runs from the outer neck to the front head's lower grid point.
        for s, name, front in ((-1, "left", kl), (1, "right", kr)):
            cx, top = AXIS + s * PITCH, FRONT_TOP - RISE
            inner, _ = pin_side(cx, top, -s)
            k, outer = pin_side(cx, top, s)
            assert inner["side"] == front["upper"], "rear head must cross on a front knot"
            ccw = s < 0
            members = [
                self.piece(f"{name}-head-inner-1", "arc", inner["side"], inner["upper"], ccw=ccw),
                self.piece(f"{name}-head-inner-2", "arc", inner["upper"], k["top"], ccw=ccw),
            ]
            members += [self.piece(f"{name}-{p[0]}", *p[1:], ccw=ccw) for p in outer]
            self.add_line(f"{name}-base", k["foot"], front["hip"])
            self.add_contour(name, *members, f"{name}-base")
            self.add_line(f"{name}-collar", k["neck"], front["lower"])
            self.relate("connect", "front", name)
            self.relate("connect", name, f"{name}-collar")
            self.relate("connect", "front", f"{name}-collar")
