"""Pie chart and square (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17f79cde-6e3f-435d-9f0d-3ea8fa026ef2'
SOURCE_PATH = 'icons-json/symbol/pie chart and square_17f79cde-6e3f-435d-9f0d-3ea8fa026ef2.json'
AUTHOR = 'json_to_solo'

class PieChartAndSquareSymbol(Solo48):
    icon_id = 'pie-chart-and-square-symbol'
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
        self.add_bezier('e6', (42, 41), ((42, 41.27), (42, 41.73), (42, 42)))
        self.add_bezier('e7', (20, 42), ((20, 41.73), (20, 41.27), (20, 41)))
        self.add_bezier('e8', (31, 20), ((31.016, 18.077), (30.521, 16.203), (29.948, 14.354)), ((28.565, 9.837), (23.943, 6.008), (19.124, 6.008)), ((19.059, 6.008), (18.995, 6), (18.93, 6)), ((18.929, 6), (18.928, 6), (18.927, 6)), ((18.608, 6), (18.281, 6.008), (17.962, 6.008)), ((11.654, 6.008), (6.008, 11.834), (6.008, 18.117)), ((6.008, 18.182), (6, 18.246), (6, 18.311)), ((6, 18.312), (6, 18.313), (6, 18.314)), ((6, 18.584), (6.008, 18.845), (6.008, 19.115)), ((6.008, 24.221), (9.911, 29.138), (14.697, 30.685)), ((16.44, 31.241), (18.184, 30.992), (20, 31)))
        self.add_contour('c0', 'e0', 'e1', 'e6', 'e2', 'e7', 'e3')
        self.add_contour('c1', 'e4', 'e5')
        self.add_contour('c2', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
