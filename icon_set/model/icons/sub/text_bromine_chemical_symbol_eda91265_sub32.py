"""Independent 32px profile of text-bromine-chemical-symbol-eda91265.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'eda91265-1b5e-483f-8919-b0ad768010ea'
SOURCE_PATH = 'icon_set/dist/text32/text-bromine-chemical-symbol-eda91265.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('eda91265-1b5e-483f-8919-b0ad768010ea', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/Br_eda91265-1b5e-483f-8919-b0ad768010ea.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-bromine-chemical-symbol-eda91265', 'text/text-underlined-bromine-chemical-symbol-59fae115')
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-b-uppercase', 'letter-r')
REFERENCE_EXPORT_SHA256 = '3d6af9f4e273546aa84a6075b4ed40c1e7f7754ff1d9a90e08246efbe6cf8009'

class Drawing(TextSub32):
    icon_id = 'text-bromine-chemical-symbol-eda91265-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 28
    text_ink_bounds = (0.0, 0.0, 28.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (26, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (21, 8), (21, 12))
        self.add_line('p2-r1-2', (21, 12), (21, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (21, 12), ((21, 10), (23, 8), (25, 8)))
        self.add_line('p3-r1-2', (25, 8), (26, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
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
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-3')
        self.relate("connect", 'p4-r1-4', 'p5-r1-1')
        self.relate("connect", 'p4-r1-5', 'p5-r1-1')
