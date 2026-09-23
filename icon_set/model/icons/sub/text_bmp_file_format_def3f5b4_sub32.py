"""Independent 32px profile of text-bmp-file-format-def3f5b4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'def3f5b4-965a-491a-aafa-f539a425bff2'
SOURCE_PATH = 'icon_set/dist/text32/text-bmp-file-format-def3f5b4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('def3f5b4-965a-491a-aafa-f539a425bff2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/bmp (text)_def3f5b4-965a-491a-aafa-f539a425bff2.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-bmp-file-format-def3f5b4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-b-uppercase', 'letter-m-uppercase', 'letter-p-uppercase')
REFERENCE_EXPORT_SHA256 = '8e3a0a6d9bc6888008de710a5622c9b40425c934c396e05d862dbe85cbcbcf7e'































TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-bmp-file-format-def3f5b4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, -1.9539862061712654e-06, 65.2856, 20.000000000000007)

    def build(self):
        """Source-native uppercase composition for 'BMP'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (4, 2), (10.1362, 2))
        self.add_bezier('p1-r1-2', (10.1362, 2), ((12.3453, 2), (14.1362, 3.79086), (14.1362, 6)))
        self.add_bezier('p1-r1-3', (14.1362, 6), ((14.1362, 8.20914), (12.3453, 10), (10.1362, 10)))
        self.add_line('p1-r1-4', (10.1362, 10), (4, 10))
        self.add_line('p1-r1-5', (4, 10), (4, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (4, 10.0101), (12.005, 10.0101))
        self.add_bezier('p2-r1-2', (12.005, 10.0101), ((14.2114, 10.0101), (16, 11.7987), (16, 14.005)))
        self.add_bezier('p2-r1-3', (16, 14.005), ((16, 16.2114), (14.2114, 18), (12.005, 18)))
        self.add_line('p2-r1-4', (12.005, 18), (4, 18))
        self.add_line('p2-r1-5', (4, 18), (4, 10.0101))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (26, 18), (26, 2.4248))
        self.add_bezier('p3-r1-2', (26, 2.4248), ((26, 2.01632), (26.53474, 1.84408), (26.78474, 2.17204)))
        self.add_line('p3-r1-3', (26.78474, 2.17204), (33.65053, 11.1787))
        self.add_bezier('p3-r1-4', (33.65053, 11.1787), ((33.82456, 11.407), (34.175399999999996, 11.407), (34.3495, 11.1787)))
        self.add_line('p3-r1-5', (34.3495, 11.1787), (41.2153, 2.17204))
        self.add_bezier('p3-r1-6', (41.2153, 2.17204), ((41.4653, 1.84408), (42, 2.01632), (42, 2.4248)))
        self.add_line('p3-r1-7', (42, 2.4248), (42, 18))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
        self.add_line('p4-r1-1', (52.28564, 18), (52.29181, 10.5774))
        self.add_line('p4-r1-2', (52.29181, 10.5774), (52.29893, 2))
        self.add_line('p4-r1-3', (52.29893, 2), (57.64904, 2.00753))
        self.add_bezier('p4-r1-4', (57.64904, 2.00753), ((58.1077, 2.01958), (58.5409, 2.041), (58.9487, 2.07179)))
        self.add_bezier('p4-r1-5', (58.9487, 2.07179), ((59.3851, 2.12879), (59.811099999999996, 2.2219), (60.286699999999996, 2.36449)))
        self.add_bezier('p4-r1-6', (60.286699999999996, 2.36449), ((60.7801, 2.55852), (61.2043, 2.77015), (61.637, 3.0401)))
        self.add_bezier('p4-r1-7', (61.637, 3.0401), ((61.9679, 3.29449), (62.302099999999996, 3.61272), (62.5893, 3.96211)))
        self.add_bezier('p4-r1-8', (62.5893, 3.96211), ((62.766, 4.23631), (62.9471, 4.62258), (63.0976, 5.05178)))
        self.add_bezier('p4-r1-9', (63.0976, 5.05178), ((63.202799999999996, 5.48466), (63.2638, 5.8952), (63.2856, 6.34185)))
        self.add_bezier('p4-r1-10', (63.2856, 6.34185), ((63.260400000000004, 6.79677), (63.1877, 7.24165), (63.0685, 7.66639)))
        self.add_bezier('p4-r1-11', (63.0685, 7.66639), ((62.8847, 8.10903), (62.6866, 8.46208), (62.4339, 8.81466)))
        self.add_bezier('p4-r1-12', (62.4339, 8.81466), ((62.1451, 9.12857), (61.7742, 9.45307), (61.4258, 9.69745)))
        self.add_bezier('p4-r1-13', (61.4258, 9.69745), ((61.0394, 9.91626), (60.6062, 10.1115), (60.1306, 10.2789)))
        self.add_bezier('p4-r1-14', (60.1306, 10.2789), ((59.6242, 10.4123), (59.257999999999996, 10.5774), (58.5219, 10.5774)))
        self.add_bezier('p4-r1-15', (58.5219, 10.5774), ((57.78573, 10.5774), (52.29181, 10.5774), (52.29181, 10.5774)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', 'p4-r1-8', 'p4-r1-9', 'p4-r1-10', 'p4-r1-11', 'p4-r1-12', 'p4-r1-13', 'p4-r1-14', 'p4-r1-15', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
