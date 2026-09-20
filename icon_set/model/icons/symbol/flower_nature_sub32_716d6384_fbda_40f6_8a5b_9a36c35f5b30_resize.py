"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '716d6384-fbda-40f6-8a5b-9a36c35f5b30'
SOURCE_PATH = 'icon_set/model/icons/symbol/flower_nature_sub32_716d6384_fbda_40f6_8a5b_9a36c35f5b30.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '6b21793efa8a586115e417dd7667419942801008093985eef27e8ad85f5a35a9'
SOURCE_REFERENCES = (('716d6384-fbda-40f6-8a5b-9a36c35f5b30', 'pictographic-primitives/nature/flower_716d6384-fbda-40f6-8a5b-9a36c35f5b30.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'flower-nature-sub32-resize'
    variant_of = 'flower-nature-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'nature'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (12, 2), ((15, 2), (16, 3), (16, 6)))
        self.add_bezier('p1-r1-2', (16, 6), ((16, 5), (17, 5), (18, 5)))
        self.add_bezier('p1-r1-3', (18, 5), ((20, 5), (22, 7), (22, 9)))
        self.add_bezier('p1-r1-4', (22, 9), ((22, 11), (19, 13), (18, 13)))
        self.add_bezier('p1-r1-5', (18, 13), ((18, 14), (18, 14), (18, 15)))
        self.add_bezier('p1-r1-6', (18, 15), ((18, 17), (17, 18), (15, 18)))
        self.add_bezier('p1-r1-7', (15, 18), ((13, 18), (13, 18), (12, 17)))
        self.add_bezier('p1-r1-8', (12, 17), ((11, 17), (11, 18), (9, 18)))
        self.add_bezier('p1-r1-9', (9, 18), ((7, 18), (6, 17), (6, 15)))
        self.add_bezier('p1-r1-10', (6, 15), ((6, 14), (6, 14), (6, 13)))
        self.add_bezier('p1-r1-11', (6, 13), ((5, 13), (2, 11), (2, 9)))
        self.add_bezier('p1-r1-12', (2, 9), ((2, 7), (4, 5), (6, 5)))
        self.add_bezier('p1-r1-13', (6, 5), ((7, 5), (8, 5), (8, 6)))
        self.add_bezier('p1-r1-14', (8, 6), ((8, 3), (10, 2), (12, 2)))
        self.add_arc('p2-r1-1', (10, 10), (14, 10), radius_x=2, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (14, 10), (10, 10), radius_x=2, radius_y=1, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
