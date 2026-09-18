"""Independent 32px profile of text-numeric-digit-four-1b2e9958.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '1b2e9958-1a24-4980-b7ee-0e7fca211f6f'
SOURCE_PATH = 'icon_set/dist/text32/text-numeric-digit-four-1b2e9958.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1b2e9958-1a24-4980-b7ee-0e7fca211f6f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/4 (text)_1b2e9958-1a24-4980-b7ee-0e7fca211f6f.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-numeric-digit-four-1b2e9958',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-4',)
REFERENCE_EXPORT_SHA256 = '899bde54398171acf72356a9abbfc262c93c0be5b3fc04b0f09a933f1be80bde'

class Drawing(TextSub32):
    icon_id = 'text-numeric-digit-four-1b2e9958-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 28
    text_ink_bounds = (0.0, 0.0, 28.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (2, 20))
        self.add_bezier('p1-r1-2', (2, 20), ((2, 20), (2, 20), (3, 20)))
        self.add_line('p1-r1-3', (3, 20), (26, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (21, 2), (21, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
