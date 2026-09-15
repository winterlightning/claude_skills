"""Alluvium (_uncategorized_02), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3e4a9c7-dc3d-4a9b-81c9-23a3db70e396'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/alluvium_b3e4a9c7-dc3d-4a9b-81c9-23a3db70e396.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Alluvium(Solo48):
    icon_id = 'alluvium'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_02'
    aliases = ()
    keywords = ('alluvium', '_uncategorized_02')

    def build(self):
        self.add_line('e0', (21, 10), (26, 13))
        self.add_line('e1', (21, 23), (26, 25))
        self.add_line('e2', (21, 35), (26, 38))
        self.add_arc('e3-1', (4, 12), (13, 8), radius_x=17)
        self.add_line('e3-2', (13, 8), (21, 10))
        self.add_arc('e4', (26, 13), (44, 9), radius_x=13, sweep=False)
        self.add_arc('e5', (4, 24), (21, 23), radius_x=14)
        self.add_arc('e6', (26, 25), (44, 22), radius_x=13, sweep=False)
        self.add_arc('e7', (4, 36), (21, 35), radius_x=15)
        self.add_line('e8-1', (26, 38), (32, 40))
        self.add_arc('e8-2', (32, 40), (44, 33), radius_x=18, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e0', 'e4')
        self.add_contour('c1', 'e5', 'e1', 'e6')
        self.add_contour('c2', 'e7', 'e2', 'e8-1', 'e8-2')
