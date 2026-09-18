"""Independent 32px profile of text-double-opening-quotation-marks-a4bb6523.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-double-opening-quotation-marks-a4bb6523.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-double-opening-quotation-marks-a4bb6523',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '3d4d83793d057c07a553e6d5699f07abc852efee8028543ecfc515fa901b6570'

class Drawing(TextSub32):
    icon_id = 'text-double-opening-quotation-marks-a4bb6523-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 34
    text_ink_bounds = (0.0, 0.0, 34.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (12, 2), ((5, 4), (4, 12), (4, 19)))
        self.add_line('p1-r1-2', (4, 19), (13, 19))
        self.add_line('p1-r1-3', (13, 19), (13, 30))
        self.add_line('p1-r1-4', (13, 30), (2, 30))
        self.add_line('p1-r1-5', (2, 30), (2, 19))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_bezier('p2-r1-1', (31, 2), ((25, 4), (24, 12), (24, 19)))
        self.add_line('p2-r1-2', (24, 19), (32, 19))
        self.add_line('p2-r1-3', (32, 19), (32, 30))
        self.add_line('p2-r1-4', (32, 30), (21, 30))
        self.add_line('p2-r1-5', (21, 30), (21, 19))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
