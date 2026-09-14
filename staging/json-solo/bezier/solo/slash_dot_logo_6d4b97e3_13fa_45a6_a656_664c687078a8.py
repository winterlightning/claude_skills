"""Slash dot logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d4b97e3-13fa-45a6-a656-664c687078a8'
SOURCE_PATH = 'icons-json/logos/slash dot logo_6d4b97e3-13fa-45a6-a656-664c687078a8.json'
AUTHOR = 'json_to_solo'

class SlashDotLogoLogos(Solo48):
    icon_id = 'slash-dot-logo-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('slash', 'dot', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (34, 5), (18, 43))
        self.add_line('e1', (17, 44), (8, 44))
        self.add_line('e2', (8, 43), (24, 5))
        self.add_line('e3', (25, 4), (35, 4))
        self.add_arc('e4-top', (30, 39), (40, 39), radius_x=5)
        self.add_arc('e4-bottom', (40, 39), (30, 39), radius_x=5)
        self.add_bezier('e5', (35, 4), ((34.67, 4.3), (34.17, 4.6), (34, 5)))
        self.add_bezier('e6', (18, 43), ((17.73, 43.318), (17.58, 44), (17, 44)))
        self.add_bezier('e7', (8, 44), ((8.12, 43.7), (8, 43.282), (8, 43)))
        self.add_bezier('e8', (24, 5), ((24.24, 4.736), (24.22, 4.445), (24.5, 4.2)), ((24.82, 4), (24.69, 4.227), (25, 4)))
        self.add_contour('c0', 'e5', 'e0', 'e6', 'e1', 'e7', 'e2', 'e8', 'e3', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
