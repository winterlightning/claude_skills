"""Independent 32px profile of text-helium-chemical-element-symbol-5099a236.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '5099a236-69df-4d18-a978-5f74d95d8836'
SOURCE_PATH = 'icon_set/dist/text32/text-helium-chemical-element-symbol-5099a236.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5099a236-69df-4d18-a978-5f74d95d8836', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/he (text u)_5099a236-69df-4d18-a978-5f74d95d8836.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-helium-chemical-element-symbol-5099a236',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-h-uppercase', 'letter-e')
REFERENCE_EXPORT_SHA256 = '5dbc024720b882bd1780415f33ad51ba9f123bae0cd593ae91718f7a598416cc'

class Drawing(TextSub32):
    icon_id = 'text-helium-chemical-element-symbol-5099a236-sub32'
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
        self.add_bezier('p2-r1-1', (36, 15), ((36, 11), (33, 8), (29, 8)))
        self.add_bezier('p2-r1-2', (29, 8), ((25, 8), (22, 11), (22, 15)))
        self.add_bezier('p2-r1-3', (22, 15), ((22, 18), (25, 21), (29, 21)))
        self.add_bezier('p2-r1-4', (29, 21), ((32, 21), (34, 20), (35, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (22, 15), (36, 15))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 2), (2, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (16, 2), (16, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (2, 12), (16, 12))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
