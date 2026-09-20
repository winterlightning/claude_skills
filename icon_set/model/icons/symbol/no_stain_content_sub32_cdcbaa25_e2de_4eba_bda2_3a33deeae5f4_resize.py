"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'cdcbaa25-e2de-4eba-bda2-3a33deeae5f4'
SOURCE_PATH = 'icon_set/model/icons/symbol/no_stain_content_sub32_cdcbaa25_e2de_4eba_bda2_3a33deeae5f4.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'ead5f29dc711eb28e72b42a58eb3e27daaf8eda38ea48f8cd80b789fd526ef0e'
SOURCE_REFERENCES = (('cdcbaa25-e2de-4eba-bda2-3a33deeae5f4', 'icon_set/dist/gallery/combination-originals/cdcbaa25-e2de-4eba-bda2-3a33deeae5f4.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'no-stain-content-sub32-resize'
    variant_of = 'no-stain-content-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (8, 2), ((10, 2), (11, 3), (12, 3)))
        self.add_bezier('p1-r1-2', (12, 3), ((13, 4), (13, 6), (13, 6)))
        self.add_line('p1-r1-3', (13, 6), (18, 6))
        self.add_bezier('p1-r1-4', (18, 6), ((18, 6), (18, 6), (18, 6)), ((19, 6), (19, 6), (20, 6)), ((20, 7), (21, 7), (21, 7)), ((22, 8), (22, 9), (22, 9)), ((22, 9), (22, 10), (22, 10)), ((22, 10), (22, 11), (22, 11)))
        self.add_bezier('p1-r1-5', (22, 11), ((22, 12), (21, 13), (21, 14)))
        self.add_bezier('p1-r1-6', (21, 14), ((20, 15), (18, 16), (18, 16)))
        self.add_line('p1-r1-7', (18, 16), (13, 16))
        self.add_bezier('p1-r1-8', (13, 16), ((13, 16), (13, 16), (13, 16)), ((13, 17), (13, 17), (13, 18)), ((12, 18), (12, 19), (12, 19)), ((11, 20), (11, 20), (10, 20)), ((10, 20), (9, 20), (9, 20)), ((9, 20), (8, 20), (8, 20)))
        self.add_bezier('p1-r1-9', (8, 20), ((8, 20), (7, 20), (7, 20)), ((6, 19), (6, 19), (5, 19)), ((5, 18), (5, 18), (5, 18)), ((4, 17), (4, 17), (4, 16)))
        self.add_line('p1-r1-10', (4, 16), (4, 11))
        self.add_bezier('p1-r1-11', (4, 11), ((4, 11), (4, 11), (4, 11)), ((4, 11), (3, 11), (3, 11)), ((3, 11), (3, 10), (2, 10)), ((2, 10), (2, 9), (2, 9)), ((2, 9), (2, 9), (2, 9)), ((2, 9), (2, 8), (2, 8)))
        self.add_bezier('p1-r1-12', (2, 8), ((2, 7), (2, 7), (3, 6)), ((3, 6), (3, 6), (3, 5)), ((4, 5), (4, 5), (5, 4)), ((5, 4), (6, 4), (6, 4)))
        self.add_line('p1-r1-13', (6, 4), (8, 2))
        self.add_line('p2-r1-1', (2, 2), (22, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
