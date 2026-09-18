"""Independent 32px profile of text-underlined-si-letters-7512d618.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '7512d618-e73f-4326-8e41-3f3d445862ca'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-si-letters-7512d618.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7512d618-e73f-4326-8e41-3f3d445862ca', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/si (text u)_7512d618-e73f-4326-8e41-3f3d445862ca.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-si-letters-7512d618',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-i')
REFERENCE_EXPORT_SHA256 = '6be448bb2dcc3cf0a3e1ab32e1bf5f0e8c63bfd6e7b12cd50c7bd8eba5565a82'

class Drawing(TextSub32):
    icon_id = 'text-underlined-si-letters-7512d618-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 23
    text_ink_bounds = (0.0, 0.0, 23.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (21, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (21, 2), (21, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (21, 8), (21, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (14, 5), ((13, 3), (11, 2), (9, 2)))
        self.add_bezier('p4-r1-2', (9, 2), ((6, 2), (3, 3), (3, 7)))
        self.add_bezier('p4-r1-3', (3, 7), ((2, 7), (2, 7), (2, 7)))
        self.add_bezier('p4-r1-4', (2, 7), ((2, 12), (14, 10), (15, 16)))
        self.add_bezier('p4-r1-5', (15, 16), ((15, 16), (15, 16), (15, 16)))
        self.add_bezier('p4-r1-6', (15, 16), ((15, 20), (11, 21), (8, 21)))
        self.add_bezier('p4-r1-7', (8, 21), ((6, 21), (3, 20), (2, 18)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', closed=False)
