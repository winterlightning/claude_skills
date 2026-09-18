"""Independent 32px profile of text-silver-chemical-element-symbol-a8aa1719.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'a8aa1719-868b-47cf-b8dd-d616d6cfe0da'
SOURCE_PATH = 'icon_set/dist/text32/text-silver-chemical-element-symbol-a8aa1719.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a8aa1719-868b-47cf-b8dd-d616d6cfe0da', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/ag (text u)_a8aa1719-868b-47cf-b8dd-d616d6cfe0da.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-silver-chemical-element-symbol-a8aa1719',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-g')
REFERENCE_EXPORT_SHA256 = '88d7f1e04efe147cf2a09d666e5c994631a37db6b42cf263efc65074140bb178'

class Drawing(TextSub32):
    icon_id = 'text-silver-chemical-element-symbol-a8aa1719-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 35
    text_ink_bounds = (0.0, 0.0, 35.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (32, 15), (32, 10))
        self.add_bezier('p1-r1-2', (32, 10), ((32, 10), (32, 10), (32, 9)))
        self.add_bezier('p1-r1-3', (32, 9), ((31, 8), (29, 7), (27, 7)))
        self.add_bezier('p1-r1-4', (27, 7), ((24, 7), (22, 9), (22, 13)))
        self.add_bezier('p1-r1-5', (22, 13), ((22, 16), (24, 18), (27, 18)))
        self.add_bezier('p1-r1-6', (27, 18), ((29, 18), (31, 17), (32, 15)))
        self.add_line('p1-r1-7', (32, 15), (32, 19))
        self.add_bezier('p1-r1-8', (32, 19), ((32, 22), (30, 24), (27, 24)))
        self.add_line('p1-r1-9', (27, 24), (26, 24))
        self.add_bezier('p1-r1-10', (26, 24), ((24, 24), (23, 23), (22, 21)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (2, 18), (7, 3))
        self.add_bezier('p2-r1-2', (7, 3), ((7.666666666666667, 2.3333333333333335), (8, 2), (8, 2)))
        self.add_bezier('p2-r1-3', (8, 2), ((8, 2), (8.333333333333334, 2.3333333333333335), (9, 3)))
        self.add_line('p2-r1-4', (9, 3), (14, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (4, 11), (12, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 30), (33, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
