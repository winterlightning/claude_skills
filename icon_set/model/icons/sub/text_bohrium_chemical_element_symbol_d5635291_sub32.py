"""Independent 32px profile of text-bohrium-chemical-element-symbol-d5635291.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'd5635291-9570-40c9-ba89-ef57fb091088'
SOURCE_PATH = 'icon_set/dist/text32/text-bohrium-chemical-element-symbol-d5635291.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d5635291-9570-40c9-ba89-ef57fb091088', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/bh (text u)_d5635291-9570-40c9-ba89-ef57fb091088.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-bohrium-chemical-element-symbol-d5635291',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-b-uppercase', 'letter-h')
REFERENCE_EXPORT_SHA256 = '9f33d15749c6b9b675702438d5849073d6f1005812fa34645f21d8739d651aa6'

class Drawing(TextSub32):
    icon_id = 'text-bohrium-chemical-element-symbol-d5635291-sub32'
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
        self.add_line('p2-r1-1', (21, 2), (21, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (21, 14), ((21, 11), (24, 8), (28, 8)))
        self.add_bezier('p3-r1-2', (28, 8), ((31, 8), (34, 11), (34, 14)))
        self.add_line('p3-r1-3', (34, 14), (34, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 21), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (8, 2))
        self.add_bezier('p4-r1-3', (8, 2), ((12, 2), (14, 4), (14, 7)))
        self.add_bezier('p4-r1-4', (14, 7), ((14, 9), (12, 12), (8, 12)))
        self.add_line('p4-r1-5', (8, 12), (2, 12))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_bezier('p5-r1-1', (8, 12), ((13, 12), (15, 14), (15, 16)))
        self.add_bezier('p5-r1-2', (15, 16), ((15, 19), (13, 21), (8, 21)))
        self.add_line('p5-r1-3', (8, 21), (2, 21))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.relate("connect", 'p4-r1-1', 'p5-r1-3')
        self.relate("connect", 'p4-r1-4', 'p5-r1-1')
        self.relate("connect", 'p4-r1-5', 'p5-r1-1')
