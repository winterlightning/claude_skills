"""Independent 32px profile of text-seven-days-duration-text-e220de6b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'e220de6b-3280-456c-b80e-dc2702654cac'
SOURCE_PATH = 'icon_set/dist/text32/text-seven-days-duration-text-e220de6b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e220de6b-3280-456c-b80e-dc2702654cac', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/7day (text)_e220de6b-3280-456c-b80e-dc2702654cac.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-seven-days-duration-text-e220de6b',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-7', 'letter-d-uppercase', 'letter-a-uppercase', 'letter-y-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = '4636e43c2682e67635927bd24b959e57fcc66a3c873da0d096feae4f726398cd'

class Drawing(TextSub32):
    icon_id = 'text-seven-days-duration-text-e220de6b-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 156
    text_ink_bounds = (0.0, 0.0, 156.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (153, 6), ((152, 3), (149, 2), (145, 2)))
        self.add_bezier('p1-r1-2', (145, 2), ((141, 2), (137, 4), (136, 9)))
        self.add_bezier('p1-r1-3', (136, 9), ((136, 9), (136, 9), (136, 10)))
        self.add_bezier('p1-r1-4', (136, 10), ((136, 17), (153, 13), (154, 22)))
        self.add_bezier('p1-r1-5', (154, 22), ((154, 22), (154, 22), (154, 23)))
        self.add_bezier('p1-r1-6', (154, 23), ((154, 28), (149, 30), (145, 30)))
        self.add_bezier('p1-r1-7', (145, 30), ((141, 30), (137, 29), (136, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (103, 2), (114, 17))
        self.add_line('p2-r1-2', (114, 17), (125, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (114, 17), (114, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (72, 30), (81, 3))
        self.add_bezier('p4-r1-2', (81, 3), ((81.66666666666667, 2.3333333333333335), (82, 2), (82, 2)))
        self.add_bezier('p4-r1-3', (82, 2), ((82.66666666666667, 2), (83, 2.3333333333333335), (83, 3)))
        self.add_line('p4-r1-4', (83, 3), (93, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (76, 18), (89, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (42, 2), (50, 2))
        self.add_bezier('p6-r1-2', (50, 2), ((58, 2), (61, 9), (61, 16)))
        self.add_bezier('p6-r1-3', (61, 16), ((61, 23), (58, 30), (50, 30)))
        self.add_line('p6-r1-4', (50, 30), (42, 30))
        self.add_line('p6-r1-5', (42, 30), (42, 2))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', 'p6-r1-5', closed=False)
        self.add_line('p7-r1-1', (2, 2), (20, 2))
        self.add_bezier('p7-r1-2', (20, 2), ((21, 2), (21, 2), (21, 3)))
        self.add_bezier('p7-r1-3', (21, 3), ((21, 3), (21, 3), (21, 3)))
        self.add_line('p7-r1-4', (21, 3), (8, 30))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', 'p7-r1-4', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
