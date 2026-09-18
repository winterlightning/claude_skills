"""Independent 32px profile of text-underlined-uppercase-letter-n-fd05a265.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'fd05a265-b84e-4457-8155-b0fd7a2b9504'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-uppercase-letter-n-fd05a265.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fd05a265-b84e-4457-8155-b0fd7a2b9504', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/n (text u)_fd05a265-b84e-4457-8155-b0fd7a2b9504.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-uppercase-letter-n-fd05a265',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-n-uppercase',)
REFERENCE_EXPORT_SHA256 = 'ac7516b038af0a2bd8f599760b1b5c98c3199850f9e53899257032e6bb4502fc'

class Drawing(TextSub32):
    icon_id = 'text-underlined-uppercase-letter-n-fd05a265-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 18
    text_ink_bounds = (0.0, 0.0, 18.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (16, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 21), (2, 2))
        self.add_line('p2-r1-2', (2, 2), (16, 21))
        self.add_line('p2-r1-3', (16, 21), (16, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
