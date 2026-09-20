"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '623f8b25-c15d-42c1-87af-b086cba90fe2'
SOURCE_PATH = 'icon_set/model/icons/symbol/math_sub32_623f8b25_c15d_42c1_87af_b086cba90fe2.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '2aa3074664f026019bfd30fcdeedb65e26dd6cd0f420e8a4cbf12f081b729cc4'
SOURCE_REFERENCES = (('623f8b25-c15d-42c1-87af-b086cba90fe2', 'pictographic-primitives/symbol/math_623f8b25-c15d-42c1-87af-b086cba90fe2.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'math-sub32-resize'
    variant_of = 'math-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (10, 2), (10, 10))
        self.add_line('p1-r1-2', (10, 10), (2, 10))
        self.add_line('p2-r1-1', (10, 18), (10, 10))
        self.add_line('p2-r1-2', (10, 10), (18, 10))
        self.add_line('p3-r1-1', (2, 22), (18, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
