"""Ice cream stick 1 (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '500e139c-ae79-400e-8292-d7a6a08b0328'
SOURCE_PATH = 'pictographic-primitives/food/ice cream stick 1_500e139c-ae79-400e-8292-d7a6a08b0328.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class IceCreamStick1(Solo48):
    icon_id = 'ice-cream-stick-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('ice', 'cream', 'stick', 'food')

    def build(self):
        self.add_line('e0', (24, 44), (24, 33))
        self.add_line('e1', (8, 15), (40, 15))
        self.add_line('e2', (8, 15), (8, 31))
        self.add_line('e3', (10, 33), (24, 33))
        self.add_line('e4', (40, 15), (40, 31))
        self.add_line('e5', (38, 33), (24, 33))
        self.add_arc('e6', (8, 31), (10, 33), radius_x=2, sweep=False)
        self.add_arc('e7-1', (8, 15), (13, 7), radius_x=10)
        self.add_arc('e7-2', (13, 7), (17, 5), radius_x=19)
        self.add_line('e7-3', (17, 5), (24, 4))
        self.add_line('e7-4', (24, 4), (31, 5))
        self.add_arc('e7-5', (31, 5), (40, 14), radius_x=12)
        self.add_arc('e7-6', (40, 14), (40, 15), radius_x=23, sweep=False)
        self.add_line('e8', (40, 31), (38, 33))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6', 'e3')
        self.add_contour('c3', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e7-6')
        self.add_contour('c4', 'e4', 'e8', 'e5')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
