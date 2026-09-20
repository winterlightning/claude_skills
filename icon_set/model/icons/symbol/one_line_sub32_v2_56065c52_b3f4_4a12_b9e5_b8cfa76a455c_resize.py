"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '56065c52-b3f4-4a12-b9e5-b8cfa76a455c'
SOURCE_PATH = 'icon_set/model/icons/symbol/one_line_sub32_v2_56065c52_b3f4_4a12_b9e5_b8cfa76a455c.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '035ee868a9f0f3823e0c3ebd5d9dd7632bced83aae9ff8b42437ac91704f840f'
SOURCE_REFERENCES = (('56065c52-b3f4-4a12-b9e5-b8cfa76a455c', 'pictographic-primitives/symbol/one line_56065c52-b3f4-4a12-b9e5-b8cfa76a455c.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'one-line-sub32-v2-resize'
    variant_of = 'one-line-sub32-v2'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (19, 2), (2, 22))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
