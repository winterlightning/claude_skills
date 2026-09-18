"""Independent 32px profile of text-underlined-magnesium-chemical-symbol-c6c64d6b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'c6c64d6b-cdee-4ee0-aa6b-3fdfc5e0e2ae'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-magnesium-chemical-symbol-c6c64d6b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c6c64d6b-cdee-4ee0-aa6b-3fdfc5e0e2ae', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mg (text u)_c6c64d6b-cdee-4ee0-aa6b-3fdfc5e0e2ae.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-magnesium-chemical-symbol-c6c64d6b',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-m-uppercase', 'letter-g')
REFERENCE_EXPORT_SHA256 = 'c1a908043cc96f9ba2a9466c8177a2934ad10463c4193fc90d4cccc461214a31'

class Drawing(TextSub32):
    icon_id = 'text-underlined-magnesium-chemical-symbol-c6c64d6b-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 33
    text_ink_bounds = (0.0, 0.0, 33.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (31, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (31, 14), (31, 9))
        self.add_bezier('p2-r1-2', (31, 9), ((31, 9), (31, 9), (30, 8)))
        self.add_bezier('p2-r1-3', (30, 8), ((29, 7), (28, 6), (26, 6)))
        self.add_bezier('p2-r1-4', (26, 6), ((24, 6), (21, 9), (21, 11)))
        self.add_bezier('p2-r1-5', (21, 11), ((21, 14), (24, 16), (26, 16)))
        self.add_bezier('p2-r1-6', (26, 16), ((28, 16), (30, 15), (31, 14)))
        self.add_line('p2-r1-7', (31, 14), (31, 17))
        self.add_bezier('p2-r1-8', (31, 17), ((31, 19), (28, 21), (26, 21)))
        self.add_line('p2-r1-9', (26, 21), (25, 21))
        self.add_bezier('p2-r1-10', (25, 21), ((24, 21), (22, 20), (22, 19)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', closed=False)
        self.add_line('p3-r1-1', (2, 16), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (9, 11))
        self.add_line('p3-r1-3', (9, 11), (15, 2))
        self.add_line('p3-r1-4', (15, 2), (15, 16))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
