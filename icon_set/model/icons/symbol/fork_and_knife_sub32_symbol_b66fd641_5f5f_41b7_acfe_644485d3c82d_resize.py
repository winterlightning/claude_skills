"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'b66fd641-5f5f-41b7-acfe-644485d3c82d'
SOURCE_PATH = 'icon_set/model/icons/symbol/fork_and_knife_sub32_symbol_b66fd641_5f5f_41b7_acfe_644485d3c82d.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '637f2832a86dee9ecc882ef05308b5a2d2c92de6f78ceecb54db5ae9ae7220e3'
SOURCE_REFERENCES = (('b66fd641-5f5f-41b7-acfe-644485d3c82d', 'pictographic-primitives/symbol/fork and knife_b66fd641-5f5f-41b7-acfe-644485d3c82d.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'fork-and-knife-sub32-symbol-resize'
    variant_of = 'fork-and-knife-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (2, 8))
        self.add_bezier('p1-r1-2', (2, 8), ((2, 10), (3, 11), (3, 12)))
        self.add_bezier('p1-r1-3', (3, 12), ((4, 13), (6, 13), (6, 13)))
        self.add_bezier('p1-r1-4', (6, 13), ((6, 13), (6, 13), (6, 13)))
        self.add_arc('p1-r1-5', (6, 13), (11, 8), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p1-r1-6', (11, 8), (11, 2))
        self.add_line('p2-r1-1', (6, 2), (6, 13))
        self.add_line('p3-r1-1', (6, 13), (6, 22))
        self.add_line('p4-r1-1', (18, 22), (18, 2))
        self.add_line('p4-r1-2', (18, 2), (22, 11))
        self.add_line('p4-r1-3', (22, 11), (22, 16))
        self.add_line('p4-r1-4', (22, 16), (18, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
