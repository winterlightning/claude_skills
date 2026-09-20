"""Independent 32px profile of text-subset-of-or-equal-to-symbol-a83c7456.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-subset-of-or-equal-to-symbol-a83c7456.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-subset-of-or-equal-to-symbol-a83c7456',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'cb680854114ac03cc6943f26f1aa2cbecd8b381ecfb016d234c3b5cadd1c4ade'

class Drawing(TextSub32):
    icon_id = 'text-subset-of-or-equal-to-symbol-a83c7456-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 26
    text_ink_bounds = (0.0, 0.0, 26.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (24, 2), (14, 2))
        self.add_bezier('p1-r1-2', (14, 2), ((6, 2), (2, 7), (2, 12)))
        self.add_bezier('p1-r1-3', (2, 12), ((2, 17), (6, 22), (14, 22)))
        self.add_line('p1-r1-4', (14, 22), (24, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (4, 30), (24, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
