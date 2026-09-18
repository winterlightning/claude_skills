"""Independent 32px profile of text-selenium-chemical-symbol-3133a9b0.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '3133a9b0-78d2-4162-8f81-e2370a4d6493'
SOURCE_PATH = 'icon_set/dist/text32/text-selenium-chemical-symbol-3133a9b0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3133a9b0-78d2-4162-8f81-e2370a4d6493', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/se (text u)_3133a9b0-78d2-4162-8f81-e2370a4d6493.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-selenium-chemical-symbol-3133a9b0',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-e')
REFERENCE_EXPORT_SHA256 = '691c5cb8a1e9cb653879218b34ecd0ae78d6fac47ffedcdb2cbaea788d7e3936'

class Drawing(TextSub32):
    icon_id = 'text-selenium-chemical-symbol-3133a9b0-sub32'
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
        self.add_bezier('p2-r1-1', (34, 15), ((34, 11), (32, 8), (28, 8)))
        self.add_bezier('p2-r1-2', (28, 8), ((24, 8), (21, 11), (21, 15)))
        self.add_bezier('p2-r1-3', (21, 15), ((21, 18), (24, 21), (28, 21)))
        self.add_bezier('p2-r1-4', (28, 21), ((30, 21), (32, 20), (34, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (21, 15), (34, 15))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
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
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
