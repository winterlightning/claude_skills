"""Cryengine logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7da1e055-283b-4344-8cbf-9e4f26589f09'
SOURCE_PATH = 'icons-json/logos/cryengine logo_7da1e055-283b-4344-8cbf-9e4f26589f09.json'
AUTHOR = 'json_to_solo'

class CryengineLogoLogos(Solo48):
    icon_id = 'cryengine-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('cryengine', 'logo', 'logos')

    def build(self):
        self.add_arc('e0-top', (19, 24), (29, 24), radius_x=5, radius_y=10)
        self.add_arc('e0-bottom', (29, 24), (19, 24), radius_x=5, radius_y=10)
        self.add_bezier('e1', (18, 8), ((13.891, 10), (9.736, 13.36), (6.627, 18.56)), ((6.218, 19.248), (4, 23.296), (4, 24.048)), ((4, 24.059), (4, 24.07), (4, 24.082)), ((4, 24.846), (5.997, 28.298), (6.364, 28.912)), ((9.064, 33.44), (12.482, 35.968), (16, 38)))
        self.add_bezier('e2', (30, 8), ((34.155, 9.936), (38.273, 13.52), (41.4, 18.752)), ((41.758, 19.351), (44, 23.282), (44, 24.046)), ((44, 24.058), (44, 24.07), (44, 24.08)), ((44, 24.656), (41.5, 29.008), (41.136, 29.6)), ((38.209, 34.272), (34.591, 37.696), (30.745, 39.296)), ((30.082, 39.568), (29.345, 39.968), (28.664, 39.968)), ((28.627, 39.984), (29.036, 39.984), (29, 40)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
