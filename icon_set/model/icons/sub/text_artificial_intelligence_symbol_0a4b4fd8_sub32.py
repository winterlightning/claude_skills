"""Independent 32px profile of text-artificial-intelligence-symbol-0a4b4fd8.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '0a4b4fd8-4d98-4ed6-a8ce-22dfe89a0ef8'
SOURCE_PATH = 'icon_set/dist/text32/text-artificial-intelligence-symbol-0a4b4fd8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0a4b4fd8-4d98-4ed6-a8ce-22dfe89a0ef8', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/Ai_0a4b4fd8-4d98-4ed6-a8ce-22dfe89a0ef8.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-artificial-intelligence-symbol-0a4b4fd8',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-i-uppercase')
REFERENCE_EXPORT_SHA256 = 'fdad5d997c16b959824bd6821be8eab9efb73b578f06bad858f1fbada66cec94'

class Drawing(TextSub32):
    icon_id = 'text-artificial-intelligence-symbol-0a4b4fd8-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 42
    text_ink_bounds = (0.0, 0.0, 42.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (31, 2), (40, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (35, 2), (35, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (31, 30), (40, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 30), (11, 3))
        self.add_bezier('p4-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p4-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p4-r1-4', (14, 3), (23, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (6, 18), (19, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
