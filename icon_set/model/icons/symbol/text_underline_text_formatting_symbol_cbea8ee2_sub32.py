"""Independent 32px profile of text-underline-text-formatting-symbol-cbea8ee2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'cbea8ee2-f633-4b79-b53e-34d3c9bcf990'
SOURCE_PATH = 'icon_set/dist/text32/text-underline-text-formatting-symbol-cbea8ee2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cbea8ee2-f633-4b79-b53e-34d3c9bcf990', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/u (text u)_cbea8ee2-f633-4b79-b53e-34d3c9bcf990.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underline-text-formatting-symbol-cbea8ee2',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-u-uppercase',)
REFERENCE_EXPORT_SHA256 = 'f6c67ba1d0adf7b811a8834aba1f9870c43517aebeb89396f6c954fc630cefd7'

class Drawing(TextSub32):
    icon_id = 'text-underline-text-formatting-symbol-cbea8ee2-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 18
    text_ink_bounds = (0.0, 0.0, 18.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (16, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 2), (2, 14))
        self.add_bezier('p2-r1-2', (2, 14), ((2, 19), (5, 21), (9, 21)))
        self.add_bezier('p2-r1-3', (9, 21), ((12, 21), (16, 19), (16, 14)))
        self.add_line('p2-r1-4', (16, 14), (16, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
