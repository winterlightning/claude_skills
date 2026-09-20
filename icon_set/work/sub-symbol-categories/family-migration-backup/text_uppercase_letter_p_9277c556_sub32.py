"""Independent 32px profile of text-uppercase-letter-p-9277c556.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '9277c556-7da0-4c0f-a606-79c9c8aa82aa'
SOURCE_PATH = 'icon_set/dist/text32/text-uppercase-letter-p-9277c556.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9277c556-7da0-4c0f-a606-79c9c8aa82aa', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/P (text)_9277c556-7da0-4c0f-a606-79c9c8aa82aa.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-uppercase-letter-p-9277c556', 'text/text-capital-letter-p-symbol-8eb10225', 'text/text-uppercase-letter-p-symbol-309b4b8c')
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase',)
REFERENCE_EXPORT_SHA256 = '1346178fb234aa760221eec4f8346e6256d3f70b932ac0947dcaea664de91346'

class Drawing(TextSub32):
    icon_id = 'text-uppercase-letter-p-9277c556-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 23
    text_ink_bounds = (0.0, 0.0, 23.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (12, 2))
        self.add_bezier('p1-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p1-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p1-r1-5', (12, 17), (2, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
