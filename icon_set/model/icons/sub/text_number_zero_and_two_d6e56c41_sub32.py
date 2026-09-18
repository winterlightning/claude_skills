"""Independent 32px profile of text-number-zero-and-two-d6e56c41.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'd6e56c41-6c89-4f3e-907d-b0dd5183d961'
SOURCE_PATH = 'icon_set/dist/text32/text-number-zero-and-two-d6e56c41.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d6e56c41-6c89-4f3e-907d-b0dd5183d961', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/O2_d6e56c41-6c89-4f3e-907d-b0dd5183d961.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-zero-and-two-d6e56c41',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-0', 'digit-2')
REFERENCE_EXPORT_SHA256 = '4dd1877ef201e4ba241fc25c7dd048a8dff533e89e92deff9dfec26cdaeafed7'

class Drawing(TextSub32):
    icon_id = 'text-number-zero-and-two-d6e56c41-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 51
    text_ink_bounds = (0.0, 0.0, 51.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (29, 2), (43, 2))
        self.add_bezier('p1-r1-2', (43, 2), ((47, 2), (49, 5), (49, 8)))
        self.add_bezier('p1-r1-3', (49, 8), ((49, 9), (48, 11), (46, 12)))
        self.add_line('p1-r1-4', (46, 12), (33, 21))
        self.add_bezier('p1-r1-5', (33, 21), ((31, 23), (29, 25), (29, 28)))
        self.add_line('p1-r1-6', (29, 28), (29, 29))
        self.add_bezier('p1-r1-7', (29, 29), ((29, 29), (30, 30), (31, 30)))
        self.add_line('p1-r1-8', (31, 30), (49, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_arc('p2-r1-1', (2, 10), (21, 10), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-2', (21, 10), (21, 22))
        self.add_arc('p2-r1-3', (21, 22), (2, 22), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (2, 22), (2, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
