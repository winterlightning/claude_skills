"""Independent 32px profile of text-for-rent-text-76df62d1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '76df62d1-fa3a-4d3a-a8c2-732196c43a7d'
SOURCE_PATH = 'icon_set/dist/text32/text-for-rent-text-76df62d1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('76df62d1-fa3a-4d3a-a8c2-732196c43a7d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/for rent (text)_76df62d1-fa3a-4d3a-a8c2-732196c43a7d.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-for-rent-text-76df62d1',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-f-uppercase', 'letter-o-uppercase', 'letter-r-uppercase', 'letter-r-uppercase', 'letter-e-uppercase', 'letter-n-uppercase', 'letter-t-uppercase')
REFERENCE_EXPORT_SHA256 = '60930a8a2cde3f6e6a5b727698b5ca41f5c4e558061009d82c808646954d39f3'

class Drawing(TextSub32):
    icon_id = 'text-for-rent-text-76df62d1-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 215
    text_ink_bounds = (0.0, 0.0, 214.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (191, 2), (212, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (201, 2), (201, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (160, 30), (160, 2))
        self.add_line('p3-r1-2', (160, 2), (180, 30))
        self.add_line('p3-r1-3', (180, 30), (180, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (149, 2), (132, 2))
        self.add_line('p4-r1-2', (132, 2), (132, 30))
        self.add_line('p4-r1-3', (132, 30), (149, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.add_line('p5-r1-1', (132, 16), (146, 16))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (102, 30), (102, 2))
        self.add_line('p6-r1-2', (102, 2), (112, 2))
        self.add_bezier('p6-r1-3', (112, 2), ((118, 2), (121, 6), (121, 9)))
        self.add_bezier('p6-r1-4', (121, 9), ((121, 13), (118, 17), (112, 17)))
        self.add_line('p6-r1-5', (112, 17), (102, 17))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', 'p6-r1-5', closed=False)
        self.add_line('p7-r1-1', (112, 17), (122, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (60, 30), (60, 2))
        self.add_line('p8-r1-2', (60, 2), (70, 2))
        self.add_bezier('p8-r1-3', (70, 2), ((77, 2), (80, 6), (80, 9)))
        self.add_bezier('p8-r1-4', (80, 9), ((80, 13), (77, 17), (70, 17)))
        self.add_line('p8-r1-5', (70, 17), (60, 17))
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', 'p8-r1-3', 'p8-r1-4', 'p8-r1-5', closed=False)
        self.add_line('p9-r1-1', (70, 17), (80, 30))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.add_bezier('p10-r1-1', (30, 16), ((30, 8), (34, 2), (40, 2)))
        self.add_bezier('p10-r1-2', (40, 2), ((45, 2), (50, 8), (50, 16)))
        self.add_bezier('p10-r1-3', (50, 16), ((50, 24), (45, 30), (40, 30)))
        self.add_bezier('p10-r1-4', (40, 30), ((34, 30), (30, 24), (30, 16)))
        self.add_contour('path-10-1', 'p10-r1-1', 'p10-r1-2', 'p10-r1-3', 'p10-r1-4', closed=False)
        self.add_line('p11-r1-1', (19, 2), (2, 2))
        self.add_line('p11-r1-2', (2, 2), (2, 30))
        self.add_contour('path-11-1', 'p11-r1-1', 'p11-r1-2', closed=False)
        self.add_line('p12-r1-1', (2, 16), (16, 16))
        self.add_contour('path-12-1', 'p12-r1-1', closed=False)
        self.relate('connect', 'p6-r1-4', 'p7-r1-1')
        self.relate('connect', 'p6-r1-5', 'p7-r1-1')
        self.relate('connect', 'p8-r1-4', 'p9-r1-1')
        self.relate('connect', 'p8-r1-5', 'p9-r1-1')
