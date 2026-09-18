"""Independent 32px profile of text-sodium-chemical-element-symbol-99772563.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '99772563-7d66-4072-9261-7e4e0b8e831d'
SOURCE_PATH = 'icon_set/dist/text32/text-sodium-chemical-element-symbol-99772563.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('99772563-7d66-4072-9261-7e4e0b8e831d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/na (text u)_99772563-7d66-4072-9261-7e4e0b8e831d.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-sodium-chemical-element-symbol-99772563',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-n-uppercase', 'letter-a')
REFERENCE_EXPORT_SHA256 = '7e32529897f58a25857b98dbc146a5e677e8e75e95e0008f86393d76196a2bec'

class Drawing(TextSub32):
    icon_id = 'text-sodium-chemical-element-symbol-99772563-sub32'
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
        self.add_line('p2-r1-1', (35, 18), (35, 12))
        self.add_bezier('p2-r1-2', (35, 12), ((35, 11), (35, 11), (35, 11)))
        self.add_bezier('p2-r1-3', (35, 11), ((33, 9), (31, 8), (29, 8)))
        self.add_bezier('p2-r1-4', (29, 8), ((25, 8), (22, 11), (22, 15)))
        self.add_bezier('p2-r1-5', (22, 15), ((22, 18), (25, 21), (29, 21)))
        self.add_bezier('p2-r1-6', (29, 21), ((32, 21), (34, 20), (35, 18)))
        self.add_line('p2-r1-7', (35, 18), (35, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_line('p3-r1-1', (2, 21), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (16, 21))
        self.add_line('p3-r1-3', (16, 21), (16, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
