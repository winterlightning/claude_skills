"""Bars chart (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c4684d55-3c14-4506-a1f7-229b8c33ab85'
SOURCE_PATH = 'icons-json/symbol/bars chart_c4684d55-3c14-4506-a1f7-229b8c33ab85.json'
AUTHOR = 'json_to_solo'

class BarsChartSymbol(Solo48):
    icon_id = 'bars-chart-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bars', 'chart', 'symbol')

    def build(self):
        self.add_line('e0', (44, 40), (4, 40))
        self.add_line('e1', (4, 40), (4, 8))
        self.add_line('e2', (32, 26), (32, 40))
        self.add_line('e3', (16, 18), (16, 40))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
