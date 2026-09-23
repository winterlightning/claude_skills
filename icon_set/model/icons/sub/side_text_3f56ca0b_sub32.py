"""Independent 32px profile of side-text-3f56ca0b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '3f56ca0b-8416-402d-aabd-eff420b147d9'
SOURCE_PATH = 'icon_set/dist/text32/side-text-3f56ca0b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3f56ca0b-8416-402d-aabd-eff420b147d9', 'icon_set/dist/gallery/combination-originals/3f56ca0b-8416-402d-aabd-eff420b147d9.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-3f56ca0b',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-3', 'letter-d-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = '9c45702055ac1889aa1603544ffcc1050a961b0ec0775c9c5b0a9f68e38eba43'


































TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'side-text-3f56ca0b-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0000000000000053, 0.0, 66.0000075398524, 20.000000000000004)

    def build(self):
        """Source-native uppercase composition for '3DS'; 4-unit letter spacing."""
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
        self.add_line('p4-r1-1', (63.9314, 2), (56.77906, 2))
        self.add_bezier('p4-r1-2', (56.77906, 2), ((51.70172, 2), (50.21029, 7.42857), (54.98284, 9.42857)))
        self.add_line('p4-r1-3', (54.98284, 9.42857), (61.4623, 11.608))
        self.add_bezier('p4-r1-4', (61.4623, 11.608), ((65.7211, 13.4286), (64.2526, 18), (59.7787, 18)))
        self.add_line('p4-r1-5', (59.7787, 18), (52, 18))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
