"""Independent 32px profile of text-underlined-serbian-text-symbol-2ae3aaea.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '2ae3aaea-c96d-4420-a757-abdfc64cfd21'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-serbian-text-symbol-2ae3aaea.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2ae3aaea-c96d-4420-a757-abdfc64cfd21', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/sr (text u)_2ae3aaea-c96d-4420-a757-abdfc64cfd21.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-serbian-text-symbol-2ae3aaea',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-r')
REFERENCE_EXPORT_SHA256 = 'c8b1ef2c551f32d776fcb19506a183347846a52061c191e99f196c1f5edd5842'

class Drawing(TextSub32):
    icon_id = 'text-underlined-serbian-text-symbol-2ae3aaea-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 28
    text_ink_bounds = (0.0, 0.0, 28.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (26, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (21, 8), (21, 12))
        self.add_line('p2-r1-2', (21, 12), (21, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (21, 12), ((21, 10), (23, 8), (25, 8)))
        self.add_line('p3-r1-2', (25, 8), (26, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_bezier('p4-r1-1', (14, 5), ((13, 3), (11, 2), (9, 2)))
        self.add_bezier('p4-r1-2', (9, 2), ((6, 2), (3, 3), (3, 7)))
        self.add_bezier('p4-r1-3', (3, 7), ((2, 7), (2, 7), (2, 7)))
        self.add_bezier('p4-r1-4', (2, 7), ((2, 12), (14, 10), (15, 16)))
        self.add_bezier('p4-r1-5', (15, 16), ((15, 16), (15, 16), (15, 16)))
        self.add_bezier('p4-r1-6', (15, 16), ((15, 20), (11, 21), (8, 21)))
        self.add_bezier('p4-r1-7', (8, 21), ((6, 21), (3, 20), (2, 18)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
