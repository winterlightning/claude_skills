"""Independent 32px profile of side-text-cc92659e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'cc92659e-8528-43c1-b8cd-489fe1f8785e'
SOURCE_PATH = 'icon_set/dist/text32/side-text-cc92659e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cc92659e-8528-43c1-b8cd-489fe1f8785e', 'icon_set/dist/gallery/combination-originals/cc92659e-8528-43c1-b8cd-489fe1f8785e.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-cc92659e',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'digit-3')
REFERENCE_EXPORT_SHA256 = 'e296819595145e337bc73ac4ede6fb8e9384ee5647971f256ba7e10ad5245696'


































TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'side-text-cc92659e-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 44
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 42.0, 20.0)

    def build(self):
        """Source-native uppercase composition for 'A3'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (4, 18), ((4, 18), (5.26667, 2), (10.1333, 2)))
        self.add_bezier('p1-r1-2', (10.1333, 2), ((15, 2), (16, 18), (16, 18)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p1-r2-1', (4.49782, 13.9921), (15.5709, 14.0032))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
        self.add_line('p2-r1-1', (29.6581, 10.0027), (36.25, 10.0027))
        self.add_bezier('p2-r1-2', (36.25, 10.0027), ((38.3211, 10.0027), (40, 8.32377), (40, 6.2527)))
        self.add_line('p2-r1-3', (40, 6.2527), (40, 5.75))
        self.add_bezier('p2-r1-4', (40, 5.75), ((40, 3.67893), (38.3221, 2), (36.251, 2)))
        self.add_bezier('p2-r1-5', (36.251, 2), ((33.56933, 2), (30.07957, 2), (28, 2)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (29.6581, 9.99733), (36.25, 9.99733))
        self.add_bezier('p3-r1-2', (36.25, 9.99733), ((38.3211, 9.99733), (40, 11.6763), (40, 13.7473)))
        self.add_line('p3-r1-3', (40, 13.7473), (40, 14.25))
        self.add_bezier('p3-r1-4', (40, 14.25), ((40, 16.3211), (38.3221, 18), (36.251, 18)))
        self.add_bezier('p3-r1-5', (36.251, 18), ((33.56933, 18), (30.07957, 18), (28, 18)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.relate("connect", 'path-2-1', 'path-3-1')
