"""Independent 32px profile of text-thirty-percent-discount-symbol-b382b4ba.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-thirty-percent-discount-symbol-b382b4ba.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-thirty-percent-discount-symbol-b382b4ba',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '562a6ce93f3a2862f2dd84f57cc9414ef785bdad35d694fcb58dcb171e5fc2b5'

class Drawing(TextSub32):
    icon_id = 'text-thirty-percent-discount-symbol-b382b4ba-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 81
    text_ink_bounds = (0.0, 0.0, 81.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (59, 30), (79, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (59, 7), ((59, 4), (60, 2), (63, 2)))
        self.add_bezier('p2-r1-2', (63, 2), ((65, 2), (67, 4), (67, 7)))
        self.add_bezier('p2-r1-3', (67, 7), ((67, 10), (65, 13), (63, 13)))
        self.add_bezier('p2-r1-4', (63, 13), ((60, 13), (59, 10), (59, 7)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (71, 25), ((71, 22), (73, 19), (75, 19)))
        self.add_bezier('p3-r1-2', (75, 19), ((77, 19), (79, 22), (79, 25)))
        self.add_bezier('p3-r1-3', (79, 25), ((79, 28), (77, 30), (75, 30)))
        self.add_bezier('p3-r1-4', (75, 30), ((73, 30), (71, 28), (71, 25)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_bezier('p4-r1-1', (30, 11), ((30, 7), (34, 3), (39, 3)))
        self.add_bezier('p4-r1-2', (39, 3), ((44, 3), (49, 7), (49, 11)))
        self.add_line('p4-r1-3', (49, 11), (49, 22))
        self.add_bezier('p4-r1-4', (49, 22), ((49, 27), (44, 30), (39, 30)))
        self.add_bezier('p4-r1-5', (39, 30), ((34, 30), (30, 27), (30, 22)))
        self.add_line('p4-r1-6', (30, 22), (30, 11))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', closed=False)
        self.add_line('p5-r1-1', (2, 3), (13, 3))
        self.add_bezier('p5-r1-2', (13, 3), ((16, 3), (20, 6), (20, 10)))
        self.add_bezier('p5-r1-3', (20, 10), ((20, 14), (16, 17), (13, 17)))
        self.add_line('p5-r1-4', (13, 17), (9, 17))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
        self.add_line('p6-r1-1', (9, 17), (13, 17))
        self.add_bezier('p6-r1-2', (13, 17), ((16, 17), (20, 20), (20, 23)))
        self.add_bezier('p6-r1-3', (20, 23), ((20, 27), (16, 30), (13, 30)))
        self.add_line('p6-r1-4', (13, 30), (2, 30))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', closed=False)
        self.relate('connect', 'p5-r1-3', 'p6-r1-1')
        self.relate('connect', 'p5-r1-3', 'p6-r1-2')
        self.relate('connect', 'p5-r1-4', 'p6-r1-1')
        self.relate('connect', 'p5-r1-4', 'p6-r1-2')
