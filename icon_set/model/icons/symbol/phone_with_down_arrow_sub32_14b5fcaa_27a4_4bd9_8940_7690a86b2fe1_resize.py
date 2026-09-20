"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '14b5fcaa-27a4-4bd9-8940-7690a86b2fe1'
SOURCE_PATH = 'icon_set/model/icons/symbol/phone_with_down_arrow_sub32_14b5fcaa_27a4_4bd9_8940_7690a86b2fe1.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'aeaec06df18f8349f7febb788645407251525d7882bdf552154d6f9a30865da9'
SOURCE_REFERENCES = (('14b5fcaa-27a4-4bd9-8940-7690a86b2fe1', 'pictographic-primitives/symbol/phone with down arrow_14b5fcaa-27a4-4bd9-8940-7690a86b2fe1.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'phone-with-down-arrow-sub32-resize'
    variant_of = 'phone-with-down-arrow-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (22, 2), (16, 8))
        self.add_line('p1-r1-2', (16, 8), (21, 8))
        self.add_line('p2-r1-1', (16, 3), (16, 8))
        self.add_bezier('p3-r1-1', (12, 19), ((13, 18), (14, 18), (15, 16)))
        self.add_bezier('p3-r1-2', (15, 16), ((16, 16), (16, 15), (16, 15)))
        self.add_bezier('p3-r1-3', (16, 15), ((17, 15), (18, 16), (18, 16)))
        self.add_line('p3-r1-4', (18, 16), (21, 18))
        self.add_bezier('p3-r1-5', (21, 18), ((21, 18), (21, 18), (21, 18)))
        self.add_bezier('p3-r1-6', (21, 18), ((21, 19), (20, 20), (20, 21)))
        self.add_bezier('p3-r1-7', (20, 21), ((19, 21), (18, 22), (18, 22)))
        self.add_bezier('p3-r1-8', (18, 22), ((18, 22), (18, 22), (17, 22)))
        self.add_bezier('p3-r1-9', (17, 22), ((17, 22), (17, 22), (17, 22)))
        self.add_bezier('p3-r1-10', (17, 22), ((16, 22), (13, 21), (12, 19)))
        self.add_bezier('p3-r1-11', (12, 19), ((9, 17), (6, 14), (4, 11)))
        self.add_bezier('p3-r1-12', (4, 11), ((3, 10), (2, 8), (2, 6)))
        self.add_bezier('p3-r1-13', (2, 6), ((2, 6), (2, 6), (2, 6)))
        self.add_bezier('p3-r1-14', (2, 6), ((2, 6), (2, 6), (2, 6)))
        self.add_bezier('p3-r1-15', (2, 6), ((2, 5), (2, 4), (3, 4)))
        self.add_bezier('p3-r1-16', (3, 4), ((3, 3), (4, 2), (5, 2)))
        self.add_bezier('p3-r1-17', (5, 2), ((6, 2), (6, 2), (6, 3)))
        self.add_line('p3-r1-18', (6, 3), (8, 5))
        self.add_bezier('p3-r1-19', (8, 5), ((8, 5), (8, 6), (8, 6)))
        self.add_bezier('p3-r1-20', (8, 6), ((8, 6), (8, 7), (8, 8)))
        self.add_line('p3-r1-21', (8, 8), (4, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', 'p3-r1-10', 'p3-r1-11', 'p3-r1-12', 'p3-r1-13', 'p3-r1-14', 'p3-r1-15', 'p3-r1-16', 'p3-r1-17', 'p3-r1-18', 'p3-r1-19', 'p3-r1-20', 'p3-r1-21', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
