"""Independent 32px profile of text-eight-kilometers-distance-indicator-d043ba47.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'd043ba47-ff65-403b-bbfb-e7d0fb874430'
SOURCE_PATH = 'icon_set/dist/text32/text-eight-kilometers-distance-indicator-d043ba47.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d043ba47-ff65-403b-bbfb-e7d0fb874430', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/8 km_d043ba47-ff65-403b-bbfb-e7d0fb874430.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-eight-kilometers-distance-indicator-d043ba47',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-8', 'letter-k-uppercase', 'letter-m-uppercase')
REFERENCE_EXPORT_SHA256 = 'bae4f96862f21f201dea0b4cb808217d091faf58e7ae944461a4957c73e2296f'

class Drawing(TextSub32):
    icon_id = 'text-eight-kilometers-distance-indicator-d043ba47-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 101
    text_ink_bounds = (0.0, 0.0, 101.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (72, 30), (72, 2))
        self.add_line('p1-r1-2', (72, 2), (85, 20))
        self.add_line('p1-r1-3', (85, 20), (99, 2))
        self.add_line('p1-r1-4', (99, 2), (99, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (42, 2), (42, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (62, 2), (42, 17))
        self.add_line('p3-r1-2', (42, 17), (62, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_bezier('p4-r1-1', (3, 9), ((3, 5), (6, 2), (10, 2)))
        self.add_line('p4-r1-2', (10, 2), (14, 2))
        self.add_bezier('p4-r1-3', (14, 2), ((17, 2), (20, 5), (20, 9)))
        self.add_bezier('p4-r1-4', (20, 9), ((20, 12), (17, 15), (14, 15)))
        self.add_line('p4-r1-5', (14, 15), (10, 15))
        self.add_bezier('p4-r1-6', (10, 15), ((6, 15), (3, 12), (3, 9)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', closed=False)
        self.add_bezier('p5-r1-1', (2, 23), ((2, 19), (5, 15), (9, 15)))
        self.add_line('p5-r1-2', (9, 15), (14, 15))
        self.add_bezier('p5-r1-3', (14, 15), ((18, 15), (21, 19), (21, 23)))
        self.add_bezier('p5-r1-4', (21, 23), ((21, 27), (18, 30), (14, 30)))
        self.add_line('p5-r1-5', (14, 30), (9, 30))
        self.add_bezier('p5-r1-6', (9, 30), ((5, 30), (2, 27), (2, 23)))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', 'p5-r1-6', closed=False)
        self.relate("connect", 'p4-r1-4', 'p5-r1-2')
        self.relate("connect", 'p4-r1-4', 'p5-r1-3')
        self.relate("connect", 'p4-r1-5', 'p5-r1-2')
        self.relate("connect", 'p4-r1-5', 'p5-r1-3')
