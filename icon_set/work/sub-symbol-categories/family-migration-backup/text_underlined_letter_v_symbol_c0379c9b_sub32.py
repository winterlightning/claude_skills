"""Independent 32px profile of text-underlined-letter-v-symbol-c0379c9b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'c0379c9b-21bd-4be4-aa8b-9b95b14d2c82'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letter-v-symbol-c0379c9b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c0379c9b-21bd-4be4-aa8b-9b95b14d2c82', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/v (text u)_c0379c9b-21bd-4be4-aa8b-9b95b14d2c82.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letter-v-symbol-c0379c9b',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-v-uppercase',)
REFERENCE_EXPORT_SHA256 = '3b9c29c258c32c519b54da3760f09b1b9312f1dc27635215cd9d25927812a51a'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letter-v-symbol-c0379c9b-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 18
    text_ink_bounds = (0.0, 0.0, 18.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (16, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 2), (8, 20))
        self.add_bezier('p2-r1-2', (8, 20), ((8.666666666666666, 20.666666666666668), (9, 21), (9, 21)))
        self.add_bezier('p2-r1-3', (9, 21), ((9.666666666666666, 21), (10, 20.666666666666668), (10, 20)))
        self.add_line('p2-r1-4', (10, 20), (16, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
