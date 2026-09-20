"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '7775a880-67c6-4fa0-96c0-ea7609b88a8e'
SOURCE_PATH = 'icon_set/model/icons/symbol/unlock_symbol_sub32_7775a880_67c6_4fa0_96c0_ea7609b88a8e.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '0a72112fda93fa1ba47fc0fd38b5265b12413b939f892270ba50ad04d3389b3b'
SOURCE_REFERENCES = (('7775a880-67c6-4fa0-96c0-ea7609b88a8e', 'pictographic-primitives/symbol/unlock_7775a880-67c6-4fa0-96c0-ea7609b88a8e.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'unlock-symbol-sub32-resize'
    variant_of = 'unlock-symbol-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (8, 11), (16, 11))
        self.add_arc('p1-r1-2', (16, 11), (18, 13), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (18, 13), (18, 20))
        self.add_arc('p1-r1-4', (18, 20), (16, 22), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (16, 22), (8, 22))
        self.add_arc('p1-r1-6', (8, 22), (6, 20), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (6, 20), (6, 13))
        self.add_arc('p1-r1-8', (6, 13), (8, 11), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (2, 9), (2, 7))
        self.add_arc('p2-r1-2', (2, 7), (12, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (12, 7), (12, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
