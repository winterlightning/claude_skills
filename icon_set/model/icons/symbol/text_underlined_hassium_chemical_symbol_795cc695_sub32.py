"""Independent 32px profile of text-underlined-hassium-chemical-symbol-795cc695.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '795cc695-5c61-4b13-9cd1-79695030ccc4'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-hassium-chemical-symbol-795cc695.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('795cc695-5c61-4b13-9cd1-79695030ccc4', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/hs (text u)_795cc695-5c61-4b13-9cd1-79695030ccc4.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-hassium-chemical-symbol-795cc695',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-h-uppercase', 'letter-s')
REFERENCE_EXPORT_SHA256 = '2c316b17e5916d338950a7a64937e3e1f97184ef0362fd27eabbea10452e42f5'

class Drawing(TextSub32):
    icon_id = 'text-underlined-hassium-chemical-symbol-795cc695-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 33
    text_ink_bounds = (0.0, 0.0, 33.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (31, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (31, 10), ((31, 10), (31, 8), (27, 8)))
        self.add_bezier('p2-r1-2', (27, 8), ((25, 8), (23, 10), (23, 11)))
        self.add_bezier('p2-r1-3', (23, 11), ((23, 12), (23, 13), (25, 14)))
        self.add_bezier('p2-r1-4', (25, 14), ((28, 15), (28, 15), (30, 16)))
        self.add_bezier('p2-r1-5', (30, 16), ((31, 16), (31, 17), (31, 18)))
        self.add_bezier('p2-r1-6', (31, 18), ((31, 19), (30, 21), (27, 21)))
        self.add_bezier('p2-r1-7', (27, 21), ((22, 21), (22, 19), (22, 19)))
        self.add_bezier('p2-r1-8', (22, 19), ((22, 19), (22, 19), (22, 19)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.add_line('p3-r1-1', (2, 2), (2, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 2), (16, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 12), (16, 12))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
