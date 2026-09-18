"""Independent 32px profile of text-underlined-letter-p-f4ccc80a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'f4ccc80a-2c90-4322-986f-12721c0cba8d'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letter-p-f4ccc80a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f4ccc80a-2c90-4322-986f-12721c0cba8d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/p (text u)_f4ccc80a-2c90-4322-986f-12721c0cba8d.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letter-p-f4ccc80a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase',)
REFERENCE_EXPORT_SHA256 = '09ff2ca0bbf5f2da451814d5906a34a6a6aa50203d529e86be4b0a56d372b8a5'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letter-p-f4ccc80a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 17
    text_ink_bounds = (0.0, 0.0, 17.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (15, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 21), (2, 2))
        self.add_line('p2-r1-2', (2, 2), (9, 2))
        self.add_bezier('p2-r1-3', (9, 2), ((13, 2), (15, 5), (15, 7)))
        self.add_bezier('p2-r1-4', (15, 7), ((15, 10), (13, 12), (9, 12)))
        self.add_line('p2-r1-5', (9, 12), (2, 12))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
