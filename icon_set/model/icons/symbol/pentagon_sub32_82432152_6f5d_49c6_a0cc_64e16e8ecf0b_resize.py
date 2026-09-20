"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '82432152-6f5d-49c6-a0cc-64e16e8ecf0b'
SOURCE_PATH = 'icon_set/model/icons/symbol/pentagon_sub32_82432152_6f5d_49c6_a0cc_64e16e8ecf0b.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '714fdc159f8210a6476fe5e6a285afcb86c41070e2531c9f8a6fa16611c3a9c2'
SOURCE_REFERENCES = (('82432152-6f5d-49c6-a0cc-64e16e8ecf0b', 'pictographic-primitives/symbol/pentagon_82432152-6f5d-49c6-a0cc-64e16e8ecf0b.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'pentagon-sub32-resize'
    variant_of = 'pentagon-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (12, 2), (22, 10))
        self.add_line('p1-r1-2', (22, 10), (18, 22))
        self.add_line('p1-r1-3', (18, 22), (6, 22))
        self.add_line('p1-r1-4', (6, 22), (2, 10))
        self.add_line('p1-r1-5', (2, 10), (12, 2))
        self.add_line('p1-r1-6', (12, 2), (12, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
