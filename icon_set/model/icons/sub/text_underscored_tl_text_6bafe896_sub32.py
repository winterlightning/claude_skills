"""Independent 32px profile of text-underscored-tl-text-6bafe896.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '6bafe896-295a-4a17-b0b3-eb41f6bcd555'
SOURCE_PATH = 'icon_set/dist/text32/text-underscored-tl-text-6bafe896.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6bafe896-295a-4a17-b0b3-eb41f6bcd555', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/tl (text u)_6bafe896-295a-4a17-b0b3-eb41f6bcd555.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underscored-tl-text-6bafe896',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-t-uppercase', 'letter-l')
REFERENCE_EXPORT_SHA256 = 'a5406c6a46c39539dc759af33d52e2d17cb5c902d160ca2bf1c2fd6a3d3972db'

class Drawing(TextSub32):
    icon_id = 'text-underscored-tl-text-6bafe896-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 26
    text_ink_bounds = (0.0, 0.0, 26.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (24, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (24, 3), (24, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 2), (17, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (9, 2), (9, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
