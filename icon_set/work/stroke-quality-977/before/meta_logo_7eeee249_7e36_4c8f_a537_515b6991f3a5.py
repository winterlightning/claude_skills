"""Meta logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7eeee249-7e36-4c8f-a537-515b6991f3a5'
SOURCE_PATH = 'pictographic-primitives/logos/meta logo_7eeee249-7e36-4c8f-a537-515b6991f3a5.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MetaLogo(Solo48):
    icon_id = 'meta-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('meta', 'logo', 'logos')

    def build(self):
        self.add_line('sym-e0', (24, 21), (23, 19))
        self.add_arc('sym-e1', (23, 19), (21, 16), radius_x=61, sweep=False)
        self.add_arc('sym-e2', (21, 16), (13, 8), radius_x=13, sweep=False)
        self.add_line('sym-e4', (13, 8), (12, 8))
        self.add_arc('sym-e5-1', (12, 8), (8, 11), radius_x=6, sweep=False)
        self.add_arc('sym-e5-2', (8, 11), (4, 25), radius_x=27, sweep=False)
        self.add_line('sym-e7', (4, 25), (4, 27))
        self.add_arc('sym-e8-1', (4, 27), (6, 36), radius_x=25, sweep=False)
        self.add_arc('sym-e8-2', (6, 36), (10, 40), radius_x=5, sweep=False)
        self.add_arc('sym-e10', (10, 40), (11, 40), radius_x=1)
        self.add_arc('sym-e11', (11, 40), (19, 30), radius_x=16, sweep=False)
        self.add_line('sym-e12', (19, 30), (24, 21))
        self.add_line('sym-e13', (24, 21), (25, 19))
        self.add_arc('sym-e14', (25, 19), (27, 16), radius_x=61)
        self.add_arc('sym-e15', (27, 16), (35, 8), radius_x=13)
        self.add_line('sym-e17', (35, 8), (36, 8))
        self.add_arc('sym-e18-1', (36, 8), (40, 11), radius_x=6)
        self.add_arc('sym-e18-2', (40, 11), (44, 25), radius_x=27)
        self.add_arc('sym-e20-1', (44, 25), (44, 26), radius_x=30, sweep=False)
        self.add_arc('sym-e20-2', (44, 26), (44, 27), radius_x=30, sweep=False)
        self.add_arc('sym-e21-1', (44, 27), (42, 36), radius_x=24)
        self.add_arc('sym-e21-2', (42, 36), (38, 40), radius_x=5)
        self.add_line('sym-e23', (38, 40), (37, 40))
        self.add_arc('sym-e24', (37, 40), (29, 30), radius_x=17)
        self.add_line('sym-e25', (29, 30), (24, 21))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5-1', 'sym-e5-2', 'sym-e7', 'sym-e8-1', 'sym-e8-2', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18-1', 'sym-e18-2', 'sym-e20-1', 'sym-e20-2', 'sym-e21-1', 'sym-e21-2', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
