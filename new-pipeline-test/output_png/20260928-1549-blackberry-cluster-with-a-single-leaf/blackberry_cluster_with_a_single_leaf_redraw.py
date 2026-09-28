"""blackberry-cluster-with-a-single-leaf (redraw of the new-pipeline traced SVG).

Plan: an upright blackberry on VRECT_L (centerline box (8,4)-(40,44)), with the
berry mirrored about x=24 and a leaf rising to the upper right.
- berry: one closed contour of drupelet arcs. The crown is three r4 semicircles
  on y=23 (x 12..36, apex y=19). The side drupelets are r4 semicircles on
  x=12/36 (y 23..31), and their apexes land on x=8/40. The lower tier is two r7
  lobes into an r4 bottom drupelet whose apex is y=44.
- seam: the tier line from side cusp to side cusp (y=31). Its cusps sit
  exactly 8 below the crown cusps. The centre dip is flattened to r5 so it
  keeps 8 from the lower lobes.
- stem: one cubic from the crown apex (24,19) up to the leaf base (26,10).
  It shares both endpoints and is related "connect" to berry and leaf.
- leaf: two cubics from the base to the tip (38,4). The upper edge arrives
  level, so the tip is the top extreme and never overshoots y=4.

Keyshape: VRECT_L, not the suggested VRECT_M. On the 28-wide M box the side
drupelets could only be shallow r5 slivers, and at 48 px the berry read as a
smooth pear (drawn and rejected). The 32-wide L box lets every drupelet be a
true r4 semicircle with deep cusps. VRECT_L was the metrics' second candidate
(score 1.16 vs 1.21, fill y 1.0). All four extremes sit on the box: x 8/40 at
the side drupelets, y 4 at the leaf tip, y 44 at the bottom drupelet.

Metric issues:
- stroke-width (info): redrawn at stroke 4, and every gap is budgeted at 8 on
  centerlines.
- keyshape-short-axis (VRECT_M y 96%): fixed by the rebuild. Extremes are
  exact on VRECT_L (tolerance 0).
- clearance e0/e1 (berry-leaf 2.56): fixed. The leaf was lifted above the
  crown, and the stem carries the gap.
- clearance e0/e3, e2/e3 (seam vs outline and bottom tier): fixed. The seam
  cusps are 8 below the crown cusps, and the flattened centre clears the
  lower lobes.
- clearance e3/e5 (seam-stem): fixed. The stem now starts at the crown apex,
  12 above the seam.
- clearance e0/e4, e1/e4, e4/e5 and loose-join e4/e1 (leaf midrib): fixed by
  dropping the midrib. The leaf interior is about 7 wide, and a midrib needs 16
  between walls.
- holes at (35.5,7.2) and (33,12) (0.9 and 1.0 wide): fixed. These were
  midrib slivers and are gone.
- holes at (23.1,22.5) and (27.7,30.3) (5.2 and 4.3 wide): fixed. The crown
  pocket and the lower-tier pocket pass the build gate's hole check.
Dropped: the trace's second seam (a third tier). Rows of drupelets need about
12 between seams at stroke 4, and a 25-tall berry has room for only one.
Lucide: no blackberry. The grape's cluster of round drupelets informed the
semicircle lobes. The leaf follows Lucide leaf's level/plumb pointed tip.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1549-blackberry-cluster-with-a-single-leaf/"
    "blackberry-cluster-with-a-single-leaf_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
DRUPE_R = 4                 # crown, side and bottom drupelets (semicircles)
SIDE_TOP = (12, 23)         # crown end = side drupelet top; side apex x=8
CROWN_CUSP = (20, 23)
CROWN_APEX = (AXIS, 19)     # stem foot
SIDE_LOW = (12, 31)         # side drupelet bottom = seam end
SEAM_CUSP = (20, 31)        # 8 below the crown cusp
SEAM_END_R = 6
SEAM_MID_R = 5              # flattened so the dip clears the lower lobes
LOW_CUSP = (20, 40)         # bottom drupelet r4, apex y=44
LOW_R = 7
LEAF_BASE = (26, 10)
LEAF_TIP = (38, 4)


def mx(p):
    return (2 * AXIS - p[0], p[1])


class BlackberryClusterWithASingleLeafRedraw(Solo48):
    icon_id = "blackberry-cluster-with-a-single-leaf-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/fruit"
    aliases = ("blackberry", "bramble", "blackberry with leaf")
    keywords = ("blackberry", "berry", "fruit", "bramble", "leaf", "drupelet")

    def build(self) -> None:
        a = self.add_arc
        # Berry, clockwise from the upper-left side cusp.
        a("crown-l", SIDE_TOP, CROWN_CUSP, radius_x=DRUPE_R)
        a("crown-c1", CROWN_CUSP, CROWN_APEX, radius_x=DRUPE_R)
        a("crown-c2", CROWN_APEX, mx(CROWN_CUSP), radius_x=DRUPE_R)
        a("crown-r", mx(CROWN_CUSP), mx(SIDE_TOP), radius_x=DRUPE_R)
        a("side-r", mx(SIDE_TOP), mx(SIDE_LOW), radius_x=DRUPE_R)
        a("low-r", mx(SIDE_LOW), mx(LOW_CUSP), radius_x=LOW_R)
        a("bottom", mx(LOW_CUSP), LOW_CUSP, radius_x=DRUPE_R)
        a("low-l", LOW_CUSP, SIDE_LOW, radius_x=LOW_R)
        a("side-l", SIDE_LOW, SIDE_TOP, radius_x=DRUPE_R)
        self.add_contour("berry", "crown-l", "crown-c1", "crown-c2", "crown-r", "side-r",
                         "low-r", "bottom", "low-l", "side-l", closed=True)

        # Tier seam, dipping between the side cusps.
        a("seam-l", SIDE_LOW, SEAM_CUSP, radius_x=SEAM_END_R, sweep=False)
        a("seam-c", SEAM_CUSP, mx(SEAM_CUSP), radius_x=SEAM_MID_R, sweep=False)
        a("seam-r", mx(SEAM_CUSP), mx(SIDE_LOW), radius_x=SEAM_END_R, sweep=False)
        self.add_contour("seam", "seam-l", "seam-c", "seam-r")
        self.relate("connect", "seam", "berry")

        # Stem and leaf. The upper edge arrives level at the tip.
        self.add_bezier("stem", CROWN_APEX, ((24, 16), (24, 13), LEAF_BASE))
        self.relate("connect", "stem", "berry")
        self.add_bezier("leaf-top", LEAF_BASE, ((24, 5), (30, 4), LEAF_TIP))
        self.add_bezier("leaf-low", LEAF_TIP, ((38, 10), (32, 12), LEAF_BASE))
        self.add_contour("leaf", "leaf-top", "leaf-low", closed=True)
        self.relate("connect", "stem", "leaf")
