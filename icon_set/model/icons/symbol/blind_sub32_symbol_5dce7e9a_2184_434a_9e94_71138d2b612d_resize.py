"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '5dce7e9a-2184-434a-9e94-71138d2b612d'
SOURCE_PATH = 'icon_set/model/icons/symbol/blind_sub32_symbol_5dce7e9a_2184_434a_9e94_71138d2b612d.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '4de59bb9940f6a83e68871e0ff937ff2bf755936595393a592ca014fc4796e94'
SOURCE_REFERENCES = (('5dce7e9a-2184-434a-9e94-71138d2b612d', 'pictographic-primitives/interface-essential/blind_5dce7e9a-2184-434a-9e94-71138d2b612d.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'blind-sub32-symbol-resize'
    variant_of = 'blind-sub32-symbol'
    variant_label = 'Resize 24 × 17'
    canvas_width = 24
    canvas_height = 17
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (2, 8), ((2, 8), (2, 8), (3, 7)), ((3, 7), (3, 7), (3, 6)), ((4, 6), (4, 6), (4, 6)), ((4, 5), (5, 5), (5, 5)))
        self.add_bezier('p1-r1-2', (5, 5), ((6, 4), (8, 3), (9, 2)), ((10, 2), (11, 2), (12, 2)), ((13, 2), (13, 2), (14, 2)), ((15, 2), (17, 3), (18, 4)), ((20, 5), (21, 7), (22, 8)))
        self.add_bezier('p1-r1-3', (22, 8), ((22, 9), (22, 9), (21, 9)), ((21, 10), (21, 10), (21, 10)), ((20, 11), (20, 11), (20, 11)), ((20, 12), (19, 12), (19, 12)))
        self.add_bezier('p1-r1-4', (19, 12), ((18, 14), (16, 14), (15, 15)), ((14, 15), (13, 15), (12, 15)), ((11, 15), (11, 15), (10, 15)), ((8, 14), (7, 14), (6, 12)), ((4, 11), (3, 10), (2, 8)))
        self.add_line('p2-r1-1', (5, 5), (20, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
