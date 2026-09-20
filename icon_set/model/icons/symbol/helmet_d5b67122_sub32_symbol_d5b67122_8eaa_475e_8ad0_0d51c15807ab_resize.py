"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'd5b67122-8eaa-475e-8ad0-0d51c15807ab'
SOURCE_PATH = 'icon_set/model/icons/symbol/helmet_d5b67122_sub32_symbol_d5b67122_8eaa_475e_8ad0_0d51c15807ab.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '3cdf572dac342607b984c18c96d4b036807bf338dd23d9a67d9cbab57867d1dd'
SOURCE_REFERENCES = (('d5b67122-8eaa-475e-8ad0-0d51c15807ab', 'pictographic-primitives/protection/helmet_d5b67122-8eaa-475e-8ad0-0d51c15807ab.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'helmet-d5b67122-sub32-symbol-resize'
    variant_of = 'helmet-d5b67122-sub32-symbol'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'protection'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (22, 18), (2, 18))
        self.add_line('p2-r1-1', (14, 2), (10, 2))
        self.add_line('p2-r1-2', (10, 2), (10, 4))
        self.add_line('p2-r1-3', (10, 4), (10, 5))
        self.add_arc('p2-r1-4', (10, 5), (4, 14), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_arc('p2-r1-5', (4, 14), (4, 18), radius_x=29, radius_y=30, large_arc=False, sweep=False)
        self.add_line('p3-r1-1', (10, 13), (10, 5))
        self.add_arc('p4-r1-1', (15, 5), (20, 14), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (20, 14), (20, 18), radius_x=29, radius_y=30, large_arc=False, sweep=True)
        self.add_line('p5-r1-1', (15, 13), (15, 4))
        self.add_line('p5-r1-2', (15, 4), (14, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p5-r1-2')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
        self.relate('connect', 'p2-r1-4', 'p3-r1-1')
