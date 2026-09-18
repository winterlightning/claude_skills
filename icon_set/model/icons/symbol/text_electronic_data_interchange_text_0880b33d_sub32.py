"""Independent 32px profile of text-electronic-data-interchange-text-0880b33d.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '0880b33d-b40b-4439-a3af-94286a419e15'
SOURCE_PATH = 'icon_set/dist/text32/text-electronic-data-interchange-text-0880b33d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0880b33d-b40b-4439-a3af-94286a419e15', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/edi (text)_0880b33d-b40b-4439-a3af-94286a419e15.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-electronic-data-interchange-text-0880b33d',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-e-uppercase', 'letter-d-uppercase', 'letter-i-uppercase')
REFERENCE_EXPORT_SHA256 = '363f36b9f5bbf150ce3ff27b0ca58a074b66d5f1ab7d9a988ec1a2ec6fbacf4d'

class Drawing(TextSub32):
    icon_id = 'text-electronic-data-interchange-text-0880b33d-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 66
    text_ink_bounds = (0.0, 0.0, 66.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (54, 2), (64, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (59, 2), (59, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (54, 30), (64, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (27, 2), (35, 2))
        self.add_bezier('p4-r1-2', (35, 2), ((43, 2), (46, 9), (46, 16)))
        self.add_bezier('p4-r1-3', (46, 16), ((46, 23), (43, 30), (35, 30)))
        self.add_line('p4-r1-4', (35, 30), (27, 30))
        self.add_line('p4-r1-5', (27, 30), (27, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (19, 2), (2, 2))
        self.add_line('p5-r1-2', (2, 2), (2, 30))
        self.add_line('p5-r1-3', (2, 30), (19, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.add_line('p6-r1-1', (2, 16), (16, 16))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
