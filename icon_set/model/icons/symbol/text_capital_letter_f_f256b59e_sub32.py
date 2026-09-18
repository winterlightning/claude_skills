"""Independent 32px profile of text-capital-letter-f-f256b59e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'f256b59e-6fc7-4190-8d86-68f1d1804875'
SOURCE_PATH = 'icon_set/dist/text32/text-capital-letter-f-f256b59e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f256b59e-6fc7-4190-8d86-68f1d1804875', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/f (text)_f256b59e-6fc7-4190-8d86-68f1d1804875.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-capital-letter-f-f256b59e', 'text/text-uppercase-letter-f-symbol-370104c4')
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-f-uppercase',)
REFERENCE_EXPORT_SHA256 = '1eee0d1b0d1484b32ba6357cbbb13fde9d31275f94dace780d200d88caf624f1'

class Drawing(TextSub32):
    icon_id = 'text-capital-letter-f-f256b59e-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 21
    text_ink_bounds = (0.0, 0.0, 21.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (19, 2), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (2, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 16), (16, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
