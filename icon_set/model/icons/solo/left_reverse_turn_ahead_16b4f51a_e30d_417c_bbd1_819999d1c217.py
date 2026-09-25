"""Left reverse turn ahead (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '16b4f51a-e30d-417c-bbd1-819999d1c217'
SOURCE_PATH = 'pictographic-primitives/transportation/left reverse turn ahead_16b4f51a-e30d-417c-bbd1-819999d1c217.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class LeftReverseTurnAhead(Solo48):
    icon_id = 'left-reverse-turn-ahead'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('left', 'reverse', 'turn', 'ahead', 'transportation')

    def build(self):
        self.add_line('e0', (8, 12), (17, 4))
        self.add_line('e1', (40, 44), (40, 32))
        self.add_line('e2', (33, 27), (24, 27))
        self.add_line('e3', (17, 20), (17, 4))
        self.add_line('e4', (27, 13), (17, 4))
        self.add_arc('e5', (40, 32), (33, 27), radius_x=6, sweep=False)
        self.add_arc('e6', (24, 27), (17, 20), radius_x=8)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
