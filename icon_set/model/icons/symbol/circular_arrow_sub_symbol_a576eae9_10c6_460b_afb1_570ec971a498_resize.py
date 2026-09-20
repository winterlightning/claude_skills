"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'a576eae9-10c6-460b-afb1-570ec971a498'
SOURCE_PATH = 'icon_set/model/icons/symbol/circular_arrow_sub_symbol_a576eae9_10c6_460b_afb1_570ec971a498.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'c65ebc8fd5238396156b2753dcdc44d3fbd82fdd0553d4aabfd9c907269fc6c0'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'circular-arrow-sub-symbol-resize'
    variant_of = 'circular-arrow-sub-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'primitives/mark'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('top', (2, 12), (12, 2), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('turn', (12, 2), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('bottom', (22, 18), (12, 22), radius_x=10, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('left', (12, 22), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('head-1', (16, 12), (22, 12))
        self.add_line('head-2', (22, 12), (22, 6))
        self.add_contour('tail', 'bottom', 'left', 'top', 'turn', closed=False)
        self.add_contour('head', 'head-1', 'head-2', closed=False)
        self.relate('connect', 'tail', 'head')
