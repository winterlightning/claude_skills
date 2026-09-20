"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '43ebe571-7748-45bd-9b7e-bba72b5f6a14'
SOURCE_PATH = 'icon_set/model/icons/symbol/skull_1_sub32_symbol_43ebe571_7748_45bd_9b7e_bba72b5f6a14.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'c1feee9daaf4cca36719d351613b2f13fbca3359b642b200e23c7f12b27cb185'
SOURCE_REFERENCES = (('43ebe571-7748-45bd-9b7e-bba72b5f6a14', 'pictographic-primitives/interface-essential/skull 1_43ebe571-7748-45bd-9b7e-bba72b5f6a14.svg'), ('b6589244-b5a7-49bf-bf40-d9b773c9d505', 'pictographic-primitives/interface-essential/skull_b6589244-b5a7-49bf-bf40-d9b773c9d505.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'skull-1-sub32-symbol-resize'
    variant_of = 'skull-1-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (15, 12), (17, 11))
        self.add_line('p2-r1-1', (9, 12), (7, 11))
        self.add_line('p3-r1-1', (17, 22), (17, 19))
        self.add_bezier('p3-r1-2', (17, 19), ((18, 18), (21, 18), (22, 14)))
        self.add_bezier('p3-r1-3', (22, 14), ((22, 13), (22, 13), (22, 12)))
        self.add_bezier('p3-r1-4', (22, 12), ((22, 8), (21, 6), (19, 5)))
        self.add_bezier('p3-r1-5', (19, 5), ((17, 3), (15, 2), (12, 2)))
        self.add_bezier('p3-r1-6', (12, 2), ((9, 2), (7, 3), (5, 5)))
        self.add_bezier('p3-r1-7', (5, 5), ((3, 6), (2, 8), (2, 12)))
        self.add_bezier('p3-r1-8', (2, 12), ((2, 13), (2, 13), (2, 14)))
        self.add_bezier('p3-r1-9', (2, 14), ((3, 18), (6, 18), (7, 19)))
        self.add_line('p3-r1-10', (7, 19), (7, 22))
        self.add_line('p4-r1-1', (12, 22), (12, 21))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', 'p3-r1-10', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
