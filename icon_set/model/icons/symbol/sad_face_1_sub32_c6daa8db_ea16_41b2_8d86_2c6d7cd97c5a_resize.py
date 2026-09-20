"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'c6daa8db-ea16-41b2-8d86-2c6d7cd97c5a'
SOURCE_PATH = 'icon_set/model/icons/symbol/sad_face_1_sub32_c6daa8db_ea16_41b2_8d86_2c6d7cd97c5a.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'd83fca64d92dfb0f1e2f037b944f93f84322dfe3994e453901802d6af42517fd'
SOURCE_REFERENCES = (('c6daa8db-ea16-41b2-8d86-2c6d7cd97c5a', 'pictographic-primitives/symbol/sad face 1_c6daa8db-ea16-41b2-8d86-2c6d7cd97c5a.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'sad-face-1-sub32-resize'
    variant_of = 'sad-face-1-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (6, 6), (6, 2))
        self.add_line('p2-r1-1', (17, 6), (17, 2))
        self.add_bezier('p3-r1-1', (2, 18), ((3, 16), (5, 14), (7, 13)))
        self.add_bezier('p3-r1-2', (7, 13), ((8, 12), (10, 11), (12, 11)))
        self.add_bezier('p3-r1-3', (12, 11), ((16, 11), (20, 14), (22, 18)))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
