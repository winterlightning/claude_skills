"""Independent 32px profile of text-two-minus-one-math-expression-17d5ec75.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-two-minus-one-math-expression-17d5ec75.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-two-minus-one-math-expression-17d5ec75',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '8299f3da4ba765df7bff4e3f9fb99942f1d959f3e825e0d778c17f20da1d5030'

class Drawing(TextSub32):
    icon_id = 'text-two-minus-one-math-expression-17d5ec75-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 65
    text_ink_bounds = (0.0, 0.0, 65.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (57, 30), (57, 3))
        self.add_bezier('p1-r1-2', (57, 3), ((57, 2), (57, 2), (56, 2)))
        self.add_line('p1-r1-3', (56, 2), (50, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (50, 30), (63, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (29, 20), (42, 20))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 2), (16, 2))
        self.add_bezier('p4-r1-2', (16, 2), ((19, 2), (21, 5), (21, 8)))
        self.add_bezier('p4-r1-3', (21, 8), ((21, 9), (21, 11), (19, 12)))
        self.add_line('p4-r1-4', (19, 12), (6, 21))
        self.add_bezier('p4-r1-5', (6, 21), ((3, 23), (2, 25), (2, 28)))
        self.add_line('p4-r1-6', (2, 28), (2, 29))
        self.add_bezier('p4-r1-7', (2, 29), ((2, 29), (3, 30), (3, 30)))
        self.add_line('p4-r1-8', (3, 30), (22, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', 'p4-r1-8', closed=False)
