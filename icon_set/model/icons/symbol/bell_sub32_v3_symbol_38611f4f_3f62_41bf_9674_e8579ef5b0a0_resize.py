"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '38611f4f-3f62-41bf-9674-e8579ef5b0a0'
SOURCE_PATH = 'icon_set/model/icons/symbol/bell_sub32_v3_symbol_38611f4f_3f62_41bf_9674_e8579ef5b0a0.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '5383d30993ce2fbb6d219a4a35092cd63a9e23de4d33cb33ce05c3a679757161'
SOURCE_REFERENCES = (('38611f4f-3f62-41bf-9674-e8579ef5b0a0', 'pictographic-primitives/symbol/bell_38611f4f-3f62-41bf-9674-e8579ef5b0a0.svg'), ('77ec3808-7ec4-4c77-9f4e-0bb8e7476863', 'pictographic-primitives/symbol/bell_77ec3808-7ec4-4c77-9f4e-0bb8e7476863.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'bell-sub32-v3-symbol-resize'
    variant_of = 'bell-sub32-v3-symbol'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'symbols/standalone'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (10, 4), ((11, 4), (12, 5), (12, 5)), ((13, 5), (14, 6), (14, 6)), ((15, 7), (15, 8), (16, 9)), ((16, 9), (16, 10), (16, 11)))
        self.add_bezier('p1-r1-2', (16, 11), ((16, 15), (19, 15), (19, 18)))
        self.add_bezier('p1-r1-3', (19, 18), ((19, 18), (19, 19), (19, 19)), ((19, 19), (19, 19), (19, 19)), ((19, 19), (19, 19), (18, 19)), ((18, 19), (18, 19), (18, 19)))
        self.add_line('p1-r1-4', (18, 19), (13, 19))
        self.add_line('p1-r1-5', (13, 19), (8, 19))
        self.add_line('p1-r1-6', (8, 19), (3, 19))
        self.add_bezier('p1-r1-7', (3, 19), ((3, 19), (3, 19), (3, 19)), ((2, 19), (2, 19), (2, 19)), ((2, 19), (2, 19), (2, 19)), ((2, 19), (2, 18), (2, 18)))
        self.add_bezier('p1-r1-8', (2, 18), ((2, 15), (5, 15), (5, 11)))
        self.add_bezier('p1-r1-9', (5, 11), ((5, 11), (5, 11), (5, 11)), ((5, 10), (5, 10), (5, 9)), ((6, 8), (6, 7), (6, 7)), ((7, 6), (7, 6), (8, 5)), ((9, 5), (9, 4), (10, 4)))
        self.add_line('p2-r1-1', (10, 2), (10, 4))
        self.add_bezier('p3-r1-1', (13, 19), ((13, 20), (12, 21), (12, 21)), ((11, 22), (11, 22), (10, 22)), ((10, 22), (10, 22), (9, 21)), ((9, 21), (8, 20), (8, 19)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-9', 'p2-r1-1')
