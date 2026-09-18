"""Independent 32px profile of text-number-one-hundred-97f9cba2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '97f9cba2-d0f7-48f9-8122-045af66053d3'
SOURCE_PATH = 'icon_set/dist/text32/text-number-one-hundred-97f9cba2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('97f9cba2-d0f7-48f9-8122-045af66053d3', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/100 (text)_97f9cba2-d0f7-48f9-8122-045af66053d3.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-one-hundred-97f9cba2',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-1', 'digit-0', 'digit-0')
REFERENCE_EXPORT_SHA256 = 'e6bebcd7c22242a5acc606c16108a3c9db711d888a8fef3206f541bf8e05ef3c'

class Drawing(TextSub32):
    icon_id = 'text-number-one-hundred-97f9cba2-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 72
    text_ink_bounds = (0.0, 0.0, 72.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (50, 10), (70, 10), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (70, 10), (70, 22))
        self.add_arc('p1-r1-3', (70, 22), (50, 22), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (50, 22), (50, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (23, 10), (43, 10), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-2', (43, 10), (43, 22))
        self.add_arc('p2-r1-3', (43, 22), (23, 22), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (23, 22), (23, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (9, 30), (9, 3))
        self.add_bezier('p3-r1-2', (9, 3), ((9, 2), (8, 2), (8, 2)))
        self.add_line('p3-r1-3', (8, 2), (2, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 30), (15, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
