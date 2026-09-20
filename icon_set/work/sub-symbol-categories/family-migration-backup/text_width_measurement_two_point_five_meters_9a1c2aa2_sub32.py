"""Independent 32px profile of text-width-measurement-two-point-five-meters-9a1c2aa2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-width-measurement-two-point-five-meters-9a1c2aa2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-width-measurement-two-point-five-meters-9a1c2aa2',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'c2208f8386b1153c60ed11111d8cfe4c00432b860f7e44327832ba42b81308ab'

class Drawing(TextSub32):
    icon_id = 'text-width-measurement-two-point-five-meters-9a1c2aa2-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 133
    text_ink_bounds = (0.0, 0.0, 133.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (22, 2), (36, 2))
        self.add_bezier('p1-r1-2', (36, 2), ((39, 2), (41, 5), (41, 8)))
        self.add_bezier('p1-r1-3', (41, 8), ((41, 9), (41, 11), (39, 12)))
        self.add_line('p1-r1-4', (39, 12), (25, 21))
        self.add_bezier('p1-r1-5', (25, 21), ((23, 23), (22, 25), (22, 28)))
        self.add_line('p1-r1-6', (22, 28), (22, 29))
        self.add_bezier('p1-r1-7', (22, 29), ((22, 29), (22, 30), (23, 30)))
        self.add_line('p1-r1-8', (23, 30), (41, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (49, 30), (49, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (75, 2), (58, 2))
        self.add_bezier('p3-r1-2', (58, 2), ((58, 2), (57, 2), (57, 3)))
        self.add_line('p3-r1-3', (57, 3), (57, 13))
        self.add_bezier('p3-r1-4', (57, 13), ((57, 13), (58, 14), (58, 14)))
        self.add_line('p3-r1-5', (58, 14), (68, 14))
        self.add_bezier('p3-r1-6', (68, 14), ((73, 14), (77, 18), (77, 22)))
        self.add_bezier('p3-r1-7', (77, 22), ((77, 24), (76, 26), (74, 28)))
        self.add_bezier('p3-r1-8', (74, 28), ((73, 29), (71, 30), (68, 30)))
        self.add_line('p3-r1-9', (68, 30), (58, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', closed=False)
        self.add_line('p4-r1-1', (84, 30), (84, 2))
        self.add_line('p4-r1-2', (84, 2), (98, 20))
        self.add_line('p4-r1-3', (98, 20), (111, 2))
        self.add_line('p4-r1-4', (111, 2), (111, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (2, 9), (9, 16))
        self.add_line('p5-r1-2', (9, 16), (2, 23))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p5-r2-1', (131, 9), (124, 16))
        self.add_line('p5-r2-2', (124, 16), (131, 23))
        self.add_contour('path-5-2', 'p5-r2-1', 'p5-r2-2', closed=False)
