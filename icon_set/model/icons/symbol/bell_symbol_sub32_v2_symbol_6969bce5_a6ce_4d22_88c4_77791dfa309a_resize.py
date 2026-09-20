"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '6969bce5-a6ce-4d22-88c4-77791dfa309a'
SOURCE_PATH = 'icon_set/model/icons/symbol/bell_symbol_sub32_v2_symbol_6969bce5_a6ce_4d22_88c4_77791dfa309a.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '27c1115ffb3c53c467048c33abff53d7eba2c9acbab93dc5deeac96b19b28155'
SOURCE_REFERENCES = (('6969bce5-a6ce-4d22-88c4-77791dfa309a', 'pictographic-primitives/symbol/bell_6969bce5-a6ce-4d22-88c4-77791dfa309a.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'bell-symbol-sub32-v2-symbol-resize'
    variant_of = 'bell-symbol-sub32-v2-symbol'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 22), (2, 14))
        self.add_bezier('p1-r1-2', (2, 14), ((2, 13), (2, 12), (3, 11)), ((3, 10), (4, 9), (4, 8)), ((5, 8), (6, 7), (7, 7)), ((8, 6), (9, 6), (10, 6)))
        self.add_bezier('p1-r1-3', (10, 6), ((10, 6), (11, 6), (11, 6)), ((12, 6), (13, 6), (13, 6)), ((14, 7), (15, 7), (16, 8)), ((17, 9), (18, 10), (18, 11)), ((19, 12), (19, 13), (19, 14)), ((19, 14), (19, 14), (19, 14)))
        self.add_line('p1-r1-4', (19, 14), (19, 22))
        self.add_line('p2-r1-1', (2, 22), (19, 22))
        self.add_line('p3-r1-1', (10, 2), (10, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
