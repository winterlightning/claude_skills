"""Independent 32px profile of text-underlined-ra-text-symbol-a6f9f39a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'a6f9f39a-9606-4eef-85b4-7ee008e0a5eb'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-ra-text-symbol-a6f9f39a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a6f9f39a-9606-4eef-85b4-7ee008e0a5eb', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/ra (text u)_a6f9f39a-9606-4eef-85b4-7ee008e0a5eb.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-ra-text-symbol-a6f9f39a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-r-uppercase', 'letter-a')
REFERENCE_EXPORT_SHA256 = '66e8212d0d2518c96e705353104c74b13145c7751496f71121e8dfd8c5e24848'

class Drawing(TextSub32):
    icon_id = 'text-underlined-ra-text-symbol-a6f9f39a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 37
    text_ink_bounds = (0.0, 0.0, 37.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (35, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (35, 18), (35, 12))
        self.add_bezier('p2-r1-2', (35, 12), ((35, 11), (35, 11), (35, 11)))
        self.add_bezier('p2-r1-3', (35, 11), ((33, 9), (31, 8), (29, 8)))
        self.add_bezier('p2-r1-4', (29, 8), ((25, 8), (22, 11), (22, 15)))
        self.add_bezier('p2-r1-5', (22, 15), ((22, 18), (25, 21), (29, 21)))
        self.add_bezier('p2-r1-6', (29, 21), ((32, 21), (34, 20), (35, 18)))
        self.add_line('p2-r1-7', (35, 18), (35, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_line('p3-r1-1', (2, 21), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (9, 2))
        self.add_bezier('p3-r1-3', (9, 2), ((13, 2), (15, 5), (15, 7)))
        self.add_bezier('p3-r1-4', (15, 7), ((15, 10), (13, 12), (9, 12)))
        self.add_line('p3-r1-5', (9, 12), (2, 12))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (9, 12), (16, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p3-r1-4', 'p4-r1-1')
        self.relate("connect", 'p3-r1-5', 'p4-r1-1')
