"""Independent 32px profile of text-underlined-db-text-d98f0429.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'd98f0429-d034-4d6d-86d2-90889d17d1df'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-db-text-d98f0429.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d98f0429-d034-4d6d-86d2-90889d17d1df', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/db (text u)_d98f0429-d034-4d6d-86d2-90889d17d1df.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-db-text-d98f0429',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-d-uppercase', 'letter-b')
REFERENCE_EXPORT_SHA256 = '86694783051c9f6404328743e99e2c318a6d34062fbaddd356f8a825fe08f06f'

class Drawing(TextSub32):
    icon_id = 'text-underlined-db-text-d98f0429-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 36
    text_ink_bounds = (0.0, 0.0, 36.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (34, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (22, 18), ((23, 20), (25, 21), (28, 21)))
        self.add_bezier('p2-r1-2', (28, 21), ((31, 21), (34, 18), (34, 15)))
        self.add_bezier('p2-r1-3', (34, 15), ((34, 11), (31, 8), (28, 8)))
        self.add_bezier('p2-r1-4', (28, 8), ((25, 8), (23, 9), (22, 11)))
        self.add_bezier('p2-r1-5', (22, 11), ((22, 11), (22, 11), (22, 12)))
        self.add_line('p2-r1-6', (22, 12), (22, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (22, 12), (22, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 2), (7, 2))
        self.add_bezier('p4-r1-2', (7, 2), ((13, 2), (15, 7), (15, 12)))
        self.add_bezier('p4-r1-3', (15, 12), ((15, 16), (13, 21), (7, 21)))
        self.add_line('p4-r1-4', (7, 21), (2, 21))
        self.add_line('p4-r1-5', (2, 21), (2, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.relate("connect", 'p2-r1-5', 'p3-r1-1')
        self.relate("connect", 'p2-r1-6', 'p3-r1-1')
