"""Pathfinder merge (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5359e13c-d622-4650-8a34-9dcec3231c86'
SOURCE_PATH = 'pictographic-primitives/design/pathfinder merge_5359e13c-d622-4650-8a34-9dcec3231c86.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PathfinderMerge(Solo48):
    icon_id = 'pathfinder-merge'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pathfinder', 'merge', 'design')

    def build(self):
        self.add_line('e0', (16, 30), (6, 30))
        self.add_line('e1', (4, 28), (4, 10))
        self.add_line('e2', (6, 8), (28, 8))
        self.add_line('e3', (29, 10), (29, 18))
        self.add_line('e4', (29, 18), (42, 18))
        self.add_line('e5', (44, 20), (44, 38))
        self.add_line('e6', (42, 40), (19, 40))
        self.add_line('e7', (17, 38), (17, 30))
        self.add_arc('e8', (6, 30), (4, 28), radius_x=2)
        self.add_arc('e9', (4, 10), (6, 8), radius_x=2)
        self.add_arc('e10', (28, 8), (29, 10), radius_x=2)
        self.add_arc('e11', (42, 18), (44, 20), radius_x=2)
        self.add_arc('e12', (44, 38), (42, 40), radius_x=2)
        self.add_arc('e13', (19, 40), (17, 38), radius_x=2)
        self.add_line('e14', (17, 30), (16, 30))
        self.add_contour('c0', 'e0', 'e8', 'e1', 'e9', 'e2', 'e10', 'e3', 'e4', 'e11', 'e5', 'e12', 'e6', 'e13', 'e7', 'e14', closed=True)
