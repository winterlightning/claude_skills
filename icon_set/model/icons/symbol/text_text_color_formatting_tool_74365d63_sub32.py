"""Independent 32px profile of text-text-color-formatting-tool-74365d63.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '74365d63-bacc-45d5-a650-0b413e938b66'
SOURCE_PATH = 'icon_set/dist/text32/text-text-color-formatting-tool-74365d63.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('74365d63-bacc-45d5-a650-0b413e938b66', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/ac (text u)_74365d63-bacc-45d5-a650-0b413e938b66.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-text-color-formatting-tool-74365d63',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-c')
REFERENCE_EXPORT_SHA256 = 'e3fde4972a7ab6ca32fe3aa49b08ba7c3cf456528e666fc97e8bfa4fad6b5f69'

class Drawing(TextSub32):
    icon_id = 'text-text-color-formatting-tool-74365d63-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 37
    text_ink_bounds = (0.0, 0.0, 37.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (35, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (35, 11), ((34, 9), (32, 8), (30, 8)))
        self.add_bezier('p2-r1-2', (30, 8), ((26, 8), (23, 11), (23, 15)))
        self.add_bezier('p2-r1-3', (23, 15), ((23, 18), (26, 21), (30, 21)))
        self.add_bezier('p2-r1-4', (30, 21), ((32, 21), (34, 20), (35, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 21), (8, 3))
        self.add_bezier('p3-r1-2', (8, 3), ((8.666666666666666, 2.3333333333333335), (9, 2), (9, 2)))
        self.add_bezier('p3-r1-3', (9, 2), ((9.666666666666666, 2), (10, 2.3333333333333335), (10, 3)))
        self.add_line('p3-r1-4', (10, 3), (16, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (5, 13), (13, 13))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
