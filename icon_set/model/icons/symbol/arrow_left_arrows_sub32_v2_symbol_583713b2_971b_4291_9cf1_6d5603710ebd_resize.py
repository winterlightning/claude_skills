"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '583713b2-971b-4291-9cf1-6d5603710ebd'
SOURCE_PATH = 'icon_set/model/icons/symbol/arrow_left_arrows_sub32_v2_symbol_583713b2_971b_4291_9cf1_6d5603710ebd.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'df9f83c2e1bca60a62e52bb6dad335027d0531100a0c478072766ebaa44fc9f7'
SOURCE_REFERENCES = (('583713b2-971b-4291-9cf1-6d5603710ebd', 'pictographic-primitives/arrows/arrow left_583713b2-971b-4291-9cf1-6d5603710ebd.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'arrow-left-arrows-sub32-v2-symbol-resize'
    variant_of = 'arrow-left-arrows-sub32-v2-symbol'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'arrows'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 10), (8, 19))
        self.add_line('p2-r1-1', (2, 10), (8, 2))
        self.add_line('p3-r1-1', (2, 10), (22, 10))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
