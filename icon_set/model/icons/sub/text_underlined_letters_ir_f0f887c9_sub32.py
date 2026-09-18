"""Independent 32px profile of text-underlined-letters-ir-f0f887c9.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'f0f887c9-5e62-4314-84c5-4a695ee10767'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letters-ir-f0f887c9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f0f887c9-5e62-4314-84c5-4a695ee10767', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/ir (text u)_f0f887c9-5e62-4314-84c5-4a695ee10767.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letters-ir-f0f887c9',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-i-uppercase', 'letter-r')
REFERENCE_EXPORT_SHA256 = 'dbafcf81b03e3d6586967464614c3569a65efaee9b7124925a584f2d00bd2867'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letters-ir-f0f887c9-sub32'
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
        self.add_line('p2-r1-1', (15, 8), (15, 12))
        self.add_line('p2-r1-2', (15, 12), (15, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (15, 12), ((15, 10), (17, 8), (19, 8)))
        self.add_line('p3-r1-2', (19, 8), (20, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 2), (8, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (5, 2), (5, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (2, 21), (8, 21))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
