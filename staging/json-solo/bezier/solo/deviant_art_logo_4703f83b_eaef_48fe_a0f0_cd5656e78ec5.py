"""Deviant art logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4703f83b-eaef-48fe-a0f0-cd5656e78ec5'
SOURCE_PATH = 'icons-json/logos/deviant art logo_4703f83b-eaef-48fe-a0f0-cd5656e78ec5.json'
AUTHOR = 'json_to_solo'

class DeviantArtLogoLogos(Solo48):
    icon_id = 'deviant-art-logo-logos'
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
        self.add_bezier('e7', (37, 22), ((37.48, 22.291), (37.95, 22.764), (38.43, 23.055)), ((37.95, 23.364), (37.48, 23.682), (37, 24)))
        self.add_bezier('e8', (17, 43), ((16.31, 43.655), (15.01, 43.982), (14.05, 43.982)), ((13.97, 43.991), (13.89, 43.991), (13.81, 44)), ((13.789, 44), (13.768, 44), (13.748, 44)), ((12.439, 44), (11.139, 44), (9.83, 44)), ((9.89, 43.7), (9.94, 43.3), (10, 43)))
        self.add_bezier('e9', (25, 5), ((25.41, 4.455), (25.53, 4.373), (26, 4)))
        self.add_bezier('e10', (38, 4), ((38.67, 4), (39.33, 4), (40, 4)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2', 'e3', 'e4', 'e9', 'e5', 'e10', 'e6', closed=True)
