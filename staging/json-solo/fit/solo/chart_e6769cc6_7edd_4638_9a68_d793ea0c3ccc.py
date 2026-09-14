"""Chart (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e4', (44, 38), (38, 29), radius_x=8)
        self.add_arc('e5-1', (36, 17), (32, 8), radius_x=13, sweep=False)
        self.add_arc('e5-2', (32, 8), (29, 17), radius_x=10, sweep=False)
        self.add_arc('e6-1', (27, 29), (22, 40), radius_x=14)
        self.add_arc('e6-2', (22, 40), (19, 29), radius_x=14)
        self.add_arc('e7-1', (17, 15), (14, 9), radius_x=6, sweep=False)
        self.add_arc('e7-2', (14, 9), (10, 15), radius_x=6, sweep=False)
        self.add_arc('e8', (8, 31), (4, 35), radius_x=4)
        self.add_contour('c0', 'e4', 'e0', 'e5-1', 'e5-2', 'e1', 'e6-1', 'e6-2', 'e2', 'e7-1', 'e7-2', 'e3', 'e8')
