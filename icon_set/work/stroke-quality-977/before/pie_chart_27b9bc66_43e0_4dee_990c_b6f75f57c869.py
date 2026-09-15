"""Pie chart (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '27b9bc66-43e0-4dee-990c-b6f75f57c869'
SOURCE_PATH = 'pictographic-primitives/symbol/pie chart_27b9bc66-43e0-4dee-990c-b6f75f57c869.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PieChart(Solo48):
    icon_id = 'pie-chart'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pie', 'chart', 'symbol')

    def build(self):
        self.add_line('e0', (38, 38), (24, 23))
        self.add_line('e1', (24, 23), (10, 38))
        self.add_line('e2', (24, 4), (24, 23))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c1', 'e3')
