"""Independent 32px profile of text-zinc-symbol-with-bottom-bar-f3b84a94.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'f3b84a94-f2c6-4680-953d-5d9f2f093b55'
SOURCE_PATH = 'icon_set/dist/text32/text-zinc-symbol-with-bottom-bar-f3b84a94.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f3b84a94-f2c6-4680-953d-5d9f2f093b55', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/zn (text u)_f3b84a94-f2c6-4680-953d-5d9f2f093b55.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-zinc-symbol-with-bottom-bar-f3b84a94',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-z-uppercase', 'letter-n')
REFERENCE_EXPORT_SHA256 = '44c8e09a4fa19ec7af1ef4ada4eee8bcb48d33a8fd108405e40cbefbeca01a26'

class Drawing(TextSub32):
    icon_id = 'text-zinc-symbol-with-bottom-bar-f3b84a94-sub32'
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
        self.add_line('p3-r1-1', (2, 2), (13, 2))
        self.add_bezier('p3-r1-2', (13, 2), ((13.666666666666666, 2), (14, 2), (14, 2)))
        self.add_bezier('p3-r1-3', (14, 2), ((14, 2.6666666666666665), (14, 3), (14, 3)))
        self.add_line('p3-r1-4', (14, 3), (2, 20))
        self.add_bezier('p3-r1-5', (2, 20), ((2, 20.666666666666668), (2, 21), (2, 21)))
        self.add_bezier('p3-r1-6', (2, 21), ((2, 21), (2.3333333333333335, 21), (3, 21)))
        self.add_line('p3-r1-7', (3, 21), (14, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
