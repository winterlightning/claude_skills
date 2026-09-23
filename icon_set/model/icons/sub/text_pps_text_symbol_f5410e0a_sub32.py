"""Independent 32px profile of text-pps-text-symbol-f5410e0a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'f5410e0a-813c-4c0c-91f2-64440bd59127'
SOURCE_PATH = 'icon_set/dist/text32/text-pps-text-symbol-f5410e0a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f5410e0a-813c-4c0c-91f2-64440bd59127', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/pps (text)_f5410e0a-813c-4c0c-91f2-64440bd59127.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-pps-text-symbol-f5410e0a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-p-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = 'de8936a3c872801ceec7f79ca62bb0f6c00d172a0b158bca090098b604e153e8'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-pps-text-symbol-f5410e0a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.28564, 0.0, 66.0000075398524, 20.000000000000004)

    def build(self):
        """Source-native uppercase composition for 'PPS'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (4.28564, 18), (4.29181, 10.5774))
        self.add_line('p1-r1-2', (4.29181, 10.5774), (4.29893, 2))
        self.add_line('p1-r1-3', (4.29893, 2), (9.64904, 2.00753))
        self.add_bezier('p1-r1-4', (9.64904, 2.00753), ((10.1077, 2.01958), (10.5409, 2.041), (10.9487, 2.07179)))
        self.add_bezier('p1-r1-5', (10.9487, 2.07179), ((11.3851, 2.12879), (11.8111, 2.2219), (12.2867, 2.36449)))
        self.add_bezier('p1-r1-6', (12.2867, 2.36449), ((12.7801, 2.55852), (13.2043, 2.77015), (13.637, 3.0401)))
        self.add_bezier('p1-r1-7', (13.637, 3.0401), ((13.9679, 3.29449), (14.3021, 3.61272), (14.5893, 3.96211)))
        self.add_bezier('p1-r1-8', (14.5893, 3.96211), ((14.766, 4.23631), (14.9471, 4.62258), (15.0976, 5.05178)))
        self.add_bezier('p1-r1-9', (15.0976, 5.05178), ((15.2028, 5.48466), (15.2638, 5.8952), (15.2856, 6.34185)))
        self.add_bezier('p1-r1-10', (15.2856, 6.34185), ((15.2604, 6.79677), (15.1877, 7.24165), (15.0685, 7.66639)))
        self.add_bezier('p1-r1-11', (15.0685, 7.66639), ((14.8847, 8.10903), (14.6866, 8.46208), (14.4339, 8.81466)))
        self.add_bezier('p1-r1-12', (14.4339, 8.81466), ((14.1451, 9.12857), (13.7742, 9.45307), (13.4258, 9.69745)))
        self.add_bezier('p1-r1-13', (13.4258, 9.69745), ((13.0394, 9.91626), (12.6062, 10.1115), (12.1306, 10.2789)))
        self.add_bezier('p1-r1-14', (12.1306, 10.2789), ((11.6242, 10.4123), (11.258, 10.5774), (10.5219, 10.5774)))
        self.add_bezier('p1-r1-15', (10.5219, 10.5774), ((9.78573, 10.5774), (4.29181, 10.5774), (4.29181, 10.5774)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', closed=False)
        self.add_line('p2-r1-1', (28.28564, 18), (28.291809999999998, 10.5774))
        self.add_line('p2-r1-2', (28.291809999999998, 10.5774), (28.29893, 2))
        self.add_line('p2-r1-3', (28.29893, 2), (33.64904, 2.00753))
        self.add_bezier('p2-r1-4', (33.64904, 2.00753), ((34.1077, 2.01958), (34.5409, 2.041), (34.9487, 2.07179)))
        self.add_bezier('p2-r1-5', (34.9487, 2.07179), ((35.3851, 2.12879), (35.811099999999996, 2.2219), (36.286699999999996, 2.36449)))
        self.add_bezier('p2-r1-6', (36.286699999999996, 2.36449), ((36.7801, 2.55852), (37.2043, 2.77015), (37.637, 3.0401)))
        self.add_bezier('p2-r1-7', (37.637, 3.0401), ((37.9679, 3.29449), (38.302099999999996, 3.61272), (38.5893, 3.96211)))
        self.add_bezier('p2-r1-8', (38.5893, 3.96211), ((38.766, 4.23631), (38.9471, 4.62258), (39.0976, 5.05178)))
        self.add_bezier('p2-r1-9', (39.0976, 5.05178), ((39.202799999999996, 5.48466), (39.2638, 5.8952), (39.2856, 6.34185)))
        self.add_bezier('p2-r1-10', (39.2856, 6.34185), ((39.260400000000004, 6.79677), (39.1877, 7.24165), (39.0685, 7.66639)))
        self.add_bezier('p2-r1-11', (39.0685, 7.66639), ((38.8847, 8.10903), (38.6866, 8.46208), (38.4339, 8.81466)))
        self.add_bezier('p2-r1-12', (38.4339, 8.81466), ((38.1451, 9.12857), (37.7742, 9.45307), (37.4258, 9.69745)))
        self.add_bezier('p2-r1-13', (37.4258, 9.69745), ((37.0394, 9.91626), (36.6062, 10.1115), (36.1306, 10.2789)))
        self.add_bezier('p2-r1-14', (36.1306, 10.2789), ((35.6242, 10.4123), (35.257999999999996, 10.5774), (34.5219, 10.5774)))
        self.add_bezier('p2-r1-15', (34.5219, 10.5774), ((33.78573, 10.5774), (28.291809999999998, 10.5774), (28.291809999999998, 10.5774)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', 'p2-r1-12', 'p2-r1-13', 'p2-r1-14', 'p2-r1-15', closed=False)
        self.add_line('p3-r1-1', (63.9314, 2), (56.77906, 2))
        self.add_bezier('p3-r1-2', (56.77906, 2), ((51.70172, 2), (50.21029, 7.42857), (54.98284, 9.42857)))
        self.add_line('p3-r1-3', (54.98284, 9.42857), (61.4623, 11.608))
        self.add_bezier('p3-r1-4', (61.4623, 11.608), ((65.7211, 13.4286), (64.2526, 18), (59.7787, 18)))
        self.add_line('p3-r1-5', (59.7787, 18), (52, 18))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
