"""Independent 32px profile of text-underlined-ytterbium-chemical-symbol-d61f0e28.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'd61f0e28-5f09-40c3-ac3c-a8b0adb447e5'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-ytterbium-chemical-symbol-d61f0e28.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d61f0e28-5f09-40c3-ac3c-a8b0adb447e5', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/yb (text u)_d61f0e28-5f09-40c3-ac3c-a8b0adb447e5.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-ytterbium-chemical-symbol-d61f0e28',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-y-uppercase', 'letter-b')
REFERENCE_EXPORT_SHA256 = 'cca53ec8b964518b893ec127ced17659ffe48310f25057796f4ab544bf300d7e'

class Drawing(TextSub32):
    icon_id = 'text-underlined-ytterbium-chemical-symbol-d61f0e28-sub32'
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
        self.add_bezier('p2-r1-1', (24, 18), ((25, 20), (27, 21), (29, 21)))
        self.add_bezier('p2-r1-2', (29, 21), ((33, 21), (36, 18), (36, 15)))
        self.add_bezier('p2-r1-3', (36, 15), ((36, 11), (33, 8), (29, 8)))
        self.add_bezier('p2-r1-4', (29, 8), ((27, 8), (25, 9), (24, 11)))
        self.add_bezier('p2-r1-5', (24, 11), ((24, 11), (24, 11), (24, 12)))
        self.add_line('p2-r1-6', (24, 12), (24, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (24, 12), (24, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 2), (9, 12))
        self.add_line('p4-r1-2', (9, 12), (17, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (9, 12), (9, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p2-r1-5', 'p3-r1-1')
        self.relate("connect", 'p2-r1-6', 'p3-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-2', 'p5-r1-1')
