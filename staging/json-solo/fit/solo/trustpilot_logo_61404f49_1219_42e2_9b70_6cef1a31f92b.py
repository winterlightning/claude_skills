"""Trustpilot logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '61404f49-1219-42e2-9b70-6cef1a31f92b'
SOURCE_PATH = 'icons-json/logos/trustpilot logo_61404f49-1219-42e2-9b70-6cef1a31f92b.json'
AUTHOR = 'json_to_solo'

class TrustpilotLogoLogos(Solo48):
    icon_id = 'trustpilot-logo-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('trustpilot', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (18, 17), (22, 8))
        self.add_line('e1', (26, 8), (30, 18))
        self.add_line('e2', (30, 18), (40, 18))
        self.add_line('e3', (41, 22), (33, 29))
        self.add_line('e4', (33, 29), (36, 40))
        self.add_line('e5', (34, 42), (24, 35))
        self.add_line('e6', (24, 35), (14, 42))
        self.add_line('e7', (12, 40), (15, 29))
        self.add_line('e8', (15, 29), (7, 22))
        self.add_line('e9', (8, 18), (18, 17))
        self.add_line('e10-1', (22, 8), (24, 6))
        self.add_line('e10-2', (24, 6), (26, 8))
        self.add_arc('e11-1', (40, 18), (42, 20), radius_x=2)
        self.add_line('e11-2', (42, 20), (41, 22))
        self.add_line('e12-1', (36, 40), (35, 42))
        self.add_line('e12-2', (35, 42), (34, 42))
        self.add_arc('e13', (14, 42), (12, 40), radius_x=2)
        self.add_arc('e14-1', (7, 22), (6, 20), radius_x=3)
        self.add_line('e14-2', (6, 20), (8, 18))
        self.add_contour('c0', 'e0', 'e10-1', 'e10-2', 'e1', 'e2', 'e11-1', 'e11-2', 'e3', 'e4', 'e12-1', 'e12-2', 'e5', 'e6', 'e13', 'e7', 'e8', 'e14-1', 'e14-2', 'e9', closed=True)
