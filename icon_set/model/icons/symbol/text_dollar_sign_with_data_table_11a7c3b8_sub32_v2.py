"""Independent 32px profile of text-dollar-sign-with-data-table-11a7c3b8.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-dollar-sign-with-data-table-11a7c3b8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-dollar-sign-with-data-table-11a7c3b8',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '964ba44ee6aa5b6bfa8675c1e2c1a60c2e664ad22382c92d10ca9669167dff6c'

class DrawingVariant2(TextSub32):
    icon_id = 'text-dollar-sign-with-data-table-11a7c3b8-sub32-v2'
    related_origin_icon_id = 'text-dollar-sign-with-data-table-11a7c3b8-sub32'
    variant_label = 'Record the actual joined strokes; preserve reviewed artwork'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 71
    text_ink_bounds = (0.0, 0.0, 71.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (17, 8), ((16, 6), (13, 5), (10, 5)))
        self.add_bezier('p1-r1-2', (10, 5), ((7, 5), (3, 7), (3, 11)))
        self.add_bezier('p1-r1-3', (3, 11), ((3, 11), (3, 11), (3, 11)))
        self.add_bezier('p1-r1-4', (3, 11), ((3, 18), (17, 14), (17, 21)))
        self.add_bezier('p1-r1-5', (17, 21), ((17, 22), (17, 22), (17, 22)))
        self.add_bezier('p1-r1-6', (17, 22), ((17, 26), (13, 28), (10, 28)))
        self.add_bezier('p1-r1-7', (10, 28), ((6, 28), (3, 27), (2, 25)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (10, 2), (10, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (31, 2), (69, 2))
        self.add_line('p3-r1-2', (69, 2), (69, 30))
        self.add_line('p3-r1-3', (69, 30), (31, 30))
        self.add_line('p3-r1-4', (31, 30), (31, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p3-r2-1', (50, 2), (50, 30))
        self.add_contour('path-3-2', 'p3-r2-1', closed=False)
        self.add_line('p3-r3-1', (31, 16), (69, 16))
        self.add_contour('path-3-3', 'p3-r3-1', closed=False)
        self.relate('connect', 'path-1-1', 'path-2-1')
