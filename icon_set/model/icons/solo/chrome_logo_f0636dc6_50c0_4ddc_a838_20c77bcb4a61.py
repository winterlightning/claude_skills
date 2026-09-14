"""Chrome logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0636dc6-50c0-4ddc-a838-20c77bcb4a61'
SOURCE_PATH = 'icons-json/logos/chrome logo_f0636dc6-50c0-4ddc-a838-20c77bcb4a61.json'
AUTHOR = 'json_to_solo'

class ChromeLogo(Solo48):
    icon_id = 'chrome-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('chrome', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (18, 19), (10, 10))
        self.add_line('e1', (19, 43), (25, 32))
        self.add_line('e2', (43, 19), (30, 19))
        self.add_arc('e3-top', (16, 24), (32, 24), radius_x=8)
        self.add_arc('e3-bottom', (32, 24), (16, 24), radius_x=8)
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c1', 'e3')
        self.relate('connect', 'c2', 'e4')
        self.relate('connect', 'c2', 'e3')
