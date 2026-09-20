"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '97a9265b-3cf4-420c-8a2b-da7cd9955c06'
SOURCE_PATH = 'icon_set/model/icons/symbol/helmet_97a9265b_sub32_v2_symbol_97a9265b_3cf4_420c_8a2b_da7cd9955c06.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '4261e5ce7edcd0a6361772ab9d41b680767ac3d63ced791c865c7d64034b9cfa'
SOURCE_REFERENCES = (('97a9265b-3cf4-420c-8a2b-da7cd9955c06', 'pictographic-primitives/protection/helmet_97a9265b-3cf4-420c-8a2b-da7cd9955c06.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'helmet-97a9265b-sub32-v2-symbol-resize'
    variant_of = 'helmet-97a9265b-sub32-v2-symbol'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'protection'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 19), (2, 13))
        self.add_arc('p1-r1-2', (2, 13), (12, 3), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (12, 3), (22, 13), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (22, 13), (22, 19))
        self.add_line('p1-r1-5', (22, 19), (2, 19))
        self.add_line('p2-r1-1', (12, 2), (12, 3))
        self.add_line('p3-r1-1', (12, 3), (12, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
