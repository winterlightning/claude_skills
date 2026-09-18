"""Independent 32px profile of text-underlined-nh-text-dad870be.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'dad870be-8e0c-4f77-9a32-8fdec7599208'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-nh-text-dad870be.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dad870be-8e0c-4f77-9a32-8fdec7599208', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/nh (text u)_dad870be-8e0c-4f77-9a32-8fdec7599208.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-nh-text-dad870be',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-n-uppercase', 'letter-h')
REFERENCE_EXPORT_SHA256 = 'ebc366950d301a1fdee555d035250ffa865c47cf064f51ee6bc37fc1edab0926'

class Drawing(TextSub32):
    icon_id = 'text-underlined-nh-text-dad870be-sub32'
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
        self.add_line('p2-r1-1', (22, 2), (22, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (22, 14), ((22, 11), (25, 8), (29, 8)))
        self.add_bezier('p3-r1-2', (29, 8), ((32, 8), (35, 11), (35, 14)))
        self.add_line('p3-r1-3', (35, 14), (35, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 21), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (16, 21))
        self.add_line('p4-r1-3', (16, 21), (16, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
