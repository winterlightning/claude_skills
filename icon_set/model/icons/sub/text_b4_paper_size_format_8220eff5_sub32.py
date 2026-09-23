"""V2 typeface composition for B4 Paper Size Format."""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '8220eff5-889a-4ed4-abe8-9cb5b3c749d9'
SOURCE_PATH = 'published/gallery/combination-originals/8220eff5-889a-4ed4-abe8-9cb5b3c749d9.svg'
AUTHOR = 'codex'
SOURCE_REFERENCES = (('8220eff5-889a-4ed4-abe8-9cb5b3c749d9', 'published/gallery/combination-originals/8220eff5-889a-4ed4-abe8-9cb5b3c749d9.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-8220eff5',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-b-uppercase', 'digit-4')


REFERENCE_EXPORT_SHA256 = '467e8f7a625b43d5725915af9b6b26618661453b3fc9108c3e4c9f009925fdec'




























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-b4-paper-size-format-8220eff5-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 44
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 42.0, 20.0001)

    def build(self):
        """Source-native uppercase composition for 'B4'; 4-unit letter spacing."""
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
        self.add_line('p3-r1-1', (40, 12.8572), (28.40861, 12.8572))
        self.add_bezier('p3-r1-2', (28.40861, 12.8572), ((28.18045, 12.8572), (27.81423, 12.5715), (28.11142, 12.2858)))
        self.add_line('p3-r1-3', (28.11142, 12.2858), (37.622299999999996, 2.00009))
        self.add_line('p3-r1-4', (37.622299999999996, 2.00009), (37.622299999999996, 18.0001))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
