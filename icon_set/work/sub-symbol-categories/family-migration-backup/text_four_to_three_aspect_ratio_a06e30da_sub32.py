"""Independent 32px profile of text-four-to-three-aspect-ratio-a06e30da.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-four-to-three-aspect-ratio-a06e30da.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-four-to-three-aspect-ratio-a06e30da',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '24a805290faa1d43d5cc30f2eebd2444192ab3ef3432f1904b7f7ee0c02bfc1f'

class Drawing(TextSub32):
    icon_id = 'text-four-to-three-aspect-ratio-a06e30da-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 62
    text_ink_bounds = (0.0, 0.0, 62.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (41, 2), (53, 2))
        self.add_bezier('p1-r1-2', (53, 2), ((56, 2), (60, 5), (60, 9)))
        self.add_bezier('p1-r1-3', (60, 9), ((60, 13), (56, 16), (53, 16)))
        self.add_line('p1-r1-4', (53, 16), (48, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (49, 16), (53, 16))
        self.add_bezier('p2-r1-2', (53, 16), ((56, 16), (60, 19), (60, 23)))
        self.add_bezier('p2-r1-3', (60, 23), ((60, 27), (56, 30), (53, 30)))
        self.add_line('p2-r1-4', (53, 30), (41, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (33, 14), (33, 14))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (33, 28), (33, 28))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 2), (2, 20))
        self.add_bezier('p5-r1-2', (2, 20), ((2, 20), (2, 20), (3, 20)))
        self.add_line('p5-r1-3', (3, 20), (26, 20))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.add_line('p6-r1-1', (21, 2), (21, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-2')
