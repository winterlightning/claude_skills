"""Chart (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6769cc6-7edd-4638-9a68-d793ea0c3ccc'
SOURCE_PATH = 'icons-json/symbol/chart_e6769cc6-7edd-4638-9a68-d793ea0c3ccc.json'
AUTHOR = 'json_to_solo'

class ChartSymbol(Solo48):
    icon_id = 'chart-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('chart', 'symbol')

    def build(self):
        self.add_line('e0', (38, 29), (36, 17))
        self.add_line('e1', (29, 17), (27, 29))
        self.add_line('e2', (19, 29), (17, 15))
        self.add_line('e3', (10, 15), (8, 31))
        self.add_bezier('e4', (44, 38), ((43.164, 38.023), (42.245, 37.92), (41.427, 37.371)), ((39.727, 36.274), (38.645, 33.069), (38, 29)))
        self.add_bezier('e5', (36, 17), ((35.409, 13.297), (33.9, 8), (32.1, 8)), ((32.099, 8), (32.098, 8), (32.097, 8)), ((32.035, 8), (31.981, 8.023), (31.918, 8.046)), ((30.155, 8.046), (29.545, 13.549), (29, 17)))
        self.add_bezier('e6', (27, 29), ((26.391, 32.817), (24.555, 39.954), (22.636, 39.954)), ((22.582, 39.977), (22.527, 39.977), (22.482, 40)), ((22.481, 40), (22.48, 40), (22.479, 40)), ((22.426, 40), (22.381, 39.977), (22.327, 39.977)), ((20.482, 39.977), (19.491, 32.703), (19, 29)))
        self.add_bezier('e7', (17, 15), ((15.982, 8), (11.191, 8.029), (10, 15)))
        self.add_bezier('e8', (8, 31), ((7.236, 35.457), (5.809, 35.16), (4, 35)))
        self.add_contour('c0', 'e4', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e8')
