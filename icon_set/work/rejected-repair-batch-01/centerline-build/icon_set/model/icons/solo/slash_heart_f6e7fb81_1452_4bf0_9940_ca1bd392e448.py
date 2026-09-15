"""Slash heart (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f6e7fb81-1452-4bf0-9940-ca1bd392e448'
SOURCE_PATH = 'pictographic-primitives/symbol/slash heart_f6e7fb81-1452-4bf0-9940-ca1bd392e448.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class SlashHeart(Solo48):
    icon_id = 'slash-heart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('slash', 'heart', 'symbol')

    def build(self):
        self.add_line('e0', (39, 39), (6, 8))
        self.add_line('e1', (7, 24), (24, 40))
        self.add_line('e2', (24, 40), (41, 24))
        self.add_arc('e3-1', (41, 24), (44, 18), radius_x=9, sweep=False)
        self.add_arc('e3-2', (44, 18), (34, 8), radius_x=10, sweep=False)
        self.add_arc('e3-3', (34, 8), (24, 13), radius_x=13, sweep=False)
        self.add_line('e3-4', (24, 13), (20, 10))
        self.add_arc('e3-5', (20, 10), (14, 8), radius_x=12, sweep=False)
        self.add_arc('e3-6', (14, 8), (4, 17), radius_x=11, sweep=False)
        self.add_arc('e3-7', (4, 17), (7, 24), radius_x=10, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', closed=True)
