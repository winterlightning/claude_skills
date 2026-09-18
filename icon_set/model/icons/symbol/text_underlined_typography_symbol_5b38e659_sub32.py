"""Independent 32px profile of text-underlined-typography-symbol-5b38e659.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '5b38e659-48f8-4f18-9e05-9231acd17fdb'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-typography-symbol-5b38e659.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5b38e659-48f8-4f18-9e05-9231acd17fdb', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/ti (text u)_5b38e659-48f8-4f18-9e05-9231acd17fdb.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-typography-symbol-5b38e659',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-t-uppercase', 'letter-i')
REFERENCE_EXPORT_SHA256 = '492eac92b3bbbf1a4f9a2d1493df574ea63bcd667b21e85e8c40014edf3c8074'

class Drawing(TextSub32):
    icon_id = 'text-underlined-typography-symbol-5b38e659-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 26
    text_ink_bounds = (0.0, 0.0, 26.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (24, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (24, 2), (24, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (24, 8), (24, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 2), (17, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (9, 2), (9, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
