"""Independent 32px profile of text-american-express-text-logo-0f9d7b16.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '0f9d7b16-bd14-41ce-84bb-216c4ac6c8c9'
SOURCE_PATH = 'icon_set/dist/text32/text-american-express-text-logo-0f9d7b16.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0f9d7b16-bd14-41ce-84bb-216c4ac6c8c9', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/amex (text)_0f9d7b16-bd14-41ce-84bb-216c4ac6c8c9.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-american-express-text-logo-0f9d7b16',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-m-uppercase', 'letter-e-uppercase', 'letter-x-uppercase')
REFERENCE_EXPORT_SHA256 = 'a001ca7e821dcd63caa7074ee6fd7ddfea4f32065a029194478f5f545de4ca1b'

class Drawing(TextSub32):
    icon_id = 'text-american-express-text-logo-0f9d7b16-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 112
    text_ink_bounds = (0.0, 0.0, 112.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (90, 2), (110, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (110, 2), (90, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (82, 2), (65, 2))
        self.add_line('p3-r1-2', (65, 2), (65, 30))
        self.add_line('p3-r1-3', (65, 30), (82, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (65, 16), (79, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (31, 30), (31, 2))
        self.add_line('p5-r1-2', (31, 2), (44, 20))
        self.add_line('p5-r1-3', (44, 20), (57, 2))
        self.add_line('p5-r1-4', (57, 2), (57, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
        self.add_line('p6-r1-1', (2, 30), (11, 3))
        self.add_bezier('p6-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p6-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p6-r1-4', (14, 3), (23, 30))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', closed=False)
        self.add_line('p7-r1-1', (6, 18), (19, 18))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
