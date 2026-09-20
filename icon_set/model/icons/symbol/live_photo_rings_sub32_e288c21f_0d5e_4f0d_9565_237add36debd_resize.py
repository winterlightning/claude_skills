"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'e288c21f-0d5e-4f0d-9565-237add36debd'
SOURCE_PATH = 'icon_set/model/icons/symbol/live_photo_rings_sub32_e288c21f_0d5e_4f0d_9565_237add36debd.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '017379b748c7a4dee4c2cb09cd755fece343e9f52844b9aa51e02630a3633a16'
SOURCE_REFERENCES = (('e288c21f-0d5e-4f0d-9565-237add36debd', 'pictographic-primitives/photography/live photos_e288c21f-0d5e-4f0d-9565-237add36debd.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'live-photo-rings-sub32-resize'
    variant_of = 'live-photo-rings-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/photography'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (9, 3), ((10, 2), (11, 2), (12, 2)))
        self.add_bezier('p1-r1-2', (12, 2), ((13, 2), (14, 2), (15, 3)))
        self.add_bezier('p2-r1-1', (21, 9), ((22, 10), (22, 11), (22, 12)))
        self.add_bezier('p2-r1-2', (22, 12), ((22, 13), (22, 14), (21, 15)))
        self.add_bezier('p3-r1-1', (15, 21), ((14, 22), (13, 22), (12, 22)))
        self.add_bezier('p3-r1-2', (12, 22), ((11, 22), (10, 22), (9, 21)))
        self.add_bezier('p4-r1-1', (3, 15), ((2, 14), (2, 13), (2, 12)))
        self.add_bezier('p4-r1-2', (2, 12), ((2, 11), (2, 10), (3, 9)))
        self.add_bezier('p5-r1-1', (7, 12), ((7, 9), (9, 7), (12, 7)))
        self.add_bezier('p5-r1-2', (12, 7), ((15, 7), (17, 9), (17, 12)))
        self.add_bezier('p5-r1-3', (17, 12), ((17, 15), (15, 17), (12, 17)))
        self.add_bezier('p5-r1-4', (12, 17), ((9, 17), (7, 15), (7, 12)))
        self.add_line('p6-r1-1', (12, 12), (12, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
