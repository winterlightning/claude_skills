"""Flag (social), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c753cf19-a137-4abc-ac45-e83ec45cd778'
SOURCE_PATH = 'pictographic-primitives/social/flag_c753cf19-a137-4abc-ac45-e83ec45cd778.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class FlagC753cf19(Solo48):
    icon_id = 'flag-c753cf19'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    categories = ('social', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('flag', 'social')

    def build(self):
        self.add_line('e0', (8, 4), (8, 9))
        self.add_line('e1', (8, 44), (8, 29))
        self.add_line('e2', (23, 6), (28, 8))
        self.add_line('e3', (40, 7), (40, 28))
        self.add_line('e4', (28, 29), (22, 27))
        self.add_line('e5', (12, 27), (8, 29))
        self.add_line('e6', (8, 9), (8, 29))
        self.add_arc('e7', (8, 9), (23, 6), radius_x=15)
        self.add_arc('e8', (28, 8), (40, 7), radius_x=14, sweep=False)
        self.add_arc('e9', (40, 28), (28, 29), radius_x=12)
        self.add_arc('e10', (22, 27), (12, 27), radius_x=13, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', 'e10', 'e5')
        self.add_contour('c3', 'e6')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
