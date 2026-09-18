"""Independent 32px profile of text-rar-compressed-archive-text-c62d42dd.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'c62d42dd-71d9-43d8-bd33-062a182b2527'
SOURCE_PATH = 'icon_set/dist/text32/text-rar-compressed-archive-text-c62d42dd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c62d42dd-71d9-43d8-bd33-062a182b2527', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/rar (text)_c62d42dd-71d9-43d8-bd33-062a182b2527.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-rar-compressed-archive-text-c62d42dd',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-r-uppercase', 'letter-a-uppercase', 'letter-r-uppercase')
REFERENCE_EXPORT_SHA256 = '9eb3a4cd5c72a98b486fb3cc7d5c2c56837a592d8c5b2c38e68f72eae1011539'

class Drawing(TextSub32):
    icon_id = 'text-rar-compressed-archive-text-c62d42dd-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 81
    text_ink_bounds = (0.0, 0.0, 81.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (59, 30), (59, 2))
        self.add_line('p1-r1-2', (59, 2), (69, 2))
        self.add_bezier('p1-r1-3', (69, 2), ((75, 2), (78, 6), (78, 9)))
        self.add_bezier('p1-r1-4', (78, 9), ((78, 13), (75, 17), (69, 17)))
        self.add_line('p1-r1-5', (69, 17), (59, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (69, 17), (79, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (30, 30), (39, 3))
        self.add_bezier('p3-r1-2', (39, 3), ((39.666666666666664, 2.3333333333333335), (40.333333333333336, 2), (41, 2)))
        self.add_bezier('p3-r1-3', (41, 2), ((41, 2), (41.333333333333336, 2.3333333333333335), (42, 3)))
        self.add_line('p3-r1-4', (42, 3), (51, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (34, 18), (47, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 30), (2, 2))
        self.add_line('p5-r1-2', (2, 2), (12, 2))
        self.add_bezier('p5-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p5-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p5-r1-5', (12, 17), (2, 17))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
        self.add_line('p6-r1-1', (12, 17), (22, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p5-r1-4', 'p6-r1-1')
        self.relate("connect", 'p5-r1-5', 'p6-r1-1')
