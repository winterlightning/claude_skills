"""Independent 32px profile of text-underlined-tin-element-symbol-b1b903d5.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'b1b903d5-9189-45f0-9880-e909e013544b'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-tin-element-symbol-b1b903d5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b1b903d5-9189-45f0-9880-e909e013544b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/sn (text u)_b1b903d5-9189-45f0-9880-e909e013544b.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-tin-element-symbol-b1b903d5',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-n')
REFERENCE_EXPORT_SHA256 = '84cf9fda70c30a406b7fbb0de4698150b9d884dd5c01c10c5581593e8e84d946'

class Drawing(TextSub32):
    icon_id = 'text-underlined-tin-element-symbol-b1b903d5-sub32'
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
        self.add_line('p2-r1-1', (32, 21), (32, 13))
        self.add_bezier('p2-r1-2', (32, 13), ((32, 10), (29, 8), (26, 8)))
        self.add_bezier('p2-r1-3', (26, 8), ((24, 8), (21, 10), (21, 13)))
        self.add_line('p2-r1-4', (21, 13), (21, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (14, 5), ((13, 3), (11, 2), (9, 2)))
        self.add_bezier('p3-r1-2', (9, 2), ((6, 2), (3, 3), (3, 7)))
        self.add_bezier('p3-r1-3', (3, 7), ((2, 7), (2, 7), (2, 7)))
        self.add_bezier('p3-r1-4', (2, 7), ((2, 12), (14, 10), (15, 16)))
        self.add_bezier('p3-r1-5', (15, 16), ((15, 16), (15, 16), (15, 16)))
        self.add_bezier('p3-r1-6', (15, 16), ((15, 20), (11, 21), (8, 21)))
        self.add_bezier('p3-r1-7', (8, 21), ((6, 21), (3, 20), (2, 18)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
