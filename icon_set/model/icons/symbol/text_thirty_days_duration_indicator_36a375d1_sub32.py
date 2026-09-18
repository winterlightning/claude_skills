"""Independent 32px profile of text-thirty-days-duration-indicator-36a375d1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '36a375d1-0b51-4625-9639-8c6afb0d4382'
SOURCE_PATH = 'icon_set/dist/text32/text-thirty-days-duration-indicator-36a375d1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('36a375d1-0b51-4625-9639-8c6afb0d4382', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/30day (text)_36a375d1-0b51-4625-9639-8c6afb0d4382.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-thirty-days-duration-indicator-36a375d1',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-3', 'digit-0', 'letter-d-uppercase', 'letter-a-uppercase', 'letter-y-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = 'cc1cb6c0fc19bd5c98425faee72af895aa4579574b66d18ba0b4019710272c50'

class Drawing(TextSub32):
    icon_id = 'text-thirty-days-duration-indicator-36a375d1-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 186
    text_ink_bounds = (0.0, 0.0, 185.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (182, 6), ((181, 3), (178, 2), (175, 2)))
        self.add_bezier('p1-r1-2', (175, 2), ((171, 2), (166, 4), (166, 9)))
        self.add_bezier('p1-r1-3', (166, 9), ((165, 9), (165, 9), (165, 10)))
        self.add_bezier('p1-r1-4', (165, 10), ((165, 17), (182, 13), (183, 22)))
        self.add_bezier('p1-r1-5', (183, 22), ((183, 22), (183, 22), (183, 23)))
        self.add_bezier('p1-r1-6', (183, 23), ((183, 28), (179, 30), (174, 30)))
        self.add_bezier('p1-r1-7', (174, 30), ((170, 30), (166, 29), (165, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (133, 2), (143, 17))
        self.add_line('p2-r1-2', (143, 17), (154, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (143, 17), (143, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (101, 30), (111, 3))
        self.add_bezier('p4-r1-2', (111, 3), ((111, 2.3333333333333335), (111.33333333333333, 2), (112, 2)))
        self.add_bezier('p4-r1-3', (112, 2), ((112, 2), (112.33333333333333, 2.3333333333333335), (113, 3)))
        self.add_line('p4-r1-4', (113, 3), (122, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (105, 18), (118, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (71, 2), (79, 2))
        self.add_bezier('p6-r1-2', (79, 2), ((87, 2), (91, 9), (91, 16)))
        self.add_bezier('p6-r1-3', (91, 16), ((91, 23), (87, 30), (79, 30)))
        self.add_line('p6-r1-4', (79, 30), (71, 30))
        self.add_line('p6-r1-5', (71, 30), (71, 2))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', 'p6-r1-5', closed=False)
        self.add_bezier('p7-r1-1', (31, 10), ((31, 6), (35, 2), (40, 2)))
        self.add_bezier('p7-r1-2', (40, 2), ((46, 2), (50, 6), (50, 10)))
        self.add_line('p7-r1-3', (50, 10), (50, 22))
        self.add_bezier('p7-r1-4', (50, 22), ((50, 26), (46, 30), (40, 30)))
        self.add_bezier('p7-r1-5', (40, 30), ((35, 30), (31, 26), (31, 22)))
        self.add_line('p7-r1-6', (31, 22), (31, 10))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', 'p7-r1-4', 'p7-r1-5', 'p7-r1-6', closed=False)
        self.add_line('p8-r1-1', (2, 2), (13, 2))
        self.add_bezier('p8-r1-2', (13, 2), ((17, 2), (20, 5), (20, 9)))
        self.add_bezier('p8-r1-3', (20, 9), ((20, 13), (17, 16), (13, 16)))
        self.add_line('p8-r1-4', (13, 16), (9, 16))
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', 'p8-r1-3', 'p8-r1-4', closed=False)
        self.add_line('p9-r1-1', (10, 16), (13, 16))
        self.add_bezier('p9-r1-2', (13, 16), ((17, 16), (20, 19), (20, 23)))
        self.add_bezier('p9-r1-3', (20, 23), ((20, 27), (17, 30), (13, 30)))
        self.add_line('p9-r1-4', (13, 30), (2, 30))
        self.add_contour('path-9-1', 'p9-r1-1', 'p9-r1-2', 'p9-r1-3', 'p9-r1-4', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p8-r1-3', 'p9-r1-1')
        self.relate('connect', 'p8-r1-3', 'p9-r1-2')
        self.relate('connect', 'p8-r1-4', 'p9-r1-1')
        self.relate('connect', 'p8-r1-4', 'p9-r1-2')
