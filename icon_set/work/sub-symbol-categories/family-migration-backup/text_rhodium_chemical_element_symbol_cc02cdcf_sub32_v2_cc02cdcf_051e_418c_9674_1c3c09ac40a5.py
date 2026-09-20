# Variant of text-rhodium-chemical-element-symbol-cc02cdcf-sub32; parent file remains unchanged.
"""Independent 32px profile of text-rhodium-chemical-element-symbol-cc02cdcf.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'cc02cdcf-051e-418c-9674-1c3c09ac40a5'
SOURCE_PATH = 'icon_set/dist/text32/text-rhodium-chemical-element-symbol-cc02cdcf.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cc02cdcf-051e-418c-9674-1c3c09ac40a5', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/rh (text u)_cc02cdcf-051e-418c-9674-1c3c09ac40a5.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-rhodium-chemical-element-symbol-cc02cdcf',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-r-uppercase', 'letter-h')
REFERENCE_EXPORT_SHA256 = '1027e109d1292166e53f1729da9b5dec83d78f3d1023d72767475c5706ef53e2'

class DrawingVariant2(TextSub32):
    icon_id = 'text-rhodium-chemical-element-symbol-cc02cdcf-sub32-v2'
    variant_of = 'text-rhodium-chemical-element-symbol-cc02cdcf-sub32'
    variant_label = 'Record the actual joined strokes; preserve reviewed artwork'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 37
    text_ink_bounds = (0.0, 0.0, 37.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (35, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (22, 2), (22, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (22, 14), ((22, 11), (25, 8), (29, 8)))
        self.add_bezier('p3-r1-2', (29, 8), ((32, 8), (35, 11), (35, 14)))
        self.add_line('p3-r1-3', (35, 14), (35, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 21), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (9, 2))
        self.add_bezier('p4-r1-3', (9, 2), ((13, 2), (15, 5), (15, 7)))
        self.add_bezier('p4-r1-4', (15, 7), ((15, 10), (13, 12), (9, 12)))
        self.add_line('p4-r1-5', (9, 12), (2, 12))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (9, 12), (16, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p4-r1-4', 'p5-r1-1')
        self.relate('connect', 'p4-r1-5', 'p5-r1-1')
        self.relate('connect', 'path-2-1', 'path-3-1')
