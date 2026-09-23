"""Independent 32px profile of text-three-dimensional-view-symbol-bb238e45.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'bb238e45-d5b9-4df3-ac32-6ad48db5fac4'
SOURCE_PATH = 'icon_set/dist/text32/text-three-dimensional-view-symbol-bb238e45.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bb238e45-d5b9-4df3-ac32-6ad48db5fac4', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/3D (text)_bb238e45-d5b9-4df3-ac32-6ad48db5fac4.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-three-dimensional-view-symbol-bb238e45',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-3', 'letter-d-uppercase')
REFERENCE_EXPORT_SHA256 = '40e8a4930e92c1d413291e7a7cb884f62578d05c6fd4b2d051fa3442839186e4'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-three-dimensional-view-symbol-bb238e45-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 44
    text_canvas_height = 20
    text_ink_bounds = (2.0000000000000053, 0.0, 42.000000000000014, 20.0)

    def build(self):
        """Source-native uppercase composition for '3D'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (5.6581, 10.0027), (12.25, 10.0027))
        self.add_bezier('p1-r1-2', (12.25, 10.0027), ((14.3211, 10.0027), (16, 8.32377), (16, 6.2527)))
        self.add_line('p1-r1-3', (16, 6.2527), (16, 5.75))
        self.add_bezier('p1-r1-4', (16, 5.75), ((16, 3.67893), (14.3221, 2), (12.251, 2)))
        self.add_bezier('p1-r1-5', (12.251, 2), ((9.56933, 2), (6.07957, 2), (4, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (5.6581, 9.99733), (12.25, 9.99733))
        self.add_bezier('p2-r1-2', (12.25, 9.99733), ((14.3211, 9.99733), (16, 11.6763), (16, 13.7473)))
        self.add_line('p2-r1-3', (16, 13.7473), (16, 14.25))
        self.add_bezier('p2-r1-4', (16, 14.25), ((16, 16.3211), (14.3221, 18), (12.251, 18)))
        self.add_bezier('p2-r1-5', (12.251, 18), ((9.56933, 18), (6.07957, 18), (4, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (28, 2), (32.88681, 2))
        self.add_bezier('p3-r1-2', (32.88681, 2), ((36.8153, 2), (40, 5.58172), (40, 10)))
        self.add_bezier('p3-r1-3', (40, 10), ((40, 14.4183), (36.8153, 18), (32.88681, 18)))
        self.add_line('p3-r1-4', (32.88681, 18), (28, 18))
        self.add_line('p3-r1-5', (28, 18), (28, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
