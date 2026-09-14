"""Mobile me logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '936a3619-3936-495a-bbd0-7dd442d5c39e'
SOURCE_PATH = 'icons-json/logos/mobile me logo_936a3619-3936-495a-bbd0-7dd442d5c39e.json'
AUTHOR = 'json_to_solo'

class MobileMeLogoLogos(Solo48):
    icon_id = 'mobile-me-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('mobile', 'me', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (38, 40), (12, 40))
        self.add_arc('e1-1', (12, 40), (7, 37), radius_x=8)
        self.add_arc('e1-2', (7, 37), (5, 34), radius_x=11)
        self.add_line('e1-3', (5, 34), (4, 29))
        self.add_arc('e1-4', (4, 29), (4, 28), radius_x=21, sweep=False)
        self.add_arc('e1-5', (4, 28), (12, 17), radius_x=12)
        self.add_arc('e1-6', (12, 17), (15, 17), radius_x=6)
        self.add_arc('e1-7', (15, 17), (26, 8), radius_x=12)
        self.add_arc('e1-8', (26, 8), (30, 9), radius_x=9)
        self.add_arc('e1-9', (30, 9), (36, 16), radius_x=14)
        self.add_line('e1-10', (36, 16), (37, 21))
        self.add_line('e1-11', (37, 21), (38, 22))
        self.add_arc('e1-12', (38, 22), (44, 30), radius_x=9)
        self.add_line('e1-13', (44, 30), (42, 37))
        self.add_arc('e1-14', (42, 37), (38, 40), radius_x=6)
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e1-10', 'e1-11', 'e1-12', 'e1-13', 'e1-14', closed=True)
