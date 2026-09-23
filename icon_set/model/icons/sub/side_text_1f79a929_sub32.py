"""Independent 32px profile of side-text-1f79a929.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '1f79a929-e6ab-47a9-8cee-07a575e91e9b'
SOURCE_PATH = 'icon_set/dist/text32/side-text-1f79a929.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1f79a929-e6ab-47a9-8cee-07a575e91e9b', 'icon_set/dist/gallery/combination-originals/1f79a929-e6ab-47a9-8cee-07a575e91e9b.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-1f79a929',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-x-uppercase', 'letter-l-uppercase', 'letter-s-uppercase', 'letter-x-uppercase')
REFERENCE_EXPORT_SHA256 = 'ae861910b73bbf7ad951530799c19ff5dbd5d45829f79a669b87ff56346149e6'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'side-text-1f79a929-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 92
    text_canvas_height = 20
    text_ink_bounds = (1.0, 0.0, 91.0, 20.000000000000004)

    def build(self):
        """Source-native uppercase composition for 'XLSX'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (3, 2.00003), (17, 17.9909))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (3.02295, 18), (16.9638, 2.04587))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (39, 18), ((35.9428, 18), (28.23973, 18), (28, 18)))
        self.add_line('p3-r1-2', (28, 18), (28, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (63.9314, 2), (56.77906, 2))
        self.add_bezier('p4-r1-2', (56.77906, 2), ((51.70172, 2), (50.21029, 7.42857), (54.98284, 9.42857)))
        self.add_line('p4-r1-3', (54.98284, 9.42857), (61.4623, 11.608))
        self.add_bezier('p4-r1-4', (61.4623, 11.608), ((65.7211, 13.4286), (64.2526, 18), (59.7787, 18)))
        self.add_line('p4-r1-5', (59.7787, 18), (52, 18))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (75, 2.00003), (89, 17.9909))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (75.02295, 18), (88.96379999999999, 2.04587))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
        self.relate("connect", 'path-5-1', 'path-6-1')
