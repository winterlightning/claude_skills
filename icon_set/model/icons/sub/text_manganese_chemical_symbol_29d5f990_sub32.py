"""Independent 32px profile of text-manganese-chemical-symbol-29d5f990.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '29d5f990-d45a-4a45-b57d-009d40fb1d94'
SOURCE_PATH = 'icon_set/dist/text32/text-manganese-chemical-symbol-29d5f990.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('29d5f990-d45a-4a45-b57d-009d40fb1d94', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/mn (text u)_29d5f990-d45a-4a45-b57d-009d40fb1d94.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-manganese-chemical-symbol-29d5f990',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-m-uppercase', 'letter-n')
REFERENCE_EXPORT_SHA256 = 'dc82c4262e982b3d4339816ff6e0660cdf6e1bd4fb947e31313a4b0b5b9f780a'

class Drawing(TextSub32):
    icon_id = 'text-manganese-chemical-symbol-29d5f990-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 39
    text_ink_bounds = (0.0, 0.0, 39.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (37, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (37, 21), (37, 13))
        self.add_bezier('p2-r1-2', (37, 13), ((37, 10), (35, 8), (32, 8)))
        self.add_bezier('p2-r1-3', (32, 8), ((29, 8), (27, 10), (27, 13)))
        self.add_line('p2-r1-4', (27, 13), (27, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 21), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (11, 14))
        self.add_line('p3-r1-3', (11, 14), (20, 2))
        self.add_line('p3-r1-4', (20, 2), (20, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
