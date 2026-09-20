"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '9ec250e0-3b4c-4302-a78f-3f0f5baf59cb'
SOURCE_PATH = 'icon_set/model/icons/symbol/tooth_sub32_9ec250e0_3b4c_4302_a78f_3f0f5baf59cb.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '81ac4d68aee43a1322a40fa8f9b9ecd2fd1f3a488917a2b8363ae85e93f2d1c2'
SOURCE_REFERENCES = (('9ec250e0-3b4c-4302-a78f-3f0f5baf59cb', 'pictographic-primitives/health/tooth_9ec250e0-3b4c-4302-a78f-3f0f5baf59cb.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'tooth-sub32-resize'
    variant_of = 'tooth-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'health'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (10, 3), ((12, 3), (13, 2), (14, 2)))
        self.add_bezier('p1-r1-2', (14, 2), ((17, 2), (18, 4), (18, 7)))
        self.add_bezier('p1-r1-3', (18, 7), ((18, 10), (16, 11), (16, 13)))
        self.add_bezier('p1-r1-4', (16, 13), ((16, 15), (16, 16), (16, 17)))
        self.add_bezier('p1-r1-5', (16, 17), ((16, 20), (16, 22), (14, 22)))
        self.add_bezier('p1-r1-6', (14, 22), ((11, 22), (13, 15), (10, 15)))
        self.add_bezier('p1-r1-7', (10, 15), ((7, 15), (9, 22), (6, 22)))
        self.add_bezier('p1-r1-8', (6, 22), ((4, 22), (4, 20), (4, 17)))
        self.add_bezier('p1-r1-9', (4, 17), ((4, 16), (4, 15), (4, 13)))
        self.add_bezier('p1-r1-10', (4, 13), ((4, 11), (2, 10), (2, 7)))
        self.add_bezier('p1-r1-11', (2, 7), ((2, 4), (3, 2), (6, 2)))
        self.add_bezier('p1-r1-12', (6, 2), ((7, 2), (8, 3), (10, 3)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
