"""Independent 32px profile of text-number-seven-numeric-symbol-f2e450c0.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'f2e450c0-559a-4dff-bbb6-ddef944b0e55'
SOURCE_PATH = 'icon_set/dist/text32/text-number-seven-numeric-symbol-f2e450c0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f2e450c0-559a-4dff-bbb6-ddef944b0e55', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/7_f2e450c0-559a-4dff-bbb6-ddef944b0e55.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-seven-numeric-symbol-f2e450c0',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-7',)
REFERENCE_EXPORT_SHA256 = 'fd2ce572d15395d48c5ef0635e2bf7f173fe6e30f938924badb82c50eb1a40c5'

class Drawing(TextSub32):
    icon_id = 'text-number-seven-numeric-symbol-f2e450c0-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 23
    text_ink_bounds = (0.0, 0.0, 23.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (20, 2))
        self.add_bezier('p1-r1-2', (20, 2), ((21, 2), (21, 2), (21, 3)))
        self.add_bezier('p1-r1-3', (21, 3), ((21, 3), (21, 3), (21, 3)))
        self.add_line('p1-r1-4', (21, 3), (8, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
