"""Baseline chart (business), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a17aa6b1-10bf-519b-a037-138a7ac38f29'
SOURCE_PATH = 'pictographic-primitives/business/baseline chart_a17aa6b1-10bf-519b-a037-138a7ac38f29.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class BaselineChart(Solo48):
    icon_id = 'baseline-chart'
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
        self.add_arc('e3', (14, 25), (19, 23), radius_x=4)
        self.add_arc('e4', (29, 25), (35, 22), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4', 'e2')
