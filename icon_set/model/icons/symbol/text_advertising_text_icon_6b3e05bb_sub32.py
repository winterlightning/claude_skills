"""Independent 32px profile of text-advertising-text-icon-6b3e05bb.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '6b3e05bb-0aa2-4255-8561-4e5b1fcbc0f7'
SOURCE_PATH = 'icon_set/dist/text32/text-advertising-text-icon-6b3e05bb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6b3e05bb-0aa2-4255-8561-4e5b1fcbc0f7', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/ads (text)_6b3e05bb-0aa2-4255-8561-4e5b1fcbc0f7.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-advertising-text-icon-6b3e05bb',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-d-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = 'e4db4a5dbccff34586c224d47638184c9057844278ff79ea6857d0f6603bc264'

class Drawing(TextSub32):
    icon_id = 'text-advertising-text-icon-6b3e05bb-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 78
    text_ink_bounds = (0.0, 0.0, 78.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (76, 6), ((75, 3), (71, 2), (68, 2)))
        self.add_bezier('p1-r1-2', (68, 2), ((64, 2), (60, 4), (59, 9)))
        self.add_bezier('p1-r1-3', (59, 9), ((59, 9), (59, 9), (59, 10)))
        self.add_bezier('p1-r1-4', (59, 10), ((59, 17), (76, 13), (76, 22)))
        self.add_bezier('p1-r1-5', (76, 22), ((76, 22), (76, 22), (76, 23)))
        self.add_bezier('p1-r1-6', (76, 23), ((76, 28), (72, 30), (67, 30)))
        self.add_bezier('p1-r1-7', (67, 30), ((63, 30), (60, 29), (58, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (31, 2), (39, 2))
        self.add_bezier('p2-r1-2', (39, 2), ((46, 2), (50, 9), (50, 16)))
        self.add_bezier('p2-r1-3', (50, 16), ((50, 23), (46, 30), (39, 30)))
        self.add_line('p2-r1-4', (39, 30), (31, 30))
        self.add_line('p2-r1-5', (31, 30), (31, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (2, 30), (11, 3))
        self.add_bezier('p3-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p3-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p3-r1-4', (14, 3), (23, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (6, 18), (19, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
