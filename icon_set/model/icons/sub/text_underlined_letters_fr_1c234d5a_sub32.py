"""Independent 32px profile of text-underlined-letters-fr-1c234d5a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '1c234d5a-675f-46f8-98db-4cf6d3b23336'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letters-fr-1c234d5a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1c234d5a-675f-46f8-98db-4cf6d3b23336', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/fr (text u)_1c234d5a-675f-46f8-98db-4cf6d3b23336.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letters-fr-1c234d5a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-f-uppercase', 'letter-r')
REFERENCE_EXPORT_SHA256 = 'b3570139df469a34e22dcf83c39081cbdee658ebd5b69af9de58e8f298bbcc63'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letters-fr-1c234d5a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 27
    text_ink_bounds = (0.0, 0.0, 27.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (25, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (20, 8), (20, 12))
        self.add_line('p2-r1-2', (20, 12), (20, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (20, 12), ((20, 10), (22, 8), (24, 8)))
        self.add_line('p3-r1-2', (24, 8), (25, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (14, 2), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (2, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (2, 12), (12, 12))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
