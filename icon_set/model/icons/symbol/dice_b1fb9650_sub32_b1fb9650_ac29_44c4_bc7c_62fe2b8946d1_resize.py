"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'b1fb9650-ac29-44c4-bc7c-62fe2b8946d1'
SOURCE_PATH = 'icon_set/model/icons/symbol/dice_b1fb9650_sub32_b1fb9650_ac29_44c4_bc7c_62fe2b8946d1.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '49bae4e1f4d5a5b9783b43f91f2a9c5c1b1f69a2d80261c92f3f88d9c8d8e533'
SOURCE_REFERENCES = (('b1fb9650-ac29-44c4-bc7c-62fe2b8946d1', 'pictographic-primitives/entertainment/dice_b1fb9650-ac29-44c4-bc7c-62fe2b8946d1.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'dice-b1fb9650-sub32-resize'
    variant_of = 'dice-b1fb9650-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'entertainment'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (12, 12), (12, 12))
        self.add_line('p2-r1-1', (2, 12), (2, 5))
        self.add_arc('p2-r1-2', (2, 5), (5, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (5, 2), (12, 2))
        self.add_line('p2-r1-4', (12, 2), (19, 2))
        self.add_arc('p2-r1-5', (19, 2), (22, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-6', (22, 5), (22, 12))
        self.add_line('p2-r1-7', (22, 12), (22, 19))
        self.add_arc('p2-r1-8', (22, 19), (19, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-9', (19, 22), (12, 22))
        self.add_line('p2-r1-10', (12, 22), (5, 22))
        self.add_arc('p2-r1-11', (5, 22), (2, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-12', (2, 19), (2, 12))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', 'p2-r1-12', closed=False)
