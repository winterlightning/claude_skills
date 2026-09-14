"""Hidden (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f48fc2c-5ebe-4a21-b259-42ee5c3ca129'
SOURCE_PATH = 'icons-json/symbol/hidden_2f48fc2c-5ebe-4a21-b259-42ee5c3ca129.json'
AUTHOR = 'json_to_solo'

class Hidden(Solo48):
    icon_id = 'hidden'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('hidden', 'symbol')

    def build(self):
        self.add_line('e0', (13, 12), (33, 38))
        self.add_bezier('e1', (13, 12), ((10.055, 14.105), (7.627, 16.763), (5.673, 20.418)), ((5.404, 20.915), (4, 23.237), (4, 23.767)), ((4, 23.775), (4, 23.783), (4, 23.791)), ((4, 24.431), (6.555, 28.751), (6.982, 29.44)), ((10.918, 35.828), (17.355, 39.988), (23.5, 39.988)), ((23.804, 39.988), (24.109, 40), (24.413, 40)), ((24.418, 40), (24.422, 40), (24.427, 40)), ((24.627, 40), (24.827, 39.988), (25.018, 39.988)), ((27.791, 39.988), (30.464, 39.465), (33, 38)))
        self.add_bezier('e2', (13, 12), ((16.109, 9.846), (19.8, 8.012), (23.327, 8.012)), ((23.435, 8.012), (23.542, 8), (23.649, 8)), ((23.651, 8), (23.653, 8), (23.655, 8)), ((24.155, 8), (24.655, 8.025), (25.155, 8.025)), ((30.982, 8.025), (36.991, 12.246), (40.864, 17.969)), ((41.382, 18.732), (44, 22.954), (44, 23.815)), ((44, 23.822), (44, 23.829), (44, 23.837)), ((44, 24.331), (42.304, 27.381), (41.991, 27.914)), ((39.573, 32.111), (36.618, 35.846), (33, 38)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
