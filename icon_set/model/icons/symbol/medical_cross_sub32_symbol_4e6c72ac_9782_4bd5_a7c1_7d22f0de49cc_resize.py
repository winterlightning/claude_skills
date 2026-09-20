"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '4e6c72ac-9782-4bd5-a7c1-7d22f0de49cc'
SOURCE_PATH = 'icon_set/model/icons/symbol/medical_cross_sub32_symbol_4e6c72ac_9782_4bd5_a7c1_7d22f0de49cc.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '7f077b4a8c5e56ec88a35abef24ec2d3fa4f86d77e0da2b6f8cdd4473c8a6081'
SOURCE_REFERENCES = (('4e6c72ac-9782-4bd5-a7c1-7d22f0de49cc', 'pictographic-primitives/health/medical cross_4e6c72ac-9782-4bd5-a7c1-7d22f0de49cc.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'medical-cross-sub32-symbol-resize'
    variant_of = 'medical-cross-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'health'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (16, 8))
        self.add_line('p1-r1-3', (16, 8), (22, 8))
        self.add_line('p1-r1-4', (22, 8), (22, 16))
        self.add_line('p1-r1-5', (22, 16), (16, 16))
        self.add_line('p1-r1-6', (16, 16), (16, 22))
        self.add_line('p1-r1-7', (16, 22), (8, 22))
        self.add_line('p1-r1-8', (8, 22), (8, 16))
        self.add_line('p1-r1-9', (8, 16), (2, 16))
        self.add_line('p1-r1-10', (2, 16), (2, 8))
        self.add_line('p1-r1-11', (2, 8), (8, 8))
        self.add_line('p1-r1-12', (8, 8), (8, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
