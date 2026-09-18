"""Independent 32px profile of text-capital-letter-l-symbol-a1f304c9.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'a1f304c9-b1f2-4c50-9777-0270443ac262'
SOURCE_PATH = 'icon_set/dist/text32/text-capital-letter-l-symbol-a1f304c9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a1f304c9-b1f2-4c50-9777-0270443ac262', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/L (text)_a1f304c9-b1f2-4c50-9777-0270443ac262.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-capital-letter-l-symbol-a1f304c9',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-l-uppercase',)
REFERENCE_EXPORT_SHA256 = 'ecaf5a51bbfae91e5d8b3e2e5b70765625c03b2e9954997b70b019ce05f2e864'

class Drawing(TextSub32):
    icon_id = 'text-capital-letter-l-symbol-a1f304c9-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 20
    text_ink_bounds = (0.0, 0.0, 20.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (2, 30))
        self.add_line('p1-r1-2', (2, 30), (18, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
