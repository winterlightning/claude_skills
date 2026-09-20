"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '5552619f-de1f-40a4-b0e9-95549bca7398'
SOURCE_PATH = 'icon_set/model/icons/symbol/graph_finance_sub32_v2_5552619f_de1f_40a4_b0e9_95549bca7398.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '240662318cc68ce531108e0b59aae8e86bdb5017236ef270b65c628cf711d53a'
SOURCE_REFERENCES = (('5552619f-de1f-40a4-b0e9-95549bca7398', 'pictographic-primitives/finance/graph_5552619f-de1f-40a4-b0e9-95549bca7398.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'graph-finance-sub32-v2-resize'
    variant_of = 'graph-finance-sub32-v2'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'finance'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 19), (5, 19))
        self.add_line('p1-r1-2', (5, 19), (12, 19))
        self.add_line('p1-r1-3', (12, 19), (19, 19))
        self.add_line('p1-r1-4', (19, 19), (22, 19))
        self.add_line('p2-r1-1', (5, 2), (5, 19))
        self.add_line('p3-r1-1', (12, 7), (12, 19))
        self.add_line('p4-r1-1', (19, 10), (19, 19))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p4-r1-1')
        self.relate('connect', 'p1-r1-4', 'p4-r1-1')
