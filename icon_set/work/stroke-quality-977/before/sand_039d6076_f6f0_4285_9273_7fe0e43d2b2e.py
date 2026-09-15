"""Sand (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '039d6076-f6f0-4285-9273-7fe0e43d2b2e'
SOURCE_PATH = 'pictographic-primitives/state/sand_039d6076-f6f0-4285-9273-7fe0e43d2b2e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Sand(Solo48):
    icon_id = 'sand'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('sand', 'state')

    def build(self):
        self.add_line('e0', (4, 40), (23, 8))
        self.add_line('e1', (25, 8), (44, 40))
        self.add_arc('e2', (23, 8), (25, 8), radius_x=40, sweep=False)
        self.add_line('e3', (16, 40), (15, 40))
        self.add_arc('e4', (24, 27), (23, 27), radius_x=24)
        self.add_arc('e5', (32, 38), (31, 38), radius_x=33, sweep=False)
        self.add_contour('c0', 'e0', 'e2', 'e1')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
