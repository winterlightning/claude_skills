"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '39d4dade-8ad3-48bc-a8ba-99e528562c38'
SOURCE_PATH = 'icon_set/model/icons/symbol/person_sub32_39d4dade_8ad3_48bc_a8ba_99e528562c38.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'df256fcbe5fa01f3304abf1899c07fbc3ea7eee68718d820bf8c32fb706518a9'
SOURCE_REFERENCES = (('39d4dade-8ad3-48bc-a8ba-99e528562c38', 'pictographic-primitives/symbol/person_39d4dade-8ad3-48bc-a8ba-99e528562c38.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'person-sub32-resize'
    variant_of = 'person-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (6, 6), (10, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (10, 2), (14, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (14, 6), (10, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (10, 9), (6, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('p2-r1-1', (10, 13), ((7, 13), (4, 16), (2, 16)))
        self.add_bezier('p3-r1-1', (10, 13), ((13, 13), (16, 16), (18, 16)))
        self.add_line('p4-r1-1', (10, 13), (10, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
