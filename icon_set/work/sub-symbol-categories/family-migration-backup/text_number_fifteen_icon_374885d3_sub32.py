"""Independent 32px profile of text-number-fifteen-icon-374885d3.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '374885d3-0df3-4239-bb81-0f1c062cd2fb'
SOURCE_PATH = 'icon_set/dist/text32/text-number-fifteen-icon-374885d3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('374885d3-0df3-4239-bb81-0f1c062cd2fb', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/15_374885d3-0df3-4239-bb81-0f1c062cd2fb.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-fifteen-icon-374885d3',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-1', 'digit-5')
REFERENCE_EXPORT_SHA256 = '41a37f755b50e58d7fa399fde93c9bf407e48713f44a6d46e9126043b055c007'

class Drawing(TextSub32):
    icon_id = 'text-number-fifteen-icon-374885d3-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 45
    text_ink_bounds = (0.0, 0.0, 45.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (40, 2), (24, 2))
        self.add_bezier('p1-r1-2', (24, 2), ((23, 2), (23, 2), (23, 3)))
        self.add_line('p1-r1-3', (23, 3), (23, 13))
        self.add_bezier('p1-r1-4', (23, 13), ((23, 13), (23, 14), (24, 14)))
        self.add_line('p1-r1-5', (24, 14), (34, 14))
        self.add_bezier('p1-r1-6', (34, 14), ((39, 14), (43, 18), (43, 22)))
        self.add_bezier('p1-r1-7', (43, 22), ((43, 24), (42, 26), (40, 28)))
        self.add_bezier('p1-r1-8', (40, 28), ((39, 29), (37, 30), (34, 30)))
        self.add_line('p1-r1-9', (34, 30), (24, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_line('p2-r1-1', (9, 30), (9, 3))
        self.add_bezier('p2-r1-2', (9, 3), ((9, 2), (8, 2), (8, 2)))
        self.add_line('p2-r1-3', (8, 2), (2, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (2, 30), (15, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
