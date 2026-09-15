"""Performance metrics (websites), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09b69cb0-496c-4ef9-8c51-97dfc5efddeb'
SOURCE_PATH = 'pictographic-primitives/websites/performance metrics_09b69cb0-496c-4ef9-8c51-97dfc5efddeb.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PerformanceMetrics(Solo48):
    icon_id = 'performance-metrics'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    aliases = ()
    keywords = ('performance', 'metrics', 'websites')

    def build(self):
        self.add_line('e0', (4, 16), (44, 16))
        self.add_line('e1', (4, 16), (4, 37))
        self.add_line('e2', (7, 40), (41, 40))
        self.add_line('e3', (44, 37), (44, 16))
        self.add_line('e4', (4, 16), (4, 11))
        self.add_line('e5', (7, 8), (41, 8))
        self.add_line('e6', (44, 11), (44, 16))
        self.add_arc('e7', (4, 37), (7, 40), radius_x=4, sweep=False)
        self.add_arc('e8', (41, 40), (44, 37), radius_x=4, sweep=False)
        self.add_arc('e9', (4, 11), (7, 8), radius_x=4)
        self.add_arc('e10', (41, 8), (44, 11), radius_x=3)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2', 'e8', 'e3')
        self.add_contour('c2', 'e4', 'e9', 'e5', 'e10', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
