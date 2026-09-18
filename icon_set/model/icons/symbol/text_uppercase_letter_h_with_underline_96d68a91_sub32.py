"""Independent 32px profile of text-uppercase-letter-h-with-underline-96d68a91.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '96d68a91-3a00-41a4-a897-167cf369ad6f'
SOURCE_PATH = 'icon_set/dist/text32/text-uppercase-letter-h-with-underline-96d68a91.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('96d68a91-3a00-41a4-a897-167cf369ad6f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/h (text u)_96d68a91-3a00-41a4-a897-167cf369ad6f.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-uppercase-letter-h-with-underline-96d68a91',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-h-uppercase',)
REFERENCE_EXPORT_SHA256 = 'ac0a8b4365cb7d9b31db04824b88ea95f1fb0b4be16297fbb9d5a3d972004da1'

class Drawing(TextSub32):
    icon_id = 'text-uppercase-letter-h-with-underline-96d68a91-sub32'
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
        self.add_line('p2-r1-1', (2, 2), (2, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 2), (16, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 12), (16, 12))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
