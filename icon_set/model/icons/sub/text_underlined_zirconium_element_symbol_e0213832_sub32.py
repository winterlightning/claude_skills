"""Independent 32px profile of text-underlined-zirconium-element-symbol-e0213832.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'e0213832-3fb9-47a5-854c-3831a4aa94c2'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-zirconium-element-symbol-e0213832.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e0213832-3fb9-47a5-854c-3831a4aa94c2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/zr (text u)_e0213832-3fb9-47a5-854c-3831a4aa94c2.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-zirconium-element-symbol-e0213832',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-z-uppercase', 'letter-r')
REFERENCE_EXPORT_SHA256 = '8231340675c25f3e4e94b96e99596cf97cbf938a2e500dcb51e9cc57c9bab353'

class Drawing(TextSub32):
    icon_id = 'text-underlined-zirconium-element-symbol-e0213832-sub32'
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
        self.add_bezier('p3-r1-1', (20, 12), ((20, 10), (22, 8), (25, 8)))
        self.add_line('p3-r1-2', (25, 8), (25, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 2), (13, 2))
        self.add_bezier('p4-r1-2', (13, 2), ((13.666666666666666, 2), (14, 2), (14, 2)))
        self.add_bezier('p4-r1-3', (14, 2), ((14, 2.6666666666666665), (14, 3), (14, 3)))
        self.add_line('p4-r1-4', (14, 3), (2, 20))
        self.add_bezier('p4-r1-5', (2, 20), ((2, 20.666666666666668), (2, 21), (2, 21)))
        self.add_bezier('p4-r1-6', (2, 21), ((2, 21), (2.3333333333333335, 21), (3, 21)))
        self.add_line('p4-r1-7', (3, 21), (14, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
