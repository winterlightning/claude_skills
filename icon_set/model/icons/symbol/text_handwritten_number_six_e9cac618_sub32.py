"""Independent 32px profile of text-handwritten-number-six-e9cac618.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'e9cac618-2327-4516-b01d-1f8392db0bc1'
SOURCE_PATH = 'icon_set/dist/text32/text-handwritten-number-six-e9cac618.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e9cac618-2327-4516-b01d-1f8392db0bc1', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/6_e9cac618-2327-4516-b01d-1f8392db0bc1.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-handwritten-number-six-e9cac618',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-6',)
REFERENCE_EXPORT_SHA256 = '16f6118fe0f986c99419d01b3136baed9d39929e494e47cdd2fb2045c4bd6023'

class Drawing(TextSub32):
    icon_id = 'text-handwritten-number-six-e9cac618-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 24
    text_ink_bounds = (0.0, 0.0, 24.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (2, 22), (22, 22), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_arc('p1-r1-2', (22, 22), (2, 22), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 22), (2, 12))
        self.add_bezier('p2-r1-2', (2, 12), ((2, 6), (6, 2), (12, 2)))
        self.add_line('p2-r1-3', (12, 2), (19, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
