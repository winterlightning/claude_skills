"""Five pointed oval leaves on a branching stem, with a shared lower-left branch and rounded pot. Lucide sprout informs the leaf arcs; asymmetrical lower-left cluster follows the source."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53cfd912-2296-5a4a-a135-4701ab649e23'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_53cfd912-2296-5a4a-a135-4701ab649e23.svg'
AUTHOR = 'gpt-6'


class PottedBranchingLeafPlant(Solo48):
    icon_id = 'potted-branching-leaf-plant'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/plants"
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        # VRECT_XL extremes (5,2)-(43,46). Five leaves on staggered branches.
        self.add_polyline("stem", (24,13), (24,22), (24,33))
        self.add_arc("top-left-a", (11, 2), (22, 13), radius_x=11, radius_y=11)
        self.add_arc("top-left-b", (22, 13), (11, 2), radius_x=11, radius_y=11)
        self.add_contour("top-left", "top-left-a", "top-left-b", closed=True)
        self.add_arc("top-right-a", (26, 13), (37, 2), radius_x=11, radius_y=11)
        self.add_arc("top-right-b", (37, 2), (26, 13), radius_x=11, radius_y=11)
        self.add_contour("top-right", "top-right-a", "top-right-b", closed=True)
        self.add_arc("middle-left-a", (5, 15), (16, 26), radius_x=11, radius_y=11)
        self.add_arc("middle-left-b", (16, 26), (5, 15), radius_x=11, radius_y=11)
        self.add_contour("middle-left", "middle-left-a", "middle-left-b", closed=True)
        self.add_arc("middle-right-a", (32, 26), (43, 15), radius_x=11, radius_y=11)
        self.add_arc("middle-right-b", (43, 15), (32, 26), radius_x=11, radius_y=11)
        self.add_contour("middle-right", "middle-right-a", "middle-right-b", closed=True)
        self.add_arc("lower-left-a", (5, 37), (16, 26), radius_x=11, radius_y=11)
        self.add_arc("lower-left-b", (16, 26), (5, 37), radius_x=11, radius_y=11)
        self.add_contour("lower-left", "lower-left-a", "lower-left-b", closed=True)
        self.add_polyline("top-branches", (22,13), (24,13), (26,13))
        self.add_polyline("lower-branches", (16,26), (24,33), (32,26))
        self.relate("connect", "stem", "top-branches")
        self.relate("connect", "stem", "lower-branches")
        self.relate("connect", "top-left", "top-branches")
        self.relate("connect", "top-right", "top-branches")
        self.relate("connect", "middle-left", "lower-branches")
        self.relate("connect", "middle-right", "lower-branches")
        self.relate("connect", "lower-left", "lower-branches")
        self.relate("connect", "middle-left", "lower-left")
        self.add_polyline("mouth", (17,39), (24,39), (31,39))
        self.add_line("pot-right", (31,39), (31,41))
        self.add_arc("pot-round-right", (31,41), (26,46), radius_x=5)
        self.add_line("pot-bottom", (26,46), (22,46))
        self.add_arc("pot-round-left", (22,46), (17,41), radius_x=5)
        self.add_line("pot-left", (17,41), (17,39))
        self.add_contour("pot", "pot-right", "pot-round-right", "pot-bottom", "pot-round-left", "pot-left")
        self.add_line("base-stem", (24,33), (24,39))
        self.relate("connect", "base-stem", "stem")
        self.relate("connect", "base-stem", "lower-branches")
        self.relate("connect", "base-stem", "mouth")
        self.relate("connect", "pot", "mouth")
