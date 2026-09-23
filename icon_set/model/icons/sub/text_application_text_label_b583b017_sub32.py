"""Independent 32px profile of text-application-text-label-b583b017.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'b583b017-1004-447b-b65e-c7c25b920a81'
SOURCE_PATH = 'icon_set/dist/text32/text-application-text-label-b583b017.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b583b017-1004-447b-b65e-c7c25b920a81', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/app (text)_b583b017-1004-447b-b65e-c7c25b920a81.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-application-text-label-b583b017',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-p-uppercase', 'letter-p-uppercase')
REFERENCE_EXPORT_SHA256 = 'eda7f8181a186732e59cd28aec2dfea8f2cd57071d72e4b0d246dbc89146c579'































TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-application-text-label-b583b017-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 65.2856, 20.0)

    def build(self):
        """Source-native uppercase composition for 'APP'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (4, 18), ((4, 18), (5.26667, 2), (10.1333, 2)))
        self.add_bezier('p1-r1-2', (10.1333, 2), ((15, 2), (16, 18), (16, 18)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p1-r2-1', (4.49782, 13.9921), (15.5709, 14.0032))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
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
