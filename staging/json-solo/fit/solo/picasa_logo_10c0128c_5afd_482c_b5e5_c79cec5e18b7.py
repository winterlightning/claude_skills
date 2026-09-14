"""Picasa logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '10c0128c-5afd-482c-b5e5-c79cec5e18b7'
SOURCE_PATH = 'icons-json/logos/picasa logo_10c0128c-5afd-482c-b5e5-c79cec5e18b7.json'
AUTHOR = 'json_to_solo'

class PicasaLogoLogos(Solo48):
    icon_id = 'picasa-logo-logos'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('picasa', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (15, 31), (35, 31))
        self.add_line('e1', (15, 31), (15, 41))
        self.add_line('e2', (15, 31), (15, 23))
        self.add_line('e3', (35, 31), (35, 26))
        self.add_line('e4', (35, 31), (42, 31))
        self.add_line('e5', (14, 7), (23, 15))
        self.add_line('e6', (15, 23), (23, 15))
        self.add_line('e7', (15, 23), (6, 32))
        self.add_line('e8', (23, 15), (35, 26))
        self.add_line('e9', (35, 26), (35, 8))
        self.add_arc('e10-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e10-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8')
        self.add_contour('c9', 'e9')
        self.add_contour('e10', 'e10-top', 'e10-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c3', 'c8')
        self.relate('connect', 'c3', 'c9')
        self.relate('connect', 'c8', 'c9')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c1', 'e10')
        self.relate('connect', 'c4', 'e10')
        self.relate('connect', 'c5', 'e10')
        self.relate('connect', 'c7', 'e10')
        self.relate('connect', 'c9', 'e10')
