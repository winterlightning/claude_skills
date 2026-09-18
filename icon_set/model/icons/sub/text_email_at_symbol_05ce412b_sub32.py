"""Independent 32px profile of text-email-at-symbol-05ce412b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-email-at-symbol-05ce412b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-email-at-symbol-05ce412b',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '18dfdf239014335fc90d2ef9255a61f618a1ee15a6cd460c85bd6b23e24dd871'

class Drawing(TextSub32):
    icon_id = 'text-email-at-symbol-05ce412b-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 31
    text_ink_bounds = (0.0, 0.0, 31.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (21, 11), (21, 20))
        self.add_bezier('p1-r1-2', (21, 20), ((21, 23), (22, 24), (23, 24)))
        self.add_bezier('p1-r1-3', (23, 24), ((26, 24), (29, 21), (29, 15)))
        self.add_bezier('p1-r1-4', (29, 15), ((29, 6), (22, 2), (16, 2)))
        self.add_bezier('p1-r1-5', (16, 2), ((9, 2), (2, 7), (2, 16)))
        self.add_bezier('p1-r1-6', (2, 16), ((2, 25), (8, 30), (16, 30)))
        self.add_bezier('p1-r1-7', (16, 30), ((18, 30), (21, 29), (24, 28)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_bezier('p2-r1-1', (21, 16), ((21, 12), (18, 10), (15, 10)))
        self.add_bezier('p2-r1-2', (15, 10), ((13, 10), (10, 12), (10, 17)))
        self.add_bezier('p2-r1-3', (10, 17), ((10, 22), (12, 24), (15, 24)))
        self.add_bezier('p2-r1-4', (15, 24), ((18, 24), (21, 21), (21, 16)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
