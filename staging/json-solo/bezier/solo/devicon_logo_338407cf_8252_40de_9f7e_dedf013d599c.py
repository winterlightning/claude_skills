"""Devicon logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '338407cf-8252-40de-9f7e-dedf013d599c'
SOURCE_PATH = 'icons-json/logos/devicon logo_338407cf-8252-40de-9f7e-dedf013d599c.json'
AUTHOR = 'json_to_solo'

class DeviconLogoLogos(Solo48):
    icon_id = 'devicon-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('devicon', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (17, 9), (4, 24))
        self.add_line('e1', (4, 24), (18, 40))
        self.add_line('e2', (20, 39), (30, 8))
        self.add_line('e3', (30, 8), (44, 23))
        self.add_line('e4', (44, 25), (31, 40))
        self.add_bezier('e5', (18, 40), ((18.227, 40), (18.091, 39.99), (18.318, 39.99)), ((18.482, 39.99), (18.655, 39.99), (18.818, 39.99)), ((18.918, 39.99), (19.018, 40), (19.127, 40)), ((19.236, 40), (19.345, 40), (19.455, 40)), ((19.855, 40), (19.891, 39.35), (20, 39)))
        self.add_bezier('e6', (44, 23), ((44, 23.16), (44, 23.33), (44, 23.49)), ((44, 23.83), (44, 24.17), (44, 24.51)), ((44, 24.67), (44, 24.84), (44, 25)))
        self.add_contour('c0', 'e0', 'e1', 'e5', 'e2', 'e3', 'e6', 'e4')
