"""Kickstarter logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94e0f013-4f57-4c6b-8b28-449bba9c98f1'
SOURCE_PATH = 'icons-json/logos/kickstarter logo_94e0f013-4f57-4c6b-8b28-449bba9c98f1.json'
AUTHOR = 'json_to_solo'

class KickstarterLogoLogos(Solo48):
    icon_id = 'kickstarter-logo-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('kickstarter', 'logo', 'logos')

    def build(self):
        self.add_line('sym-e0', (32, 24), (37, 30))
        self.add_line('sym-e1', (37, 30), (40, 36))
        self.add_line('sym-e3', (40, 36), (40, 37))
        self.add_arc('sym-e4', (40, 37), (34, 44), radius_x=8)
        self.add_line('sym-e6', (34, 44), (33, 44))
        self.add_arc('sym-e7', (33, 44), (28, 41), radius_x=8)
        self.add_line('sym-e8', (28, 41), (21, 34))
        self.add_arc('sym-e9', (21, 34), (18, 43), radius_x=9)
        self.add_arc('sym-e10', (18, 43), (15, 44), radius_x=5)
        self.add_line('sym-e13-1', (15, 44), (11, 43))
        self.add_arc('sym-e13-2', (11, 43), (8, 40), radius_x=6, sweep=False)
        self.add_line('sym-e14', (8, 40), (8, 38))
        self.add_line('sym-e16', (8, 38), (8, 24))
        self.add_line('sym-e17', (8, 24), (8, 10))
        self.add_line('sym-e19', (8, 10), (8, 8))
        self.add_arc('sym-e20-1', (8, 8), (11, 5), radius_x=6, sweep=False)
        self.add_line('sym-e20-2', (11, 5), (15, 4))
        self.add_arc('sym-e23', (15, 4), (18, 5), radius_x=5)
        self.add_arc('sym-e24', (18, 5), (21, 14), radius_x=9)
        self.add_line('sym-e25', (21, 14), (28, 7))
        self.add_arc('sym-e26', (28, 7), (33, 4), radius_x=9)
        self.add_line('sym-e27', (33, 4), (34, 4))
        self.add_arc('sym-e29', (34, 4), (40, 11), radius_x=8)
        self.add_arc('sym-e30', (40, 11), (40, 12), radius_x=21, sweep=False)
        self.add_line('sym-e32', (40, 12), (37, 18))
        self.add_line('sym-e33', (37, 18), (32, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e13-1', 'sym-e13-2', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e19', 'sym-e20-1', 'sym-e20-2', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e29', 'sym-e30', 'sym-e32', 'sym-e33', closed=True)
