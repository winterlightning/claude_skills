"""Field corner kick (sports), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9ec94c5-4ddc-4911-8248-43fbc7fa3b42'
SOURCE_PATH = 'pictographic-primitives/sports/field corner kick_c9ec94c5-4ddc-4911-8248-43fbc7fa3b42.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class FieldCornerKick(Solo48):
    icon_id = 'field-corner-kick'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('field', 'corner', 'kick', 'sports')

    def build(self):
        self.add_line('e0', (21, 4), (21, 17))
        self.add_line('e1', (8, 42), (14, 39))
        self.add_line('e2', (40, 44), (30, 39))
        self.add_line('e3', (21, 34), (30, 39))
        self.add_line('e4', (21, 34), (14, 39))
        self.add_line('e5', (21, 34), (21, 17))
        self.add_line('e6', (28, 4), (33, 6))
        self.add_line('e7', (40, 5), (40, 16))
        self.add_line('e8', (33, 18), (28, 16))
        self.add_arc('e9-1', (21, 6), (25, 4), radius_x=8)
        self.add_line('e9-2', (25, 4), (28, 4))
        self.add_arc('e10', (33, 6), (40, 5), radius_x=9, sweep=False)
        self.add_arc('e11', (40, 16), (33, 18), radius_x=8)
        self.add_arc('e12', (28, 16), (21, 17), radius_x=7, sweep=False)
        self.add_arc('e13', (30, 39), (14, 39), radius_x=11)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e9-1', 'e9-2', 'e6', 'e10', 'e7', 'e11', 'e8', 'e12')
        self.add_contour('c7', 'e13')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c6', 'c0')
