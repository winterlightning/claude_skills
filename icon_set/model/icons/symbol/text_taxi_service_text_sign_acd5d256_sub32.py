"""Independent 32px profile of text-taxi-service-text-sign-acd5d256.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'acd5d256-9232-4f53-adda-670c60675231'
SOURCE_PATH = 'icon_set/dist/text32/text-taxi-service-text-sign-acd5d256.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('acd5d256-9232-4f53-adda-670c60675231', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/taxi (text)_acd5d256-9232-4f53-adda-670c60675231.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-taxi-service-text-sign-acd5d256',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-t-uppercase', 'letter-a-uppercase', 'letter-x-uppercase', 'letter-i-uppercase')
REFERENCE_EXPORT_SHA256 = '2f0a6616de71eb97144418984419861673695d93c22761ecec10477bae1b6834'

class Drawing(TextSub32):
    icon_id = 'text-taxi-service-text-sign-acd5d256-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 100
    text_ink_bounds = (0.0, 0.0, 100.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (88, 2), (98, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (93, 2), (93, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (88, 30), (98, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (60, 2), (81, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (81, 2), (60, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (32, 30), (41, 3))
        self.add_bezier('p6-r1-2', (41, 3), ((41.666666666666664, 2.3333333333333335), (42, 2), (42, 2)))
        self.add_bezier('p6-r1-3', (42, 2), ((42.666666666666664, 2), (43, 2.3333333333333335), (43, 3)))
        self.add_line('p6-r1-4', (43, 3), (53, 30))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', closed=False)
        self.add_line('p7-r1-1', (36, 18), (48, 18))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (2, 2), (24, 2))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (13, 2), (13, 30))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
