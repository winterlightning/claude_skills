"""B (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04b0190e-3678-5fe6-a871-c1e778237c92'
SOURCE_PATH = 'icons-json/typeface/B_04b0190e-3678-5fe6-a871-c1e778237c92.json'
AUTHOR = 'json_to_solo'

class B04b0190e(Solo48):
    icon_id = 'b-04b0190e'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('b', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (8, 44))
        self.add_line('e1', (8, 44), (20, 44))
        self.add_line('e2', (24, 4), (8, 4))
        self.add_line('e3', (26, 24), (8, 24))
        self.add_bezier('e4', (20, 44), ((21.083, 44), (22.474, 43.982), (23.557, 43.982)), ((30.129, 43.982), (36.702, 42.545), (39.089, 37.518)), ((39.582, 36.482), (39.988, 35.391), (39.988, 34.273)), ((39.988, 34.067), (40, 33.852), (40, 33.646)), ((40, 33.643), (40, 33.64), (40, 33.636)), ((40, 33.418), (39.975, 33.209), (39.975, 32.991)), ((39.975, 29.418), (36.665, 26.373), (32.283, 25.127)), ((31.065, 24.782), (27.052, 24.345), (26.462, 24)), ((26.634, 23.964), (26.806, 23.936), (26.978, 23.9)), ((27.434, 23.809), (27.902, 23.709), (28.357, 23.591)), ((29.452, 23.3), (30.498, 22.909), (31.446, 22.409)), ((34.462, 20.809), (36.615, 18.355), (37.329, 15.682)), ((38.671, 10.691), (36.037, 6.545), (29.428, 4.782)), ((27.766, 4.345), (25.772, 4), (24, 4)))
        self.add_contour('c0', 'e0', 'e1', 'e4', 'e2', closed=True)
        self.add_contour('c1', 'e3')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
