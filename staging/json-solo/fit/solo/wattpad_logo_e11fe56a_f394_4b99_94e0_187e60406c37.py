"""Wattpad logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e11fe56a-f394-4b99-94e0-187e60406c37'
SOURCE_PATH = 'icons-json/logos/wattpad logo_e11fe56a-f394-4b99-94e0-187e60406c37.json'
AUTHOR = 'json_to_solo'

class WattpadLogoLogos(Solo48):
    icon_id = 'wattpad-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('wattpad', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (44, 8), (44, 38))
        self.add_line('e1', (42, 40), (15, 40))
        self.add_line('e2', (4, 29), (4, 8))
        self.add_line('e3', (4, 8), (12, 8))
        self.add_line('e4', (12, 8), (12, 29))
        self.add_line('e5', (20, 32), (20, 8))
        self.add_line('e6', (20, 8), (28, 8))
        self.add_line('e7', (28, 8), (28, 32))
        self.add_line('e8', (28, 32), (36, 32))
        self.add_line('e9', (36, 32), (36, 8))
        self.add_line('e10', (36, 8), (44, 8))
        self.add_arc('e11', (44, 38), (42, 40), radius_x=2)
        self.add_arc('e12', (15, 40), (4, 29), radius_x=12)
        self.add_arc('e13', (12, 29), (20, 32), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e11', 'e1', 'e12', 'e2', 'e3', 'e4', 'e13', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', closed=True)
