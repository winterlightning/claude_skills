"""Independent 32px profile of text-underlined-letters-as-8a434cfd.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '8a434cfd-38e8-47a2-aa36-3ae47ef93617'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letters-as-8a434cfd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8a434cfd-38e8-47a2-aa36-3ae47ef93617', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/as (text u)_8a434cfd-38e8-47a2-aa36-3ae47ef93617.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letters-as-8a434cfd',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-s')
REFERENCE_EXPORT_SHA256 = '356e9263296955cc9df8694299d495d1a4c4ec652611f74c474946ca5f73a2af'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letters-as-8a434cfd-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 34
    text_ink_bounds = (0.0, 0.0, 34.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (32, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (31, 10), ((31, 10), (31, 8), (27, 8)))
        self.add_bezier('p2-r1-2', (27, 8), ((25, 8), (23, 10), (23, 11)))
        self.add_bezier('p2-r1-3', (23, 11), ((23, 12), (24, 13), (25, 14)))
        self.add_bezier('p2-r1-4', (25, 14), ((29, 15), (28, 15), (30, 16)))
        self.add_bezier('p2-r1-5', (30, 16), ((31, 16), (32, 17), (32, 18)))
        self.add_bezier('p2-r1-6', (32, 18), ((32, 19), (30, 21), (27, 21)))
        self.add_bezier('p2-r1-7', (27, 21), ((23, 21), (23, 19), (23, 19)))
        self.add_bezier('p2-r1-8', (23, 19), ((23, 19), (23, 19), (23, 19)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.add_line('p3-r1-1', (2, 21), (8, 3))
        self.add_bezier('p3-r1-2', (8, 3), ((8.666666666666666, 2.3333333333333335), (9, 2), (9, 2)))
        self.add_bezier('p3-r1-3', (9, 2), ((9.666666666666666, 2), (10, 2.3333333333333335), (10, 3)))
        self.add_line('p3-r1-4', (10, 3), (16, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (5, 13), (13, 13))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
