"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '97903c22-da46-4913-b7f3-4e20608ab202'
SOURCE_PATH = 'icon_set/model/icons/symbol/head_sub32_97903c22_da46_4913_b7f3_4e20608ab202.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f84014a8db536c7fad120a3744dcd4cf75fdc3622ef1b5fce70c59d1b66b5750'
SOURCE_REFERENCES = (('97903c22-da46-4913-b7f3-4e20608ab202', 'pictographic-primitives/symbol/head_97903c22-da46-4913-b7f3-4e20608ab202.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'head-sub32-resize'
    variant_of = 'head-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (4, 22), (4, 16))
        self.add_bezier('p1-r1-2', (4, 16), ((4, 13), (2, 13), (2, 9)))
        self.add_bezier('p1-r1-3', (2, 9), ((2, 5), (5, 2), (9, 2)))
        self.add_bezier('p1-r1-4', (9, 2), ((13, 2), (16, 5), (16, 9)))
        self.add_line('p1-r1-5', (16, 9), (18, 14))
        self.add_line('p1-r1-6', (18, 14), (16, 14))
        self.add_line('p1-r1-7', (16, 14), (16, 17))
        self.add_bezier('p1-r1-8', (16, 17), ((16, 18), (16, 18), (16, 18)))
        self.add_bezier('p1-r1-9', (16, 18), ((15, 19), (14, 19), (14, 19)))
        self.add_line('p1-r1-10', (14, 19), (12, 19))
        self.add_line('p1-r1-11', (12, 19), (12, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
