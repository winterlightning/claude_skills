"""Independent 32px profile of side-text-5d129d3a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '5d129d3a-0cd4-4a54-9809-a0823aa8bd17'
SOURCE_PATH = 'icon_set/dist/text32/side-text-5d129d3a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5d129d3a-0cd4-4a54-9809-a0823aa8bd17', 'icon_set/dist/gallery/combination-originals/5d129d3a-0cd4-4a54-9809-a0823aa8bd17.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-5d129d3a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-f-uppercase', 'letter-a-uppercase', 'letter-k-uppercase', 'letter-e-uppercase')
REFERENCE_EXPORT_SHA256 = '10a4bdc7c7b9552b091d993ace0ea0de9f43fddd85e0bcb2d67b10c4ef6e0ba0'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'side-text-5d129d3a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 92
    text_canvas_height = 20
    text_ink_bounds = (2.2099599999999997, -1.3322676295501878e-15, 90.0, 20.0024)

    def build(self):
        """Source-native uppercase composition for 'FAKE'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (4.21094, 10.4907), (14.2337, 10.4907))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (4.20996, 18.0024), (4.20996, 2.3249))
        self.add_bezier('p2-r1-2', (4.20996, 2.3249), ((4.20996, 2.14546), (4.35542, 2), (4.53486, 2)))
        self.add_line('p2-r1-3', (4.53486, 2), (16.21, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_bezier('p3-r1-1', (28, 18), ((28, 18), (29.26667, 2), (34.1333, 2)))
        self.add_bezier('p3-r1-2', (34.1333, 2), ((39, 2), (40, 18), (40, 18)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p3-r2-1', (28.49782, 13.9921), (39.5709, 14.0032))
        self.add_contour('path-3-2', 'p3-r2-1', closed=False)
        self.add_line('p4-r1-1', (52.017089999999996, 2), (52.017089999999996, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (64.0001, 17.889), (54.1001, 9.42859))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (62.8968, 2.09521), (52, 11.1429))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (88, 17.9999), (76.26183, 18))
        self.add_bezier('p7-r1-2', (76.26183, 18), ((76.11723, 18), (76, 17.8828), (76, 17.7382)))
        self.add_line('p7-r1-3', (76, 17.7382), (76, 9.98924))
        self.add_line('p7-r1-4', (76, 9.98924), (76, 2.01314))
        self.add_line('p7-r1-5', (76, 2.01314), (88, 2))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', 'p7-r1-4', 'p7-r1-5', closed=False)
        self.add_line('p8-r1-1', (84.4, 10), (76, 10))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
        self.relate("connect", 'path-4-1', 'path-5-1')
        self.relate("connect", 'path-4-1', 'path-6-1')
        self.relate("connect", 'path-5-1', 'path-6-1')
        self.relate("connect", 'path-7-1', 'path-8-1')
