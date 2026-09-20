"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'd11d120b-44dc-4986-8c2a-a773c8830e0c'
SOURCE_PATH = 'icon_set/model/icons/symbol/flame_with_inner_drop_sub32_symbol_d11d120b_44dc_4986_8c2a_a773c8830e0c.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'a0c486c66e443e6efad06405ca2321e6ead985a3776b29086b471c06faddec5d'
SOURCE_REFERENCES = (('d11d120b-44dc-4986-8c2a-a773c8830e0c', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/flame_d11d120b-44dc-4986-8c2a-a773c8830e0c.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'flame-with-inner-drop-sub32-symbol-resize'
    variant_of = 'flame-with-inner-drop-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'objects/fire'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (7, 22), ((3, 20), (2, 18), (2, 15)))
        self.add_bezier('p1-r1-2', (2, 15), ((2, 10), (9, 8), (9, 4)))
        self.add_bezier('p1-r1-3', (9, 4), ((9, 3), (9, 3), (9, 2)))
        self.add_bezier('p1-r1-4', (9, 2), ((12, 4), (14, 6), (14, 9)))
        self.add_bezier('p1-r1-5', (14, 9), ((14, 10), (14, 11), (13, 11)))
        self.add_bezier('p1-r1-6', (13, 11), ((16, 11), (18, 10), (18, 8)))
        self.add_bezier('p1-r1-7', (18, 8), ((18, 11), (18, 13), (18, 15)))
        self.add_bezier('p1-r1-8', (18, 15), ((18, 18), (16, 21), (13, 22)))
        self.add_bezier('p2-r1-1', (7, 22), ((6, 21), (6, 20), (6, 18)))
        self.add_bezier('p2-r1-2', (6, 18), ((6, 16), (8, 14), (10, 13)))
        self.add_bezier('p2-r1-3', (10, 13), ((10, 16), (14, 16), (14, 19)))
        self.add_bezier('p2-r1-4', (14, 19), ((14, 20), (14, 21), (13, 22)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-4')
