"""Independent 32px profile of text-simple-digit-number-one-88b7583b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '88b7583b-fcb1-4d9c-af2e-e71964ebbb83'
SOURCE_PATH = 'icon_set/dist/text32/text-simple-digit-number-one-88b7583b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('88b7583b-fcb1-4d9c-af2e-e71964ebbb83', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/1 (text)_88b7583b-fcb1-4d9c-af2e-e71964ebbb83.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-simple-digit-number-one-88b7583b',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-1',)
REFERENCE_EXPORT_SHA256 = '7ac758ccf3bcef992666d5558d99dd355928ea47b5fd6245d78962326d91c31c'

class Drawing(TextSub32):
    icon_id = 'text-simple-digit-number-one-88b7583b-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 17
    text_ink_bounds = (0.0, 0.0, 17.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (9, 30), (9, 3))
        self.add_bezier('p1-r1-2', (9, 3), ((9, 2), (8, 2), (8, 2)))
        self.add_line('p1-r1-3', (8, 2), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (2, 30), (15, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
