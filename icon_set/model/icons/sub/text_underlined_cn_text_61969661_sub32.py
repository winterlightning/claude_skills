"""Independent 32px profile of text-underlined-cn-text-61969661.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '61969661-3096-4c1e-aeb5-ef43f7fc457f'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-cn-text-61969661.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('61969661-3096-4c1e-aeb5-ef43f7fc457f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/cn (text u)_61969661-3096-4c1e-aeb5-ef43f7fc457f.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-cn-text-61969661',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-n')
REFERENCE_EXPORT_SHA256 = '8608eb067ce4a14171e9683ed0625acaad9dd4ef140e2a26b0e0fc095d1ff6a8'

class Drawing(TextSub32):
    icon_id = 'text-underlined-cn-text-61969661-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 33
    text_ink_bounds = (0.0, 0.0, 33.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (31, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (31, 21), (31, 13))
        self.add_bezier('p2-r1-2', (31, 13), ((31, 10), (29, 8), (26, 8)))
        self.add_bezier('p2-r1-3', (26, 8), ((23, 8), (20, 10), (20, 13)))
        self.add_line('p2-r1-4', (20, 13), (20, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (14, 5), ((12, 3), (11, 2), (9, 2)))
        self.add_bezier('p3-r1-2', (9, 2), ((6, 2), (2, 6), (2, 12)))
        self.add_bezier('p3-r1-3', (2, 12), ((2, 17), (6, 21), (9, 21)))
        self.add_bezier('p3-r1-4', (9, 21), ((11, 21), (12, 20), (14, 18)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
