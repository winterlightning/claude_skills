"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '9eac7172-d6a3-4992-aaad-dd1cdbd21c70'
SOURCE_PATH = 'icon_set/model/icons/symbol/bar_graph_rising_sub32_9eac7172_d6a3_4992_aaad_dd1cdbd21c70.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '98eeb59293f66f62982803fdfa9f6956e72d65b718f34da639882f60ba715e33'
SOURCE_REFERENCES = (('9eac7172-d6a3-4992-aaad-dd1cdbd21c70', 'pictographic-primitives/symbol/bar graph_9eac7172-d6a3-4992-aaad-dd1cdbd21c70.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'bar-graph-rising-sub32-resize-40x32'
    variant_of = 'bar-graph-rising-sub32'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'symbols/standalone'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (10, 30))
        self.add_line('p1-r1-2', (10, 30), (16, 30))
        self.add_line('p1-r1-3', (16, 30), (24, 30))
        self.add_line('p1-r1-4', (24, 30), (30, 30))
        self.add_line('p1-r1-5', (30, 30), (38, 30))
        self.add_line('p2-r1-1', (2, 30), (2, 20))
        self.add_line('p2-r1-2', (2, 20), (10, 20))
        self.add_line('p2-r1-3', (10, 20), (10, 30))
        self.add_line('p3-r1-1', (16, 30), (16, 11))
        self.add_line('p3-r1-2', (16, 11), (24, 11))
        self.add_line('p3-r1-3', (24, 11), (24, 30))
        self.add_line('p4-r1-1', (30, 30), (30, 2))
        self.add_line('p4-r1-2', (30, 2), (38, 2))
        self.add_line('p4-r1-3', (38, 2), (38, 30))
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
