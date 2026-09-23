"""Independent 32px profile of text-capital-letters-p-and-l-e5930783.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'e5930783-e58a-4a2c-8abe-dffea8e85cfe'
SOURCE_PATH = 'icon_set/dist/text32/text-capital-letters-p-and-l-e5930783.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e5930783-e58a-4a2c-8abe-dffea8e85cfe', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/pl (text)_e5930783-e58a-4a2c-8abe-dffea8e85cfe.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-capital-letters-p-and-l-e5930783',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-l-uppercase')
REFERENCE_EXPORT_SHA256 = 'e7430d8b6f72fca07c0ae595573b3b84fea7d925d11e7814f8702a4114e0e365'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-capital-letters-p-and-l-e5930783-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 44
    text_canvas_height = 20
    text_ink_bounds = (2.28564, 0.0, 41.0, 20.0)

    def build(self):
        """Source-native uppercase composition for 'PL'; 4-unit letter spacing."""
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
        self.add_bezier('p2-r1-1', (39, 18), ((35.9428, 18), (28.23973, 18), (28, 18)))
        self.add_line('p2-r1-2', (28, 18), (28, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
