"""Independent 32px profile of text-underlined-al-letters-c2306778.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'c2306778-41d5-4836-93a4-7175608aabed'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-al-letters-c2306778.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c2306778-41d5-4836-93a4-7175608aabed', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/al (text u)_c2306778-41d5-4836-93a4-7175608aabed.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-al-letters-c2306778',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-l')
REFERENCE_EXPORT_SHA256 = '50d154521e40d1c84a4332996d635b2d2a7805dc05e012f4164845e8da725080'

class Drawing(TextSub32):
    icon_id = 'text-underlined-al-letters-c2306778-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 25
    text_ink_bounds = (0.0, 0.0, 25.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (23, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (23, 3), (23, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 21), (8, 3))
        self.add_bezier('p3-r1-2', (8, 3), ((8.666666666666666, 2.3333333333333335), (9, 2), (9, 2)))
        self.add_bezier('p3-r1-3', (9, 2), ((9.666666666666666, 2), (10, 2.3333333333333335), (10, 3)))
        self.add_line('p3-r1-4', (10, 3), (16, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (5, 13), (13, 13))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
