"""Independent 32px profile of text-jpg-image-file-format-9b773d14.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '9b773d14-9d90-491b-9303-5f391fe84672'
SOURCE_PATH = 'icon_set/dist/text32/text-jpg-image-file-format-9b773d14.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9b773d14-9d90-491b-9303-5f391fe84672', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/jpg (text)_9b773d14-9d90-491b-9303-5f391fe84672.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-jpg-image-file-format-9b773d14',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-j-uppercase', 'letter-p-uppercase', 'letter-g-uppercase')
REFERENCE_EXPORT_SHA256 = '3fdface11821d3ae05ba4ff0b7660e3ce8d28dc7937b4453abafd30b8d8dcb49'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-jpg-image-file-format-9b773d14-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 68.00000000000009, 20.0)

    def build(self):
        """Source-native uppercase composition for 'JPG'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (4, 13.4286), ((4, 16.5714), (6.68629, 18), (10, 18)))
        self.add_bezier('p1-r1-2', (10, 18), ((13.3137, 18), (16, 16.5714), (16, 13.6918)))
        self.add_line('p1-r1-3', (16, 13.6918), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
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
        self.add_bezier('p3-r1-1', (62.8699, 3.51954), ((61.5334, 2.56364), (59.8896, 2), (58.1123, 2)))
        self.add_bezier('p3-r1-2', (58.1123, 2), ((53.63199, 2), (50, 5.58172), (50, 10)))
        self.add_bezier('p3-r1-3', (50, 10), ((50, 14.4183), (53.63199, 18), (58.1123, 18)))
        self.add_bezier('p3-r1-4', (58.1123, 18), ((62.373599999999996, 18), (65.6686, 14.5166), (66, 10.3983)))
        self.add_line('p3-r1-5', (66, 10.3983), (59.9716, 10.3983))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
