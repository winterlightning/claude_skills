"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'b79b156d-60e1-4f36-abe1-8af289a9b6cc'
SOURCE_PATH = 'icon_set/model/icons/symbol/three_lobed_sprout_sub32_b79b156d_60e1_4f36_abe1_8af289a9b6cc.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '18510ab42b0e0c8a4adaebb414e3ff35641eff227116fe3fb2d2370d10a62d32'
SOURCE_REFERENCES = (('b79b156d-60e1-4f36-abe1-8af289a9b6cc', 'pictographic-primitives/nature/wheat_b79b156d-60e1-4f36-abe1-8af289a9b6cc.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'three-lobed-sprout-sub32-resize'
    variant_of = 'three-lobed-sprout-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'nature/batch-04'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (2, 9), (7, 12), radius_x=8, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (7, 12), (10, 2), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (10, 2), (13, 12), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (13, 12), (18, 9), radius_x=8, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (18, 9), (10, 18), radius_x=8, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (10, 18), (2, 9), radius_x=8, radius_y=9, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (10, 18), (10, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
