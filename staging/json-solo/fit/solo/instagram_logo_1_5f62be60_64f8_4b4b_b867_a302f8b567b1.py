"""Instagram logo 1 (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f62be60-64f8-4b4b-b867-a302f8b567b1'
SOURCE_PATH = 'icons-json/logos/instagram logo 1_5f62be60-64f8-4b4b-b867-a302f8b567b1.json'
AUTHOR = 'json_to_solo'

class InstagramLogo1Logos(Solo48):
    icon_id = 'instagram-logo-1-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('instagram', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (35, 42), (13, 42))
        self.add_line('e1', (6, 35), (6, 13))
        self.add_line('e2', (14, 6), (35, 6))
        self.add_line('e3', (42, 13), (42, 35))
        self.add_arc('e4-top', (16, 24), (32, 24), radius_x=8)
        self.add_arc('e4-bottom', (32, 24), (16, 24), radius_x=8)
        self.add_arc('e5', (13, 42), (6, 35), radius_x=8)
        self.add_arc('e6', (6, 13), (14, 6), radius_x=9)
        self.add_arc('e7', (35, 6), (42, 13), radius_x=8)
        self.add_arc('e8', (42, 35), (35, 42), radius_x=8)
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e8', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
