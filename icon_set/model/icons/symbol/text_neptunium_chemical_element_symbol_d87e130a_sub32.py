"""Independent 32px profile of text-neptunium-chemical-element-symbol-d87e130a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'd87e130a-25da-498e-924b-ceb9d5c0a211'
SOURCE_PATH = 'icon_set/dist/text32/text-neptunium-chemical-element-symbol-d87e130a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d87e130a-25da-498e-924b-ceb9d5c0a211', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/np (text u)_d87e130a-25da-498e-924b-ceb9d5c0a211.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-neptunium-chemical-element-symbol-d87e130a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-n-uppercase', 'letter-p')
REFERENCE_EXPORT_SHA256 = '70bf0b3ff0a70a9b36605e1e81e03c363bf87d11e773c3d4fa58502746be2633'

class Drawing(TextSub32):
    icon_id = 'text-neptunium-chemical-element-symbol-d87e130a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 29
    text_ink_bounds = (0.0, 0.0, 29.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (27, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (18, 21), (18, 9))
        self.add_bezier('p2-r1-2', (18, 9), ((18, 9), (18, 9), (18, 9)))
        self.add_bezier('p2-r1-3', (18, 9), ((19, 7), (21, 6), (22, 6)))
        self.add_bezier('p2-r1-4', (22, 6), ((25, 6), (27, 8), (27, 11)))
        self.add_bezier('p2-r1-5', (27, 11), ((27, 14), (25, 16), (22, 16)))
        self.add_bezier('p2-r1-6', (22, 16), ((20, 16), (19, 15), (18, 13)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (2, 16), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (12, 16))
        self.add_line('p3-r1-3', (12, 16), (12, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
