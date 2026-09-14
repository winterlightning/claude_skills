"""Vodafone logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c67d0db4-f1ce-4316-b613-652728c2ba82'
SOURCE_PATH = 'icons-json/logos/vodafone logo_c67d0db4-f1ce-4316-b613-652728c2ba82.json'
AUTHOR = 'json_to_solo'

class VodafoneLogoLogos(Solo48):
    icon_id = 'vodafone-logo-logos'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('vodafone', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (21, 15), (19, 15))
        self.add_line('e1', (27, 8), (32, 6))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e3-1', (19, 15), (17, 29), radius_x=15, sweep=False)
        self.add_arc('e3-2', (17, 29), (27, 34), radius_x=8, sweep=False)
        self.add_arc('e3-3', (27, 34), (33, 20), radius_x=10, sweep=False)
        self.add_arc('e3-4', (33, 20), (21, 15), radius_x=10, sweep=False)
        self.add_arc('e4', (19, 15), (27, 8), radius_x=17)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e0', closed=True)
        self.add_contour('c1', 'e4', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'e2')
