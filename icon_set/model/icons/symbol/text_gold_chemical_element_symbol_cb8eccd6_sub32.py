"""Independent 32px profile of text-gold-chemical-element-symbol-cb8eccd6.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'cb8eccd6-3dbd-47c2-9fa0-355d14a6b13b'
SOURCE_PATH = 'icon_set/dist/text32/text-gold-chemical-element-symbol-cb8eccd6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cb8eccd6-3dbd-47c2-9fa0-355d14a6b13b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/au (text u)_cb8eccd6-3dbd-47c2-9fa0-355d14a6b13b.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-gold-chemical-element-symbol-cb8eccd6', 'text/text-gold-element-chemical-symbol-9e32ea71')
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-u')
REFERENCE_EXPORT_SHA256 = '88dc8a45d4d0127f2b4abf265c0b17a7b3d5b9ff30241baf9529a8221be0001c'

class Drawing(TextSub32):
    icon_id = 'text-gold-chemical-element-symbol-cb8eccd6-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 35
    text_ink_bounds = (0.0, 0.0, 35.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (33, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (23, 8), (23, 16))
        self.add_bezier('p2-r1-2', (23, 16), ((23, 19), (25, 21), (28, 21)))
        self.add_bezier('p2-r1-3', (28, 21), ((31, 21), (33, 19), (33, 16)))
        self.add_line('p2-r1-4', (33, 16), (33, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 21), (8, 3))
        self.add_bezier('p3-r1-2', (8, 3), ((8.666666666666666, 2.3333333333333335), (9, 2), (9, 2)))
        self.add_bezier('p3-r1-3', (9, 2), ((9.666666666666666, 2), (10, 2.3333333333333335), (10, 3)))
        self.add_line('p3-r1-4', (10, 3), (16, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (5, 13), (13, 13))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
