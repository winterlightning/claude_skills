"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '986af714-6fb8-449a-ad31-d5271f278137'
SOURCE_PATH = 'icon_set/model/icons/symbol/liras_sub32_symbol_986af714_6fb8_449a_ad31_d5271f278137.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '13cebb97fadd931ac77d790b255a66a37a18ee8d37613851b83ce5aa6082cb34'
SOURCE_REFERENCES = (('986af714-6fb8-449a-ad31-d5271f278137', 'pictographic-primitives/money/liras_986af714-6fb8-449a-ad31-d5271f278137.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'liras-sub32-symbol-resize'
    variant_of = 'liras-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'money'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (18, 6), ((18, 3), (16, 2), (13, 2)))
        self.add_bezier('p1-r1-2', (13, 2), ((9, 2), (7, 3), (7, 6)))
        self.add_line('p1-r1-3', (7, 6), (7, 17))
        self.add_arc('p1-r1-4', (7, 17), (2, 22), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (2, 22), (18, 22))
        self.add_line('p3-r1-1', (3, 10), (13, 10))
        self.add_line('p4-r1-1', (3, 16), (13, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
