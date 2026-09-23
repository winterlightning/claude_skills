"""Independent 32px profile of text-sale-typography-label-5aa2cae3.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '5aa2cae3-ce6d-4cd7-92d4-a010f71d4238'
SOURCE_PATH = 'icon_set/dist/text32/text-sale-typography-label-5aa2cae3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5aa2cae3-ce6d-4cd7-92d4-a010f71d4238', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/sale (text)_5aa2cae3-ce6d-4cd7-92d4-a010f71d4238.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-sale-typography-label-5aa2cae3',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-a-uppercase', 'letter-l-uppercase', 'letter-e-uppercase')
REFERENCE_EXPORT_SHA256 = '3f210b9ff55bf06a6929a1b9caa6c5e2080923d708824f27a4c3e77b589fa155'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-sale-typography-label-5aa2cae3-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 92
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 90.0, 20.000000000000004)

    def build(self):
        """Source-native uppercase composition for 'SALE'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (15.9314, 2), (8.77906, 2))
        self.add_bezier('p1-r1-2', (8.77906, 2), ((3.70172, 2), (2.21029, 7.42857), (6.98284, 9.42857)))
        self.add_line('p1-r1-3', (6.98284, 9.42857), (13.4623, 11.608))
        self.add_bezier('p1-r1-4', (13.4623, 11.608), ((17.7211, 13.4286), (16.2526, 18), (11.7787, 18)))
        self.add_line('p1-r1-5', (11.7787, 18), (4, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_bezier('p2-r1-1', (28, 18), ((28, 18), (29.26667, 2), (34.1333, 2)))
        self.add_bezier('p2-r1-2', (34.1333, 2), ((39, 2), (40, 18), (40, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p2-r2-1', (28.49782, 13.9921), (39.5709, 14.0032))
        self.add_contour('path-2-2', 'p2-r2-1', closed=False)
        self.add_bezier('p3-r1-1', (63, 18), ((59.9428, 18), (52.23973, 18), (52, 18)))
        self.add_line('p3-r1-2', (52, 18), (52, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (88, 17.9999), (76.26183, 18))
        self.add_bezier('p4-r1-2', (76.26183, 18), ((76.11723, 18), (76, 17.8828), (76, 17.7382)))
        self.add_line('p4-r1-3', (76, 17.7382), (76, 9.98924))
        self.add_line('p4-r1-4', (76, 9.98924), (76, 2.01314))
        self.add_line('p4-r1-5', (76, 2.01314), (88, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (84.4, 10), (76, 10))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'path-4-1', 'path-5-1')
