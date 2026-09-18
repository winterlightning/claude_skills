"""Independent 32px profile of text-spa-typography-label-d1278012.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'd1278012-41b1-467e-a300-f4f563f20969'
SOURCE_PATH = 'icon_set/dist/text32/text-spa-typography-label-d1278012.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d1278012-41b1-467e-a300-f4f563f20969', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/spa (text)_d1278012-41b1-467e-a300-f4f563f20969.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-spa-typography-label-d1278012',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-p-uppercase', 'letter-a-uppercase')
REFERENCE_EXPORT_SHA256 = '17a17f3b4a37773b0b057bf1663da1d7ed31fdd4210028f2e09fcc012ee342e8'

class Drawing(TextSub32):
    icon_id = 'text-spa-typography-label-d1278012-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 78
    text_ink_bounds = (0.0, 0.0, 78.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (56, 30), (65, 3))
        self.add_bezier('p1-r1-2', (65, 3), ((65, 2.3333333333333335), (65.33333333333333, 2), (66, 2)))
        self.add_bezier('p1-r1-3', (66, 2), ((66.66666666666667, 2), (67, 2.3333333333333335), (67, 3)))
        self.add_line('p1-r1-4', (67, 3), (76, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (60, 18), (72, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (28, 30), (28, 2))
        self.add_line('p3-r1-2', (28, 2), (38, 2))
        self.add_bezier('p3-r1-3', (38, 2), ((45, 2), (48, 6), (48, 9)))
        self.add_bezier('p3-r1-4', (48, 9), ((48, 13), (45, 17), (38, 17)))
        self.add_line('p3-r1-5', (38, 17), (28, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_bezier('p4-r1-1', (20, 6), ((19, 3), (15, 2), (12, 2)))
        self.add_bezier('p4-r1-2', (12, 2), ((8, 2), (4, 4), (3, 9)))
        self.add_bezier('p4-r1-3', (3, 9), ((3, 9), (3, 9), (3, 10)))
        self.add_bezier('p4-r1-4', (3, 10), ((3, 17), (20, 13), (20, 22)))
        self.add_bezier('p4-r1-5', (20, 22), ((20, 22), (20, 22), (20, 23)))
        self.add_bezier('p4-r1-6', (20, 23), ((20, 28), (16, 30), (11, 30)))
        self.add_bezier('p4-r1-7', (11, 30), ((7, 30), (4, 29), (2, 26)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', closed=False)
