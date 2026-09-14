"""Ello logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffdc3f61-3f5e-4ec1-ab2c-725ed785dddc'
SOURCE_PATH = 'icons-json/logos/ello logo_ffdc3f61-3f5e-4ec1-ab2c-725ed785dddc.json'
AUTHOR = 'json_to_solo'

class ElloLogoLogos(Solo48):
    icon_id = 'ello-logo-logos'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('ello', 'logo', 'logos')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (14, 26), ((14.791, 31.491), (19.109, 34.936), (24.664, 34.745)), ((27.036, 34.664), (29.382, 33.655), (31.036, 31.945)), ((32.709, 30.218), (33.6, 28.336), (34, 26)))
        self.add_contour('c0', 'e1')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
