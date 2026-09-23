"""Independent 32px profile of side-text-64a2b4af.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '64a2b4af-fe31-430a-9a05-7f19e316aba7'
SOURCE_PATH = 'icon_set/dist/text32/side-text-64a2b4af.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('64a2b4af-fe31-430a-9a05-7f19e316aba7', 'icon_set/dist/gallery/combination-originals/64a2b4af-fe31-430a-9a05-7f19e316aba7.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-64a2b4af',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'symbol-plus', 'symbol-plus')
REFERENCE_EXPORT_SHA256 = '927d9b5e4ec057a272a21d2d2ea8f0aaec4699873675503dd29406603a9fff1e'































TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'side-text-64a2b4af-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 48
    text_canvas_height = 24
    text_ink_bounds = (2.0, 0.0, 48.0, 24.0)

    def build(self):
        """Source-native uppercase composition for 'C++'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (16, 2.6879), ((14.9406, 2.24575), (13.7674, 2), (12.533, 2)))
        self.add_bezier('p1-r1-2', (12.533, 2), ((7.82037, 2), (4, 5.58172), (4, 10)))
        self.add_bezier('p1-r1-3', (4, 10), ((4, 14.4183), (7.82037, 18), (12.533, 18)))
        self.add_bezier('p1-r1-4', (12.533, 18), ((13.7674, 18), (14.9406, 17.7543), (16, 17.3121)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (26, 12), (32, 12))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (29, 2), (29, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (40, 12), (46, 12))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (43, 2), (43, 22))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'path-2-1', 'path-3-1')
        self.relate("connect", 'path-4-1', 'path-5-1')
