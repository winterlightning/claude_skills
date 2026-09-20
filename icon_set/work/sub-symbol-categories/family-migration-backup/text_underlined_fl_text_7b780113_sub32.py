"""Independent 32px profile of text-underlined-fl-text-7b780113.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '7b780113-07f9-474f-84b4-2fdfe5af7dba'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-fl-text-7b780113.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7b780113-07f9-474f-84b4-2fdfe5af7dba', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/fl (text u)_7b780113-07f9-474f-84b4-2fdfe5af7dba.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-fl-text-7b780113',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-f-uppercase', 'letter-l')
REFERENCE_EXPORT_SHA256 = '80c23192fc16cac10d57443dece75a10ad540f655ceb038473fe61d63e4d5121'

class Drawing(TextSub32):
    icon_id = 'text-underlined-fl-text-7b780113-sub32'
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
        self.add_line('p2-r1-1', (20, 3), (20, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (14, 2), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (2, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 12), (12, 12))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
