"""Independent 32px profile of text-two-plus-numeric-indicator-f6bca356.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'f6bca356-800d-4c0a-b6aa-c204a6cca58e'
SOURCE_PATH = 'icon_set/dist/text32/text-two-plus-numeric-indicator-f6bca356.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f6bca356-800d-4c0a-b6aa-c204a6cca58e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/2 PLUS (text)_f6bca356-800d-4c0a-b6aa-c204a6cca58e.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-two-plus-numeric-indicator-f6bca356',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-2', 'letter-p-uppercase', 'letter-l-uppercase', 'letter-u-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = '3f6f4078896af63820d3faf907009c8157238d9200d95f52090090ac0c76ca96'

class Drawing(TextSub32):
    icon_id = 'text-two-plus-numeric-indicator-f6bca356-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 140
    text_ink_bounds = (0.0, 0.0, 140.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (137, 6), ((136, 3), (133, 2), (129, 2)))
        self.add_bezier('p1-r1-2', (129, 2), ((125, 2), (121, 4), (120, 9)))
        self.add_bezier('p1-r1-3', (120, 9), ((120, 9), (120, 9), (120, 10)))
        self.add_bezier('p1-r1-4', (120, 10), ((120, 17), (137, 13), (138, 22)))
        self.add_bezier('p1-r1-5', (138, 22), ((138, 22), (138, 22), (138, 23)))
        self.add_bezier('p1-r1-6', (138, 23), ((138, 28), (133, 30), (128, 30)))
        self.add_bezier('p1-r1-7', (128, 30), ((125, 30), (121, 29), (119, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (92, 2), (92, 20))
        self.add_bezier('p2-r1-2', (92, 20), ((92, 27), (96, 30), (101, 30)))
        self.add_bezier('p2-r1-3', (101, 30), ((106, 30), (111, 27), (111, 20)))
        self.add_line('p2-r1-4', (111, 20), (111, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (67, 2), (67, 30))
        self.add_line('p3-r1-2', (67, 30), (84, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (40, 30), (40, 2))
        self.add_line('p4-r1-2', (40, 2), (50, 2))
        self.add_bezier('p4-r1-3', (50, 2), ((56, 2), (59, 6), (59, 9)))
        self.add_bezier('p4-r1-4', (59, 9), ((59, 13), (56, 17), (50, 17)))
        self.add_line('p4-r1-5', (50, 17), (40, 17))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (2, 2), (16, 2))
        self.add_bezier('p5-r1-2', (16, 2), ((19, 2), (21, 5), (21, 8)))
        self.add_bezier('p5-r1-3', (21, 8), ((21, 9), (21, 11), (19, 12)))
        self.add_line('p5-r1-4', (19, 12), (6, 21))
        self.add_bezier('p5-r1-5', (6, 21), ((3, 23), (2, 25), (2, 28)))
        self.add_line('p5-r1-6', (2, 28), (2, 29))
        self.add_bezier('p5-r1-7', (2, 29), ((2, 29), (3, 30), (3, 30)))
        self.add_line('p5-r1-8', (3, 30), (22, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', 'p5-r1-6', 'p5-r1-7', 'p5-r1-8', closed=False)
