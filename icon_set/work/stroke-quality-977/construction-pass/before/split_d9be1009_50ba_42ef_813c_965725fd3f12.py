"""Split (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9be1009-50ba-42ef-813c-965725fd3f12'
SOURCE_PATH = 'pictographic-primitives/transportation/split_d9be1009-50ba-42ef-813c-965725fd3f12.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class SplitTransportation(Solo48):
    icon_id = 'split-transportation'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('split', 'transportation')

    def build(self):
        self.add_line('e0', (39, 8), (44, 13))
        self.add_line('e1', (4, 24), (20, 24))
        self.add_line('e2', (40, 40), (44, 36))
        self.add_line('e3', (40, 31), (44, 36))
        self.add_line('e4', (39, 17), (44, 13))
        self.add_line('e5', (25, 20), (28, 16))
        self.add_line('e6', (34, 13), (44, 13))
        self.add_line('e7', (25, 28), (28, 32))
        self.add_line('e8', (34, 36), (44, 36))
        self.add_arc('e9', (20, 24), (25, 20), radius_x=14, sweep=False)
        self.add_arc('e10', (28, 16), (34, 13), radius_x=9)
        self.add_arc('e11', (20, 24), (25, 28), radius_x=13)
        self.add_arc('e12', (28, 32), (34, 36), radius_x=10, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e9', 'e5', 'e10', 'e6')
        self.add_contour('c6', 'e11', 'e7', 'e12', 'e8')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c3', 'c6')
