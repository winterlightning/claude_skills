"""Pie chart and square (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17f79cde-6e3f-435d-9f0d-3ea8fa026ef2'
SOURCE_PATH = 'icons-json/symbol/pie chart and square_17f79cde-6e3f-435d-9f0d-3ea8fa026ef2.json'
AUTHOR = 'json_to_solo'

class PieChartAndSquare(Solo48):
    icon_id = 'pie-chart-and-square'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pie', 'chart', 'and', 'square', 'symbol')

    def build(self):
        self.add_line('e0', (31, 20), (42, 20))
        self.add_line('e1', (42, 20), (42, 41))
        self.add_line('e2', (42, 42), (20, 42))
        self.add_line('e3', (20, 41), (20, 31))
        self.add_line('e4', (31, 20), (20, 20))
        self.add_line('e5', (20, 20), (20, 31))
        self.add_line('e6', (42, 41), (42, 42))
        self.add_arc('e7', (20, 42), (20, 41), radius_x=53)
        self.add_arc('e8-1', (31, 20), (19, 6), radius_x=13, sweep=False)
        self.add_line('e8-2', (19, 6), (13, 7))
        self.add_arc('e8-3', (13, 7), (8, 12), radius_x=14, sweep=False)
        self.add_arc('e8-4', (8, 12), (6, 18), radius_x=11, sweep=False)
        self.add_line('e8-5', (6, 18), (7, 24))
        self.add_line('e8-6', (7, 24), (10, 28))
        self.add_arc('e8-7', (10, 28), (20, 31), radius_x=13, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e6', 'e2', 'e7', 'e3')
        self.add_contour('c1', 'e4', 'e5')
        self.add_contour('c2', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e8-5', 'e8-6', 'e8-7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
