"""Independent 32px profile of text-gdpr-data-privacy-text-602db514.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '602db514-f9ff-4dc0-874b-ecc9030684ee'
SOURCE_PATH = 'icon_set/dist/text32/text-gdpr-data-privacy-text-602db514.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('602db514-f9ff-4dc0-874b-ecc9030684ee', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/gdpr (text)_602db514-f9ff-4dc0-874b-ecc9030684ee.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-gdpr-data-privacy-text-602db514',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-g-uppercase', 'letter-d-uppercase', 'letter-p-uppercase', 'letter-r-uppercase')
REFERENCE_EXPORT_SHA256 = '26438886455d9fead2f05386555524816d1aef9c9400afbaceeedc941c393052'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-gdpr-data-privacy-text-602db514-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 92
    text_canvas_height = 20
    text_ink_bounds = (0.0, 0.0, 90.0002, 20.0)

    def build(self):
        """Source-native uppercase composition for 'GDPR'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (14.8699, 3.51954), ((13.5334, 2.56364), (11.8896, 2), (10.1123, 2)))
        self.add_bezier('p1-r1-2', (10.1123, 2), ((5.63199, 2), (2, 5.58172), (2, 10)))
        self.add_bezier('p1-r1-3', (2, 10), ((2, 14.4183), (5.63199, 18), (10.1123, 18)))
        self.add_bezier('p1-r1-4', (10.1123, 18), ((14.3736, 18), (17.6686, 14.5166), (18, 10.3983)))
        self.add_line('p1-r1-5', (18, 10.3983), (11.9716, 10.3983))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (28, 2), (32.88681, 2))
        self.add_bezier('p2-r1-2', (32.88681, 2), ((36.8153, 2), (40, 5.58172), (40, 10)))
        self.add_bezier('p2-r1-3', (40, 10), ((40, 14.4183), (36.8153, 18), (32.88681, 18)))
        self.add_line('p2-r1-4', (32.88681, 18), (28, 18))
        self.add_line('p2-r1-5', (28, 18), (28, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (52.28564, 18), (52.29181, 10.5774))
        self.add_line('p3-r1-2', (52.29181, 10.5774), (52.29893, 2))
        self.add_line('p3-r1-3', (52.29893, 2), (57.64904, 2.00753))
        self.add_bezier('p3-r1-4', (57.64904, 2.00753), ((58.1077, 2.01958), (58.5409, 2.041), (58.9487, 2.07179)))
        self.add_bezier('p3-r1-5', (58.9487, 2.07179), ((59.3851, 2.12879), (59.811099999999996, 2.2219), (60.286699999999996, 2.36449)))
        self.add_bezier('p3-r1-6', (60.286699999999996, 2.36449), ((60.7801, 2.55852), (61.2043, 2.77015), (61.637, 3.0401)))
        self.add_bezier('p3-r1-7', (61.637, 3.0401), ((61.9679, 3.29449), (62.302099999999996, 3.61272), (62.5893, 3.96211)))
        self.add_bezier('p3-r1-8', (62.5893, 3.96211), ((62.766, 4.23631), (62.9471, 4.62258), (63.0976, 5.05178)))
        self.add_bezier('p3-r1-9', (63.0976, 5.05178), ((63.202799999999996, 5.48466), (63.2638, 5.8952), (63.2856, 6.34185)))
        self.add_bezier('p3-r1-10', (63.2856, 6.34185), ((63.260400000000004, 6.79677), (63.1877, 7.24165), (63.0685, 7.66639)))
        self.add_bezier('p3-r1-11', (63.0685, 7.66639), ((62.8847, 8.10903), (62.6866, 8.46208), (62.4339, 8.81466)))
        self.add_bezier('p3-r1-12', (62.4339, 8.81466), ((62.1451, 9.12857), (61.7742, 9.45307), (61.4258, 9.69745)))
        self.add_bezier('p3-r1-13', (61.4258, 9.69745), ((61.0394, 9.91626), (60.6062, 10.1115), (60.1306, 10.2789)))
        self.add_bezier('p3-r1-14', (60.1306, 10.2789), ((59.6242, 10.4123), (59.257999999999996, 10.5774), (58.5219, 10.5774)))
        self.add_bezier('p3-r1-15', (58.5219, 10.5774), ((57.78573, 10.5774), (52.29181, 10.5774), (52.29181, 10.5774)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', 'p3-r1-10', 'p3-r1-11', 'p3-r1-12', 'p3-r1-13', 'p3-r1-14', 'p3-r1-15', closed=False)
        self.add_bezier('p4-r1-1', (82.8873, 10.2597), ((82.9927, 10.2656), (83.7461, 10.2002), (84.1943, 10.1448)))
        self.add_bezier('p4-r1-2', (84.1943, 10.1448), ((84.7739, 10.0215), (85.2364, 9.87383), (85.5786, 9.7323)))
        self.add_bezier('p4-r1-3', (85.5786, 9.7323), ((85.8168, 9.61569), (86.0581, 9.47953), (86.2933, 9.32693)))
        self.add_bezier('p4-r1-4', (86.2933, 9.32693), ((86.5206, 9.15663), (86.7316, 8.97268), (87.0066, 8.68112)))
        self.add_bezier('p4-r1-5', (87.0066, 8.68112), ((87.3006, 8.29491), (87.5148, 7.91654), (87.6705, 7.53332)))
        self.add_bezier('p4-r1-6', (87.6705, 7.53332), ((87.7876, 7.06309), (87.8622, 6.49759), (87.8754, 6.1192)))
        self.add_bezier('p4-r1-7', (87.8754, 6.1192), ((87.8688, 5.74217), (87.8129, 5.17647), (87.7555, 4.89334)))
        self.add_bezier('p4-r1-8', (87.7555, 4.89334), ((87.6735, 4.61016), (87.5144, 4.2323), (87.34440000000001, 3.94479)))
        self.add_bezier('p4-r1-9', (87.34440000000001, 3.94479), ((87.0433, 3.56633), (86.7559, 3.28724), (86.3151, 2.93323)))
        self.add_bezier('p4-r1-10', (86.3151, 2.93323), ((85.9612, 2.70704), (85.6152, 2.5248), (85.1474, 2.32978)))
        self.add_bezier('p4-r1-11', (85.1474, 2.32978), ((84.8004, 2.2177), (84.4606, 2.13329), (84.115, 2.07444)))
        self.add_bezier('p4-r1-12', (84.115, 2.07444), ((83.8881, 2.0514), (83.4301, 2.02658), (82.7396, 2.01318)))
        self.add_line('p4-r1-13', (82.7396, 2.01318), (80.21436, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', 'p4-r1-8', 'p4-r1-9', 'p4-r1-10', 'p4-r1-11', 'p4-r1-12', 'p4-r1-13', closed=False)
        self.add_line('p5-r1-1', (76.00684, 10.2662), (82.8877, 10.2598))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (88.0002, 17.9842), (82.9937, 10.2657))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (80.21543, 2), (76.32855, 2))
        self.add_bezier('p7-r1-2', (76.32855, 2), ((76.1471, 2), (76, 2.1471), (76, 2.32855)))
        self.add_line('p7-r1-3', (76, 2.32855), (76, 18))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', closed=False)
        self.relate("connect", 'path-4-1', 'path-5-1')
        self.relate("connect", 'path-4-1', 'path-6-1')
        self.relate("connect", 'path-4-1', 'path-7-1')
        self.relate("connect", 'path-5-1', 'path-6-1')
        self.relate("connect", 'path-5-1', 'path-7-1')
        self.relate("connect", 'path-6-1', 'path-7-1')
