"""Independent 32px profile of text-cerium-chemical-element-symbol-c8302404.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'c8302404-8bb0-4abd-ad0a-69790af88bfe'
SOURCE_PATH = 'icon_set/dist/text32/text-cerium-chemical-element-symbol-c8302404.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c8302404-8bb0-4abd-ad0a-69790af88bfe', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/ce (text u)_c8302404-8bb0-4abd-ad0a-69790af88bfe.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-cerium-chemical-element-symbol-c8302404',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-e')
REFERENCE_EXPORT_SHA256 = 'cfd078b79301b3df58c86be7cb77adbf62f26b2f5988e21c73a46d78b9ee8f78'

class Drawing(TextSub32):
    icon_id = 'text-cerium-chemical-element-symbol-c8302404-sub32'
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
        self.add_bezier('p2-r1-1', (34, 15), ((34, 11), (31, 8), (27, 8)))
        self.add_bezier('p2-r1-2', (27, 8), ((23, 8), (20, 11), (20, 15)))
        self.add_bezier('p2-r1-3', (20, 15), ((20, 18), (23, 21), (27, 21)))
        self.add_bezier('p2-r1-4', (27, 21), ((30, 21), (32, 20), (33, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (20, 15), (34, 15))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (14, 5), ((12, 3), (11, 2), (9, 2)))
        self.add_bezier('p4-r1-2', (9, 2), ((6, 2), (2, 6), (2, 12)))
        self.add_bezier('p4-r1-3', (2, 12), ((2, 17), (6, 21), (9, 21)))
        self.add_bezier('p4-r1-4', (9, 21), ((11, 21), (12, 20), (14, 18)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
