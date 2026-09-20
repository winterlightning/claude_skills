"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'd62fa8d6-31ca-4052-9e36-0909d6c1a80e'
SOURCE_PATH = 'icon_set/model/icons/symbol/chip_sub32_symbol_d62fa8d6_31ca_4052_9e36_0909d6c1a80e.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '430b98a3f80b3cc13b977ed838a1db51320488ee06d7920772a41f0568e5ee7c'
SOURCE_REFERENCES = (('d62fa8d6-31ca-4052-9e36-0909d6c1a80e', 'pictographic-primitives/state/chip_d62fa8d6-31ca-4052-9e36-0909d6c1a80e.svg'), ('d0dd0f52-f552-4b31-8bb1-bed37c84eff0', 'pictographic-primitives/symbol/chip_d0dd0f52-f552-4b31-8bb1-bed37c84eff0.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'chip-sub32-symbol-resize'
    variant_of = 'chip-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'state'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (6, 6), (18, 6))
        self.add_line('p1-r1-2', (18, 6), (18, 18))
        self.add_line('p1-r1-3', (18, 18), (6, 18))
        self.add_line('p1-r1-4', (6, 18), (6, 6))
        self.add_line('p2-r1-1', (10, 2), (10, 6))
        self.add_line('p3-r1-1', (10, 18), (10, 22))
        self.add_line('p4-r1-1', (2, 10), (6, 10))
        self.add_line('p5-r1-1', (18, 10), (22, 10))
        self.add_line('p6-r1-1', (14, 2), (14, 6))
        self.add_line('p7-r1-1', (14, 18), (14, 22))
        self.add_line('p8-r1-1', (2, 14), (6, 14))
        self.add_line('p9-r1-1', (18, 14), (22, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
