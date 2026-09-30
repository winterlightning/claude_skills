"""crawdad (redraw of the new-pipeline traced SVG).

Plan: a crawdad seen from above, reduced to three parts on VRECT_L (the
suggested keyshape, centerline box (8,4)-(40,44)), mirrored on the axis x=24:
- two closed mitten-shaped pincers, each with a V notch between an outer and
  an inner jaw tip, growing straight out of the body shoulders. The outer
  tips make the top edge (y=4) and the swollen outer edges the side edges
  (x=8 / x=40). The inner edges stay on x<=20 / x>=28, so the two claws are 8
  apart and leave an 8-wide slot above the body.
- one closed body + tail-fan outline: a short rounded body from the shoulders
  (19,24)/(29,24), narrowing to a waist 8 wide at y=35, flaring to a two-lobed
  fan whose lobes touch the bottom edge (y=44) either side of a centre notch.
Claws and body share the shoulder nodes and are declared connected.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap is sized for it.
- keyshape-short-axis (warn, y 94%): fixed; ink now fills VRECT_L exactly
  (claw tips at y=4, fan lobes at y=44, claws at x=8/40).
- clearance e0/e1 and e2/e1 (claws against body, 1.0 and 6.87): the claws
  now join the body at a shared shoulder node instead of nearly touching it.
- clearance e0/e3, e2/e4, e3/e4 (antennae against claws and each other,
  2.97-3.93): not fixable with antennae kept. Between the claws there is one
  8-wide slot (x 20-28), which cannot hold two antennae that are 8 from the
  claws and 8 from each other. The antennae are dropped; the notched pincers
  and fan tail carry the identity.
- holes at the claw joints (2.0/2.6 wide), the body (5.4) and the tail
  (3.39): fixed. Each claw now encloses a single hole, and the body and fan
  enclose one open hole; all pass the 6-inscribed hole gate.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f4812ef0-fce6-4380-9124-384916ee103d"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1100-crawdad/crawdad_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24


def mx(p):
    """Mirror a point across the vertical axis x=24."""
    return (2 * AXIS - p[0], p[1])


def reverse(start, run):
    """The same Bezier run walked from its end back to its start."""
    knots = [start] + [seg[2] for seg in run]
    return knots[-1], tuple((c2, c1, knots[i]) for i, (c1, c2, _) in reversed(list(enumerate(run))))


def mirrored(start, run):
    """Mirror image of a left-half run, walked the other way so the right
    half keeps the same winding as the left."""
    return reverse(mx(start), tuple(tuple(mx(p) for p in seg) for seg in run))


# Left claw (the right one is its mirror). Walked from the shoulder: up the
# inner edge to the inner jaw tip, into the V notch, out to the outer jaw tip,
# then round the swollen outer edge back to the shoulder.
SHOULDER = (19, 24)      # shared by claw and body
INNER_TIP = (20, 5)      # inner edge stays on x<=20: 8 clear of its mirror
NOTCH = (16, 11)         # both jaw edges run >30 deg off the claw walls
OUTER_TIP = (11, 4)      # top of the box
CLAW_LEFT = (8, 13)      # left extreme of the box
CLAW_INNER = (SHOULDER, (((20, 19), (20, 10), INNER_TIP),))
CLAW_OUTER = (OUTER_TIP, (((9, 6), (8, 9), CLAW_LEFT), ((8, 20), (13, 24), SHOULDER)))

# Body + tail fan, left half, walked down from the top of the body.
BODY_TOP = (24, 21)
WAIST = (20, 35)         # waist 8 wide on centerlines
FAN_TIP = (14, 41)
TAIL_NOTCH = (24, 41)
BODY_RUNS = {
    "body-top": (BODY_TOP, (((21, 21), (19, 22), SHOULDER),)),
    "body-side": (SHOULDER, (((17, 28), (18, 32), WAIST),)),
    "fan-side": (WAIST, (((16, 37), (14, 39), FAN_TIP),)),
    # lobe bottom touches y=44 (bottom of the box) with a level tangent
    "fan-lobe": (FAN_TIP, (((14, 43), (16, 44), (19, 44)), ((21, 44), (23, 43), TAIL_NOTCH))),
}


class CrawdadRedraw(Solo48):
    icon_id = "crawdad-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/sea"
    aliases = ("crayfish", "crawfish", "lobster")
    keywords = ("crawdad", "crayfish", "crawfish", "lobster", "claws", "pincers", "seafood", "crustacean")

    def build(self) -> None:
        for side in ("l", "r"):
            left = side == "l"
            for name, (start, run) in BODY_RUNS.items():
                if not left:
                    start, run = mirrored(start, run)
                self.add_bezier(f"{name}-{side}", start, *run)

            inner = CLAW_INNER if left else mirrored(*CLAW_INNER)
            outer = CLAW_OUTER if left else mirrored(*CLAW_OUTER)
            jaws = [(INNER_TIP, NOTCH), (NOTCH, OUTER_TIP)]
            if not left:
                jaws = [(mx(b), mx(a)) for a, b in jaws]
            self.add_bezier(f"claw-inner-{side}", inner[0], *inner[1])
            self.add_line(f"jaw-inner-{side}", *jaws[0])
            self.add_line(f"jaw-outer-{side}", *jaws[1])
            self.add_bezier(f"claw-outer-{side}", outer[0], *outer[1])
            members = [f"claw-inner-{side}", f"jaw-inner-{side}", f"jaw-outer-{side}", f"claw-outer-{side}"]
            self.add_contour(f"claw-{side}", *(members if left else members[::-1]), closed=True)

        order = tuple(BODY_RUNS)
        self.add_contour("body", *[f"{n}-l" for n in order],
                         *[f"{n}-r" for n in reversed(order)], closed=True)
        for side in ("l", "r"):
            for claw in ("claw-inner", "claw-outer"):
                for part in ("body-top", "body-side"):
                    self.relate("connect", f"{claw}-{side}", f"{part}-{side}")
