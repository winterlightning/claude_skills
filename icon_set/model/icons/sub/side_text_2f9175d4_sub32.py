"""Independent 32px profile of side-text-2f9175d4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '2f9175d4-638c-4619-a72b-95215338f0fe'
SOURCE_PATH = 'icon_set/dist/text32/side-text-2f9175d4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2f9175d4-638c-4619-a72b-95215338f0fe', 'icon_set/dist/gallery/combination-originals/2f9175d4-638c-4619-a72b-95215338f0fe.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-2f9175d4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-d-uppercase', 'letter-m-uppercase', 'letter-g-uppercase')
REFERENCE_EXPORT_SHA256 = 'adb7e4d166946b87707aa822887d74dcf80bbba2a590158f23df2d78ac84a72e'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'side-text-2f9175d4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, -1.9539862061712654e-06, 68.00000000000009, 20.0)

    def build(self):
        """Source-native uppercase composition for 'DMG'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (4, 2), (8.88681, 2))
        self.add_bezier('p1-r1-2', (8.88681, 2), ((12.8153, 2), (16, 5.58172), (16, 10)))
        self.add_bezier('p1-r1-3', (16, 10), ((16, 14.4183), (12.8153, 18), (8.88681, 18)))
        self.add_line('p1-r1-4', (8.88681, 18), (4, 18))
        self.add_line('p1-r1-5', (4, 18), (4, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (26, 18), (26, 2.4248))
        self.add_bezier('p2-r1-2', (26, 2.4248), ((26, 2.01632), (26.53474, 1.84408), (26.78474, 2.17204)))
        self.add_line('p2-r1-3', (26.78474, 2.17204), (33.65053, 11.1787))
        self.add_bezier('p2-r1-4', (33.65053, 11.1787), ((33.82456, 11.407), (34.175399999999996, 11.407), (34.3495, 11.1787)))
        self.add_line('p2-r1-5', (34.3495, 11.1787), (41.2153, 2.17204))
        self.add_bezier('p2-r1-6', (41.2153, 2.17204), ((41.4653, 1.84408), (42, 2.01632), (42, 2.4248)))
        self.add_line('p2-r1-7', (42, 2.4248), (42, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_bezier('p3-r1-1', (62.8699, 3.51954), ((61.5334, 2.56364), (59.8896, 2), (58.1123, 2)))
        self.add_bezier('p3-r1-2', (58.1123, 2), ((53.63199, 2), (50, 5.58172), (50, 10)))
        self.add_bezier('p3-r1-3', (50, 10), ((50, 14.4183), (53.63199, 18), (58.1123, 18)))
        self.add_bezier('p3-r1-4', (58.1123, 18), ((62.373599999999996, 18), (65.6686, 14.5166), (66, 10.3983)))
        self.add_line('p3-r1-5', (66, 10.3983), (59.9716, 10.3983))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
