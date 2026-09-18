"""Independent 32px profile of text-404-page-not-found-error-b54c402a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'b54c402a-66b3-456f-ae3a-44c3e23e8c4c'
SOURCE_PATH = 'icon_set/dist/text32/text-404-page-not-found-error-b54c402a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b54c402a-66b3-456f-ae3a-44c3e23e8c4c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/404 XXX_b54c402a-66b3-456f-ae3a-44c3e23e8c4c.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-404-page-not-found-error-b54c402a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-4', 'digit-0', 'digit-4', 'letter-x-uppercase', 'letter-x-uppercase', 'letter-x-uppercase')
REFERENCE_EXPORT_SHA256 = '1f6af2cba8348fd97da7417f25478ebb20e69c61e8873420ff97248da8b58f37'

class Drawing(TextSub32):
    icon_id = 'text-404-page-not-found-error-b54c402a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 195
    text_ink_bounds = (0.0, 0.0, 194.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (172, 2), (192, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (192, 2), (172, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (141, 2), (162, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (162, 2), (141, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (111, 2), (131, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (131, 2), (111, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (66, 2), (66, 20))
        self.add_bezier('p7-r1-2', (66, 20), ((66, 20), (66, 20), (67, 20)))
        self.add_line('p7-r1-3', (67, 20), (90, 20))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', closed=False)
        self.add_line('p8-r1-1', (85, 2), (85, 30))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_bezier('p9-r1-1', (36, 10), ((36, 6), (40, 2), (46, 2)))
        self.add_bezier('p9-r1-2', (46, 2), ((51, 2), (56, 6), (56, 10)))
        self.add_line('p9-r1-3', (56, 10), (56, 22))
        self.add_bezier('p9-r1-4', (56, 22), ((56, 26), (51, 30), (46, 30)))
        self.add_bezier('p9-r1-5', (46, 30), ((40, 30), (36, 26), (36, 22)))
        self.add_line('p9-r1-6', (36, 22), (36, 10))
        self.add_contour('path-9-1', 'p9-r1-1', 'p9-r1-2', 'p9-r1-3', 'p9-r1-4', 'p9-r1-5', 'p9-r1-6', closed=False)
        self.add_line('p10-r1-1', (2, 2), (2, 20))
        self.add_bezier('p10-r1-2', (2, 20), ((2, 20), (2, 20), (3, 20)))
        self.add_line('p10-r1-3', (3, 20), (26, 20))
        self.add_contour('path-10-1', 'p10-r1-1', 'p10-r1-2', 'p10-r1-3', closed=False)
        self.add_line('p11-r1-1', (21, 2), (21, 30))
        self.add_contour('path-11-1', 'p11-r1-1', closed=False)
