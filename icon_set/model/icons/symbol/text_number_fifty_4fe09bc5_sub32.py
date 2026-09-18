"""Independent 32px profile of text-number-fifty-4fe09bc5.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '4fe09bc5-d901-46d3-b7df-29f4ed696a4a'
SOURCE_PATH = 'icon_set/dist/text32/text-number-fifty-4fe09bc5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4fe09bc5-d901-46d3-b7df-29f4ed696a4a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/50 (text)_4fe09bc5-d901-46d3-b7df-29f4ed696a4a.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-fifty-4fe09bc5',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-5', 'digit-0')
REFERENCE_EXPORT_SHA256 = 'df413086ec9a3ee285e038acf8638bffebfbc9e17c8cec6d91a04a249072b7f5'

class Drawing(TextSub32):
    icon_id = 'text-number-fifty-4fe09bc5-sub32'
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
        self.add_line('p2-r1-1', (19, 2), (3, 2))
        self.add_bezier('p2-r1-2', (3, 2), ((2, 2), (2, 2), (2, 3)))
        self.add_line('p2-r1-3', (2, 3), (2, 13))
        self.add_bezier('p2-r1-4', (2, 13), ((2, 13), (2, 14), (3, 14)))
        self.add_line('p2-r1-5', (3, 14), (13, 14))
        self.add_bezier('p2-r1-6', (13, 14), ((18, 14), (21, 18), (21, 22)))
        self.add_bezier('p2-r1-7', (21, 22), ((21, 24), (21, 26), (19, 28)))
        self.add_bezier('p2-r1-8', (19, 28), ((18, 29), (15, 30), (13, 30)))
        self.add_line('p2-r1-9', (13, 30), (3, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', closed=False)
