"""Slash dot logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d4b97e3-13fa-45a6-a656-664c687078a8'
SOURCE_PATH = 'pictographic-primitives/logos/slash dot logo_6d4b97e3-13fa-45a6-a656-664c687078a8.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class SlashDotLogo(Solo48):
    icon_id = 'slash-dot-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('slash', 'dot', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (34, 5), (18, 43))
        self.add_line('e1', (17, 44), (8, 44))
        self.add_line('e2', (8, 43), (24, 5))
        self.add_line('e3', (25, 4), (35, 4))
        self.add_arc('e4-top', (30, 39), (40, 39), radius_x=5)
        self.add_arc('e4-bottom', (40, 39), (30, 39), radius_x=5)
        self.add_arc('e5', (35, 4), (34, 5), radius_x=2, sweep=False)
        self.add_arc('e6', (18, 43), (17, 44), radius_x=2)
        self.add_arc('e7', (8, 44), (8, 43), radius_x=2, sweep=False)
        self.add_arc('e8', (24, 5), (25, 4), radius_x=1)
        self.add_contour('c0', 'e5', 'e0', 'e6', 'e1', 'e7', 'e2', 'e8', 'e3', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
