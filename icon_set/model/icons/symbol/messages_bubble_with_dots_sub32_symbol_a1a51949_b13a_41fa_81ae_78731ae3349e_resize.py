"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'a1a51949-b13a-41fa-81ae-78731ae3349e'
SOURCE_PATH = 'icon_set/model/icons/symbol/messages_bubble_with_dots_sub32_symbol_a1a51949_b13a_41fa_81ae_78731ae3349e.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '823870da7eab5d08bdd7ba8f441b66057245d8205b60744637c2731348fc7fac'
SOURCE_REFERENCES = (('a1a51949-b13a-41fa-81ae-78731ae3349e', 'pictographic-primitives/symbol/messages bubble with dots_a1a51949-b13a-41fa-81ae-78731ae3349e.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'messages-bubble-with-dots-sub32-symbol-resize'
    variant_of = 'messages-bubble-with-dots-sub32-symbol'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (3, 18), ((3, 17), (4, 17), (5, 16)))
        self.add_bezier('p1-r1-2', (5, 16), ((5, 16), (5, 15), (5, 15)))
        self.add_bezier('p1-r1-3', (5, 15), ((5, 15), (5, 15), (5, 15)))
        self.add_bezier('p1-r1-4', (5, 15), ((5, 15), (4, 14), (3, 14)))
        self.add_bezier('p1-r1-5', (3, 14), ((3, 13), (2, 11), (2, 10)))
        self.add_bezier('p1-r1-6', (2, 10), ((2, 9), (2, 9), (2, 9)))
        self.add_bezier('p1-r1-7', (2, 9), ((2, 9), (2, 9), (2, 9)))
        self.add_bezier('p1-r1-8', (2, 9), ((2, 9), (2, 8), (3, 7)))
        self.add_bezier('p1-r1-9', (3, 7), ((4, 3), (8, 2), (11, 2)))
        self.add_bezier('p1-r1-10', (11, 2), ((11, 2), (11, 2), (12, 2)))
        self.add_bezier('p1-r1-11', (12, 2), ((12, 2), (12, 2), (13, 2)))
        self.add_bezier('p1-r1-12', (13, 2), ((16, 2), (20, 3), (21, 7)))
        self.add_bezier('p1-r1-13', (21, 7), ((22, 8), (22, 9), (22, 9)))
        self.add_bezier('p1-r1-14', (22, 9), ((22, 9), (22, 9), (22, 10)))
        self.add_bezier('p1-r1-15', (22, 10), ((22, 11), (22, 11), (21, 12)))
        self.add_bezier('p1-r1-16', (21, 12), ((19, 16), (16, 17), (12, 17)))
        self.add_bezier('p1-r1-17', (12, 17), ((12, 17), (12, 17), (11, 17)))
        self.add_bezier('p1-r1-18', (11, 17), ((11, 17), (10, 17), (9, 17)))
        self.add_bezier('p1-r1-19', (9, 17), ((8, 17), (8, 17), (8, 17)))
        self.add_bezier('p1-r1-20', (8, 17), ((8, 17), (8, 17), (8, 17)))
        self.add_bezier('p1-r1-21', (8, 17), ((8, 17), (7, 17), (6, 17)))
        self.add_bezier('p1-r1-22', (6, 17), ((6, 18), (5, 18), (3, 18)))
        self.add_bezier('p1-r1-23', (3, 18), ((3, 18), (3, 18), (3, 18)))
        self.add_bezier('p1-r1-24', (3, 18), ((3, 18), (3, 18), (3, 18)))
        self.add_line('p2-r1-1', (6, 9), (6, 9))
        self.add_line('p3-r1-1', (12, 9), (12, 9))
        self.add_line('p4-r1-1', (18, 9), (18, 9))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', 'p1-r1-21', 'p1-r1-22', 'p1-r1-23', 'p1-r1-24', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
