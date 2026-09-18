"""Independent 32px profile of text-antimony-chemical-symbol-4374c108.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '4374c108-630e-4085-9b64-899ed4675f23'
SOURCE_PATH = 'icon_set/dist/text32/text-antimony-chemical-symbol-4374c108.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4374c108-630e-4085-9b64-899ed4675f23', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/sb (text u)_4374c108-630e-4085-9b64-899ed4675f23.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-antimony-chemical-symbol-4374c108',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-b')
REFERENCE_EXPORT_SHA256 = '986e37d0e77cec816101cdf7db1260940f74bb9b1bc494067b6e757e961c2360'

class Drawing(TextSub32):
    icon_id = 'text-antimony-chemical-symbol-4374c108-sub32'
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
        self.add_bezier('p2-r1-1', (21, 18), ((22, 20), (25, 21), (27, 21)))
        self.add_bezier('p2-r1-2', (27, 21), ((31, 21), (34, 18), (34, 15)))
        self.add_bezier('p2-r1-3', (34, 15), ((34, 11), (31, 8), (27, 8)))
        self.add_bezier('p2-r1-4', (27, 8), ((25, 8), (23, 9), (22, 11)))
        self.add_bezier('p2-r1-5', (22, 11), ((21, 11), (21, 11), (21, 12)))
        self.add_line('p2-r1-6', (21, 12), (21, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (21, 12), (21, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (14, 5), ((13, 3), (11, 2), (9, 2)))
        self.add_bezier('p4-r1-2', (9, 2), ((6, 2), (3, 3), (3, 7)))
        self.add_bezier('p4-r1-3', (3, 7), ((2, 7), (2, 7), (2, 7)))
        self.add_bezier('p4-r1-4', (2, 7), ((2, 12), (14, 10), (15, 16)))
        self.add_bezier('p4-r1-5', (15, 16), ((15, 16), (15, 16), (15, 16)))
        self.add_bezier('p4-r1-6', (15, 16), ((15, 20), (11, 21), (8, 21)))
        self.add_bezier('p4-r1-7', (8, 21), ((6, 21), (3, 20), (2, 18)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', closed=False)
        self.relate('connect', 'p2-r1-5', 'p3-r1-1')
        self.relate('connect', 'p2-r1-6', 'p3-r1-1')
