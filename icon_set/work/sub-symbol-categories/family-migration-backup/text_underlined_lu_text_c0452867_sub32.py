"""Independent 32px profile of text-underlined-lu-text-c0452867.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'c0452867-4df0-44b3-9d49-f75cb007f9ca'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-lu-text-c0452867.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c0452867-4df0-44b3-9d49-f75cb007f9ca', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/lu (text u)_c0452867-4df0-44b3-9d49-f75cb007f9ca.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-lu-text-c0452867',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-l-uppercase', 'letter-u')
REFERENCE_EXPORT_SHA256 = '0fb0eb836a90d9415b4e48fe95cd7989e284009166afbe4cb9025f89d75b4174'

class Drawing(TextSub32):
    icon_id = 'text-underlined-lu-text-c0452867-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 32
    text_ink_bounds = (0.0, 0.0, 32.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (30, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (20, 8), (20, 16))
        self.add_bezier('p2-r1-2', (20, 16), ((20, 19), (22, 21), (25, 21)))
        self.add_bezier('p2-r1-3', (25, 21), ((28, 21), (30, 19), (30, 16)))
        self.add_line('p2-r1-4', (30, 16), (30, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 2), (2, 21))
        self.add_line('p3-r1-2', (2, 21), (13, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
