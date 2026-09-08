"""Three scalloped orchid blossoms above a shallow planter. SQUARE (2,2)-(46,46). Lucide flower informs repeated petal arcs. Four broad lobes replace five small petals; leaves reduced to outward curves."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1671babf-646b-4546-9934-15f0b91cdf66'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/orchid_1671babf-646b-4546-9934-15f0b91cdf66.svg'
AUTHOR = 'gpt-6'


class OrchidInShallowPlanter(Solo48):
    icon_id = 'orchid-in-shallow-planter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('orchid', 'flowers', 'blossoms', 'planter', 'leaves', 'stems', 'plant')

    def build(self) -> None:
        self.add_arc('left0', (5, 13), (11, 13), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('left1', (11, 13), (11, 19), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('left3', (5, 19), (5, 13), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('left2a', (11, 19), (8, 22), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('left2b', (8, 22), (5, 19), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('left', 'left0', 'left1', 'left2a', 'left2b', 'left3', closed=True)
        self.add_polyline('left-stem', (8, 22), (8, 32), (8, 36), closed=False)
        self.relate('connect', 'left', 'left-stem')
        self.add_arc('middle0', (21, 5), (27, 5), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('middle1', (27, 5), (27, 11), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('middle3', (21, 11), (21, 5), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('middle2a', (27, 11), (24, 14), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('middle2b', (24, 14), (21, 11), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('middle', 'middle0', 'middle1', 'middle2a', 'middle2b', 'middle3', closed=True)
        self.add_polyline('middle-stem', (24, 14), (24, 32), (24, 36), closed=False)
        self.relate('connect', 'middle', 'middle-stem')
        self.add_arc('right0', (37, 13), (43, 13), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('right1', (43, 13), (43, 19), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('right3', (37, 19), (37, 13), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('right2a', (43, 19), (40, 22), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('right2b', (40, 22), (37, 19), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('right', 'right0', 'right1', 'right2a', 'right2b', 'right3', closed=True)
        self.add_polyline('right-stem', (40, 22), (40, 32), (40, 36), closed=False)
        self.relate('connect', 'right', 'right-stem')
        self.add_polyline('planter', (4, 36), (44, 36), (40, 46), (8, 46), closed=True)
        self.relate('connect', 'left-stem', 'planter')
        self.relate('connect', 'middle-stem', 'planter')
        self.relate('connect', 'right-stem', 'planter')
        self.add_arc('leaf-left', (2, 28), (8, 32), radius_x=6, radius_y=4, sweep=False, large_arc=False)
        self.add_arc('leaf-right', (40, 32), (46, 28), radius_x=6, radius_y=4, sweep=False, large_arc=False)
        self.relate('connect', 'leaf-left', 'left-stem')
        self.relate('connect', 'leaf-right', 'right-stem')
