"""Kips (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53a2b4a3-1baf-47dc-a7f6-5760e32d3d59'
SOURCE_PATH = 'pictographic-primitives/money/kips_53a2b4a3-1baf-47dc-a7f6-5760e32d3d59.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Kips(Solo48):
    icon_id = 'kips'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    categories = ('money', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('kips', 'money')

    def build(self):
        self.add_line('e0', (38, 24), (8, 24))
        self.add_line('e1', (40, 44), (21, 24))
        self.add_line('e2', (38, 6), (21, 24))
        self.add_line('e3', (16, 4), (16, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
