"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '9eac7172-d6a3-4992-aaad-dd1cdbd21c70'
SOURCE_PATH = 'icon_set/model/icons/symbol/bar_graph_rising_sub32_9eac7172_d6a3_4992_aaad_dd1cdbd21c70.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '98eeb59293f66f62982803fdfa9f6956e72d65b718f34da639882f60ba715e33'
SOURCE_REFERENCES = (('9eac7172-d6a3-4992-aaad-dd1cdbd21c70', 'pictographic-primitives/symbol/bar graph_9eac7172-d6a3-4992-aaad-dd1cdbd21c70.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'bar-graph-rising-sub32-resize'
    variant_of = 'bar-graph-rising-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'symbols/standalone'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 18), (6, 18))
        self.add_line('p1-r1-2', (6, 18), (10, 18))
        self.add_line('p1-r1-3', (10, 18), (14, 18))
        self.add_line('p1-r1-4', (14, 18), (18, 18))
        self.add_line('p1-r1-5', (18, 18), (22, 18))
        self.add_line('p2-r1-1', (2, 18), (2, 12))
        self.add_line('p2-r1-2', (2, 12), (6, 12))
        self.add_line('p2-r1-3', (6, 12), (6, 18))
        self.add_line('p3-r1-1', (10, 18), (10, 7))
        self.add_line('p3-r1-2', (10, 7), (14, 7))
        self.add_line('p3-r1-3', (14, 7), (14, 18))
        self.add_line('p4-r1-1', (18, 18), (18, 2))
        self.add_line('p4-r1-2', (18, 2), (22, 2))
        self.add_line('p4-r1-3', (22, 2), (22, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-3')
        self.relate('connect', 'p1-r1-4', 'p3-r1-3')
        self.relate('connect', 'p1-r1-4', 'p4-r1-1')
        self.relate('connect', 'p1-r1-5', 'p4-r1-1')
        self.relate('connect', 'p1-r1-5', 'p4-r1-3')
