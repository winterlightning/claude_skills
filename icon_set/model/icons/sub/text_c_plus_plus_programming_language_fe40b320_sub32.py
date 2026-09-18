"""Independent 32px profile of text-c-plus-plus-programming-language-fe40b320.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-c-plus-plus-programming-language-fe40b320.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-c-plus-plus-programming-language-fe40b320',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '45a37c9a23b935b996dadbd28683c45c388d31a73c7652378bf5f90e6c83704f'

class Drawing(TextSub32):
    icon_id = 'text-c-plus-plus-programming-language-fe40b320-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 79
    text_ink_bounds = (0.0, 0.0, 79.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (55, 19), (77, 19))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (66, 9), (66, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (26, 19), (47, 19))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (37, 9), (37, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_bezier('p5-r1-1', (18, 6), ((16, 3), (14, 2), (12, 2)))
        self.add_bezier('p5-r1-2', (12, 2), ((7, 2), (2, 7), (2, 15)))
        self.add_bezier('p5-r1-3', (2, 15), ((2, 23), (7, 28), (12, 28)))
        self.add_bezier('p5-r1-4', (12, 28), ((14, 28), (16, 27), (18, 25)))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
