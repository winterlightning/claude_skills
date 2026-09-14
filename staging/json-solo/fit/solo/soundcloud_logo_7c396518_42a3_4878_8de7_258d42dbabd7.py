"""Soundcloud logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c396518-42a3-4878-8de7-258d42dbabd7'
SOURCE_PATH = 'icons-json/logos/soundcloud logo_7c396518-42a3-4878-8de7-258d42dbabd7.json'
AUTHOR = 'json_to_solo'

class SoundcloudLogoLogos(Solo48):
    icon_id = 'soundcloud-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('soundcloud', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (36, 40), (11, 40))
        self.add_arc('e1-1', (11, 40), (7, 38), radius_x=5)
        self.add_line('e1-2', (7, 38), (4, 30))
        self.add_line('e1-3', (4, 30), (6, 23))
        self.add_arc('e1-4', (6, 23), (14, 19), radius_x=8)
        self.add_arc('e1-5', (14, 19), (24, 8), radius_x=12)
        self.add_line('e1-6', (24, 8), (29, 9))
        self.add_arc('e1-7', (29, 9), (35, 19), radius_x=13)
        self.add_arc('e1-8', (35, 19), (41, 21), radius_x=6)
        self.add_arc('e1-9', (41, 21), (44, 28), radius_x=12)
        self.add_arc('e1-10', (44, 28), (44, 29), radius_x=3, sweep=False)
        self.add_line('e1-11', (44, 29), (42, 36))
        self.add_arc('e1-12', (42, 36), (36, 40), radius_x=9)
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e1-10', 'e1-11', 'e1-12', closed=True)
