"""Independent 32px profile of container-content-text-b2c5933c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text44/container-content-text-b2c5933c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/container-content-text-b2c5933c',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'ca6c4e3a266f43fb4fea717d2dd2ded754aa29133b5897078c11afc7e756707f'

class Drawing(TextSub32):
    icon_id = 'container-content-text-b2c5933c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 78
    text_ink_bounds = (0.0, 0.0, 78.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (57, 10), ((57, 6), (61, 2), (66, 2)))
        self.add_bezier('p1-r1-2', (66, 2), ((72, 2), (76, 6), (76, 10)))
        self.add_bezier('p1-r1-3', (76, 10), ((76, 15), (72, 19), (66, 19)))
        self.add_bezier('p1-r1-4', (66, 19), ((61, 19), (57, 15), (57, 10)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (76, 10), (76, 20))
        self.add_bezier('p2-r1-2', (76, 20), ((76, 26), (72, 30), (66, 30)))
        self.add_line('p2-r1-3', (66, 30), (59, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (49, 14), (49, 14))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (49, 28), (49, 28))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_arc('p5-r1-1', (22, 22), (42, 22), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_arc('p5-r1-2', (42, 22), (22, 22), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (22, 22), (22, 12))
        self.add_bezier('p6-r1-2', (22, 12), ((22, 6), (27, 2), (32, 2)))
        self.add_line('p6-r1-3', (32, 2), (39, 2))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', closed=False)
        self.add_line('p7-r1-1', (9, 30), (9, 3))
        self.add_bezier('p7-r1-2', (9, 3), ((9, 2), (8, 2), (8, 2)))
        self.add_line('p7-r1-3', (8, 2), (2, 2))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', closed=False)
        self.add_line('p8-r1-1', (2, 30), (15, 30))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-2', 'p6-r1-1')
