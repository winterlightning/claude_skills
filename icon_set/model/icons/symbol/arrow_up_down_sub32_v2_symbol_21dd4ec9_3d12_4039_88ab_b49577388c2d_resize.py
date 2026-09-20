"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '21dd4ec9-3d12-4039-88ab-b49577388c2d'
SOURCE_PATH = 'icon_set/model/icons/symbol/arrow_up_down_sub32_v2_symbol_21dd4ec9_3d12_4039_88ab_b49577388c2d.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'c3d01c4ed7f413359ad935c468fd8d0c15907cd6af48d6ee140ffb8aab0d165b'
SOURCE_REFERENCES = (('21dd4ec9-3d12-4039-88ab-b49577388c2d', 'pictographic-primitives/symbol/arrow up down_21dd4ec9-3d12-4039-88ab-b49577388c2d.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'arrow-up-down-sub32-v2-symbol-resize'
    variant_of = 'arrow-up-down-sub32-v2-symbol'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 6), (6, 2))
        self.add_line('p2-r1-1', (6, 2), (6, 19))
        self.add_line('p3-r1-1', (6, 2), (10, 6))
        self.add_line('p4-r1-1', (18, 2), (18, 19))
        self.add_line('p5-r1-1', (14, 15), (18, 19))
        self.add_line('p6-r1-1', (22, 15), (18, 19))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
