"""Independent 32px profile of text-underlined-re-text-6823ab30.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '6823ab30-4344-49f7-8e39-6e11107eb51d'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-re-text-6823ab30.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6823ab30-4344-49f7-8e39-6e11107eb51d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/re (text u)_6823ab30-4344-49f7-8e39-6e11107eb51d.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-re-text-6823ab30',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-r-uppercase', 'letter-e')
REFERENCE_EXPORT_SHA256 = '71416a52b84843f921615de1a5f51a918f63684e62e53c1831e9ecec5a0028f0'

class Drawing(TextSub32):
    icon_id = 'text-underlined-re-text-6823ab30-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 38
    text_ink_bounds = (0.0, 0.0, 38.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (36, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (36, 15), ((36, 11), (33, 8), (29, 8)))
        self.add_bezier('p2-r1-2', (29, 8), ((25, 8), (22, 11), (22, 15)))
        self.add_bezier('p2-r1-3', (22, 15), ((22, 18), (25, 21), (29, 21)))
        self.add_bezier('p2-r1-4', (29, 21), ((32, 21), (34, 20), (35, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (22, 15), (36, 15))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 21), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (9, 2))
        self.add_bezier('p4-r1-3', (9, 2), ((13, 2), (15, 5), (15, 7)))
        self.add_bezier('p4-r1-4', (15, 7), ((15, 10), (13, 12), (9, 12)))
        self.add_line('p4-r1-5', (9, 12), (2, 12))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (9, 12), (16, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
        self.relate('connect', 'p4-r1-4', 'p5-r1-1')
        self.relate('connect', 'p4-r1-5', 'p5-r1-1')
