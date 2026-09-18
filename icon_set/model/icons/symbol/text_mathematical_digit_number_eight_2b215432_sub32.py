"""Independent 32px profile of text-mathematical-digit-number-eight-2b215432.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '2b215432-9630-40f7-b54c-8a46d1aa75a7'
SOURCE_PATH = 'icon_set/dist/text32/text-mathematical-digit-number-eight-2b215432.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2b215432-9630-40f7-b54c-8a46d1aa75a7', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/8_2b215432-9630-40f7-b54c-8a46d1aa75a7.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-mathematical-digit-number-eight-2b215432',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-8',)
REFERENCE_EXPORT_SHA256 = '18f496b68eb966c5385b9259e36e310a72122bb1bd5aade007eab057bde7eca6'

class Drawing(TextSub32):
    icon_id = 'text-mathematical-digit-number-eight-2b215432-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 23
    text_ink_bounds = (0.0, 0.0, 23.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (3, 9), ((3, 5), (6, 2), (10, 2)))
        self.add_line('p1-r1-2', (10, 2), (14, 2))
        self.add_bezier('p1-r1-3', (14, 2), ((17, 2), (20, 5), (20, 9)))
        self.add_bezier('p1-r1-4', (20, 9), ((20, 12), (17, 15), (14, 15)))
        self.add_line('p1-r1-5', (14, 15), (10, 15))
        self.add_bezier('p1-r1-6', (10, 15), ((6, 15), (3, 12), (3, 9)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_bezier('p2-r1-1', (2, 23), ((2, 19), (5, 15), (9, 15)))
        self.add_line('p2-r1-2', (9, 15), (14, 15))
        self.add_bezier('p2-r1-3', (14, 15), ((18, 15), (21, 19), (21, 23)))
        self.add_bezier('p2-r1-4', (21, 23), ((21, 27), (18, 30), (14, 30)))
        self.add_line('p2-r1-5', (14, 30), (9, 30))
        self.add_bezier('p2-r1-6', (9, 30), ((5, 30), (2, 27), (2, 23)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-3')
        self.relate('connect', 'p1-r1-5', 'p2-r1-2')
        self.relate('connect', 'p1-r1-5', 'p2-r1-3')
