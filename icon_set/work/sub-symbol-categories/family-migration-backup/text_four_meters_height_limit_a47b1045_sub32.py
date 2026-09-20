"""Independent 32px profile of text-four-meters-height-limit-a47b1045.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-four-meters-height-limit-a47b1045.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-four-meters-height-limit-a47b1045',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '74ccf94b7e8c6d5c44e15f8bf5a05f2118ebf74be5d91ea1f4f589bcacb67ff5'

class Drawing(TextSub32):
    icon_id = 'text-four-meters-height-limit-a47b1045-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 85
    text_ink_bounds = (0.0, 0.0, 85.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (36, 30), (36, 2))
        self.add_line('p1-r1-2', (36, 2), (49, 20))
        self.add_line('p1-r1-3', (49, 20), (62, 2))
        self.add_line('p1-r1-4', (62, 2), (62, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 2), (2, 20))
        self.add_bezier('p2-r1-2', (2, 20), ((2, 20), (2, 20), (3, 20)))
        self.add_line('p2-r1-3', (3, 20), (26, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (21, 2), (21, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (71, 2), (77, 8))
        self.add_line('p4-r1-2', (77, 8), (83, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (71, 30), (77, 24))
        self.add_line('p5-r1-2', (77, 24), (83, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
