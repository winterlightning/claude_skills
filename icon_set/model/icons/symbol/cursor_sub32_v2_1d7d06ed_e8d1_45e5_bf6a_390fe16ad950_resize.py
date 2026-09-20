"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '1d7d06ed-e8d1-45e5-bf6a-390fe16ad950'
SOURCE_PATH = 'icon_set/model/icons/symbol/cursor_sub32_v2_1d7d06ed_e8d1_45e5_bf6a_390fe16ad950.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '888583981fd35326e109f774e2148e81cf9f0aa8f53c2df846384dd98958da36'
SOURCE_REFERENCES = (('1d7d06ed-e8d1-45e5-bf6a-390fe16ad950', 'pictographic-primitives/interface-essential/cursor_1d7d06ed-e8d1-45e5-bf6a-390fe16ad950.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'cursor-sub32-v2-resize'
    variant_of = 'cursor-sub32-v2'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (19, 11), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (4, 22))
        self.add_line('p1-r1-3', (4, 22), (9, 13))
        self.add_line('p2-r1-1', (9, 13), (19, 11))
        self.add_line('p3-r1-1', (9, 13), (14, 21))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
