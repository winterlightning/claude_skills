"""Half circle (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ecc2f033-f9eb-4a2f-9a8d-470f5361b748'
SOURCE_PATH = 'icons-json/symbol/half circle_ecc2f033-f9eb-4a2f-9a8d-470f5361b748.json'
AUTHOR = 'json_to_solo'

class HalfCircle(Solo48):
    icon_id = 'half-circle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('half', 'circle', 'symbol')

    def build(self):
        self.add_line('e0', (14, 36), (14, 40))
        self.add_line('e1', (14, 40), (4, 40))
        self.add_line('e2', (4, 40), (4, 26))
        self.add_line('e3', (44, 25), (44, 40))
        self.add_line('e4', (44, 40), (34, 40))
        self.add_bezier('e5', (34, 40), ((34, 40), (34, 40), (34, 39.992)), ((34.009, 39.992), (33.991, 38.139), (33.991, 37.802)), ((33.955, 35.638), (33.873, 33.482), (32.682, 31.554)), ((29.2, 25.895), (21.255, 25.095), (16.527, 29.903)), ((14.955, 31.495), (14, 33.819), (14, 36)))
        self.add_bezier('e6', (4, 26), ((4, 24.678), (4.4, 22.922), (4.809, 21.659)), ((7.155, 14.341), (14.664, 8.017), (23.209, 8.017)), ((23.418, 8.017), (23.636, 8), (23.845, 8)), ((23.85, 8), (23.854, 8), (23.859, 8)), ((24.136, 8), (24.413, 8.008), (24.691, 8.008)), ((32.555, 8.008), (39.582, 13.28), (42.445, 19.832)), ((43.018, 21.137), (43.345, 22.467), (43.736, 23.823)), ((43.836, 24.16), (44, 24.646), (44, 25)))
        self.add_contour('c0', 'e5', 'e0', 'e1', 'e2', 'e6', 'e3', 'e4', closed=True)
