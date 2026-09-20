"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'ccad9539-3f9e-4f75-8205-11baacf5298e'
SOURCE_PATH = 'icon_set/model/icons/symbol/man_with_short_hair_and_open_shoulders_sub32_ccad9539_3f9e_4f75_8205_11baacf5298e.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '3d5634fc268c907683ad44e85d404e69400a297e2eb52236b0e8a09f188cae33'
SOURCE_REFERENCES = (('ccad9539-3f9e-4f75-8205-11baacf5298e', 'pictographic-primitives/avatars/man_ccad9539-3f9e-4f75-8205-11baacf5298e.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'man-with-short-hair-and-open-shoulders-sub32-resize'
    variant_of = 'man-with-short-hair-and-open-shoulders-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'avatars'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (7, 2), (13, 2))
        self.add_arc('p1-r1-2', (13, 2), (15, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (15, 4), (15, 7))
        self.add_arc('p1-r1-4', (15, 7), (5, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (5, 7), (5, 4))
        self.add_arc('p1-r1-6', (5, 4), (7, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (2, 22), (2, 20))
        self.add_arc('p2-r1-2', (2, 20), (8, 14), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (8, 14), (12, 14))
        self.add_arc('p2-r1-4', (12, 14), (18, 20), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (18, 20), (18, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
