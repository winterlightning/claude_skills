"""Independent 32px profile of text-high-dynamic-range-text-symbol-5580b474.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '5580b474-3597-486f-9212-1e7b6c337f96'
SOURCE_PATH = 'icon_set/dist/text32/text-high-dynamic-range-text-symbol-5580b474.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5580b474-3597-486f-9212-1e7b6c337f96', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/HDR_5580b474-3597-486f-9212-1e7b6c337f96.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-high-dynamic-range-text-symbol-5580b474',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-h-uppercase', 'letter-d-uppercase', 'letter-r-uppercase')
REFERENCE_EXPORT_SHA256 = 'c9b7b33db9810a836337f54e9715f7e079ba01d65d1bee1da2cc8c00833674ff'

class Drawing(TextSub32):
    icon_id = 'text-high-dynamic-range-text-symbol-5580b474-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 80
    text_ink_bounds = (0.0, 0.0, 80.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (57, 30), (57, 2))
        self.add_line('p1-r1-2', (57, 2), (67, 2))
        self.add_bezier('p1-r1-3', (67, 2), ((74, 2), (77, 6), (77, 9)))
        self.add_bezier('p1-r1-4', (77, 9), ((77, 13), (74, 17), (67, 17)))
        self.add_line('p1-r1-5', (67, 17), (57, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (67, 17), (78, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (30, 2), (38, 2))
        self.add_bezier('p3-r1-2', (38, 2), ((46, 2), (50, 9), (50, 16)))
        self.add_bezier('p3-r1-3', (50, 16), ((50, 23), (46, 30), (38, 30)))
        self.add_line('p3-r1-4', (38, 30), (30, 30))
        self.add_line('p3-r1-5', (30, 30), (30, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (2, 2), (2, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (22, 2), (22, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (2, 16), (22, 16))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
