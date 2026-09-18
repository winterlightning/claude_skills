"""Independent 32px profile of text-number-forty-symbol-74f712af.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '74f712af-249f-43fb-9887-0016aff122ef'
SOURCE_PATH = 'icon_set/dist/text32/text-number-forty-symbol-74f712af.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('74f712af-249f-43fb-9887-0016aff122ef', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/40 (text)_74f712af-249f-43fb-9887-0016aff122ef.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-forty-symbol-74f712af',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-4', 'digit-0')
REFERENCE_EXPORT_SHA256 = 'faea4f4587647e64ec1ab6f7b94d26f9ccde0da107289ae12be6942188d4bb56'

class Drawing(TextSub32):
    icon_id = 'text-number-forty-symbol-74f712af-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 55
    text_ink_bounds = (0.0, 0.0, 55.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (33, 10), (53, 10), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (53, 10), (53, 22))
        self.add_arc('p1-r1-3', (53, 22), (33, 22), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (33, 22), (33, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 2), (2, 20))
        self.add_bezier('p2-r1-2', (2, 20), ((2, 20), (2, 20), (3, 20)))
        self.add_line('p2-r1-3', (3, 20), (26, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (21, 2), (21, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
