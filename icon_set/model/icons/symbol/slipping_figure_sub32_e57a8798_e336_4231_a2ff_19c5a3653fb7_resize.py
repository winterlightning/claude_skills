"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'e57a8798-e336-4231-a2ff-19c5a3653fb7'
SOURCE_PATH = 'icon_set/model/icons/symbol/slipping_figure_sub32_e57a8798_e336_4231_a2ff_19c5a3653fb7.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f9a64b6bce1f789ee2a66b4487a96d62c9469584ab1bf3e294f55d50a978aa27'
SOURCE_REFERENCES = (('e57a8798-e336-4231-a2ff-19c5a3653fb7', 'pictographic-primitives/transportation/slippery_e57a8798-e336-4231-a2ff-19c5a3653fb7.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'slipping-figure-sub32-resize'
    variant_of = 'slipping-figure-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'transportation'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (16, 4), (20, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (20, 4), (16, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (4, 4), (12, 10))
        self.add_line('p2-r1-2', (12, 10), (18, 13))
        self.add_line('p2-r1-3', (18, 13), (22, 13))
        self.add_line('p3-r1-1', (12, 10), (8, 16))
        self.add_line('p4-r1-1', (8, 16), (2, 16))
        self.add_line('p5-r1-1', (8, 16), (14, 20))
        self.add_line('p5-r1-2', (14, 20), (12, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
