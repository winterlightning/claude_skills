"""Independent 32px profile of text-capital-letters-p-and-l-e5930783.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'e5930783-e58a-4a2c-8abe-dffea8e85cfe'
SOURCE_PATH = 'icon_set/dist/text32/text-capital-letters-p-and-l-e5930783.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e5930783-e58a-4a2c-8abe-dffea8e85cfe', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/pl (text)_e5930783-e58a-4a2c-8abe-dffea8e85cfe.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-capital-letters-p-and-l-e5930783',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-l-uppercase')
REFERENCE_EXPORT_SHA256 = 'e7430d8b6f72fca07c0ae595573b3b84fea7d925d11e7814f8702a4114e0e365'

class Drawing(TextSub32):
    icon_id = 'text-capital-letters-p-and-l-e5930783-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 48
    text_ink_bounds = (0.0, 0.0, 48.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (29, 2), (29, 30))
        self.add_line('p1-r1-2', (29, 30), (46, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 30), (2, 2))
        self.add_line('p2-r1-2', (2, 2), (12, 2))
        self.add_bezier('p2-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p2-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p2-r1-5', (12, 17), (2, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
