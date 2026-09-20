"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '94b02a29-f0e3-482a-8b4a-725005a9332e'
SOURCE_PATH = 'icon_set/model/icons/symbol/keyhole_sub32_94b02a29_f0e3_482a_8b4a_725005a9332e.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '647843802465903df66c5902296fc93f6dfa1e9e1c850c68f3cc09322941b3f0'
SOURCE_REFERENCES = (('94b02a29-f0e3-482a-8b4a-725005a9332e', 'pictographic-primitives/symbol/keyhole_94b02a29-f0e3-482a-8b4a-725005a9332e.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'keyhole-sub32-resize'
    variant_of = 'keyhole-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (14, 12), ((14, 12), (15, 12), (15, 12)), ((16, 11), (16, 11), (16, 11)), ((17, 10), (17, 10), (17, 9)), ((17, 9), (18, 8), (18, 8)))
        self.add_bezier('p1-r1-2', (18, 8), ((18, 8), (18, 7), (18, 7)), ((18, 7), (18, 7), (18, 7)), ((18, 6), (18, 6), (18, 5)), ((18, 5), (17, 4), (17, 4)), ((17, 4), (16, 3), (16, 3)))
        self.add_bezier('p1-r1-3', (16, 3), ((15, 3), (15, 3), (15, 3)), ((14, 2), (14, 2), (13, 2)), ((13, 2), (13, 2), (12, 2)), ((12, 2), (12, 2), (11, 2)), ((11, 2), (11, 2), (11, 2)))
        self.add_line('p1-r1-4', (11, 2), (8, 2))
        self.add_bezier('p1-r1-5', (8, 2), ((7, 2), (6, 2), (6, 3)), ((5, 3), (4, 3), (4, 4)), ((3, 5), (3, 5), (2, 6)), ((2, 7), (2, 7), (2, 8)), ((2, 8), (2, 8), (2, 8)))
        self.add_bezier('p1-r1-6', (2, 8), ((2, 8), (2, 9), (2, 9)), ((3, 10), (3, 10), (3, 11)), ((4, 11), (4, 11), (5, 12)), ((5, 12), (5, 12), (6, 12)))
        self.add_line('p1-r1-7', (6, 12), (3, 22))
        self.add_line('p1-r1-8', (3, 22), (17, 22))
        self.add_line('p1-r1-9', (17, 22), (14, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
