"""Plurk logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84175448-d777-471c-9cf7-aab8a04d553d'
SOURCE_PATH = 'icons-json/logos/plurk logo_84175448-d777-471c-9cf7-aab8a04d553d.json'
AUTHOR = 'json_to_solo'

class PlurkLogo84175448(Solo48):
    icon_id = 'plurk-logo-84175448'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('plurk', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (25, 24), (17, 24))
        self.add_line('e1', (17, 24), (17, 32))
        self.add_line('e2', (17, 32), (17, 40))
        self.add_line('e3', (8, 40), (8, 18))
        self.add_line('e4', (26, 32), (17, 32))
        self.add_arc('e5-1', (17, 24), (24, 12), radius_x=9)
        self.add_arc('e5-2', (24, 12), (30, 15), radius_x=7)
        self.add_arc('e5-3', (30, 15), (25, 24), radius_x=6)
        self.add_arc('e6-1', (17, 40), (13, 44), radius_x=4)
        self.add_line('e6-2', (13, 44), (10, 43))
        self.add_arc('e6-3', (10, 43), (8, 40), radius_x=4)
        self.add_arc('e7-1', (8, 18), (24, 4), radius_x=17)
        self.add_line('e7-2', (24, 4), (30, 5))
        self.add_arc('e7-3', (30, 5), (34, 7), radius_x=16)
        self.add_arc('e7-4', (34, 7), (39, 13), radius_x=13)
        self.add_line('e7-5', (39, 13), (40, 18))
        self.add_arc('e7-6', (40, 18), (26, 32), radius_x=14)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e5-3', 'e0', closed=True)
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e3', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e7-6', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
