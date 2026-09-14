"""Digg logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b98e2332-76f3-4432-ab6c-168b3fc4b034'
SOURCE_PATH = 'icons-json/logos/digg logo_b98e2332-76f3-4432-ab6c-168b3fc4b034.json'
AUTHOR = 'json_to_solo'

class DiggLogoLogos(Solo48):
    icon_id = 'digg-logo-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('digg', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (40, 4), (40, 18))
        self.add_line('e1', (40, 18), (14, 18))
        self.add_line('e2', (8, 21), (8, 40))
        self.add_line('e3', (14, 44), (40, 44))
        self.add_line('e4', (40, 44), (40, 18))
        self.add_bezier('e5', (14, 18), ((13.776, 18.045), (13.936, 17.718), (13.712, 17.764)), ((11.2, 18.155), (9.472, 18.736), (8.432, 20.136)), ((8.24, 20.409), (8.032, 20.582), (8.032, 20.891)), ((8.016, 21.018), (8.016, 20.873), (8, 21)))
        self.add_bezier('e6', (8, 40), ((8.016, 40.136), (8.016, 40.636), (8.032, 40.773)), ((8.032, 42.291), (11.04, 44), (13.696, 44)), ((13.936, 44), (13.76, 44), (14, 44)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
