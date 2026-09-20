"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'c718dafa-f70c-4dd4-a8fd-0d77a06c599f'
SOURCE_PATH = 'icon_set/model/icons/symbol/qr_code_shopping_sub32_v2_c718dafa_f70c_4dd4_a8fd_0d77a06c599f.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '92a2d14abed6bb6640788430f6926fc9ac30aad2f2325da788fc0755503e2320'
SOURCE_REFERENCES = (('c718dafa-f70c-4dd4-a8fd-0d77a06c599f', 'pictographic-primitives/shopping/qr code_c718dafa-f70c-4dd4-a8fd-0d77a06c599f.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'qr-code-shopping-sub32-v2-resize'
    variant_of = 'qr-code-shopping-sub32-v2'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'shopping'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 19), (2, 2))
        self.add_line('p2-r1-1', (9, 2), (9, 12))
        self.add_line('p3-r1-1', (15, 2), (15, 12))
        self.add_line('p4-r1-1', (22, 2), (22, 19))
        self.add_line('p5-r1-1', (9, 18), (9, 19))
        self.add_line('p6-r1-1', (15, 18), (15, 19))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
