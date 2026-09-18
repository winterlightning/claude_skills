"""Independent 32px profile of text-rubidium-chemical-element-symbol-c00033d9.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'c00033d9-12b6-41d1-a9cc-cbe615b46a96'
SOURCE_PATH = 'icon_set/dist/text32/text-rubidium-chemical-element-symbol-c00033d9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c00033d9-12b6-41d1-a9cc-cbe615b46a96', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/rb (text u)_c00033d9-12b6-41d1-a9cc-cbe615b46a96.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-rubidium-chemical-element-symbol-c00033d9',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-r-uppercase', 'letter-b')
REFERENCE_EXPORT_SHA256 = '494e2bc4c1da18d35885f145d5da6591612eadea1ac9131fd3b5fd70f8d3af82'

class Drawing(TextSub32):
    icon_id = 'text-rubidium-chemical-element-symbol-c00033d9-sub32'
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
        self.add_bezier('p2-r1-1', (22, 18), ((24, 20), (26, 21), (28, 21)))
        self.add_bezier('p2-r1-2', (28, 21), ((32, 21), (35, 18), (35, 15)))
        self.add_bezier('p2-r1-3', (35, 15), ((35, 11), (32, 8), (28, 8)))
        self.add_bezier('p2-r1-4', (28, 8), ((26, 8), (24, 9), (23, 11)))
        self.add_bezier('p2-r1-5', (23, 11), ((23, 11), (22, 11), (22, 12)))
        self.add_line('p2-r1-6', (22, 12), (22, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (22, 12), (22, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 21), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (9, 2))
        self.add_bezier('p4-r1-3', (9, 2), ((13, 2), (15, 5), (15, 7)))
        self.add_bezier('p4-r1-4', (15, 7), ((15, 10), (13, 12), (9, 12)))
        self.add_line('p4-r1-5', (9, 12), (2, 12))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (9, 12), (16, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p2-r1-5', 'p3-r1-1')
        self.relate('connect', 'p2-r1-6', 'p3-r1-1')
        self.relate('connect', 'p4-r1-4', 'p5-r1-1')
        self.relate('connect', 'p4-r1-5', 'p5-r1-1')
