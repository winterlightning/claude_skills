"""Twitter logo 1 (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cce9d468-ea2e-4285-afbc-349265e00c73'
SOURCE_PATH = 'icons-json/logos/twitter logo 1_cce9d468-ea2e-4285-afbc-349265e00c73.json'
AUTHOR = 'json_to_solo'

class TwitterLogo1Logos(Solo48):
    icon_id = 'twitter-logo-1-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('twitter', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (20, 24), (20, 30))
        self.add_line('e1', (23, 34), (35, 34))
        self.add_line('e2', (35, 44), (22, 44))
        self.add_line('e3', (8, 30), (8, 9))
        self.add_line('e4', (19, 9), (19, 13))
        self.add_line('e5', (19, 13), (34, 13))
        self.add_line('e6', (34, 23), (20, 23))
        self.add_arc('e7', (20, 30), (23, 34), radius_x=4, sweep=False)
        self.add_arc('e8-1', (35, 34), (40, 39), radius_x=6)
        self.add_arc('e8-2', (40, 39), (35, 44), radius_x=6)
        self.add_arc('e9', (22, 44), (8, 30), radius_x=15)
        self.add_line('e10-1', (8, 9), (9, 6))
        self.add_line('e10-2', (9, 6), (14, 4))
        self.add_arc('e10-3', (14, 4), (19, 9), radius_x=5)
        self.add_arc('e11', (34, 13), (34, 23), radius_x=5)
        self.add_arc('e12', (20, 23), (20, 24), radius_x=23, sweep=False)
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8-1', 'e8-2', 'e2', 'e9', 'e3', 'e10-1', 'e10-2', 'e10-3', 'e4', 'e5', 'e11', 'e6', 'e12', closed=True)
