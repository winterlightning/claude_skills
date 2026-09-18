"""Independent 32px profile of text-underlined-level-text-symbol-39ccb5c4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '39ccb5c4-ba10-4742-8cf1-04e617232ae7'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-level-text-symbol-39ccb5c4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('39ccb5c4-ba10-4742-8cf1-04e617232ae7', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/lv (text u)_39ccb5c4-ba10-4742-8cf1-04e617232ae7.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-level-text-symbol-39ccb5c4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-l-uppercase', 'letter-v')
REFERENCE_EXPORT_SHA256 = '59696ff528b1b6b07ea85a78b418ed53737b2461d84aa70493b1add6ad13fef3'

class Drawing(TextSub32):
    icon_id = 'text-underlined-level-text-symbol-39ccb5c4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 34
    text_ink_bounds = (0.0, 0.0, 34.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (32, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (20, 8), (24, 20))
        self.add_bezier('p2-r1-2', (24, 20), ((25, 21), (25, 21), (26, 21)))
        self.add_bezier('p2-r1-3', (26, 21), ((26, 21), (27, 21), (27, 20)))
        self.add_line('p2-r1-4', (27, 20), (32, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 2), (2, 21))
        self.add_line('p3-r1-2', (2, 21), (13, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
