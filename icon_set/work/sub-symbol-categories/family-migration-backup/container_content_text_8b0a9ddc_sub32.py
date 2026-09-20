"""Independent 32px profile of container-content-text-8b0a9ddc.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text44/container-content-text-8b0a9ddc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/container-content-text-8b0a9ddc',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'a2fdba6c3e22e0aa688e7b76abe596056c0713a110e1b0bfed838de5f160c297'

class Drawing(TextSub32):
    icon_id = 'container-content-text-8b0a9ddc-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 142
    text_ink_bounds = (0.0, 0.0, 141.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (137, 2), (121, 2))
        self.add_bezier('p1-r1-2', (121, 2), ((120, 2), (120, 2), (120, 3)))
        self.add_line('p1-r1-3', (120, 3), (120, 13))
        self.add_bezier('p1-r1-4', (120, 13), ((120, 13), (120, 14), (121, 14)))
        self.add_line('p1-r1-5', (121, 14), (131, 14))
        self.add_bezier('p1-r1-6', (131, 14), ((136, 14), (139, 18), (139, 22)))
        self.add_bezier('p1-r1-7', (139, 22), ((139, 24), (139, 26), (137, 28)))
        self.add_bezier('p1-r1-8', (137, 28), ((135, 29), (133, 30), (131, 30)))
        self.add_line('p1-r1-9', (131, 30), (121, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_line('p2-r1-1', (109, 30), (109, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (79, 2), (93, 2))
        self.add_bezier('p3-r1-2', (93, 2), ((97, 2), (99, 5), (99, 8)))
        self.add_bezier('p3-r1-3', (99, 8), ((99, 9), (98, 11), (97, 12)))
        self.add_line('p3-r1-4', (97, 12), (83, 21))
        self.add_bezier('p3-r1-5', (83, 21), ((81, 23), (79, 25), (79, 28)))
        self.add_line('p3-r1-6', (79, 28), (79, 29))
        self.add_bezier('p3-r1-7', (79, 29), ((79, 29), (80, 30), (81, 30)))
        self.add_line('p3-r1-8', (81, 30), (99, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', closed=False)
        self.add_line('p4-r1-1', (32, 30), (32, 2))
        self.add_line('p4-r1-2', (32, 2), (45, 20))
        self.add_line('p4-r1-3', (45, 20), (58, 2))
        self.add_line('p4-r1-4', (58, 2), (58, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (2, 30), (2, 2))
        self.add_line('p5-r1-2', (2, 2), (12, 2))
        self.add_bezier('p5-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p5-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p5-r1-5', (12, 17), (2, 17))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
