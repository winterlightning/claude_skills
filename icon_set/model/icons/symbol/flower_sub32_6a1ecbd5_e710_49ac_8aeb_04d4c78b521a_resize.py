"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '6a1ecbd5-e710-49ac-8aeb-04d4c78b521a'
SOURCE_PATH = 'icon_set/model/icons/symbol/flower_sub32_6a1ecbd5_e710_49ac_8aeb_04d4c78b521a.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '2de198c4919a89b2023853c33e0c8ae5b1d25481e95d81ab717adca811323219'
SOURCE_REFERENCES = (('6a1ecbd5-e710-49ac-8aeb-04d4c78b521a', 'pictographic-primitives/nature/flower_6a1ecbd5-e710-49ac-8aeb-04d4c78b521a.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'flower-sub32-resize'
    variant_of = 'flower-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'nature'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (12, 2), ((15, 2), (16, 3), (16, 7)))
        self.add_bezier('p1-r1-2', (16, 7), ((17, 7), (18, 7), (18, 7)))
        self.add_bezier('p1-r1-3', (18, 7), ((21, 7), (22, 8), (22, 11)))
        self.add_bezier('p1-r1-4', (22, 11), ((22, 13), (21, 15), (18, 16)))
        self.add_bezier('p1-r1-5', (18, 16), ((18, 16), (19, 17), (19, 18)))
        self.add_bezier('p1-r1-6', (19, 18), ((19, 21), (17, 22), (16, 22)))
        self.add_bezier('p1-r1-7', (16, 22), ((13, 22), (13, 21), (12, 19)))
        self.add_bezier('p1-r1-8', (12, 19), ((11, 21), (11, 22), (8, 22)))
        self.add_bezier('p1-r1-9', (8, 22), ((7, 22), (5, 21), (5, 18)))
        self.add_bezier('p1-r1-10', (5, 18), ((5, 17), (6, 16), (6, 16)))
        self.add_bezier('p1-r1-11', (6, 16), ((3, 15), (2, 13), (2, 11)))
        self.add_bezier('p1-r1-12', (2, 11), ((2, 8), (3, 7), (6, 7)))
        self.add_bezier('p1-r1-13', (6, 7), ((6, 7), (7, 7), (8, 7)))
        self.add_bezier('p1-r1-14', (8, 7), ((8, 3), (9, 2), (12, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', closed=False)
