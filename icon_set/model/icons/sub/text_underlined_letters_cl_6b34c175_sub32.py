"""Independent 32px profile of text-underlined-letters-cl-6b34c175.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '6b34c175-a023-4179-a990-ffa2feecc154'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letters-cl-6b34c175.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6b34c175-a023-4179-a990-ffa2feecc154', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/cl (text u)_6b34c175-a023-4179-a990-ffa2feecc154.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letters-cl-6b34c175',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-l')
REFERENCE_EXPORT_SHA256 = '92150884d3f02bf9254dc0982017dd2a45198e9b721749c2d722e8111c920fff'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letters-cl-6b34c175-sub32'
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
        self.add_bezier('p3-r1-1', (14, 5), ((12, 3), (11, 2), (9, 2)))
        self.add_bezier('p3-r1-2', (9, 2), ((6, 2), (2, 6), (2, 12)))
        self.add_bezier('p3-r1-3', (2, 12), ((2, 17), (6, 21), (9, 21)))
        self.add_bezier('p3-r1-4', (9, 21), ((11, 21), (12, 20), (14, 18)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
