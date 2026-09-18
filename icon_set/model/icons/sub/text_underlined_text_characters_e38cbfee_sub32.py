"""Independent 32px profile of text-underlined-text-characters-e38cbfee.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'e38cbfee-45cd-445c-978d-e64790667fa5'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-text-characters-e38cbfee.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e38cbfee-45cd-445c-978d-e64790667fa5', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/am (text u)_e38cbfee-45cd-445c-978d-e64790667fa5.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-text-characters-e38cbfee',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-m')
REFERENCE_EXPORT_SHA256 = 'd3314a355cf96dab6d4e3579efd1f1dc016ea5b3f47fccb475652f73d7084e4f'

class Drawing(TextSub32):
    icon_id = 'text-underlined-text-characters-e38cbfee-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 44
    text_ink_bounds = (0.0, 0.0, 44.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (42, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (32, 13), (32, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (23, 21), (23, 13))
        self.add_bezier('p3-r1-2', (23, 13), ((23, 10), (25, 8), (28, 8)))
        self.add_bezier('p3-r1-3', (28, 8), ((30, 8), (32, 10), (32, 13)))
        self.add_bezier('p3-r1-4', (32, 13), ((32, 10), (35, 8), (37, 8)))
        self.add_bezier('p3-r1-5', (37, 8), ((40, 8), (42, 10), (42, 13)))
        self.add_line('p3-r1-6', (42, 13), (42, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.add_line('p4-r1-1', (2, 21), (8, 3))
        self.add_bezier('p4-r1-2', (8, 3), ((8.666666666666666, 2.3333333333333335), (9, 2), (9, 2)))
        self.add_bezier('p4-r1-3', (9, 2), ((9.666666666666666, 2), (10, 2.3333333333333335), (10, 3)))
        self.add_line('p4-r1-4', (10, 3), (16, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (5, 13), (13, 13))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-3')
        self.relate("connect", 'p2-r1-1', 'p3-r1-4')
