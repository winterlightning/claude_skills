"""Independent 32px profile of text-pascal-pressure-unit-symbol-443d8fb3.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '443d8fb3-2e9d-434a-8f52-35b60151f3e1'
SOURCE_PATH = 'icon_set/dist/text32/text-pascal-pressure-unit-symbol-443d8fb3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('443d8fb3-2e9d-434a-8f52-35b60151f3e1', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/pa (text u)_443d8fb3-2e9d-434a-8f52-35b60151f3e1.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-pascal-pressure-unit-symbol-443d8fb3',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-a')
REFERENCE_EXPORT_SHA256 = '164ac4f7861f49fd310c97bd1363f160281481d93dec041dd9bcbf56e34d8974'

class Drawing(TextSub32):
    icon_id = 'text-pascal-pressure-unit-symbol-443d8fb3-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 36
    text_ink_bounds = (0.0, 0.0, 36.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (34, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (34, 18), (34, 12))
        self.add_bezier('p2-r1-2', (34, 12), ((34, 11), (34, 11), (34, 11)))
        self.add_bezier('p2-r1-3', (34, 11), ((33, 9), (31, 8), (29, 8)))
        self.add_bezier('p2-r1-4', (29, 8), ((25, 8), (22, 11), (22, 15)))
        self.add_bezier('p2-r1-5', (22, 15), ((22, 18), (25, 21), (29, 21)))
        self.add_bezier('p2-r1-6', (29, 21), ((31, 21), (33, 20), (34, 18)))
        self.add_line('p2-r1-7', (34, 18), (34, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_line('p3-r1-1', (2, 21), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (9, 2))
        self.add_bezier('p3-r1-3', (9, 2), ((13, 2), (15, 5), (15, 7)))
        self.add_bezier('p3-r1-4', (15, 7), ((15, 10), (13, 12), (9, 12)))
        self.add_line('p3-r1-5', (9, 12), (2, 12))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
