"""Independent 32px profile of text-rounded-capital-letter-m-3cdc9209.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '3cdc9209-2156-4816-9bd6-25aa15afe55c'
SOURCE_PATH = 'icon_set/dist/text32/text-rounded-capital-letter-m-3cdc9209.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3cdc9209-2156-4816-9bd6-25aa15afe55c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/m (text)_3cdc9209-2156-4816-9bd6-25aa15afe55c.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-rounded-capital-letter-m-3cdc9209',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-m-uppercase',)
REFERENCE_EXPORT_SHA256 = '17666148e4cce3b590209365deb9ed88f354d7c352ae2e9f8f5c04b11a62a3e5'

class Drawing(TextSub32):
    icon_id = 'text-rounded-capital-letter-m-3cdc9209-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 30
    text_ink_bounds = (0.0, 0.0, 30.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (15, 20))
        self.add_line('p1-r1-3', (15, 20), (28, 2))
        self.add_line('p1-r1-4', (28, 2), (28, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
