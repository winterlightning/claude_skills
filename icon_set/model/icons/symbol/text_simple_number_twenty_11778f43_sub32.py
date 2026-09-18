"""Independent 32px profile of text-simple-number-twenty-11778f43.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '11778f43-e4ae-47e0-a607-32a2e3ab7086'
SOURCE_PATH = 'icon_set/dist/text32/text-simple-number-twenty-11778f43.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('11778f43-e4ae-47e0-a607-32a2e3ab7086', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/20 (text)_11778f43-e4ae-47e0-a607-32a2e3ab7086.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-simple-number-twenty-11778f43',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-2', 'digit-0')
REFERENCE_EXPORT_SHA256 = 'db2c16153c33328dfd570550effaf1dd1fa348b66a139ab14e9c80111e5a7be7'

class Drawing(TextSub32):
    icon_id = 'text-simple-number-twenty-11778f43-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
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
        self.add_line('p2-r1-1', (2, 2), (16, 2))
        self.add_bezier('p2-r1-2', (16, 2), ((19, 2), (21, 5), (21, 8)))
        self.add_bezier('p2-r1-3', (21, 8), ((21, 9), (21, 11), (19, 12)))
        self.add_line('p2-r1-4', (19, 12), (6, 21))
        self.add_bezier('p2-r1-5', (6, 21), ((3, 23), (2, 25), (2, 28)))
        self.add_line('p2-r1-6', (2, 28), (2, 29))
        self.add_bezier('p2-r1-7', (2, 29), ((2, 29), (3, 30), (3, 30)))
        self.add_line('p2-r1-8', (3, 30), (22, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
