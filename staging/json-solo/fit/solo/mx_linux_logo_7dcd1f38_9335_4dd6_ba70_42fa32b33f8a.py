"""Mx linux logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7dcd1f38-9335-4dd6-ba70-42fa32b33f8a'
SOURCE_PATH = 'icons-json/logos/mx linux logo_7dcd1f38-9335-4dd6-ba70-42fa32b33f8a.json'
AUTHOR = 'json_to_solo'

class MxLinuxLogoLogos(Solo48):
    icon_id = 'mx-linux-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('mx', 'linux', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (26, 35), (19, 26))
        self.add_line('e1', (35, 8), (24, 20))
        self.add_line('e2', (24, 20), (16, 10))
        self.add_line('e3', (19, 26), (17, 25))
        self.add_line('e4', (17, 25), (4, 40))
        self.add_line('e5', (4, 40), (44, 40))
        self.add_line('e6', (44, 40), (34, 28))
        self.add_line('e7', (34, 28), (32, 30))
        self.add_line('e8', (32, 30), (24, 20))
        self.add_line('e9', (24, 20), (19, 25))
        self.add_line('e10', (19, 25), (19, 26))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
