"""Independent 32px profile of text-underlined-oval-symbol-b57126a0.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'b57126a0-ebc1-4141-bf7a-46580de05e65'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-oval-symbol-b57126a0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b57126a0-ebc1-4141-bf7a-46580de05e65', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/o (text u)_b57126a0-ebc1-4141-bf7a-46580de05e65.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-oval-symbol-b57126a0',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-o-uppercase',)
REFERENCE_EXPORT_SHA256 = 'e8554b253c718f8bfb33942f656f1c06a92462da32291fec149ddcc66e8d0f45'

class Drawing(TextSub32):
    icon_id = 'text-underlined-oval-symbol-b57126a0-sub32'
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
        self.add_arc('p2-r1-1', (2, 12), (16, 12), radius_x=7, radius_y=10, large_arc=True, sweep=True)
        self.add_arc('p2-r1-2', (16, 12), (2, 12), radius_x=7, radius_y=10, large_arc=True, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
