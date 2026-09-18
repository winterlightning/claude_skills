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

class Drawing(TextSub32):
    icon_id = 'side-text-5d129d3a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 100
    text_ink_bounds = (0.0, 0.0, 100.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (98, 2), (81, 2))
        self.add_line('p1-r1-2', (81, 2), (81, 30))
        self.add_line('p1-r1-3', (81, 30), (98, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (81, 16), (95, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (54, 2), (54, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (74, 2), (54, 17))
        self.add_line('p4-r1-2', (54, 17), (74, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (26, 30), (36, 3))
        self.add_bezier('p5-r1-2', (36, 3), ((36, 2.3333333333333335), (36.333333333333336, 2), (37, 2)))
        self.add_bezier('p5-r1-3', (37, 2), ((37, 2), (37.333333333333336, 2.3333333333333335), (38, 3)))
        self.add_line('p5-r1-4', (38, 3), (47, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
        self.add_line('p6-r1-1', (30, 18), (43, 18))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (19, 2), (2, 2))
        self.add_line('p7-r1-2', (2, 2), (2, 30))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', closed=False)
        self.add_line('p8-r1-1', (2, 16), (16, 16))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
