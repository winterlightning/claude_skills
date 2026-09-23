"""Independent 32px profile of side-text-0f609222.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '0f609222-6b88-41ee-98b6-46d2a4e33966'
SOURCE_PATH = 'icon_set/dist/text32/side-text-0f609222.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0f609222-6b88-41ee-98b6-46d2a4e33966', 'icon_set/dist/gallery/combination-originals/0f609222-6b88-41ee-98b6-46d2a4e33966.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-0f609222',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-x-uppercase', 'digit-2')
REFERENCE_EXPORT_SHA256 = 'b5248ecc99e96c79c0645b015e0b236c156cdcee483f12f59884fe82598500b8'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'side-text-0f609222-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 44
    text_canvas_height = 20
    text_ink_bounds = (1.0, 0.0, 42.0, 20.0)

    def build(self):
        """Source-native uppercase composition for 'X2'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (3, 2.00003), (17, 17.9909))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (3.02295, 18), (16.9638, 2.04587))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (28.551090000000002, 6.1626), ((28.551090000000002, 6.1626), (27.96613, 2), (33.98841, 2)))
        self.add_bezier('p3-r1-2', (33.98841, 2), ((40.0107, 2), (40.3103, 7.1822), (37.6, 8.85714)))
        self.add_line('p3-r1-3', (37.6, 8.85714), (29.8, 14))
        self.add_bezier('p3-r1-4', (29.8, 14), ((28.43905, 14.8411), (28, 16), (28, 16.9646)))
        self.add_line('p3-r1-5', (28, 16.9646), (28, 17.2495))
        self.add_bezier('p3-r1-6', (28, 17.2495), ((28, 17.664), (28.37623, 18), (28.84034, 18)))
        self.add_line('p3-r1-7', (28.84034, 18), (40, 18))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
