"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '45a7c221-ee5e-4f5f-9d50-3b2bfc2ef6e7'
SOURCE_PATH = 'icon_set/model/icons/symbol/users_two_overlap_sub32_symbol_45a7c221_ee5e_4f5f_9d50_3b2bfc2ef6e7.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '046fe5d257b99926d700c3ad6ef216dd844a4dbb24f2f35c947504697729f7a0'
SOURCE_REFERENCES = (('45a7c221-ee5e-4f5f-9d50-3b2bfc2ef6e7', 'pictographic-primitives/symbol/two persons_45a7c221-ee5e-4f5f-9d50-3b2bfc2ef6e7.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'users-two-overlap-sub32-symbol-resize-38x32'
    variant_of = 'users-two-overlap-sub32-symbol'
    variant_label = 'Resize 38 × 32'
    canvas_width = 38
    canvas_height = 32
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (3, 7), ((3, 7), (4, 6), (4, 6)), ((5, 6), (6, 5), (7, 5)), ((7, 5), (8, 6), (9, 6)), ((9, 6), (10, 7), (10, 7)))
        self.add_bezier('p1-r1-2', (10, 7), ((10, 8), (9, 9), (9, 9)), ((8, 9), (7, 9), (6, 9)), ((6, 9), (5, 9), (4, 9)), ((4, 9), (3, 8), (3, 7)))
        self.add_bezier('p2-r1-1', (20, 9), ((20, 7), (21, 6), (22, 4)), ((24, 3), (26, 2), (28, 2)), ((29, 2), (31, 3), (33, 4)), ((34, 6), (35, 7), (35, 9)))
        self.add_bezier('p2-r1-2', (35, 9), ((35, 11), (34, 13), (33, 15)), ((31, 16), (29, 17), (28, 17)), ((26, 17), (24, 16), (22, 15)), ((21, 13), (20, 11), (20, 9)))
        self.add_line('p3-r1-1', (2, 26), (2, 25))
        self.add_bezier('p3-r1-2', (2, 25), ((2, 24), (2, 23), (2, 22)), ((3, 22), (3, 21), (3, 20)), ((4, 20), (4, 19), (5, 19)), ((6, 18), (6, 18), (7, 18)))
        self.add_line('p3-r1-3', (7, 18), (10, 18))
        self.add_bezier('p4-r1-1', (15, 30), ((15, 28), (16, 27), (18, 26)), ((20, 24), (23, 24), (25, 24)), ((28, 24), (31, 24), (33, 26)), ((35, 27), (36, 28), (36, 30)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
