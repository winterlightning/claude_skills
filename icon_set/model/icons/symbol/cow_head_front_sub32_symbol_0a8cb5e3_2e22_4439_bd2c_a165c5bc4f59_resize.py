"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '0a8cb5e3-2e22-4439-bd2c-a165c5bc4f59'
SOURCE_PATH = 'icon_set/model/icons/symbol/cow_head_front_sub32_symbol_0a8cb5e3_2e22_4439_bd2c_a165c5bc4f59.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'e97b250e72ffc3d30337abaad35a2f69c4784e4e3a69dcdfc60b4af4c4aab784'
SOURCE_REFERENCES = (('0a8cb5e3-2e22-4439-bd2c-a165c5bc4f59', 'pictographic-primitives/symbol/bull head_0a8cb5e3-2e22-4439-bd2c-a165c5bc4f59.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'cow-head-front-sub32-symbol-resize'
    variant_of = 'cow-head-front-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbols/standalone'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (6, 6), (12, 6))
        self.add_line('p1-r1-2', (12, 6), (18, 6))
        self.add_line('p1-r1-3', (18, 6), (16, 18))
        self.add_arc('p1-r1-4', (16, 18), (13, 22), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (13, 22), (11, 22))
        self.add_arc('p1-r1-6', (11, 22), (8, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (8, 18), (6, 6))
        self.add_line('p2-r1-1', (6, 6), (2, 12))
        self.add_line('p2-r1-2', (2, 12), (7, 14))
        self.add_line('p3-r1-1', (18, 6), (22, 12))
        self.add_line('p3-r1-2', (22, 12), (17, 14))
        self.add_arc('p4-r1-1', (3, 2), (6, 6), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('p5-r1-1', (18, 6), (21, 2), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p5-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p5-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
