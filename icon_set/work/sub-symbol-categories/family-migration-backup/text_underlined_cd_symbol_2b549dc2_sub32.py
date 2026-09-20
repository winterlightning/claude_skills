"""Independent 32px profile of text-underlined-cd-symbol-2b549dc2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '2b549dc2-c357-42c8-9126-e2a818b17485'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-cd-symbol-2b549dc2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2b549dc2-c357-42c8-9126-e2a818b17485', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/cd (text u)_2b549dc2-c357-42c8-9126-e2a818b17485.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-cd-symbol-2b549dc2',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-d')
REFERENCE_EXPORT_SHA256 = 'b1613ec9917ef287022f5716552704d5e3897c478186eff7dd38398f08974958'

class Drawing(TextSub32):
    icon_id = 'text-underlined-cd-symbol-2b549dc2-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 35
    text_ink_bounds = (0.0, 0.0, 35.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (33, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (33, 18), ((32, 20), (30, 21), (27, 21)))
        self.add_bezier('p2-r1-2', (27, 21), ((23, 21), (20, 18), (20, 15)))
        self.add_bezier('p2-r1-3', (20, 15), ((20, 11), (23, 8), (27, 8)))
        self.add_bezier('p2-r1-4', (27, 8), ((29, 8), (31, 9), (33, 11)))
        self.add_bezier('p2-r1-5', (33, 11), ((33, 11), (33, 11), (33, 12)))
        self.add_line('p2-r1-6', (33, 12), (33, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (33, 12), (33, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (14, 5), ((12, 3), (11, 2), (9, 2)))
        self.add_bezier('p4-r1-2', (9, 2), ((6, 2), (2, 6), (2, 12)))
        self.add_bezier('p4-r1-3', (2, 12), ((2, 17), (6, 21), (9, 21)))
        self.add_bezier('p4-r1-4', (9, 21), ((11, 21), (12, 20), (14, 18)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.relate("connect", 'p2-r1-5', 'p3-r1-1')
        self.relate("connect", 'p2-r1-6', 'p3-r1-1')
