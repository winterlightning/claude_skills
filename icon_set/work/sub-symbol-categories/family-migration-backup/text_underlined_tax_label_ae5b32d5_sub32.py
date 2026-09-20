"""Independent 32px profile of text-underlined-tax-label-ae5b32d5.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'ae5b32d5-6a5b-443a-b623-973e37a4c832'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-tax-label-ae5b32d5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ae5b32d5-6a5b-443a-b623-973e37a4c832', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/tax (text u)_ae5b32d5-6a5b-443a-b623-973e37a4c832.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-tax-label-ae5b32d5',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-t-uppercase', 'letter-a-uppercase', 'letter-x-uppercase')
REFERENCE_EXPORT_SHA256 = '7d385ab3cb86ce16e39364006fc456e36803d418ab474df2d7727c7c58c4665f'

class Drawing(TextSub32):
    icon_id = 'text-underlined-tax-label-ae5b32d5-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 60
    text_ink_bounds = (0.0, 0.0, 60.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (58, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (44, 2), (58, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (58, 2), (44, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (24, 21), (30, 3))
        self.add_bezier('p4-r1-2', (30, 3), ((30, 2.3333333333333335), (30.333333333333332, 2), (31, 2)))
        self.add_bezier('p4-r1-3', (31, 2), ((31, 2), (31, 2.3333333333333335), (31, 3)))
        self.add_line('p4-r1-4', (31, 3), (38, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (26, 13), (35, 13))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (2, 2), (17, 2))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (9, 2), (9, 21))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
