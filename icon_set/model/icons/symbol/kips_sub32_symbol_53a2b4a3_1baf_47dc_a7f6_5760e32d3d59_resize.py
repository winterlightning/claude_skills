"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '53a2b4a3-1baf-47dc-a7f6-5760e32d3d59'
SOURCE_PATH = 'icon_set/model/icons/symbol/kips_sub32_symbol_53a2b4a3_1baf_47dc_a7f6_5760e32d3d59.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '3116a62119c4d96b73e314e23b8a005cf0f3c7b92e2ff6d9a98905f52ee95cd6'
SOURCE_REFERENCES = (('53a2b4a3-1baf-47dc-a7f6-5760e32d3d59', 'pictographic-primitives/money/kips_53a2b4a3-1baf-47dc-a7f6-5760e32d3d59.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'kips-sub32-symbol-resize'
    variant_of = 'kips-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'money'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (17, 12), (2, 12))
        self.add_line('p2-r1-1', (18, 22), (9, 12))
        self.add_line('p3-r1-1', (17, 3), (9, 12))
        self.add_line('p4-r1-1', (6, 2), (6, 22))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
