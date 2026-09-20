"""Independent 32px profile of text-underlined-letter-s-829ed2f4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '829ed2f4-100b-4782-ba1e-ca55515e306a'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letter-s-829ed2f4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('829ed2f4-100b-4782-ba1e-ca55515e306a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/s (text u)_829ed2f4-100b-4782-ba1e-ca55515e306a.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letter-s-829ed2f4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase',)
REFERENCE_EXPORT_SHA256 = '63d7eb4dafd89cfbc5d8c6dd16300ff8c69464b20ccf261e7c6d423d955f0fd9'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letter-s-829ed2f4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 17
    text_ink_bounds = (0.0, 0.0, 17.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (15, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (14, 5), ((13, 3), (11, 2), (9, 2)))
        self.add_bezier('p2-r1-2', (9, 2), ((6, 2), (3, 3), (3, 7)))
        self.add_bezier('p2-r1-3', (3, 7), ((2, 7), (2, 7), (2, 7)))
        self.add_bezier('p2-r1-4', (2, 7), ((2, 12), (14, 10), (15, 16)))
        self.add_bezier('p2-r1-5', (15, 16), ((15, 16), (15, 16), (15, 16)))
        self.add_bezier('p2-r1-6', (15, 16), ((15, 20), (11, 21), (8, 21)))
        self.add_bezier('p2-r1-7', (8, 21), ((6, 21), (3, 20), (2, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
