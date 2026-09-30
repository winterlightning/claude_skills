"""flower-with-paired-leaves: a five-petal flower head on an upright stem
with two leaves paired on either side of the stem (redraw of the
new-pipeline traced SVG).

Plan: VRECT_M (centerline box (10,4)-(38,44)), mirrored about x=24.
- blossom: one closed contour of five lobes meeting at five integer
  valleys (18,10), (30,10), (32,19), (24,25), (16,19) (mirrored pairs).
  Top lobe = semicircle r=6 about (24,10), its apex on y=4. The side lobes
  are r=5 major arcs, the lower lobes r=5 semicircles, so every petal is
  the same rounded bulge.
- centre: a dot at (24,16), >= 8.5 on centerlines from every valley (the
  bottom valley sits at y=25, not 24: a curved pair exactly on 8 is not
  certified).
- stem: polyline x=24 from the bottom valley (24,25) to y=44, with a
  vertex at (24,40) where both leaves attach (declared `connect`).
- leaves: one shallow r=24 blade per side from (24,40) rising to the tips
  (10,31) / (38,31); the arcs are still rising at the tips, so the tips
  are the x extremes and land exactly on x=10/38. (A deep r=12 cup read
  as an anchor at 48 px; the rising blades read as paired leaves.)

Keyshape: VRECT_M as suggested; top lobe apex y=4, stem end y=44, leaf
tips x=10/38. The blossom sits just inside x 10..38.

Metric issues fixed by the rebuild:
- keyshape-short-axis (x fill 85%): the leaf tips now reach both x
  extremes exactly, no stretching.
- clearance e0/e1, e0/e3, e1/e3 (leaves overlapping each other and the
  stem at one point): the leaves share the stem vertex (24,40) and the
  contact is declared; the two leaves only meet there.
- clearance e0/e2, e1/e2 (4.27, leaves vs blossom): leaf tips sit >= 8
  on centerlines below the lower petals.
- clearance e2/e4, e2/e5, e3/e5, e4/e5 (degenerate junction blob and the
  centre ring 3.45 from the petal valleys): the stem meets the blossom at
  its bottom valley (declared), and the centre dot keeps 8 from every
  valley.
- hole at (16.5,13.4) (4.71, inside the blossom) and (23.9,15.6) (2.33,
  inside the centre ring): the blossom interior is one open cell around
  the dot (4 ink clearance on all sides) and the centre ring became a
  dot, so there is no sub-6 enclosed hole.
- hole at (17.6,32.6) / (30.3,32.6) (1.44, inside the leaves): the leaves
  are open blades.
- stroke-width (2.65): drawn at the profile stroke 4, gaps budgeted for it.
Not kept, with reason:
- hollow centre ring: a ring with a 6-wide hole (r=5) needs every petal
  valley 13 from its centre, so the blossom would be >= 30 wide and the
  petals would lose their scallops in a 28-wide box. The dot keeps the
  centre mark.
- hollow pointed leaves: a lens with a 6-wide hole needs 10 between its
  edges; in the 14 x 12 space beside the stem that makes near-circles
  whose upper edge runs along the stem. One open blade per leaf keeps the
  pair readable, rising like the reference leaves.
Lucide: `flower-2` (lobed head, centre, stem, paired leaves at the stem)
informed the construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a5bb0ebe-31d7-43c2-a177-afcbf914e9b7"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1158-flower-with-paired-leaves/flower-with-paired-leaves_raw.svg"
AUTHOR = "claude-opus-5-5"

CX = 24                     # symmetry axis
TOP_R = 6                   # top petal semicircle about (24,10), apex y=4
PETAL_R = 5                 # side and lower petals
V_TOP = (30, 10)            # valley top / side petal (mirror 18,10)
V_SIDE = (32, 19)           # valley side / lower petal (mirror 16,19)
V_BOTTOM = (CX, 25)         # valley between lower petals = stem top
CENTRE = (CX, 16)
LEAF_AT = (CX, 40)          # stem vertex where the leaves attach
LEAF_TIP = (38, 31)         # right tip on x=38 (mirror 10,31)
LEAF_R = 24
LEAF_SWEEP = False          # right leaf sweep; False = bulges down (mirror flips)
STEM_END = (CX, 44)


def mirror(p: tuple[int, int]) -> tuple[int, int]:
    return (2 * CX - p[0], p[1])


class FlowerWithPairedLeavesRedraw(Solo48):
    icon_id = "flower-with-paired-leaves-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    aliases = ("flower with leaves", "blossom on stem")
    keywords = ("flower", "blossom", "petals", "stem", "leaves", "plant", "garden", "nature")

    def build(self) -> None:
        # Clockwise on screen: top, right side, right lower, left lower, left side.
        self.add_arc("petal-top", mirror(V_TOP), V_TOP, radius_x=TOP_R, sweep=True)
        self.add_arc("petal-right", V_TOP, V_SIDE, radius_x=PETAL_R, sweep=True, large_arc=True)
        self.add_arc("petal-lower-right", V_SIDE, V_BOTTOM, radius_x=PETAL_R, sweep=True, large_arc=True)
        self.add_arc("petal-lower-left", V_BOTTOM, mirror(V_SIDE), radius_x=PETAL_R, sweep=True, large_arc=True)
        self.add_arc("petal-left", mirror(V_SIDE), mirror(V_TOP), radius_x=PETAL_R, sweep=True, large_arc=True)
        self.add_contour(
            "blossom", "petal-top", "petal-right", "petal-lower-right",
            "petal-lower-left", "petal-left", closed=True,
        )
        self.add_dot("centre", CENTRE)

        self.add_polyline("stem", V_BOTTOM, LEAF_AT, STEM_END)
        self.relate("connect", "stem", "blossom")

        self.add_arc("leaf-right", LEAF_AT, LEAF_TIP, radius_x=LEAF_R, sweep=LEAF_SWEEP)
        self.add_arc("leaf-left", LEAF_AT, mirror(LEAF_TIP), radius_x=LEAF_R, sweep=not LEAF_SWEEP)
        self.relate("connect", "stem", "leaf-right")
        self.relate("connect", "stem", "leaf-left")
