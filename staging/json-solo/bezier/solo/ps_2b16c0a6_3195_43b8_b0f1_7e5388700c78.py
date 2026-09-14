"""Ps (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b16c0a6-3195-43b8-b0f1-7e5388700c78'
SOURCE_PATH = 'icons-json/symbol/Ps_2b16c0a6-3195-43b8-b0f1-7e5388700c78.json'
AUTHOR = 'json_to_solo'

class PsSymbol(Solo48):
    icon_id = 'ps-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ps', 'symbol')

    def build(self):
        self.add_line('e0', (4, 25), (15, 25))
        self.add_line('e1', (15, 8), (4, 8))
        self.add_line('e2', (4, 8), (4, 40))
        self.add_bezier('e3', (15, 25), ((15.6, 25), (16.236, 24.606), (16.818, 24.48)), ((25.009, 22.619), (24.755, 10.518), (16.964, 8.362)), ((16.291, 8.177), (15.691, 8), (15, 8)))
        self.add_bezier('e4', (44, 25), ((44, 24.975), (43.982, 24.8), (43.982, 24.775)), ((43.982, 24.118), (43.482, 23.251), (43.173, 22.686)), ((42.527, 21.507), (41.555, 20.404), (40.218, 19.865)), ((36.6, 18.383), (32.318, 20.977), (32.436, 24.615)), ((32.573, 28.952), (36.773, 29.516), (40.227, 31.065)), ((41.882, 31.806), (43.991, 33.044), (43.991, 34.989)), ((43.991, 35.091), (44, 35.2), (44, 35.301)), ((43.991, 35.419), (43.991, 35.528), (43.982, 35.638)), ((43.982, 38.206), (41.4, 39.983), (38.8, 39.983)), ((38.6, 39.983), (38.4, 40), (38.191, 40)), ((38.055, 40), (37.918, 39.992), (37.782, 39.992)), ((34.618, 39.992), (33.136, 38.813), (33, 36)))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e2')
        self.add_contour('c1', 'e4')
