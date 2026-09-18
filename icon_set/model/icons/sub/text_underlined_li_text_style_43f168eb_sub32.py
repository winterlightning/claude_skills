"""Independent 32px profile of text-underlined-li-text-style-43f168eb.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '43f168eb-1209-45f0-a92d-98e78f0e0624'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-li-text-style-43f168eb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('43f168eb-1209-45f0-a92d-98e78f0e0624', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/li (text u)_43f168eb-1209-45f0-a92d-98e78f0e0624.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-li-text-style-43f168eb',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-l-uppercase', 'letter-i')
REFERENCE_EXPORT_SHA256 = 'fc18cb0293ef77ed3a0e6639563fa1af8eb72de4d03207c654908c1a62bbf6d3'

class Drawing(TextSub32):
    icon_id = 'text-underlined-li-text-style-43f168eb-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 22
    text_ink_bounds = (0.0, 0.0, 22.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (20, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (20, 2), (20, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (20, 8), (20, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 2), (2, 21))
        self.add_line('p4-r1-2', (2, 21), (13, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
