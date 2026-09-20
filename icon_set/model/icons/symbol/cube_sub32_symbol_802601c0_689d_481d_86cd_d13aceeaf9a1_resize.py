"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '802601c0-689d-481d-86cd-d13aceeaf9a1'
SOURCE_PATH = 'icon_set/model/icons/symbol/cube_sub32_symbol_802601c0_689d_481d_86cd_d13aceeaf9a1.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '865ccb4fafc646bb14c9f77b06f9c9ac68f28ffcbc55386505b8db3f1f097fa2'
SOURCE_REFERENCES = (('802601c0-689d-481d-86cd-d13aceeaf9a1', 'pictographic-primitives/symbol/cube_802601c0-689d-481d-86cd-d13aceeaf9a1.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'cube-sub32-symbol-resize'
    variant_of = 'cube-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (12, 2), (22, 10))
        self.add_line('p1-r1-2', (22, 10), (22, 16))
        self.add_line('p1-r1-3', (22, 16), (12, 22))
        self.add_line('p1-r1-4', (12, 22), (2, 16))
        self.add_line('p1-r1-5', (2, 16), (2, 10))
        self.add_line('p1-r1-6', (2, 10), (12, 2))
        self.add_line('p2-r1-1', (2, 10), (12, 16))
        self.add_line('p2-r1-2', (12, 16), (22, 10))
        self.add_line('p3-r1-1', (12, 16), (12, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
