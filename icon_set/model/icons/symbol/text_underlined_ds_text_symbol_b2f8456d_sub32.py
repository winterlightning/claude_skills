"""Independent 32px profile of text-underlined-ds-text-symbol-b2f8456d.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'b2f8456d-0bd5-418c-8cb5-8aa61117c3f2'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-ds-text-symbol-b2f8456d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b2f8456d-0bd5-418c-8cb5-8aa61117c3f2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/ds (text u)_b2f8456d-0bd5-418c-8cb5-8aa61117c3f2.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-ds-text-symbol-b2f8456d',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-d-uppercase', 'letter-s')
REFERENCE_EXPORT_SHA256 = '611831909a98044280361db4db4587549a421cc78c6164fd37510bcc77534cb0'

class Drawing(TextSub32):
    icon_id = 'text-underlined-ds-text-symbol-b2f8456d-sub32'
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
        self.add_bezier('p2-r1-1', (30, 10), ((30, 10), (30, 8), (26, 8)))
        self.add_bezier('p2-r1-2', (26, 8), ((24, 8), (22, 10), (22, 11)))
        self.add_bezier('p2-r1-3', (22, 11), ((22, 12), (23, 13), (24, 14)))
        self.add_bezier('p2-r1-4', (24, 14), ((28, 15), (27, 15), (29, 16)))
        self.add_bezier('p2-r1-5', (29, 16), ((30, 16), (31, 17), (31, 18)))
        self.add_bezier('p2-r1-6', (31, 18), ((31, 19), (29, 21), (26, 21)))
        self.add_bezier('p2-r1-7', (26, 21), ((22, 21), (22, 19), (22, 19)))
        self.add_bezier('p2-r1-8', (22, 19), ((22, 19), (22, 19), (22, 19)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.add_line('p3-r1-1', (2, 2), (7, 2))
        self.add_bezier('p3-r1-2', (7, 2), ((13, 2), (15, 7), (15, 12)))
        self.add_bezier('p3-r1-3', (15, 12), ((15, 16), (13, 21), (7, 21)))
        self.add_line('p3-r1-4', (7, 21), (2, 21))
        self.add_line('p3-r1-5', (2, 21), (2, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
