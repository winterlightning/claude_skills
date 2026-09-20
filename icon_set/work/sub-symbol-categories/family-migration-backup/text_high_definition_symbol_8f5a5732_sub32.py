"""Independent 32px profile of text-high-definition-symbol-8f5a5732.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '8f5a5732-3ed8-45a3-b9a3-c76fa02c860a'
SOURCE_PATH = 'icon_set/dist/text32/text-high-definition-symbol-8f5a5732.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8f5a5732-3ed8-45a3-b9a3-c76fa02c860a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/HD (text)_8f5a5732-3ed8-45a3-b9a3-c76fa02c860a.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-high-definition-symbol-8f5a5732',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-h-uppercase', 'letter-d-uppercase')
REFERENCE_EXPORT_SHA256 = '2ad4cab52b44f095d01a87b451d0bc4ca16eaab2cace1fb98a54287f7def905a'

class Drawing(TextSub32):
    icon_id = 'text-high-definition-symbol-8f5a5732-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 52
    text_ink_bounds = (0.0, 0.0, 52.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (30, 2), (38, 2))
        self.add_bezier('p1-r1-2', (38, 2), ((46, 2), (50, 9), (50, 16)))
        self.add_bezier('p1-r1-3', (50, 16), ((50, 23), (46, 30), (38, 30)))
        self.add_line('p1-r1-4', (38, 30), (30, 30))
        self.add_line('p1-r1-5', (30, 30), (30, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (2, 2), (2, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (22, 2), (22, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 16), (22, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
