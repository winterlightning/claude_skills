"""Independent 32px profile of text-ta-underlined-text-18d74860.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '18d74860-f1c9-4d7e-8d64-0337d5eeff19'
SOURCE_PATH = 'icon_set/dist/text32/text-ta-underlined-text-18d74860.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('18d74860-f1c9-4d7e-8d64-0337d5eeff19', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/ta (text u)_18d74860-f1c9-4d7e-8d64-0337d5eeff19.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-ta-underlined-text-18d74860',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-t-uppercase', 'letter-a')
REFERENCE_EXPORT_SHA256 = 'c4b3fece65bc8ab2c96d1d4c7107f04bb48f2bb9fc302a7bac45c2798152f31d'

class Drawing(TextSub32):
    icon_id = 'text-ta-underlined-text-18d74860-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 38
    text_ink_bounds = (0.0, 0.0, 38.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (36, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (36, 18), (36, 12))
        self.add_bezier('p2-r1-2', (36, 12), ((36, 11), (36, 11), (36, 11)))
        self.add_bezier('p2-r1-3', (36, 11), ((34, 9), (32, 8), (30, 8)))
        self.add_bezier('p2-r1-4', (30, 8), ((27, 8), (24, 11), (24, 15)))
        self.add_bezier('p2-r1-5', (24, 15), ((24, 18), (27, 21), (30, 21)))
        self.add_bezier('p2-r1-6', (30, 21), ((33, 21), (35, 20), (36, 18)))
        self.add_line('p2-r1-7', (36, 18), (36, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_line('p3-r1-1', (2, 2), (17, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (9, 2), (9, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
