"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'e4cb7fec-5844-4dee-a6d5-ffcdc23d8d21'
SOURCE_PATH = 'icon_set/model/icons/symbol/brain_with_two_inner_folds_sub32_e4cb7fec_5844_4dee_a6d5_ffcdc23d8d21.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '9f09bffab569bdf6e5d467b6e1aeea21edfc13456cfeb02f830f41e92584d3c4'
SOURCE_REFERENCES = (('e4cb7fec-5844-4dee-a6d5-ffcdc23d8d21', 'pictographic-primitives/artificial-intelligence/brain_e4cb7fec-5844-4dee-a6d5-ffcdc23d8d21.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'brain-with-two-inner-folds-sub32-resize'
    variant_of = 'brain-with-two-inner-folds-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'artificial-intelligence'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (12, 4), ((11, 2), (10, 2), (8, 2)))
        self.add_bezier('p1-r1-2', (8, 2), ((8, 2), (8, 2), (8, 2)))
        self.add_bezier('p1-r1-3', (8, 2), ((4, 2), (3, 4), (3, 6)))
        self.add_bezier('p1-r1-4', (3, 6), ((2, 8), (2, 10), (2, 12)))
        self.add_bezier('p1-r1-5', (2, 12), ((2, 14), (2, 16), (3, 18)))
        self.add_bezier('p1-r1-6', (3, 18), ((3, 20), (4, 22), (8, 22)))
        self.add_bezier('p1-r1-7', (8, 22), ((10, 22), (11, 22), (12, 20)))
        self.add_bezier('p2-r1-1', (12, 4), ((13, 2), (14, 2), (16, 2)))
        self.add_bezier('p2-r1-2', (16, 2), ((16, 2), (16, 2), (16, 2)))
        self.add_bezier('p2-r1-3', (16, 2), ((20, 2), (21, 4), (21, 6)))
        self.add_bezier('p2-r1-4', (21, 6), ((22, 8), (22, 10), (22, 12)))
        self.add_bezier('p2-r1-5', (22, 12), ((22, 14), (22, 16), (21, 18)))
        self.add_bezier('p2-r1-6', (21, 18), ((21, 20), (20, 22), (16, 22)))
        self.add_bezier('p2-r1-7', (16, 22), ((14, 22), (13, 22), (12, 20)))
        self.add_line('p3-r1-1', (12, 4), (12, 20))
        self.add_bezier('p4-r1-1', (3, 6), ((3, 9), (5, 11), (7, 11)))
        self.add_bezier('p5-r1-1', (17, 11), ((17, 11), (18, 11), (18, 11)))
        self.add_bezier('p5-r1-2', (18, 11), ((18, 12), (17, 13), (17, 13)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p4-r1-1')
        self.relate('connect', 'p1-r1-4', 'p4-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-7')
        self.relate('connect', 'p1-r1-7', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-7', 'p3-r1-1')
