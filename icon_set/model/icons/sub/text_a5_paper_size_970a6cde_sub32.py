"""V2 typeface composition for A5 Paper Size."""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '970a6cde-a55d-4c40-bc6d-1f90c47200b1'
SOURCE_PATH = 'published/gallery/combination-originals/970a6cde-a55d-4c40-bc6d-1f90c47200b1.svg'
AUTHOR = 'codex'
SOURCE_REFERENCES = (('970a6cde-a55d-4c40-bc6d-1f90c47200b1', 'published/gallery/combination-originals/970a6cde-a55d-4c40-bc6d-1f90c47200b1.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-970a6cde',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'digit-5')


REFERENCE_EXPORT_SHA256 = 'e6e2c24aa55d20f888900dac67d3c16cc2ade0ba58c0c1416cd71833d0704264'




























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-a5-paper-size-970a6cde-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 44
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 42.00002484023049, 20.00000000000001)

    def build(self):
        """Source-native uppercase composition for 'A5'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (4, 18), ((4, 18), (5.26667, 2), (10.1333, 2)))
        self.add_bezier('p1-r1-2', (10.1333, 2), ((15, 2), (16, 18), (16, 18)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p1-r2-1', (4.49782, 13.9921), (15.5709, 14.0032))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
        self.add_line('p2-r1-1', (39.1498, 2.00001), (28.54829, 2.00001))
        self.add_bezier('p2-r1-2', (28.54829, 2.00001), ((28.24548, 2.00001), (28, 2.20899), (28, 2.46678)))
        self.add_line('p2-r1-3', (28, 2.46678), (28, 8.20519))
        self.add_bezier('p2-r1-4', (28, 8.20519), ((28, 8.46299), (28.24548, 8.67197), (28.54829, 8.67197)))
        self.add_line('p2-r1-5', (28.54829, 8.67197), (34.5106, 8.67197))
        self.add_bezier('p2-r1-6', (34.5106, 8.67197), ((39.3427, 8.67197), (41.808499999999995, 13.6102), (38.4555, 16.5724)))
        self.add_bezier('p2-r1-7', (38.4555, 16.5724), ((37.4229, 17.4846), (35.9988, 18), (34.5106, 18)))
        self.add_line('p2-r1-8', (34.5106, 18), (28.60888, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
