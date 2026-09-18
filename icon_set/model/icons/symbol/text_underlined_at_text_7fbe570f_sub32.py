"""Independent 32px profile of text-underlined-at-text-7fbe570f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '7fbe570f-6495-4b09-a326-af8a6324ecf7'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-at-text-7fbe570f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7fbe570f-6495-4b09-a326-af8a6324ecf7', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/at (text u)_7fbe570f-6495-4b09-a326-af8a6324ecf7.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-at-text-7fbe570f',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-t')
REFERENCE_EXPORT_SHA256 = '4a6faf2ff0da78b6d109fb09823a3be0cb36a4fe2a60f142b770ec20c68f040b'

class Drawing(TextSub32):
    icon_id = 'text-underlined-at-text-7fbe570f-sub32'
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
        self.add_bezier('p2-r1-1', (27, 3), ((27, 3), (27, 8), (27, 12)))
        self.add_bezier('p2-r1-2', (27, 12), ((27, 14), (27, 16), (27, 17)))
        self.add_bezier('p2-r1-3', (27, 17), ((27, 18), (27, 20), (29, 21)))
        self.add_bezier('p2-r1-4', (29, 21), ((30, 21), (30, 21), (31, 21)))
        self.add_bezier('p2-r1-5', (31, 21), ((32, 21), (32, 21), (32, 21)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (23, 8), (31, 8))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 21), (8, 3))
        self.add_bezier('p4-r1-2', (8, 3), ((8.666666666666666, 2.3333333333333335), (9, 2), (9, 2)))
        self.add_bezier('p4-r1-3', (9, 2), ((9.666666666666666, 2), (10, 2.3333333333333335), (10, 3)))
        self.add_line('p4-r1-4', (10, 3), (16, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (5, 13), (13, 13))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
