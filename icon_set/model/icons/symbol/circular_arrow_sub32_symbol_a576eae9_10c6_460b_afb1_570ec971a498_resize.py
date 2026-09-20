"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'a576eae9-10c6-460b-afb1-570ec971a498'
SOURCE_PATH = 'icon_set/model/icons/symbol/circular_arrow_sub32_symbol_a576eae9_10c6_460b_afb1_570ec971a498.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '3108ffe80de6710f2fad9e466bc8e52c0fafe83823d89af5339e8aa963724b60'
SOURCE_REFERENCES = (('a576eae9-10c6-460b-afb1-570ec971a498', 'pictographic-primitives/state/circular arrow_a576eae9-10c6-460b-afb1-570ec971a498.svg'), ('b4e2a04a-d4a8-40d4-a5ea-cc2cb10d5181', 'pictographic-primitives/symbol/arrow circular_b4e2a04a-d4a8-40d4-a5ea-cc2cb10d5181.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'circular-arrow-sub32-symbol-resize'
    variant_of = 'circular-arrow-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'state'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (21, 7), (18, 5))
        self.add_bezier('p1-r1-2', (18, 5), ((18, 4), (18, 4), (17, 3)))
        self.add_bezier('p1-r1-3', (17, 3), ((16, 3), (14, 2), (13, 2)))
        self.add_bezier('p1-r1-4', (13, 2), ((12, 2), (12, 2), (12, 2)))
        self.add_bezier('p1-r1-5', (12, 2), ((12, 2), (11, 2), (11, 2)))
        self.add_bezier('p1-r1-6', (11, 2), ((11, 2), (10, 2), (9, 3)))
        self.add_bezier('p1-r1-7', (9, 3), ((6, 3), (4, 6), (3, 8)))
        self.add_bezier('p1-r1-8', (3, 8), ((2, 9), (2, 10), (2, 11)))
        self.add_bezier('p1-r1-9', (2, 11), ((2, 11), (2, 11), (2, 11)))
        self.add_bezier('p1-r1-10', (2, 11), ((2, 12), (2, 12), (2, 12)))
        self.add_bezier('p1-r1-11', (2, 12), ((2, 16), (5, 20), (8, 21)))
        self.add_bezier('p1-r1-12', (8, 21), ((10, 22), (11, 22), (11, 22)))
        self.add_bezier('p1-r1-13', (11, 22), ((12, 22), (12, 22), (12, 22)))
        self.add_bezier('p1-r1-14', (12, 22), ((12, 22), (13, 22), (13, 22)))
        self.add_bezier('p1-r1-15', (13, 22), ((16, 22), (19, 20), (21, 17)))
        self.add_bezier('p1-r1-16', (21, 17), ((21, 17), (21, 16), (21, 16)))
        self.add_line('p1-r1-17', (21, 16), (22, 13))
        self.add_line('p2-r1-1', (16, 8), (21, 8))
        self.add_line('p2-r1-2', (21, 8), (21, 3))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
