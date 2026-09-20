"""Independent 32px profile of text-chromium-chemical-element-symbol-f9943c6a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'f9943c6a-963e-4891-8cd7-67b63c8e6ccc'
SOURCE_PATH = 'icon_set/dist/text32/text-chromium-chemical-element-symbol-f9943c6a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f9943c6a-963e-4891-8cd7-67b63c8e6ccc', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/cr (text u)_f9943c6a-963e-4891-8cd7-67b63c8e6ccc.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-chromium-chemical-element-symbol-f9943c6a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-r')
REFERENCE_EXPORT_SHA256 = '35e1c71cc8335e62396753b71c605890ac480bba0e129e7b7bc2919948426fbb'

class Drawing(TextSub32):
    icon_id = 'text-chromium-chemical-element-symbol-f9943c6a-sub32'
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
        self.add_bezier('p4-r1-1', (14, 5), ((12, 3), (11, 2), (9, 2)))
        self.add_bezier('p4-r1-2', (9, 2), ((6, 2), (2, 6), (2, 12)))
        self.add_bezier('p4-r1-3', (2, 12), ((2, 17), (6, 21), (9, 21)))
        self.add_bezier('p4-r1-4', (9, 21), ((11, 21), (12, 20), (14, 18)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
