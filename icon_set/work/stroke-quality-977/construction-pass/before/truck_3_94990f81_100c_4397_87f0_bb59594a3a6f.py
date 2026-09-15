"""Truck 3 (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94990f81-100c-4397-87f0-bb59594a3a6f'
SOURCE_PATH = 'pictographic-primitives/transportation/truck 3_94990f81-100c-4397-87f0-bb59594a3a6f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Truck3(Solo48):
    icon_id = 'truck-3'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('truck', 'transportation')

    def build(self):
        self.add_line('e0', (9, 34), (4, 34))
        self.add_line('e1', (4, 34), (4, 23))
        self.add_line('e2', (9, 14), (19, 14))
        self.add_line('e3', (18, 34), (30, 34))
        self.add_line('e4', (39, 34), (44, 34))
        self.add_line('e5', (44, 34), (44, 8))
        self.add_line('e6', (44, 8), (19, 8))
        self.add_line('e7', (19, 8), (19, 34))
        self.add_arc('e8-top', (8, 34), (18, 34), radius_x=5, radius_y=6)
        self.add_arc('e8-bottom', (18, 34), (8, 34), radius_x=5, radius_y=6)
        self.add_arc('e9-top', (30, 34), (40, 34), radius_x=5, radius_y=6)
        self.add_arc('e9-bottom', (40, 34), (30, 34), radius_x=5, radius_y=6)
        self.add_arc('e10', (4, 23), (9, 14), radius_x=11)
        self.add_contour('c0', 'e0', 'e1', 'e10', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e5', 'e6', 'e7')
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c2', 'c1')
