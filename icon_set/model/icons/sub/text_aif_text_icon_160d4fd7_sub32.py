"""Independent 32px profile of text-aif-text-icon-160d4fd7.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '160d4fd7-2412-44db-98f1-535785768595'
SOURCE_PATH = 'icon_set/dist/text32/text-aif-text-icon-160d4fd7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('160d4fd7-2412-44db-98f1-535785768595', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/AIF (text)_160d4fd7-2412-44db-98f1-535785768595.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-aif-text-icon-160d4fd7',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-i-uppercase', 'letter-f-uppercase')
REFERENCE_EXPORT_SHA256 = 'e8bb5fc497e00f39957c1239ff8c4f2ff4135dcb63c560eb53c485a38a10a791'

class Drawing(TextSub32):
    icon_id = 'text-aif-text-icon-160d4fd7-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 67
    text_ink_bounds = (0.0, 0.0, 67.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (65, 2), (48, 2))
        self.add_line('p1-r1-2', (48, 2), (48, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (48, 16), (62, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (31, 2), (40, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (35, 2), (35, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (31, 30), (40, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (2, 30), (11, 3))
        self.add_bezier('p6-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p6-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p6-r1-4', (14, 3), (23, 30))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', closed=False)
        self.add_line('p7-r1-1', (6, 18), (19, 18))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
