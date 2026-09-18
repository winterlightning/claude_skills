"""Independent 32px profile of text-plus-one-symbol-014b4126.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-plus-one-symbol-014b4126.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-plus-one-symbol-014b4126',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '47c0f25a7982075f832a538c520685464408c4ddd289f81e9dbafd81e8e0113a'

class Drawing(TextSub32):
    icon_id = 'text-plus-one-symbol-014b4126-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 46
    text_ink_bounds = (0.0, 0.0, 46.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (37, 28), (37, 3))
        self.add_bezier('p1-r1-2', (37, 3), ((37, 2), (37, 2), (37, 2)))
        self.add_line('p1-r1-3', (37, 2), (31, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (31, 28), (44, 28))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 19), (23, 19))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (13, 9), (13, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
