"""Independent 32px profile of text-text-formatting-and-style-e0363621.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-text-formatting-and-style-e0363621.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-text-formatting-and-style-e0363621',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'cb64cf679100533c07a0c8bad374c9f4dd080389ca443d1c4b4caea9fc62e58f'

class Drawing(TextSub32):
    icon_id = 'text-text-formatting-and-style-e0363621-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 24
    text_ink_bounds = (0.0, 0.0, 24.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (6, 17), (12, 3))
        self.add_bezier('p1-r1-2', (12, 3), ((12, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p1-r1-3', (12, 2), ((12, 2), (12.333333333333334, 2.3333333333333335), (13, 3)))
        self.add_line('p1-r1-4', (13, 3), (18, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (9, 11), (16, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 24), (22, 24))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p3-r2-1', (5, 30), (19, 30))
        self.add_contour('path-3-2', 'p3-r2-1', closed=False)
