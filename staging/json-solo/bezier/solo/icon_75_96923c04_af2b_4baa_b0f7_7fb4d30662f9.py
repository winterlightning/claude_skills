"""75 (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96923c04-af2b-4baa-b0f7-7fb4d30662f9'
SOURCE_PATH = 'icons-json/symbol/75_96923c04-af2b-4baa-b0f7-7fb4d30662f9.json'
AUTHOR = 'json_to_solo'

class Icon75Symbol(Solo48):
    icon_id = 'icon-75-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('symbol',)

    def build(self):
        self.add_line('e0', (43, 8), (31, 8))
        self.add_line('e1', (31, 8), (30, 22))
        self.add_line('e2', (4, 8), (20, 8))
        self.add_line('e3', (20, 8), (9, 40))
        self.add_bezier('e4', (30, 22), ((31.182, 20.97), (32.773, 20.13), (34.273, 19.76)), ((39.436, 18.51), (43.982, 22.88), (43.982, 28.57)), ((43.982, 28.8), (44, 29.04), (44, 29.27)), ((44, 29.274), (44, 29.277), (44, 29.281)), ((44, 29.507), (43.991, 29.723), (43.991, 29.94)), ((43.991, 34.4), (41.445, 39.99), (36.818, 39.99)), ((36.718, 39.99), (36.609, 40), (36.509, 40)), ((36.4, 40), (36.3, 40), (36.191, 40)), ((33.009, 40), (30.009, 38.28), (29, 35)))
        self.add_contour('c0', 'e0', 'e1', 'e4')
        self.add_contour('c1', 'e2', 'e3')
