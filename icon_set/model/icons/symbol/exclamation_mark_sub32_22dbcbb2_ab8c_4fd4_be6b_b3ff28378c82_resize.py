"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '22dbcbb2-ab8c-4fd4-be6b-b3ff28378c82'
SOURCE_PATH = 'icon_set/model/icons/symbol/exclamation_mark_sub32_22dbcbb2_ab8c_4fd4_be6b_b3ff28378c82.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '41c57568230fbecffd4faaa6927fa40d4586b5fc0d6bf8c846a4132d3d13a1ee'
SOURCE_REFERENCES = (('22dbcbb2-ab8c-4fd4-be6b-b3ff28378c82', 'pictographic-primitives/symbol/exclamation_22dbcbb2-ab8c-4fd4-be6b-b3ff28378c82.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'exclamation-mark-sub32-resize'
    variant_of = 'exclamation-mark-sub32'
    variant_label = 'Resize 4 × 24'
    canvas_width = 4
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (2, 16))
        self.add_line('p2-r1-1', (2, 22), (2, 22))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
