"""bunny-holding-easter-egg (redraw of the new-pipeline traced SVG).

Plan: a front-facing bunny with two long ears holding a large egg against its
body, on VRECT_M (centerline box (10,4)-(38,44)). Symmetric about x=24.
- bunny: one open cubic run, built from the left half and mirrored. It starts
  at the left paw on the egg, goes out to the arm (10,30), up the body side to
  the ear notch (15,19), around the ear (outer 11,11 / tip 16,4 / inner 20,10)
  and down into the V between the ears at (24,18). The right half mirrors it
  back to the right paw. The notches (15,19)/(33,19) and the V are the only corners.
- egg: closed, four elliptical arcs on integer nodes. The top half is ry 10 and
  the bottom half ry 9 around rx 7, so it is taller at the top. It is split at its
  widest points (17,35)/(31,35), where the paws land. Contact is declared with
  relate("connect").
- extremes: ear tips y=4, egg bottom y=44, arms x=10/38.
Dropped from the image: the rounded head and the lower notch where the arms
leave it. At stroke 4, that notch sits 2-3 units from the egg top, and the
floor is 8. The head and body are one smooth side from the ear notch to the
paw. The ears and the egg carry the subject.
No useful Lucide match (Lucide has `rabbit` in profile and `egg`, but no
front-view bunny). Only the egg's egg-shaped top/bottom split was taken from `egg`.

Metric issues (bunny-holding-easter-egg_metrics.json):
- hole [18.8, 9.6] and [29.1, 9.6] (ear holes 1.9 wide): fixed. The ears are
  9 wide at the top and open into the body through a 9-unit neck. They are no
  longer closed slivers, so the only openings are the body (well above 6) and
  the egg interior (10 x 15).
- keyshape-short-axis (x fill 66%): fixed without stretching the trace. The
  arms reach x=10/38, the ears are widened and the egg is 14 wide.
- stroke-width (trace 2.64): redrawn at stroke 4, and every gap is 8 or more.
- clearance (not in the list, but created by the stroke-4 redraw): the body
  side against the egg top was held at 8 or more by narrowing the egg to rx 7.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "606ec34e-20d1-525e-a765-4f3fca8d3c47"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1912-bunny-holding-easter-egg/bunny-holding-easter-egg_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
K = 0.4                                     # handle length as a share of the chord
# Left half of the bunny outline, paw -> V notch between the ears:
# (node, tangent arriving, tangent leaving). The right half mirrors it about x=24.
LEFT = (
    ((17, 35), None, (-0.6, 1)),            # paw, on the egg's widest point
    ((10, 30), (0, -1), (0, -1)),           # arm, outer extreme
    ((15, 19), (0.6, -1), (-0.45, -1)),     # ear notch (corner)
    ((11, 11), (0, -1), (0, -1)),           # ear, outer side
    ((16, 4), (1, 0), (1, 0)),              # ear tip, top edge
    ((20, 10), (0.3, 1), (0.3, 1)),         # ear, inner side
    ((24, 18), (0.35, 1), None),            # V notch on the axis (corner)
)
EGG_TOP, EGG_MID, EGG_BOTTOM, EGG_RX, EGG_RY_TOP = 25, 35, 44, 7, 10


def _unit(v):
    n = (v[0] ** 2 + v[1] ** 2) ** 0.5
    return (v[0] / n, v[1] / n)


def _outline():
    """Left half paw -> V, then the mirrored right half V -> paw, as one cubic run."""
    left = [(p, _unit(i) if i else None, _unit(o) if o else None) for p, i, o in LEFT]
    # Mirrored in x and walked backwards: the old arriving tangent becomes the new leaving one.
    right = [((2 * AXIS - p[0], p[1]), (o[0], -o[1]) if o else None, (i[0], -i[1]) if i else None)
             for p, i, o in reversed(left)]
    v = left[-1]
    nodes = left[:-1] + [(v[0], v[1], right[0][2])] + right[1:]
    segs = []
    for (p, _, tp), (q, tq, _) in zip(nodes, nodes[1:]):
        d = K * ((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2) ** 0.5
        segs.append(((p[0] + tp[0] * d, p[1] + tp[1] * d), (q[0] - tq[0] * d, q[1] - tq[1] * d), q))
    return nodes[0][0], segs


class BunnyHoldingEasterEggRedraw(Solo48):
    icon_id = "bunny-holding-easter-egg-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays/easter"
    aliases = ("easter bunny", "rabbit with egg")
    keywords = ("bunny", "rabbit", "easter", "egg", "holiday", "spring")

    def build(self) -> None:
        start, segs = _outline()
        self.add_bezier("bunny", start, *segs)

        # Egg: taller top half (ry 10) on a rounder bottom (ry 9), split at the paws.
        l, r = (AXIS - EGG_RX, EGG_MID), (AXIS + EGG_RX, EGG_MID)
        self.add_arc("egg-top-left", l, (AXIS, EGG_TOP), radius_x=EGG_RX, radius_y=EGG_RY_TOP, sweep=True)
        self.add_arc("egg-top-right", (AXIS, EGG_TOP), r, radius_x=EGG_RX, radius_y=EGG_RY_TOP, sweep=True)
        self.add_arc("egg-bottom-right", r, (AXIS, EGG_BOTTOM), radius_x=EGG_RX, radius_y=EGG_BOTTOM - EGG_MID, sweep=True)
        self.add_arc("egg-bottom-left", (AXIS, EGG_BOTTOM), l, radius_x=EGG_RX, radius_y=EGG_BOTTOM - EGG_MID, sweep=True)
        self.add_contour("egg", "egg-top-left", "egg-top-right", "egg-bottom-right",
                         "egg-bottom-left", closed=True)
        self.relate("connect", "bunny", "egg")
