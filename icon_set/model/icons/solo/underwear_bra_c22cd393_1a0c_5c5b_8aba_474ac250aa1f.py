"""Underwear bra (clothes), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c22cd393-1a0c-5c5b-8aba-474ac250aa1f'
SOURCE_PATH = 'icons-json/clothes/underwear bra_c22cd393-1a0c-5c5b-8aba-474ac250aa1f.json'
AUTHOR = 'json_to_solo'

class UnderwearBra(Solo48):
    icon_id = 'underwear-bra'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('underwear', 'bra', 'clothes')

    def build(self):
        self.add_line('e0', (7, 21), (7, 8))
        self.add_line('e1', (41, 20), (41, 8))
        self.add_line('e2', (26, 35), (22, 35))
        self.add_line('e3', (26, 35), (27, 30))
        self.add_line('e4', (36, 23), (42, 21))
        self.add_bezier('e5', (22, 35), ((19.836, 37.66), (17.091, 40), (13.673, 40)), ((13.672, 40), (13.67, 40), (13.669, 40)), ((13.598, 40), (13.526, 39.99), (13.455, 39.99)), ((8.855, 39.99), (4.009, 35.8), (4.009, 30.47)), ((4.009, 30.391), (4, 30.303), (4, 30.224)), ((4, 30.223), (4, 30.221), (4, 30.22)), ((4, 30.14), (4.009, 30.05), (4.009, 29.97)), ((4.009, 27.79), (4.882, 25.67), (5.645, 23.71)), ((5.836, 23.24), (7, 21.34), (7, 21)))
        self.add_bezier('e6', (26, 35), ((26.627, 35.87), (27.064, 36.84), (27.873, 37.53)), ((29.345, 38.8), (31.627, 39.99), (33.536, 39.99)), ((33.682, 39.99), (33.827, 40), (33.982, 40)), ((34.2, 40), (34.418, 39.99), (34.645, 39.99)), ((39.873, 39.99), (43.982, 35.44), (43.982, 29.73)), ((43.982, 29.57), (44, 29.4), (44, 29.23)), ((44, 29.229), (44, 29.228), (44, 29.226)), ((44, 29.148), (43.991, 29.069), (43.991, 28.99)), ((43.991, 26.22), (43.155, 23.53), (42.182, 21)), ((42.036, 20.62), (41, 20.44), (41, 20)))
        self.add_bezier('e7', (27, 30), ((27.1, 29.45), (27.282, 28.81), (27.591, 28.38)), ((29.627, 25.58), (32.936, 23.96), (36, 23)))
        self.add_bezier('e8', (7, 21), ((14.273, 22.45), (21.491, 25.62), (22, 35)))
        self.add_contour('c0', 'e5', 'e0')
        self.add_contour('c1', 'e6', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e7', 'e4')
        self.add_contour('c4', 'e8')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c1')
        self.relate('connect', 'c4', 'c0')
