"""Independent 32px profile of text-number-fifty-three-74616fe2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '74616fe2-7fa5-4153-90e2-d47735996627'
SOURCE_PATH = 'icon_set/dist/text32/text-number-fifty-three-74616fe2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('74616fe2-7fa5-4153-90e2-d47735996627', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/53_74616fe2-7fa5-4153-90e2-d47735996627.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-fifty-three-74616fe2',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-5', 'digit-3')
REFERENCE_EXPORT_SHA256 = '0fab8b961244835eb0e57a109b4c2a96b92244220783cddcf8e1320f021b29ef'

class Drawing(TextSub32):
    icon_id = 'text-number-fifty-three-74616fe2-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 49
    text_ink_bounds = (0.0, 0.0, 49.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (29, 2), (40, 2))
        self.add_bezier('p1-r1-2', (40, 2), ((44, 2), (47, 5), (47, 9)))
        self.add_bezier('p1-r1-3', (47, 9), ((47, 13), (44, 16), (40, 16)))
        self.add_line('p1-r1-4', (40, 16), (36, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (37, 16), (40, 16))
        self.add_bezier('p2-r1-2', (40, 16), ((44, 16), (47, 19), (47, 23)))
        self.add_bezier('p2-r1-3', (47, 23), ((47, 27), (44, 30), (40, 30)))
        self.add_line('p2-r1-4', (40, 30), (29, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (19, 2), (3, 2))
        self.add_bezier('p3-r1-2', (3, 2), ((2, 2), (2, 2), (2, 3)))
        self.add_line('p3-r1-3', (2, 3), (2, 13))
        self.add_bezier('p3-r1-4', (2, 13), ((2, 13), (2, 14), (3, 14)))
        self.add_line('p3-r1-5', (3, 14), (13, 14))
        self.add_bezier('p3-r1-6', (13, 14), ((18, 14), (21, 18), (21, 22)))
        self.add_bezier('p3-r1-7', (21, 22), ((21, 24), (21, 26), (19, 28)))
        self.add_bezier('p3-r1-8', (19, 28), ((18, 29), (15, 30), (13, 30)))
        self.add_line('p3-r1-9', (13, 30), (3, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
