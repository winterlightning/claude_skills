"""Deviant art logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4703f83b-eaef-48fe-a0f0-cd5656e78ec5'
SOURCE_PATH = 'icons-json/logos/deviant art logo_4703f83b-eaef-48fe-a0f0-cd5656e78ec5.json'
AUTHOR = 'json_to_solo'

class DeviantArtLogo(Solo48):
    icon_id = 'deviant-art-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('deviant', 'art', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (28, 22), (37, 22))
        self.add_line('e1', (37, 24), (17, 43))
        self.add_line('e2', (10, 43), (19, 28))
        self.add_line('e3', (19, 28), (8, 28))
        self.add_line('e4', (8, 28), (25, 5))
        self.add_line('e5', (26, 4), (38, 4))
        self.add_line('e6', (40, 4), (28, 22))
        self.add_arc('e7', (37, 22), (37, 24), radius_x=1)
        self.add_line('e8-1', (17, 43), (12, 44))
        self.add_arc('e8-2', (12, 44), (10, 44), radius_x=24, sweep=False)
        self.add_arc('e8-3', (10, 44), (10, 43), radius_x=1)
        self.add_arc('e9', (25, 5), (26, 4), radius_x=3)
        self.add_line('e10', (38, 4), (40, 4))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8-1', 'e8-2', 'e8-3', 'e2', 'e3', 'e4', 'e9', 'e5', 'e10', 'e6', closed=True)
