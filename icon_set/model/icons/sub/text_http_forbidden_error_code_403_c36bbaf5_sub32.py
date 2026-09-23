"""V2 typeface composition for HTTP Forbidden Error Code 403."""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'c36bbaf5-0df9-4ef9-b526-038bb89856ec'
SOURCE_PATH = 'published/gallery/combination-originals/c36bbaf5-0df9-4ef9-b526-038bb89856ec.svg'
AUTHOR = 'codex'
SOURCE_REFERENCES = (('c36bbaf5-0df9-4ef9-b526-038bb89856ec', 'published/gallery/combination-originals/c36bbaf5-0df9-4ef9-b526-038bb89856ec.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-c36bbaf5',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-4', 'digit-0', 'digit-3')


REFERENCE_EXPORT_SHA256 = '5de97812649fb74935871069199a35f17a34a92ad0336a09f25854e6353f8716'






















TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-http-forbidden-error-code-403-c36bbaf5-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (1.9999969987873927, 0.0, 66.0, 20.0001)

    def build(self):
        """Source-native uppercase composition for '403'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (16, 12.8572), (4.40861, 12.8572))
        self.add_bezier('p1-r1-2', (4.40861, 12.8572), ((4.18045, 12.8572), (3.81423, 12.5715), (4.11142, 12.2858)))
        self.add_line('p1-r1-3', (4.11142, 12.2858), (13.6223, 2.00009))
        self.add_line('p1-r1-4', (13.6223, 2.00009), (13.6223, 18.0001))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (28, 2), (40, 2))
        self.add_line('p2-r1-2', (40, 2), (40, 18))
        self.add_line('p2-r1-3', (40, 18), (28, 18))
        self.add_line('p2-r1-4', (28, 18), (28, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (53.6581, 10.0027), (60.25, 10.0027))
        self.add_bezier('p3-r1-2', (60.25, 10.0027), ((62.3211, 10.0027), (64, 8.32377), (64, 6.2527)))
        self.add_line('p3-r1-3', (64, 6.2527), (64, 5.75))
        self.add_bezier('p3-r1-4', (64, 5.75), ((64, 3.67893), (62.3221, 2), (60.251, 2)))
        self.add_bezier('p3-r1-5', (60.251, 2), ((57.56933, 2), (54.079570000000004, 2), (52, 2)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (53.6581, 9.99733), (60.25, 9.99733))
        self.add_bezier('p4-r1-2', (60.25, 9.99733), ((62.3211, 9.99733), (64, 11.6763), (64, 13.7473)))
        self.add_line('p4-r1-3', (64, 13.7473), (64, 14.25))
        self.add_bezier('p4-r1-4', (64, 14.25), ((64, 16.3211), (62.3221, 18), (60.251, 18)))
        self.add_bezier('p4-r1-5', (60.251, 18), ((57.56933, 18), (54.079570000000004, 18), (52, 18)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.relate("connect", 'path-3-1', 'path-4-1')
