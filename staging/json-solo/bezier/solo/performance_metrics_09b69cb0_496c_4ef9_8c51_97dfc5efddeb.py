"""Performance metrics (websites), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09b69cb0-496c-4ef9-8c51-97dfc5efddeb'
SOURCE_PATH = 'icons-json/websites/performance metrics_09b69cb0-496c-4ef9-8c51-97dfc5efddeb.json'
AUTHOR = 'json_to_solo'

class PerformanceMetricsWebsites(Solo48):
    icon_id = 'performance-metrics-websites'
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
        self.add_bezier('e7', (4, 37), ((4.573, 38.74), (5.409, 39.31), (7, 40)))
        self.add_bezier('e8', (41, 40), ((42.582, 39.37), (43.391, 38.72), (44, 37)))
        self.add_bezier('e9', (4, 11), ((4.409, 9.92), (5.327, 8.02), (6.609, 8.02)), ((6.645, 8.01), (6.964, 8.01), (7, 8)))
        self.add_bezier('e10', (41, 8), ((41.182, 8.07), (41.664, 8.05), (41.855, 8.13)), ((42.7, 8.51), (43.491, 9.47), (43.864, 10.37)), ((43.945, 10.58), (43.927, 10.79), (44, 11)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2', 'e8', 'e3')
        self.add_contour('c2', 'e4', 'e9', 'e5', 'e10', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
