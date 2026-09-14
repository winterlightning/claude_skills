"""Shadow tech logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0da7f960-5b51-4ffb-a278-3607d28af876'
SOURCE_PATH = 'icons-json/logos/shadow tech logo_0da7f960-5b51-4ffb-a278-3607d28af876.json'
AUTHOR = 'json_to_solo'

class ShadowTechLogoLogos(Solo48):
    icon_id = 'shadow-tech-logo-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('shadow', 'tech', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (25, 42), (23, 42))
        self.add_arc('e1-1', (23, 42), (20, 26), radius_x=9, sweep=False)
        self.add_arc('e1-2', (20, 26), (9, 33), radius_x=9, sweep=False)
        self.add_arc('e1-3', (9, 33), (6, 24), radius_x=17)
        self.add_arc('e1-4', (6, 24), (24, 6), radius_x=18)
        self.add_line('e1-5', (24, 6), (30, 7))
        self.add_arc('e1-6', (30, 7), (34, 9), radius_x=18)
        self.add_arc('e1-7', (34, 9), (42, 23), radius_x=17)
        self.add_line('e1-8', (42, 23), (41, 30))
        self.add_arc('e1-9', (41, 30), (38, 35), radius_x=17)
        self.add_arc('e1-10', (38, 35), (35, 38), radius_x=19)
        self.add_arc('e1-11', (35, 38), (25, 42), radius_x=17)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e1-10', 'e1-11', 'e0', closed=True)
