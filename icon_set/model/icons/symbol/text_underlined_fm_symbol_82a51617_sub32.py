"""Independent 32px profile of text-underlined-fm-symbol-82a51617.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '82a51617-1848-4fd3-a632-11bc61dcc756'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-fm-symbol-82a51617.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('82a51617-1848-4fd3-a632-11bc61dcc756', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/fm (text u)_82a51617-1848-4fd3-a632-11bc61dcc756.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-fm-symbol-82a51617',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-f-uppercase', 'letter-m')
REFERENCE_EXPORT_SHA256 = 'b4f1d23de99e60806675e29b3f837e3b5387d31572af16a6c337bb5d88aba05f'

class Drawing(TextSub32):
    icon_id = 'text-underlined-fm-symbol-82a51617-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 41
    text_ink_bounds = (0.0, 0.0, 41.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (39, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (30, 13), (30, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (20, 21), (20, 13))
        self.add_bezier('p3-r1-2', (20, 13), ((20, 10), (22, 8), (25, 8)))
        self.add_bezier('p3-r1-3', (25, 8), ((28, 8), (30, 10), (30, 13)))
        self.add_bezier('p3-r1-4', (30, 13), ((30, 10), (32, 8), (35, 8)))
        self.add_bezier('p3-r1-5', (35, 8), ((37, 8), (39, 10), (39, 13)))
        self.add_line('p3-r1-6', (39, 13), (39, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.add_line('p4-r1-1', (14, 2), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (2, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (2, 12), (12, 12))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-3')
        self.relate('connect', 'p2-r1-1', 'p3-r1-4')
