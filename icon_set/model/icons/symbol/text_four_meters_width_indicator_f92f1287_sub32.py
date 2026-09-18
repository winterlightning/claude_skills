"""Independent 32px profile of text-four-meters-width-indicator-f92f1287.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-four-meters-width-indicator-f92f1287.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-four-meters-width-indicator-f92f1287',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '4212988776b3a56e9024dba73440c56825180a29b2b19c8f85f9b01f64be5395'

class Drawing(TextSub32):
    icon_id = 'text-four-meters-width-indicator-f92f1287-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 102
    text_ink_bounds = (0.0, 0.0, 102.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (22, 2), (22, 20))
        self.add_bezier('p1-r1-2', (22, 20), ((22, 20), (22, 20), (23, 20)))
        self.add_line('p1-r1-3', (23, 20), (45, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (41, 2), (41, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (53, 30), (53, 2))
        self.add_line('p3-r1-2', (53, 2), (67, 20))
        self.add_line('p3-r1-3', (67, 20), (80, 2))
        self.add_line('p3-r1-4', (80, 2), (80, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (2, 9), (9, 16))
        self.add_line('p4-r1-2', (9, 16), (2, 23))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p4-r2-1', (100, 9), (93, 16))
        self.add_line('p4-r2-2', (93, 16), (100, 23))
        self.add_contour('path-4-2', 'p4-r2-1', 'p4-r2-2', closed=False)
