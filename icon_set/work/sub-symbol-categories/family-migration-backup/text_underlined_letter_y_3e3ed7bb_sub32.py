"""Independent 32px profile of text-underlined-letter-y-3e3ed7bb.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '3e3ed7bb-d89b-4e70-8626-86bf89ecf115'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letter-y-3e3ed7bb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3e3ed7bb-d89b-4e70-8626-86bf89ecf115', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/y (text u)_3e3ed7bb-d89b-4e70-8626-86bf89ecf115.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letter-y-3e3ed7bb',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-y-uppercase',)
REFERENCE_EXPORT_SHA256 = 'd3a4f6bab795939f8b7539b9fc0065e687815ec9d0b1a76b24587cc4d383f771'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letter-y-3e3ed7bb-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 19
    text_ink_bounds = (0.0, 0.0, 19.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (17, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 2), (9, 12))
        self.add_line('p2-r1-2', (9, 12), (17, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (9, 12), (9, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
