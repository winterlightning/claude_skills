"""blackberry-cluster-with-a-single-leaf (redraw of the new-pipeline traced SVG).

Plan: seven overlapping drupelets in a hex cluster, drawn with occlusion as in the
generated image (the centre drupelet is in front), plus a stem and one pointed leaf
to the upper right. The cluster is on VRECT_M (centerline box (10,4)-(38,44)).
- drupelets: r5 circles on a lattice built from the vectors (8,0) and (4,8)
  about the centre M=(23,31). For r5 circles, both vectors put every cusp on an
  integer 3-4-5 point. So every visible piece is an exact integer arc. There
  are no snapped Beziers and no wobble.
  Rows: T1/T2 (y 23), L/M/R (y 31), B1/B2 (y 39). L and R reach the x 10/38
  walls. B1/B2 reach y 44.
- occlusion order M, L, R, T1, T2, B1, B2. Each visible span is one arc between
  its cusps. The side drupelets L/R stay as single arcs, so each crescent's
  outer wall shares both cusps with M's inner wall. The build gate's internal
  spacing exempts shared-endpoint pairs. A d=8 crescent is under 8 wide
  everywhere except its centre line.
- stem: a cubic from the T1/T2 notch (23,20) up to the leaf base (24,9).
- leaf: an upper edge of two cubics that levels off at y=4, which gives the top
  extreme, and a single lower cubic. The edges meet at the pointed tip (38,5),
  the right extreme on the leaf side. The lower edge stays 13 from T2's centre,
  a full 8 from its arc.

Keyshape: VRECT_M, the suggested one (score 1.1). The cluster is 28 wide, so
x 10..38 is exact. VRECT_L would need 32, and the r5 lattice can only give 26
or 28.

Metric issues:
- stroke-width (info): redrawn at stroke 4, and every gap is budgeted at 8 on
  centerlines.
- stroke-count (13 strokes, budget 6): fixed by the rebuild. The model is one
  connected drupelet network plus the stem and leaf, 16 primitives. The trace's
  loose fragments (duplicate seams, stem curl) are gone.
- keyshape-short-axis (x fill 85%): fixed. The extremes are exact on VRECT_M:
  x 10/38 from the L/R drupelets, y 4 from the leaf's upper edge and y 44 from
  B1/B2.
- clearance e0/e2, e0/e11, e2/e11 (leaf vs stem vs midrib, 2.8-3.3): fixed. The
  midrib and the doubled stem strokes were dropped. The leaf is one closed lens
  on a single stem.
- clearance e0/e7, e0/e8, e1/e6, e1/e8, e2/e7, e2/e8 (leaf/stem vs top
  drupelets, 3.7-6.2): fixed. The leaf was lifted into the band above the
  cluster. Its lower edge keeps 8 from the T1/T2 arcs, and the stem starts
  exactly at the drupelet notch.
- clearance e3/e4, e3/e5 and the other drupelet pairs: fixed by construction.
  Drupelets meet only at shared integer cusps (declared connect), with no near
  misses.
- holes (0.4-4.4 inscribed, all failing): fixed. Every drupelet cell and
  crescent is at least 6 on centerlines, and the leaf lens clears the 6 floor.
  The build gate passes.
Dropped: the trace's fourth drupelet row and bottom single drupelet. At stroke 4,
a cusp-exact 3-3-2-1 taper needs about 34 of height, and the leaf band leaves 26.
The 2-3-2 hex keeps the clustered-drupelet read.
Lucide: no blackberry. Lucide grape (circles packed in a cluster, stem and
leaf at the top) informed the circle cluster and the leaf-on-stem attachment.
The berry is mirrored about x=23. The stem and leaf are deliberately asymmetric
(the leaf is angled to the upper right, as in the reference).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3278a9d5-891d-4c6a-acc3-7bd972888b5c"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1720-blackberry-cluster-with-a-single-leaf/"
    "blackberry-cluster-with-a-single-leaf_raw.svg"
)
AUTHOR = "claude-opus-5-5"

R = 5                       # every drupelet
M = (23, 31)                # front drupelet; the berry's mirror axis is x=23


def at(dx, dy):
    """Lattice point relative to the centre drupelet."""
    return (M[0] + dx, M[1] + dy)


# Cusps: 3-4-5 points shared by overlapping drupelets.
M_TOP, M_BOT = at(0, -5), at(0, 5)
M_UL, M_UR, M_LL, M_LR = at(-4, -3), at(4, -3), at(-4, 3), at(4, 3)
NOTCH, BASE = at(0, -11), at(0, 11)       # T1/T2 and B1/B2 meeting points
T1_OUT, T2_OUT = at(-8, -5), at(8, -5)    # upper drupelets meet L / R
B1_OUT, B2_OUT = at(-8, 5), at(8, 5)      # lower drupelets meet L / R

LEAF_BASE = (24, 9)
LEAF_TIP = (38, 5)


class BlackberryClusterWithASingleLeafRedraw(Solo48):
    icon_id = "blackberry-cluster-with-a-single-leaf-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/fruit"
    aliases = ("blackberry", "bramble", "blackberry with leaf")
    keywords = ("blackberry", "berry", "fruit", "bramble", "leaf", "drupelet")

    def build(self) -> None:
        a = self.add_arc
        # M: the front drupelet, a full circle split at its six cusps.
        a("m-0", M_LR, M_BOT, radius_x=R)
        a("m-1", M_BOT, M_LL, radius_x=R)
        a("m-2", M_LL, M_UL, radius_x=R)
        a("m-3", M_UL, M_TOP, radius_x=R)
        a("m-4", M_TOP, M_UR, radius_x=R)
        a("m-5", M_UR, M_LR, radius_x=R)
        # L / R: one outer arc each, cusp to cusp around M's sides.
        a("l", M_LL, M_UL, radius_x=R, large_arc=True)
        a("r", M_UR, M_LR, radius_x=R, large_arc=True)
        # Upper row: T1 over the notch into M's top, T2 from the notch to R.
        a("t1-0", T1_OUT, NOTCH, radius_x=R)
        a("t1-1", NOTCH, M_TOP, radius_x=R)
        a("t2", NOTCH, T2_OUT, radius_x=R)
        # Lower row, mirrored.
        a("b1-0", M_BOT, BASE, radius_x=R)
        a("b1-1", BASE, B1_OUT, radius_x=R)
        a("b2", B2_OUT, BASE, radius_x=R)

        # Stem from the drupelet notch to the leaf base.
        self.add_bezier("stem", NOTCH, ((23, 16), (23.5, 12), LEAF_BASE))
        # Leaf: the upper edge levels at y=4, and the lower edge keeps 8 off T2.
        self.add_bezier("leaf-top", LEAF_BASE,
                        ((25, 5), (29, 4), (32, 4)),
                        ((35, 4), (37, 4.5), LEAF_TIP))
        self.add_bezier("leaf-low", LEAF_TIP, ((37, 11.5), (31, 10.5), LEAF_BASE))
        self.add_contour("leaf", "leaf-top", "leaf-low", closed=True)

        # Declare contact only where two parts share an endpoint.
        owner = {m: c.contour_id for c in self.contours for m in c.members}
        ends = {}
        for p in self.primitives:
            part = owner.get(p.element_id, p.element_id)
            ends.setdefault(part, set()).update((p.start.as_tuple(), p.end.as_tuple()))
        parts = list(ends)
        for i, first in enumerate(parts):
            for second in parts[i + 1:]:
                if ends[first] & ends[second]:
                    self.relate("connect", first, second)
