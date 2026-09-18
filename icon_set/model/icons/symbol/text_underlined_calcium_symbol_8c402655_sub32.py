"""Independent 32px profile of text-underlined-calcium-symbol-8c402655.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '8c402655-e593-48d7-b819-f0043a385dd2'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-calcium-symbol-8c402655.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8c402655-e593-48d7-b819-f0043a385dd2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/ca (text u)_8c402655-e593-48d7-b819-f0043a385dd2.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-calcium-symbol-8c402655',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-a')
REFERENCE_EXPORT_SHA256 = 'aeb90616503604543efe4c7ee0141e4d5b94a4bd7f50e0bfd0fd4374374a4277'

class Drawing(TextSub32):
    icon_id = 'text-underlined-calcium-symbol-8c402655-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 35
    text_ink_bounds = (0.0, 0.0, 35.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (33, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (33, 18), (33, 12))
        self.add_bezier('p2-r1-2', (33, 12), ((33, 11), (33, 11), (33, 11)))
        self.add_bezier('p2-r1-3', (33, 11), ((31, 9), (29, 8), (27, 8)))
        self.add_bezier('p2-r1-4', (27, 8), ((23, 8), (20, 11), (20, 15)))
        self.add_bezier('p2-r1-5', (20, 15), ((20, 18), (23, 21), (27, 21)))
        self.add_bezier('p2-r1-6', (27, 21), ((30, 21), (32, 20), (33, 18)))
        self.add_line('p2-r1-7', (33, 18), (33, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_bezier('p3-r1-1', (14, 5), ((12, 3), (11, 2), (9, 2)))
        self.add_bezier('p3-r1-2', (9, 2), ((6, 2), (2, 6), (2, 12)))
        self.add_bezier('p3-r1-3', (2, 12), ((2, 17), (6, 21), (9, 21)))
        self.add_bezier('p3-r1-4', (9, 21), ((11, 21), (12, 20), (14, 18)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
