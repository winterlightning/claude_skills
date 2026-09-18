"""Independent 32px profile of text-underlined-ar-text-a642d559.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'a642d559-a61c-4224-b0ae-b1681b0be69e'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-ar-text-a642d559.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a642d559-a61c-4224-b0ae-b1681b0be69e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/ar (text u)_a642d559-a61c-4224-b0ae-b1681b0be69e.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-ar-text-a642d559',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-r')
REFERENCE_EXPORT_SHA256 = '95ca8b4979f8ce48e0d65205612df92ceec46cde1684bb53305b4529d2c2a9c8'

class Drawing(TextSub32):
    icon_id = 'text-underlined-ar-text-a642d559-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 30
    text_ink_bounds = (0.0, 0.0, 30.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (28, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (23, 8), (23, 12))
        self.add_line('p2-r1-2', (23, 12), (23, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (23, 12), ((23, 10), (25, 8), (27, 8)))
        self.add_line('p3-r1-2', (27, 8), (28, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 21), (8, 3))
        self.add_bezier('p4-r1-2', (8, 3), ((8.666666666666666, 2.3333333333333335), (9, 2), (9, 2)))
        self.add_bezier('p4-r1-3', (9, 2), ((9.666666666666666, 2), (10, 2.3333333333333335), (10, 3)))
        self.add_line('p4-r1-4', (10, 3), (16, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (5, 13), (13, 13))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
