"""Microstrategy logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ae63458-7f45-4f51-bcc5-6cb53c2d88b8'
SOURCE_PATH = 'icons-json/logos/microstrategy logo_7ae63458-7f45-4f51-bcc5-6cb53c2d88b8.json'
AUTHOR = 'json_to_solo'

class MicrostrategyLogoLogos(Solo48):
    icon_id = 'microstrategy-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('microstrategy', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (44, 40), (44, 16))
        self.add_line('e1', (44, 16), (36, 8))
        self.add_line('e2', (36, 8), (34, 8))
        self.add_line('e3', (24, 8), (24, 19))
        self.add_line('e4', (24, 8), (34, 8))
        self.add_line('e5', (24, 8), (14, 8))
        self.add_line('e6', (14, 19), (24, 19))
        self.add_line('e7', (14, 19), (14, 8))
        self.add_line('e8', (14, 19), (14, 40))
        self.add_line('e9', (14, 40), (4, 40))
        self.add_line('e10', (4, 40), (4, 8))
        self.add_line('e11', (4, 8), (14, 8))
        self.add_line('e12', (24, 19), (24, 40))
        self.add_line('e13', (24, 40), (34, 40))
        self.add_line('e14', (34, 40), (34, 8))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e8', 'e9', 'e10', 'e11')
        self.add_contour('c7', 'e12', 'e13', 'e14')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
