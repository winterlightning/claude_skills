"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '81086a0a-72d8-44ff-a50f-d01d9600033b'
SOURCE_PATH = 'icon_set/model/icons/symbol/graph_line_sub32_v2_81086a0a_72d8_44ff_a50f_d01d9600033b.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f973fdf66e0af287dad47b91708f08029480217e5fec943346686f323994e769'
SOURCE_REFERENCES = (('81086a0a-72d8-44ff-a50f-d01d9600033b', 'pictographic-primitives/business/graph line_81086a0a-72d8-44ff-a50f-d01d9600033b.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'graph-line-sub32-v2-resize'
    variant_of = 'graph-line-sub32-v2'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'business'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (17, 2), (22, 2))
        self.add_line('p2-r1-1', (22, 2), (15, 13))
        self.add_line('p2-r1-3', (15, 13), (10, 8))
        self.add_line('p2-r1-4', (10, 8), (2, 19))
        self.add_line('p3-r1-1', (22, 2), (22, 10))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
