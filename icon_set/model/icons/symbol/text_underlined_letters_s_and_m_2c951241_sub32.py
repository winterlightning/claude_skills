"""Independent 32px profile of text-underlined-letters-s-and-m-2c951241.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '2c951241-2be7-484e-bb29-0e912fab8149'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letters-s-and-m-2c951241.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2c951241-2be7-484e-bb29-0e912fab8149', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/sm (text u)_2c951241-2be7-484e-bb29-0e912fab8149.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letters-s-and-m-2c951241',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-m')
REFERENCE_EXPORT_SHA256 = '3034d5c29039092072d0b2593908738d9d37234c9a083c067f2d4b4e95299a79'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letters-s-and-m-2c951241-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 42
    text_ink_bounds = (0.0, 0.0, 42.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (40, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (31, 13), (31, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (21, 21), (21, 13))
        self.add_bezier('p3-r1-2', (21, 13), ((21, 10), (23, 8), (26, 8)))
        self.add_bezier('p3-r1-3', (26, 8), ((29, 8), (31, 10), (31, 13)))
        self.add_bezier('p3-r1-4', (31, 13), ((31, 10), (33, 8), (36, 8)))
        self.add_bezier('p3-r1-5', (36, 8), ((38, 8), (40, 10), (40, 13)))
        self.add_line('p3-r1-6', (40, 13), (40, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.add_bezier('p4-r1-1', (14, 5), ((13, 3), (11, 2), (9, 2)))
        self.add_bezier('p4-r1-2', (9, 2), ((6, 2), (3, 3), (3, 7)))
        self.add_bezier('p4-r1-3', (3, 7), ((2, 7), (2, 7), (2, 7)))
        self.add_bezier('p4-r1-4', (2, 7), ((2, 12), (14, 10), (15, 16)))
        self.add_bezier('p4-r1-5', (15, 16), ((15, 16), (15, 16), (15, 16)))
        self.add_bezier('p4-r1-6', (15, 16), ((15, 20), (11, 21), (8, 21)))
        self.add_bezier('p4-r1-7', (8, 21), ((6, 21), (3, 20), (2, 18)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-3')
        self.relate('connect', 'p2-r1-1', 'p3-r1-4')
