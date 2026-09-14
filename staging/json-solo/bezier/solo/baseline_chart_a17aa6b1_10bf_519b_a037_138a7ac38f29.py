"""Baseline chart (business), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a17aa6b1-10bf-519b-a037-138a7ac38f29'
SOURCE_PATH = 'icons-json/business/baseline chart_a17aa6b1-10bf-519b-a037-138a7ac38f29.json'
AUTHOR = 'json_to_solo'

class BaselineChartBusiness(Solo48):
    icon_id = 'baseline-chart-business'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('baseline', 'chart', 'business')

    def build(self):
        self.add_line('e0', (4, 40), (14, 25))
        self.add_line('e1', (19, 23), (29, 25))
        self.add_line('e2', (35, 22), (44, 8))
        self.add_bezier('e3', (14, 25), ((15.109, 23.33), (17.191, 22.64), (19, 23)))
        self.add_bezier('e4', (29, 25), ((32.227, 25.65), (33.118, 24.9), (35, 22)))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4', 'e2')
