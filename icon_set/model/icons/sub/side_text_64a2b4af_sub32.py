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

class Drawing(TextSub32):
    icon_id = 'side-text-64a2b4af-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 77
    text_ink_bounds = (0.0, 0.0, 77.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (54, 19), (75, 19))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (65, 9), (65, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (25, 19), (47, 19))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (36, 9), (36, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_bezier('p5-r1-1', (18, 6), ((16, 3), (14, 2), (12, 2)))
        self.add_bezier('p5-r1-2', (12, 2), ((7, 2), (2, 7), (2, 15)))
        self.add_bezier('p5-r1-3', (2, 15), ((2, 23), (7, 28), (12, 28)))
        self.add_bezier('p5-r1-4', (12, 28), ((14, 28), (16, 27), (18, 25)))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
