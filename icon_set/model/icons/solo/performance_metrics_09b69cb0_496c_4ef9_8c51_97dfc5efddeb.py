"""Performance metrics (websites), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09b69cb0-496c-4ef9-8c51-97dfc5efddeb'
SOURCE_PATH = 'pictographic-primitives/websites/performance metrics_09b69cb0-496c-4ef9-8c51-97dfc5efddeb.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PerformanceMetrics(Solo48):
    icon_id = 'performance-metrics'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    categories = ('websites', 'primitives')
    aliases = ()
    keywords = ('performance', 'metrics', 'websites')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (4, 16), (44, 16))
        self.add_line('e1', (4, 16), (4, 40))
        self.add_line('e2', (4, 40), (44, 40))
        self.add_line('e3', (44, 40), (44, 16))
        self.add_line('e4', (4, 16), (4, 8))
        self.add_line('e5', (4, 8), (44, 8))
        self.add_line('e6', (44, 8), (44, 16))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', 'e2', 'e3', closed=False)
        self.add_contour('c2', 'e4', 'e5', 'e6', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
