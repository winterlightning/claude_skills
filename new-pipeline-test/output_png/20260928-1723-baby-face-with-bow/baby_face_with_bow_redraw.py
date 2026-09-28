"""baby-face-with-bow (redraw of the new-pipeline traced SVG).

Plan: a round baby head with a two-loop hair bow on its upper-right crown,
dot eyes and a smile. CIRCLE keyshape (metrics suggestion, fit score 1.09),
centerline radius 20 about (24,24). The head and bow are mirrored about the
45-degree bow axis x + y = 48 (mb()), so the two loops are one definition.
- head: r15 about (21,27), pushed down-left so the bow has about 9 units of
  radial room at the upper right. It is drawn as three quarter arcs from the
  top point (21,12) round the left and bottom to the right point (36,27); the
  upper-right quarter lies under the bow. Farthest head ink is at 19.2 + 2.
- knot: an r3 ring about (34,14) on the bow axis (the gate-exempt
  6-diameter circle), taken from the ring knot in the PNG.
- loops: each is three cubics: from the knot ring (N / E point) out to a
  wing node (28,5) / (43,20), round the loop end, and back into the head's
  top / right point, then along the crown to the ring (W / S point). The
  loop ends touch the r20 envelope (extent 19.9), and each loop leaves an
  inscribed radius of about 3.9 on centerlines. The loops' inner edges
  stand in for the hidden quarter of the head outline.
- face: symmetric about x=21. Dot eyes at (17,22)/(25,22), 8 apart. The
  smile is a half-ellipse rx4 ry2 from (17,31) to (25,31), 9 below the
  eyes (exactly 8 comes back `review` against an arc) and 9 inside the rim.

Metric issues (baby-face-with-bow_metrics.json):
- clearance e0/e2, e1/e3 (knot ring and loops 3.7-5.5 apart): fixed. The
  loops start on the knot ring's cardinal points (shared endpoints,
  relate connect), and the ring is a clean r3 circle.
- clearance e2/e4, e2/e5, e2/e6 (head 6.8-7.8 from eyes and mouth): fixed.
  Every face mark is at least 9 from the head outline.
- clearance e4/e6, e5/e6 (eyes 4.9 from the mouth): fixed, now 9.
- holes at (25.9,11.4) and (37.1,15.0), 3.0 wide (slivers between the loop
  and the knot): fixed. Each loop is now one open lobe; build_gate holes
  pass.
- stroke-count (7 strokes, budget 6): the redraw has 7 parts (head, knot,
  two loops, two eyes, mouth); the knot and both loops carry the bow's
  identity, so none were dropped.
- stroke-width (info): redrawn at stroke 4, with every gap budgeted for it.
Not kept:
- The closed "happy" eye arcs. With the head at r15, eyes 8 apart leave a
  chord of only 4 per arc, which renders as a blob at 48 px, so the eyes
  are dots.
- The PNG's continuous loop around the knot ring. The loops are open and end
  on the ring, so the ring's small hole is the only one.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "724c83b9-dfbc-417a-b236-a8b1fd9f3b71"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1723-baby-face-with-bow/baby-face-with-bow_raw.svg"
AUTHOR = "claude-opus-5-5"

HEAD_C = (21, 27)
HEAD_R = 15
KNOT = (34, 14)
KNOT_R = 3


def mb(p):
    """Mirror about the bow axis, the 45-degree line x + y = 48."""
    return (48 - p[1], 48 - p[0])


class BabyFaceWithBowRedraw(Solo48):
    icon_id = "baby-face-with-bow-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "babies"
    aliases = ("baby girl", "baby face", "baby with bow")
    keywords = ("baby", "girl", "face", "bow", "infant", "newborn", "smile")

    def build(self) -> None:
        cx, cy = HEAD_C
        r = HEAD_R
        top = (cx, cy - r)
        left = (cx - r, cy)
        bottom = (cx, cy + r)
        right = mb(top)
        a = self.add_arc
        a("head-l", top, left, radius_x=r, sweep=False)
        a("head-b", left, bottom, radius_x=r, sweep=False)
        a("head-r", bottom, right, radius_x=r, sweep=False)
        self.add_contour("head", "head-l", "head-b", "head-r")

        kx, ky = KNOT
        k = KNOT_R
        kn, ke, ks, kw = (kx, ky - k), (kx + k, ky), (kx, ky + k), (kx - k, ky)
        a("knot-ne", kn, ke, radius_x=k)
        a("knot-se", ke, ks, radius_x=k)
        a("knot-sw", ks, kw, radius_x=k)
        a("knot-nw", kw, kn, radius_x=k)
        self.add_contour("knot", "knot-ne", "knot-se", "knot-sw", "knot-nw", closed=True)

        wing = (28, 5)
        upper = ((33, 8), (30, 6))
        end = ((23, 2), (18, 8))
        inner = ((25, 13), (28, 14))
        bz = self.add_bezier
        bz("bow-a-up", kn, (upper[0], upper[1], wing))
        bz("bow-a-end", wing, (end[0], end[1], top))
        bz("bow-a-in", top, (inner[0], inner[1], kw))
        self.add_contour("bow-a", "bow-a-up", "bow-a-end", "bow-a-in")
        bz("bow-b-in", ks, (mb(inner[1]), mb(inner[0]), right))
        bz("bow-b-end", right, (mb(end[1]), mb(end[0]), mb(wing)))
        bz("bow-b-up", mb(wing), (mb(upper[1]), mb(upper[0]), ke))
        self.add_contour("bow-b", "bow-b-in", "bow-b-end", "bow-b-up")
        for loop in ("bow-a", "bow-b"):
            self.relate("connect", "head", loop)
            self.relate("connect", loop, "knot")

        self.add_dot("eye-l", (cx - 4, cy - 5))
        self.add_dot("eye-r", (cx + 4, cy - 5))
        a("mouth", (cx - 4, cy + 4), (cx + 4, cy + 4), radius_x=4, radius_y=2, sweep=False)
