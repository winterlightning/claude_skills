"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'aa83e1c0-9fa1-4d19-a918-3bd5f9af838a'
SOURCE_PATH = 'icon_set/model/icons/symbol/basket_sub32_v2_symbol_aa83e1c0_9fa1_4d19_a918_3bd5f9af838a.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f6d672c8a50322e80ba089788f4ffd300487f0e33b21baa58589660eda69ed80'
SOURCE_REFERENCES = (('aa83e1c0-9fa1-4d19-a918-3bd5f9af838a', 'pictographic-primitives/symbol/basket_aa83e1c0-9fa1-4d19-a918-3bd5f9af838a.svg'), ('790ba4c2-a8e0-42c1-a644-383157d2d39b', 'pictographic-primitives/spas/cart_790ba4c2-a8e0-42c1-a644-383157d2d39b.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'basket-sub32-v2-symbol-resize'
    variant_of = 'basket-sub32-v2-symbol'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 8), (6, 8))
        self.add_line('p1-r1-2', (6, 8), (18, 8))
        self.add_line('p1-r1-3', (18, 8), (22, 8))
        self.add_line('p1-r1-4', (22, 8), (19, 19))
        self.add_line('p1-r1-5', (19, 19), (5, 19))
        self.add_line('p1-r1-6', (5, 19), (2, 8))
        self.add_line('p2-r1-1', (6, 8), (9, 2))
        self.add_line('p3-r1-1', (18, 8), (15, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
