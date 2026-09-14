"""Pyup logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7bbcbf79-ae40-4fd6-9eb1-99503546fa82'
SOURCE_PATH = 'icons-json/logos/pyup logo_7bbcbf79-ae40-4fd6-9eb1-99503546fa82.json'
AUTHOR = 'json_to_solo'

class PyupLogoLogos(Solo48):
    icon_id = 'pyup-logo-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('pyup', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (25, 44), (40, 34))
        self.add_line('e1', (40, 34), (40, 15))
        self.add_line('e2', (40, 15), (24, 4))
        self.add_line('e3', (24, 4), (9, 14))
        self.add_line('e4', (8, 15), (8, 35))
        self.add_line('e5', (8, 36), (16, 40))
        self.add_line('e6', (16, 40), (16, 29))
        self.add_line('e7', (16, 29), (24, 35))
        self.add_line('e8', (24, 35), (32, 29))
        self.add_line('e9', (32, 29), (32, 19))
        self.add_line('e10', (32, 19), (24, 14))
        self.add_line('e11', (24, 14), (16, 19))
        self.add_line('e12', (16, 19), (16, 29))
        self.add_bezier('e13', (9, 14), ((8.806, 14.173), (8.379, 14.245), (8.194, 14.427)), ((8, 14.755), (8.269, 14.645), (8, 15)))
        self.add_bezier('e14', (8, 35), ((8, 35.3), (8, 35.7), (8, 36)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e13', 'e4', 'e14', 'e5', 'e6')
        self.add_contour('c1', 'e7', 'e8', 'e9', 'e10', 'e11', 'e12', closed=True)
        self.relate('connect', 'c0', 'c1')
