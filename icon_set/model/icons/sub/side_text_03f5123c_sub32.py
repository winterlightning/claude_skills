"""Independent 32px profile of side-text-03f5123c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '03f5123c-4121-4c9f-8ffb-3c6f68958ad0'
SOURCE_PATH = 'icon_set/dist/text32/side-text-03f5123c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('03f5123c-4121-4c9f-8ffb-3c6f68958ad0', 'icon_set/dist/gallery/combination-originals/03f5123c-4121-4c9f-8ffb-3c6f68958ad0.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-03f5123c',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-i-uppercase')
REFERENCE_EXPORT_SHA256 = '842efe2e4d987c9b0d67ddf1b503236da2c6628f7a7b646d90a444bfb5068e8e'































TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'side-text-03f5123c-sub32'
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
        """Source-native uppercase composition for 'AI'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (4, 18), ((4, 18), (5.26667, 2), (10.1333, 2)))
        self.add_bezier('p1-r1-2', (10.1333, 2), ((15, 2), (16, 18), (16, 18)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p1-r2-1', (4.49782, 13.9921), (15.5709, 14.0032))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
        self.add_line('p2-r1-1', (40, 18), (28, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (40, 2), (28, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (34, 2), (34, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'path-2-1', 'path-3-1')
        self.relate("connect", 'path-2-1', 'path-4-1')
        self.relate("connect", 'path-3-1', 'path-4-1')
