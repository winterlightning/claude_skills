"""Rumble logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fe1006c0-ea17-4206-9847-7abc571c8966'
SOURCE_PATH = 'icons-json/logos/rumble logo_fe1006c0-ea17-4206-9847-7abc571c8966.json'
AUTHOR = 'json_to_solo'

class RumbleLogoLogos(Solo48):
    icon_id = 'rumble-logo-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('rumble', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (30, 26), (20, 31))
        self.add_line('e1', (17, 30), (17, 18))
        self.add_line('e2', (20, 17), (30, 22))
        self.add_line('e3-1', (8, 38), (6, 25))
        self.add_line('e3-2', (6, 25), (7, 14))
        self.add_arc('e3-3', (7, 14), (9, 9), radius_x=13)
        self.add_arc('e3-4', (9, 9), (15, 6), radius_x=8)
        self.add_arc('e3-5', (15, 6), (35, 15), radius_x=38)
        self.add_arc('e3-6', (35, 15), (42, 24), radius_x=12)
        self.add_arc('e3-7', (42, 24), (35, 33), radius_x=12)
        self.add_arc('e3-8', (35, 33), (16, 42), radius_x=38)
        self.add_line('e3-9', (16, 42), (12, 41))
        self.add_line('e3-10', (12, 41), (8, 38))
        self.add_arc('e4', (20, 31), (17, 30), radius_x=2)
        self.add_arc('e5', (17, 18), (20, 17), radius_x=2)
        self.add_arc('e6-1', (30, 22), (31, 24), radius_x=3, sweep=False)
        self.add_arc('e6-2', (31, 24), (30, 26), radius_x=3, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', 'e3-10', closed=True)
        self.add_contour('c1', 'e0', 'e4', 'e1', 'e5', 'e2', 'e6-1', 'e6-2', closed=True)
