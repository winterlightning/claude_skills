"""Independent 32px profile of side-text-bfdb8de9.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'bfdb8de9-05a8-4a32-a4cf-47cecb08dfc0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/text32/side-text-bfdb8de9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bfdb8de9-05a8-4a32-a4cf-47cecb08dfc0', 'icon_set/dist/gallery/combination-originals/bfdb8de9-05a8-4a32-a4cf-47cecb08dfc0.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-bfdb8de9',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'ecffe1ed2f8f656c3322c409cc2a94b2e3e17dd1ab9092606cec7857b39c0dda'

TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-c-uppercase', 'letter-p-uppercase', 'letter-a-uppercase')
























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class DrawingVariant2(TextSub32):
    icon_id = 'side-text-bfdb8de9-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 92
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 90.00000000000004, 20.0)

    def build(self):
        """Source-native uppercase composition for 'CCPA'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (16, 2.6879), ((14.9406, 2.24575), (13.7674, 2), (12.533, 2)))
        self.add_bezier('p1-r1-2', (12.533, 2), ((7.82037, 2), (4, 5.58172), (4, 10)))
        self.add_bezier('p1-r1-3', (4, 10), ((4, 14.4183), (7.82037, 18), (12.533, 18)))
        self.add_bezier('p1-r1-4', (12.533, 18), ((13.7674, 18), (14.9406, 17.7543), (16, 17.3121)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (40, 2.6879), ((38.9406, 2.24575), (37.7674, 2), (36.533, 2)))
        self.add_bezier('p2-r1-2', (36.533, 2), ((31.82037, 2), (28, 5.58172), (28, 10)))
        self.add_bezier('p2-r1-3', (28, 10), ((28, 14.4183), (31.82037, 18), (36.533, 18)))
        self.add_bezier('p2-r1-4', (36.533, 18), ((37.7674, 18), (38.9406, 17.7543), (40, 17.3121)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
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
        self.add_bezier('p4-r1-1', (76, 18), ((76, 18), (77.26667, 2), (82.1333, 2)))
        self.add_bezier('p4-r1-2', (82.1333, 2), ((87, 2), (88, 18), (88, 18)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p4-r2-1', (76.49782, 13.9921), (87.5709, 14.0032))
        self.add_contour('path-4-2', 'p4-r2-1', closed=False)
