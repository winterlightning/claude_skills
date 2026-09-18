"""Independent 32px profile of text-underlined-letters-in-5d4b9367.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '5d4b9367-c702-404f-bcd6-fe4cc4888d83'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letters-in-5d4b9367.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5d4b9367-c702-404f-bcd6-fe4cc4888d83', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/in (text u)_5d4b9367-c702-404f-bcd6-fe4cc4888d83.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letters-in-5d4b9367',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-i-uppercase', 'letter-n')
REFERENCE_EXPORT_SHA256 = '4babbeff26e1a2154fb43f99b80b88c9492f8204053fa89b70843ced1015eb2e'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letters-in-5d4b9367-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 27
    text_ink_bounds = (0.0, 0.0, 27.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (25, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (25, 21), (25, 13))
        self.add_bezier('p2-r1-2', (25, 13), ((25, 10), (23, 8), (20, 8)))
        self.add_bezier('p2-r1-3', (20, 8), ((17, 8), (15, 10), (15, 13)))
        self.add_line('p2-r1-4', (15, 13), (15, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 2), (8, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (5, 2), (5, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 21), (8, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
