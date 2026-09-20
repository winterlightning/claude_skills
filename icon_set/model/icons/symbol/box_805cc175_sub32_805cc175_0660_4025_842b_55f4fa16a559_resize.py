"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '805cc175-0660-4025-842b-55f4fa16a559'
SOURCE_PATH = 'icon_set/model/icons/symbol/box_805cc175_sub32_805cc175_0660_4025_842b_55f4fa16a559.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '88070f7cf32b249742f3f8b054a29926ab3fb72dbb67615e8c01ff990d53e05d'
SOURCE_REFERENCES = (('805cc175-0660-4025-842b-55f4fa16a559', 'pictographic-primitives/shipping/box_805cc175-0660-4025-842b-55f4fa16a559.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'box-805cc175-sub32-resize'
    variant_of = 'box-805cc175-sub32'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'shipping'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (6, 2), (20, 2))
        self.add_line('p1-r1-2', (20, 2), (34, 2))
        self.add_arc('p1-r1-3', (34, 2), (38, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (38, 6), (38, 11))
        self.add_line('p1-r1-5', (38, 11), (38, 25))
        self.add_arc('p1-r1-6', (38, 25), (33, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (33, 30), (7, 30))
        self.add_arc('p1-r1-8', (7, 30), (2, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (2, 25), (2, 11))
        self.add_line('p1-r1-10', (2, 11), (2, 6))
        self.add_arc('p1-r1-11', (2, 6), (6, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (2, 11), (20, 11))
        self.add_line('p2-r1-2', (20, 11), (38, 11))
        self.add_line('p3-r1-1', (20, 2), (20, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
        self.relate('connect', 'p1-r1-5', 'p2-r1-2')
        self.relate('connect', 'p1-r1-9', 'p2-r1-1')
        self.relate('connect', 'p1-r1-10', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
