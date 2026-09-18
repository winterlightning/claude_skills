"""Independent 32px profile of text-share-the-road-typography-4f785d2d.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '4f785d2d-98b6-428f-a76d-5827580c3f0d'
SOURCE_PATH = 'icon_set/dist/text32/text-share-the-road-typography-4f785d2d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4f785d2d-98b6-428f-a76d-5827580c3f0d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/transportation/share the road_4f785d2d-98b6-428f-a76d-5827580c3f0d.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-share-the-road-typography-4f785d2d',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-h-uppercase', 'letter-a-uppercase', 'letter-r-uppercase', 'letter-e-uppercase', 'letter-t-uppercase', 'letter-h-uppercase', 'letter-e-uppercase', 'letter-r-uppercase', 'letter-o-uppercase', 'letter-a-uppercase', 'letter-d-uppercase')
REFERENCE_EXPORT_SHA256 = '1055f70f0c2fa0c0ebcdd51d11550c8f22b7dbc4d1a1554db24bb06720f8be73'

class Drawing(TextSub32):
    icon_id = 'text-share-the-road-typography-4f785d2d-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 378
    text_ink_bounds = (0.0, 0.0, 377.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (356, 2), (364, 2))
        self.add_bezier('p1-r1-2', (364, 2), ((371, 2), (375, 9), (375, 16)))
        self.add_bezier('p1-r1-3', (375, 16), ((375, 23), (371, 30), (364, 30)))
        self.add_line('p1-r1-4', (364, 30), (356, 30))
        self.add_line('p1-r1-5', (356, 30), (356, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (324, 30), (334, 3))
        self.add_bezier('p2-r1-2', (334, 3), ((334, 2.3333333333333335), (334.3333333333333, 2), (335, 2)))
        self.add_bezier('p2-r1-3', (335, 2), ((335, 2), (335.3333333333333, 2.3333333333333335), (336, 3)))
        self.add_line('p2-r1-4', (336, 3), (345, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (328, 18), (341, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (294, 16), ((294, 8), (298, 2), (304, 2)))
        self.add_bezier('p4-r1-2', (304, 2), ((309, 2), (314, 8), (314, 16)))
        self.add_bezier('p4-r1-3', (314, 16), ((314, 24), (309, 30), (304, 30)))
        self.add_bezier('p4-r1-4', (304, 30), ((298, 30), (294, 24), (294, 16)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (263, 30), (263, 2))
        self.add_line('p5-r1-2', (263, 2), (273, 2))
        self.add_bezier('p5-r1-3', (273, 2), ((279, 2), (282, 6), (282, 9)))
        self.add_bezier('p5-r1-4', (282, 9), ((282, 13), (279, 17), (273, 17)))
        self.add_line('p5-r1-5', (273, 17), (263, 17))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
        self.add_line('p6-r1-1', (273, 17), (283, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (242, 2), (225, 2))
        self.add_line('p7-r1-2', (225, 2), (225, 30))
        self.add_line('p7-r1-3', (225, 30), (242, 30))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', closed=False)
        self.add_line('p8-r1-1', (225, 16), (239, 16))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (194, 2), (194, 30))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.add_line('p10-r1-1', (214, 2), (214, 30))
        self.add_contour('path-10-1', 'p10-r1-1', closed=False)
        self.add_line('p11-r1-1', (194, 16), (214, 16))
        self.add_contour('path-11-1', 'p11-r1-1', closed=False)
        self.add_line('p12-r1-1', (162, 2), (184, 2))
        self.add_contour('path-12-1', 'p12-r1-1', closed=False)
        self.add_line('p13-r1-1', (173, 2), (173, 30))
        self.add_contour('path-13-1', 'p13-r1-1', closed=False)
        self.add_line('p14-r1-1', (141, 2), (124, 2))
        self.add_line('p14-r1-2', (124, 2), (124, 30))
        self.add_line('p14-r1-3', (124, 30), (141, 30))
        self.add_contour('path-14-1', 'p14-r1-1', 'p14-r1-2', 'p14-r1-3', closed=False)
        self.add_line('p15-r1-1', (124, 16), (138, 16))
        self.add_contour('path-15-1', 'p15-r1-1', closed=False)
        self.add_line('p16-r1-1', (93, 30), (93, 2))
        self.add_line('p16-r1-2', (93, 2), (103, 2))
        self.add_bezier('p16-r1-3', (103, 2), ((109, 2), (112, 6), (112, 9)))
        self.add_bezier('p16-r1-4', (112, 9), ((112, 13), (109, 17), (103, 17)))
        self.add_line('p16-r1-5', (103, 17), (93, 17))
        self.add_contour('path-16-1', 'p16-r1-1', 'p16-r1-2', 'p16-r1-3', 'p16-r1-4', 'p16-r1-5', closed=False)
        self.add_line('p17-r1-1', (103, 17), (113, 30))
        self.add_contour('path-17-1', 'p17-r1-1', closed=False)
        self.add_line('p18-r1-1', (62, 30), (71, 3))
        self.add_bezier('p18-r1-2', (71, 3), ((71, 2.3333333333333335), (71.33333333333333, 2), (72, 2)))
        self.add_bezier('p18-r1-3', (72, 2), ((72.66666666666667, 2), (73, 2.3333333333333335), (73, 3)))
        self.add_line('p18-r1-4', (73, 3), (82, 30))
        self.add_contour('path-18-1', 'p18-r1-1', 'p18-r1-2', 'p18-r1-3', 'p18-r1-4', closed=False)
        self.add_line('p19-r1-1', (66, 18), (78, 18))
        self.add_contour('path-19-1', 'p19-r1-1', closed=False)
        self.add_line('p20-r1-1', (31, 2), (31, 30))
        self.add_contour('path-20-1', 'p20-r1-1', closed=False)
        self.add_line('p21-r1-1', (51, 2), (51, 30))
        self.add_contour('path-21-1', 'p21-r1-1', closed=False)
        self.add_line('p22-r1-1', (31, 16), (51, 16))
        self.add_contour('path-22-1', 'p22-r1-1', closed=False)
        self.add_bezier('p23-r1-1', (20, 6), ((19, 3), (15, 2), (12, 2)))
        self.add_bezier('p23-r1-2', (12, 2), ((8, 2), (4, 4), (3, 9)))
        self.add_bezier('p23-r1-3', (3, 9), ((3, 9), (3, 9), (3, 10)))
        self.add_bezier('p23-r1-4', (3, 10), ((3, 17), (20, 13), (20, 22)))
        self.add_bezier('p23-r1-5', (20, 22), ((20, 22), (20, 22), (20, 23)))
        self.add_bezier('p23-r1-6', (20, 23), ((20, 28), (16, 30), (11, 30)))
        self.add_bezier('p23-r1-7', (11, 30), ((7, 30), (4, 29), (2, 26)))
        self.add_contour('path-23-1', 'p23-r1-1', 'p23-r1-2', 'p23-r1-3', 'p23-r1-4', 'p23-r1-5', 'p23-r1-6', 'p23-r1-7', closed=False)
        self.relate('connect', 'p5-r1-4', 'p6-r1-1')
        self.relate('connect', 'p5-r1-5', 'p6-r1-1')
        self.relate('connect', 'p16-r1-4', 'p17-r1-1')
        self.relate('connect', 'p16-r1-5', 'p17-r1-1')
