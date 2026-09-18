"""Independent 32px profile of text-underlined-title-case-text-2ee5ec1c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '2ee5ec1c-2e45-425c-a158-082563f5af59'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-title-case-text-2ee5ec1c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2ee5ec1c-2e45-425c-a158-082563f5af59', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/tc (text u)_2ee5ec1c-2e45-425c-a158-082563f5af59.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-title-case-text-2ee5ec1c',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-t-uppercase', 'letter-c')
REFERENCE_EXPORT_SHA256 = '4620cd7e91229fbd0a9fce1921dfe3c12c0417e4cc7f6039690ea5ba4b5e5476'

class Drawing(TextSub32):
    icon_id = 'text-underlined-title-case-text-2ee5ec1c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 38
    text_ink_bounds = (0.0, 0.0, 38.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (36, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (36, 11), ((34, 9), (32, 8), (30, 8)))
        self.add_bezier('p2-r1-2', (30, 8), ((27, 8), (24, 11), (24, 15)))
        self.add_bezier('p2-r1-3', (24, 15), ((24, 18), (27, 21), (30, 21)))
        self.add_bezier('p2-r1-4', (30, 21), ((33, 21), (35, 20), (36, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 2), (17, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (9, 2), (9, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
