"""Batch-07/umbrella (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05df3587-30f8-46af-94fa-4633b7974c08'
SOURCE_PATH = 'icons-json/accessories/batch-07/umbrella_05df3587-30f8-46af-94fa-4633b7974c08.json'
AUTHOR = 'json_to_solo'

class Batch07Umbrella(Solo48):
    icon_id = 'batch-07-umbrella'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'umbrella', 'accessories')

    def build(self):
        self.add_line('e0', (24, 40), (24, 22))
        self.add_line('e1', (24, 8), (24, 4))
        self.add_bezier('e2', (17, 40), ((17.371, 41.464), (18.594, 43.991), (20.312, 43.991)), ((20.361, 44), (20.411, 44), (20.461, 44)), ((20.462, 44), (20.462, 44), (20.463, 44)), ((20.564, 43.991), (20.674, 43.991), (20.775, 43.982)), ((22.24, 43.982), (24, 41.564), (24, 40)))
        self.add_bezier('e3', (17, 39), ((17, 39.3), (17, 39.7), (17, 40)))
        self.add_bezier('e4', (8, 26), ((10.417, 23.291), (12.589, 20.4), (16.371, 22.573)), ((17.179, 23.036), (17.785, 23.655), (18.358, 24.427)), ((18.501, 24.618), (18.88, 25.264), (18.947, 25.264)), ((18.973, 25.264), (20.051, 23.945), (20.438, 23.6)), ((21.499, 22.645), (22.644, 22.236), (24, 22.182)), ((25.246, 22.136), (26.509, 22.527), (27.444, 23.445)), ((27.697, 23.7), (28.926, 25.173), (29.036, 25.191)), ((29.095, 25.209), (29.507, 24.636), (29.566, 24.564)), ((30.139, 23.9), (30.686, 23.209), (31.436, 22.773)), ((34.24, 21.155), (36.413, 22.282), (38.467, 24.464)), ((38.644, 24.655), (40, 26.073), (40, 26.118)), ((40, 26.116), (40, 26.114), (40, 26.113)), ((40, 25.996), (39.991, 25.88), (39.983, 25.755)), ((39.983, 15.573), (33.819, 7.427), (24, 7.636)), ((17.086, 7.782), (12.101, 10.909), (9.322, 17.918)), ((8.884, 19.027), (8, 21.264), (8, 22.436)), ((8, 23.564), (8, 24.873), (8, 26)))
        self.add_contour('c0', 'e2', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
