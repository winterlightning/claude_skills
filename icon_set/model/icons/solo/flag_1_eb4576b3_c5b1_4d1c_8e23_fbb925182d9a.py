"""Flag 1 (social), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb4576b3-c5b1-4d1c-8e23-fbb925182d9a'
SOURCE_PATH = 'pictographic-primitives/social/flag 1_eb4576b3-c5b1-4d1c-8e23-fbb925182d9a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Flag1(Solo48):
    icon_id = 'flag-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    categories = ('social', 'primitives')
    aliases = ()
    keywords = ('flag', 'social')

    def build(self):
        self.add_line('e0', (4, 40), (4, 10))
        self.add_line('e1', (4, 10), (10, 8))
        self.add_line('e2', (44, 11), (44, 37))
        self.add_line('e3', (30, 39), (17, 36))
        self.add_arc('e4-1', (10, 8), (11, 8), radius_x=11, sweep=False)
        self.add_line('e4-2', (11, 8), (25, 10))
        self.add_arc('e4-3', (25, 10), (29, 11), radius_x=45, sweep=False)
        self.add_arc('e4-4', (29, 11), (42, 10), radius_x=27, sweep=False)
        self.add_arc('e4-5', (42, 10), (44, 11), radius_x=2)
        self.add_arc('e5', (44, 37), (30, 39), radius_x=20)
        self.add_arc('e6', (17, 36), (4, 38), radius_x=31, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e2', 'e5', 'e3', 'e6')
