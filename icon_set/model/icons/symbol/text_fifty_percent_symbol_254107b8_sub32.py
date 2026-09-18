"""Independent 32px profile of text-fifty-percent-symbol-254107b8.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-fifty-percent-symbol-254107b8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-fifty-percent-symbol-254107b8',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'd27629aa3f5015e9db9b7c916617c2c9a091c91e43afb5e5467e902e278ae97f'

class Drawing(TextSub32):
    icon_id = 'text-fifty-percent-symbol-254107b8-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 83
    text_ink_bounds = (0.0, 0.0, 82.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (60, 30), (80, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (60, 7), ((60, 4), (62, 2), (64, 2)))
        self.add_bezier('p2-r1-2', (64, 2), ((66, 2), (68, 4), (68, 7)))
        self.add_bezier('p2-r1-3', (68, 7), ((68, 10), (66, 13), (64, 13)))
        self.add_bezier('p2-r1-4', (64, 13), ((62, 13), (60, 10), (60, 7)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (72, 25), ((72, 22), (74, 19), (76, 19)))
        self.add_bezier('p3-r1-2', (76, 19), ((78, 19), (80, 22), (80, 25)))
        self.add_bezier('p3-r1-3', (80, 25), ((80, 28), (78, 30), (76, 30)))
        self.add_bezier('p3-r1-4', (76, 30), ((74, 30), (72, 28), (72, 25)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_bezier('p4-r1-1', (31, 11), ((31, 7), (35, 3), (40, 3)))
        self.add_bezier('p4-r1-2', (40, 3), ((45, 3), (50, 7), (50, 11)))
        self.add_line('p4-r1-3', (50, 11), (50, 22))
        self.add_bezier('p4-r1-4', (50, 22), ((50, 27), (45, 30), (40, 30)))
        self.add_bezier('p4-r1-5', (40, 30), ((35, 30), (31, 27), (31, 22)))
        self.add_line('p4-r1-6', (31, 22), (31, 11))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', closed=False)
        self.add_line('p5-r1-1', (19, 3), (3, 3))
        self.add_bezier('p5-r1-2', (3, 3), ((2, 3), (2, 3), (2, 4)))
        self.add_line('p5-r1-3', (2, 4), (2, 13))
        self.add_bezier('p5-r1-4', (2, 13), ((2, 14), (2, 14), (3, 14)))
        self.add_line('p5-r1-5', (3, 14), (13, 14))
        self.add_bezier('p5-r1-6', (13, 14), ((18, 14), (21, 18), (21, 22)))
        self.add_bezier('p5-r1-7', (21, 22), ((21, 24), (20, 26), (18, 28)))
        self.add_bezier('p5-r1-8', (18, 28), ((17, 29), (15, 30), (13, 30)))
        self.add_line('p5-r1-9', (13, 30), (3, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', 'p5-r1-6', 'p5-r1-7', 'p5-r1-8', 'p5-r1-9', closed=False)
