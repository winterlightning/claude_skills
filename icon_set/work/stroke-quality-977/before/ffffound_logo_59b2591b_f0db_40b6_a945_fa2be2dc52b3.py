"""Ffffound logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59b2591b-f0db-40b6-a945-fa2be2dc52b3'
SOURCE_PATH = 'pictographic-primitives/logos/ffffound logo_59b2591b-f0db-40b6-a945-fa2be2dc52b3.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class FfffoundLogo(Solo48):
    icon_id = 'ffffound-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('ffffound', 'logo', 'logos')

    def build(self):
        self.add_line('sym-e0', (24, 11), (25, 10))
        self.add_arc('sym-e1', (25, 10), (26, 7), radius_x=13)
        self.add_arc('sym-e2', (26, 7), (32, 4), radius_x=8)
        self.add_line('sym-e4', (32, 4), (33, 4))
        self.add_arc('sym-e5', (33, 4), (40, 12), radius_x=9)
        self.add_arc('sym-e8', (40, 12), (37, 20), radius_x=15)
        self.add_line('sym-e9', (37, 20), (30, 31))
        self.add_line('sym-e10', (30, 31), (25, 40))
        self.add_arc('sym-e11', (25, 40), (24, 44), radius_x=51, sweep=False)
        self.add_arc('sym-e12', (24, 44), (23, 40), radius_x=52)
        self.add_arc('sym-e13', (23, 40), (18, 31), radius_x=55)
        self.add_line('sym-e14', (18, 31), (11, 20))
        self.add_arc('sym-e15', (11, 20), (8, 12), radius_x=15)
        self.add_arc('sym-e18', (8, 12), (15, 4), radius_x=9)
        self.add_arc('sym-e19', (15, 4), (16, 4), radius_x=32, sweep=False)
        self.add_arc('sym-e21', (16, 4), (22, 7), radius_x=8)
        self.add_arc('sym-e22', (22, 7), (23, 10), radius_x=14, sweep=False)
        self.add_arc('sym-e23', (23, 10), (24, 11), radius_x=45, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e18', 'sym-e19', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
