"""Independent 32px profile of text-underlined-germanium-element-symbol-6a1cef81.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '6a1cef81-74dd-4aac-86f0-786b211f3267'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-germanium-element-symbol-6a1cef81.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6a1cef81-74dd-4aac-86f0-786b211f3267', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/ge (text u)_6a1cef81-74dd-4aac-86f0-786b211f3267.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-germanium-element-symbol-6a1cef81',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-g-uppercase', 'letter-e')
REFERENCE_EXPORT_SHA256 = 'e71d162c809732e2d9b3158b4259079d6e2deca7dc47bef8d807b2c7098bc811'

class Drawing(TextSub32):
    icon_id = 'text-underlined-germanium-element-symbol-6a1cef81-sub32'
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
        self.add_bezier('p4-r1-1', (14, 5), ((13, 3), (11, 2), (9, 2)))
        self.add_bezier('p4-r1-2', (9, 2), ((6, 2), (2, 7), (2, 12)))
        self.add_bezier('p4-r1-3', (2, 12), ((2, 13), (2, 14), (3, 15)))
        self.add_bezier('p4-r1-4', (3, 15), ((4, 19), (6, 21), (9, 21)))
        self.add_bezier('p4-r1-5', (9, 21), ((12, 21), (16, 17), (16, 12)))
        self.add_line('p4-r1-6', (16, 12), (11, 12))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
