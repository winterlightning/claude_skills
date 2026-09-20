# Variant of text-underlined-th-text-6dd6160e-sub32; parent file remains unchanged.
"""Independent 32px profile of text-underlined-th-text-6dd6160e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '6dd6160e-f919-4957-8eda-70be2a33d023'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-th-text-6dd6160e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6dd6160e-f919-4957-8eda-70be2a33d023', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/th (text u)_6dd6160e-f919-4957-8eda-70be2a33d023.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-th-text-6dd6160e',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-t-uppercase', 'letter-h')
REFERENCE_EXPORT_SHA256 = '077bd42c926c87e3c7541ffa5086932e951b28a278a5d3b9c4cdde3fe0fac5ca'

class DrawingVariant2(TextSub32):
    icon_id = 'text-underlined-th-text-6dd6160e-sub32-v2'
    variant_of = 'text-underlined-th-text-6dd6160e-sub32'
    variant_label = 'Record the actual joined strokes; preserve reviewed artwork'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 38
    text_ink_bounds = (0.0, 0.0, 38.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (36, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (24, 2), (24, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (24, 14), ((24, 11), (26, 8), (30, 8)))
        self.add_bezier('p3-r1-2', (30, 8), ((33, 8), (36, 11), (36, 14)))
        self.add_line('p3-r1-3', (36, 14), (36, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 2), (17, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (9, 2), (9, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'path-2-1', 'path-3-1')
