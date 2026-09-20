"""Independent 32px profile of text-chemical-symbol-for-lead-a86d4c64.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'a86d4c64-5422-40b0-81a1-1820524ddd2f'
SOURCE_PATH = 'icon_set/dist/text32/text-chemical-symbol-for-lead-a86d4c64.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a86d4c64-5422-40b0-81a1-1820524ddd2f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/pb (text u)_a86d4c64-5422-40b0-81a1-1820524ddd2f.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-chemical-symbol-for-lead-a86d4c64',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-b')
REFERENCE_EXPORT_SHA256 = '93a4d24fb85007d2e492b80d907d8b3f856c9b4e2b1ee38f124b56924144235b'

class Drawing(TextSub32):
    icon_id = 'text-chemical-symbol-for-lead-a86d4c64-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 36
    text_ink_bounds = (0.0, 0.0, 36.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (34, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (22, 18), ((23, 20), (25, 21), (28, 21)))
        self.add_bezier('p2-r1-2', (28, 21), ((31, 21), (34, 18), (34, 15)))
        self.add_bezier('p2-r1-3', (34, 15), ((34, 11), (31, 8), (28, 8)))
        self.add_bezier('p2-r1-4', (28, 8), ((25, 8), (23, 9), (22, 11)))
        self.add_bezier('p2-r1-5', (22, 11), ((22, 11), (22, 11), (22, 12)))
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
        self.relate("connect", 'p2-r1-5', 'p3-r1-1')
        self.relate("connect", 'p2-r1-6', 'p3-r1-1')
