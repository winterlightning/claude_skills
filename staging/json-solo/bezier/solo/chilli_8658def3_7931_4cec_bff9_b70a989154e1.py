"""Chilli (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8658def3-7931-4cec-bff9-b70a989154e1'
SOURCE_PATH = 'icons-json/symbol/chilli_8658def3-7931-4cec-bff9-b70a989154e1.json'
AUTHOR = 'json_to_solo'

class ChilliSymbol(Solo48):
    icon_id = 'chilli-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('chilli', 'symbol')

    def build(self):
        self.add_line('e0', (31, 19), (26, 23))
        self.add_line('e1', (12, 28), (6, 28))
        self.add_bezier('e2', (40, 8), ((41.636, 8.682), (43.991, 10.122), (43.991, 12.017)), ((44, 12.05), (44, 12.083), (44, 12.116)), ((44, 12.117), (44, 12.117), (44, 12.118)), ((44, 12.227), (43.991, 12.337), (43.991, 12.438)), ((43.991, 14.552), (41.6, 16.703), (40, 18)))
        self.add_bezier('e3', (26, 23), ((22.091, 26.015), (17.173, 28), (12, 28)))
        self.add_bezier('e4', (6, 28), ((5.4, 28.211), (4, 28.851), (4, 29.625)), ((4, 29.626), (4, 29.627), (4, 29.627)), ((4, 29.668), (4.009, 29.702), (4.009, 29.743)), ((4.009, 30.013), (5.827, 32.876), (6.136, 33.288)), ((9, 37.086), (14.736, 39.992), (19.8, 39.992)), ((19.907, 39.992), (20.024, 40), (20.131, 40)), ((20.133, 40), (20.135, 40), (20.136, 40)), ((20.455, 40), (20.764, 39.992), (21.082, 39.992)), ((28.709, 39.992), (36.709, 34.476), (40.509, 28.606)), ((42.382, 25.718), (43.573, 22.046), (41.164, 19.082)), ((40.891, 18.754), (40.818, 18.493), (40.364, 18.105)), ((40.1, 17.886), (39.355, 17.524), (38.927, 17.339)), ((36.136, 16.177), (33.209, 17.291), (31, 19)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e0', 'e3', 'e1', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
