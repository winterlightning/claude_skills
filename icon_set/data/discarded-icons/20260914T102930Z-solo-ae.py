"""Ae (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68ff4e78-e6b9-4409-8627-b9404af60121'
SOURCE_PATH = 'icons-json/symbol/Ae_68ff4e78-e6b9-4409-8627-b9404af60121.json'
AUTHOR = 'json_to_solo'

class Ae(Solo48):
    icon_id = 'ae'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ae', 'symbol')

    def build(self):
        self.add_line('e0', (22, 40), (15, 10))
        self.add_line('e1', (11, 9), (4, 40))
        self.add_line('e2', (7, 29), (19, 29))
        self.add_bezier('e3', (15, 10), ((14.645, 8.572), (14.155, 8.025), (12.945, 8.025)), ((12.829, 8.012), (12.713, 8), (12.605, 8)), ((12.603, 8), (12.602, 8), (12.6, 8)), ((12.536, 8.012), (12.482, 8.012), (12.418, 8.025)), ((11.818, 8.025), (11.182, 8.225), (11, 9)))
        self.add_bezier('e4', (32, 30), ((34.5, 30.369), (37.182, 30.708), (39.691, 30.523)), ((40.573, 30.449), (42.036, 30.511), (42.736, 29.625)), ((43.291, 28.911), (43.518, 27.778), (43.573, 26.769)), ((43.836, 22.043), (40.536, 18.831), (37.236, 19.655)), ((35.291, 20.148), (33.564, 21.945), (32.636, 24.308)), ((31.055, 28.345), (31.473, 35.643), (34.3, 38.523)), ((35.391, 39.643), (36.7, 39.988), (38.045, 39.988)), ((38.309, 39.988), (38.573, 40), (38.827, 40)), ((39.073, 40), (39.309, 39.988), (39.545, 39.988)), ((41.118, 39.988), (42.855, 39.298), (43.691, 37.354)), ((43.8, 37.095), (43.991, 36.689), (43.991, 36.369)), ((43.991, 36.357), (44, 36.025), (44, 36)))
        self.add_contour('c0', 'e0', 'e3', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
