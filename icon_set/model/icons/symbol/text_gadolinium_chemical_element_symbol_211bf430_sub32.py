"""Independent 32px profile of text-gadolinium-chemical-element-symbol-211bf430.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '211bf430-9cef-4aa6-a5a0-5ccec5c0924e'
SOURCE_PATH = 'icon_set/dist/text32/text-gadolinium-chemical-element-symbol-211bf430.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('211bf430-9cef-4aa6-a5a0-5ccec5c0924e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/gd (text u)_211bf430-9cef-4aa6-a5a0-5ccec5c0924e.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-gadolinium-chemical-element-symbol-211bf430',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-g-uppercase', 'letter-d')
REFERENCE_EXPORT_SHA256 = '552fc7e10e31d50a68520ebecb206002b0e8f2cb6696b5a6a76551e6d90caabf'

class Drawing(TextSub32):
    icon_id = 'text-gadolinium-chemical-element-symbol-211bf430-sub32'
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
        self.add_bezier('p2-r1-1', (35, 18), ((34, 20), (32, 21), (29, 21)))
        self.add_bezier('p2-r1-2', (29, 21), ((25, 21), (22, 18), (22, 15)))
        self.add_bezier('p2-r1-3', (22, 15), ((22, 11), (25, 8), (29, 8)))
        self.add_bezier('p2-r1-4', (29, 8), ((31, 8), (33, 9), (35, 11)))
        self.add_bezier('p2-r1-5', (35, 11), ((35, 11), (35, 11), (35, 12)))
        self.add_line('p2-r1-6', (35, 12), (35, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (35, 12), (35, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (14, 5), ((13, 3), (11, 2), (9, 2)))
        self.add_bezier('p4-r1-2', (9, 2), ((6, 2), (2, 7), (2, 12)))
        self.add_bezier('p4-r1-3', (2, 12), ((2, 13), (2, 14), (3, 15)))
        self.add_bezier('p4-r1-4', (3, 15), ((4, 19), (6, 21), (9, 21)))
        self.add_bezier('p4-r1-5', (9, 21), ((12, 21), (16, 17), (16, 12)))
        self.add_line('p4-r1-6', (16, 12), (11, 12))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', closed=False)
        self.relate('connect', 'p2-r1-5', 'p3-r1-1')
        self.relate('connect', 'p2-r1-6', 'p3-r1-1')
