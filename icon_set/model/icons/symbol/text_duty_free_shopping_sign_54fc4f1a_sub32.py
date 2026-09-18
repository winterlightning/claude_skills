"""Independent 32px profile of text-duty-free-shopping-sign-54fc4f1a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '54fc4f1a-7325-4e19-8437-20f3f20e25b0'
SOURCE_PATH = 'icon_set/dist/text32/text-duty-free-shopping-sign-54fc4f1a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('54fc4f1a-7325-4e19-8437-20f3f20e25b0', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/duty free (text)_54fc4f1a-7325-4e19-8437-20f3f20e25b0.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-duty-free-shopping-sign-54fc4f1a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-d-uppercase', 'letter-u-uppercase', 'letter-t-uppercase', 'letter-y-uppercase', 'letter-f-uppercase', 'letter-r-uppercase', 'letter-e-uppercase', 'letter-e-uppercase')
REFERENCE_EXPORT_SHA256 = 'db7912a0921ac52cdfa72faace67c4fab88fb2c078b1553d68072d06d1ecf303'

class Drawing(TextSub32):
    icon_id = 'text-duty-free-shopping-sign-54fc4f1a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 243
    text_ink_bounds = (0.0, 0.0, 242.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (240, 2), (223, 2))
        self.add_line('p1-r1-2', (223, 2), (223, 30))
        self.add_line('p1-r1-3', (223, 30), (240, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (223, 16), (237, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (213, 2), (196, 2))
        self.add_line('p3-r1-2', (196, 2), (196, 30))
        self.add_line('p3-r1-3', (196, 30), (213, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (196, 16), (210, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (165, 30), (165, 2))
        self.add_line('p5-r1-2', (165, 2), (175, 2))
        self.add_bezier('p5-r1-3', (175, 2), ((181, 2), (184, 6), (184, 9)))
        self.add_bezier('p5-r1-4', (184, 9), ((184, 13), (181, 17), (175, 17)))
        self.add_line('p5-r1-5', (175, 17), (165, 17))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
        self.add_line('p6-r1-1', (175, 17), (185, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (155, 2), (137, 2))
        self.add_line('p7-r1-2', (137, 2), (137, 30))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', closed=False)
        self.add_line('p8-r1-1', (137, 16), (151, 16))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (95, 2), (105, 17))
        self.add_line('p9-r1-2', (105, 17), (116, 2))
        self.add_contour('path-9-1', 'p9-r1-1', 'p9-r1-2', closed=False)
        self.add_line('p10-r1-1', (105, 17), (105, 30))
        self.add_contour('path-10-1', 'p10-r1-1', closed=False)
        self.add_line('p11-r1-1', (62, 2), (84, 2))
        self.add_contour('path-11-1', 'p11-r1-1', closed=False)
        self.add_line('p12-r1-1', (73, 2), (73, 30))
        self.add_contour('path-12-1', 'p12-r1-1', closed=False)
        self.add_line('p13-r1-1', (32, 2), (32, 20))
        self.add_bezier('p13-r1-2', (32, 20), ((32, 27), (37, 30), (42, 30)))
        self.add_bezier('p13-r1-3', (42, 30), ((47, 30), (52, 27), (52, 20)))
        self.add_line('p13-r1-4', (52, 20), (52, 2))
        self.add_contour('path-13-1', 'p13-r1-1', 'p13-r1-2', 'p13-r1-3', 'p13-r1-4', closed=False)
        self.add_line('p14-r1-1', (2, 2), (10, 2))
        self.add_bezier('p14-r1-2', (10, 2), ((18, 2), (21, 9), (21, 16)))
        self.add_bezier('p14-r1-3', (21, 16), ((21, 23), (18, 30), (10, 30)))
        self.add_line('p14-r1-4', (10, 30), (2, 30))
        self.add_line('p14-r1-5', (2, 30), (2, 2))
        self.add_contour('path-14-1', 'p14-r1-1', 'p14-r1-2', 'p14-r1-3', 'p14-r1-4', 'p14-r1-5', closed=False)
        self.relate('connect', 'p5-r1-4', 'p6-r1-1')
        self.relate('connect', 'p5-r1-5', 'p6-r1-1')
        self.relate('connect', 'p9-r1-1', 'p10-r1-1')
        self.relate('connect', 'p9-r1-2', 'p10-r1-1')
