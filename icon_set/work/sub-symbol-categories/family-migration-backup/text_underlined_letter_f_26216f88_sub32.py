"""Independent 32px profile of text-underlined-letter-f-26216f88.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '26216f88-ff25-4f50-8150-083abc102041'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letter-f-26216f88.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('26216f88-ff25-4f50-8150-083abc102041', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/f (text u)_26216f88-ff25-4f50-8150-083abc102041.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letter-f-26216f88',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-f-uppercase',)
REFERENCE_EXPORT_SHA256 = '2facace14b6350984262d35731eba45a0899521e493febd041368b62acbbbd50'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letter-f-26216f88-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 16
    text_ink_bounds = (0.0, 0.0, 16.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (14, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (14, 2), (2, 2))
        self.add_line('p2-r1-2', (2, 2), (2, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 12), (12, 12))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
