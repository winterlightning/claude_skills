"""Independent 32px profile of text-the-number-ninety-f4fa98b8.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'f4fa98b8-6d5a-4011-a4ce-b31c75e91896'
SOURCE_PATH = 'icon_set/dist/text32/text-the-number-ninety-f4fa98b8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f4fa98b8-6d5a-4011-a4ce-b31c75e91896', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/90_f4fa98b8-6d5a-4011-a4ce-b31c75e91896.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-the-number-ninety-f4fa98b8',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-9', 'digit-0')
REFERENCE_EXPORT_SHA256 = '84a925723238fc7b75fcee7e395c255a52a7fc18ab0cd5e73e594452f8f9f089'

class Drawing(TextSub32):
    icon_id = 'text-the-number-ninety-f4fa98b8-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 51
    text_ink_bounds = (0.0, 0.0, 51.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (29, 10), (49, 10), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (49, 10), (49, 22))
        self.add_arc('p1-r1-3', (49, 22), (29, 22), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (29, 22), (29, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (2, 10), (22, 10), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_arc('p2-r1-2', (22, 10), (2, 10), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (22, 10), (22, 20))
        self.add_bezier('p3-r1-2', (22, 20), ((22, 26), (17, 30), (12, 30)))
        self.add_line('p3-r1-3', (12, 30), (5, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
