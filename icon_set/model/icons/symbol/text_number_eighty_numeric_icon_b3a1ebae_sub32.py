"""Independent 32px profile of text-number-eighty-numeric-icon-b3a1ebae.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'b3a1ebae-eb75-4215-bbf1-68195d137c9d'
SOURCE_PATH = 'icon_set/dist/text32/text-number-eighty-numeric-icon-b3a1ebae.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b3a1ebae-eb75-4215-bbf1-68195d137c9d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/80 (text)_b3a1ebae-eb75-4215-bbf1-68195d137c9d.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-eighty-numeric-icon-b3a1ebae',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-8', 'digit-0')
REFERENCE_EXPORT_SHA256 = '5162c11a270f5084c0b25e5be6f48853c7f4ef3068c6faf7491b137311e65b48'

class Drawing(TextSub32):
    icon_id = 'text-number-eighty-numeric-icon-b3a1ebae-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 51
    text_ink_bounds = (0.0, 0.0, 51.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (29, 10), (49, 10), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (49, 10), (49, 22))
        self.add_arc('p1-r1-3', (49, 22), (29, 22), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (29, 22), (29, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (3, 9), ((3, 5), (6, 2), (10, 2)))
        self.add_line('p2-r1-2', (10, 2), (14, 2))
        self.add_bezier('p2-r1-3', (14, 2), ((17, 2), (20, 5), (20, 9)))
        self.add_bezier('p2-r1-4', (20, 9), ((20, 12), (17, 15), (14, 15)))
        self.add_line('p2-r1-5', (14, 15), (10, 15))
        self.add_bezier('p2-r1-6', (10, 15), ((6, 15), (3, 12), (3, 9)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_bezier('p3-r1-1', (2, 23), ((2, 19), (5, 15), (9, 15)))
        self.add_line('p3-r1-2', (9, 15), (14, 15))
        self.add_bezier('p3-r1-3', (14, 15), ((18, 15), (21, 19), (21, 23)))
        self.add_bezier('p3-r1-4', (21, 23), ((21, 27), (18, 30), (14, 30)))
        self.add_line('p3-r1-5', (14, 30), (9, 30))
        self.add_bezier('p3-r1-6', (9, 30), ((5, 30), (2, 27), (2, 23)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.relate('connect', 'p2-r1-4', 'p3-r1-2')
        self.relate('connect', 'p2-r1-4', 'p3-r1-3')
        self.relate('connect', 'p2-r1-5', 'p3-r1-2')
        self.relate('connect', 'p2-r1-5', 'p3-r1-3')
