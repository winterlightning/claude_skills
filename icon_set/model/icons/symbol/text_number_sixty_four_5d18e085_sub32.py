"""Independent 32px profile of text-number-sixty-four-5d18e085.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '5d18e085-8432-40df-9bf9-61ee5537075b'
SOURCE_PATH = 'icon_set/dist/text32/text-number-sixty-four-5d18e085.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5d18e085-8432-40df-9bf9-61ee5537075b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/64 (text)_5d18e085-8432-40df-9bf9-61ee5537075b.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-sixty-four-5d18e085',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-6', 'digit-4')
REFERENCE_EXPORT_SHA256 = 'dae08ba8116f3dbcada697f59b48650e075b1d1433d88b43e955b47afa90894c'

class Drawing(TextSub32):
    icon_id = 'text-number-sixty-four-5d18e085-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 55
    text_ink_bounds = (0.0, 0.0, 55.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (29, 2), (29, 20))
        self.add_bezier('p1-r1-2', (29, 20), ((29, 20), (30, 20), (30, 20)))
        self.add_line('p1-r1-3', (30, 20), (53, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (48, 2), (48, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (2, 22), (22, 22), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_arc('p3-r1-2', (22, 22), (2, 22), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 22), (2, 12))
        self.add_bezier('p4-r1-2', (2, 12), ((2, 6), (6, 2), (12, 2)))
        self.add_line('p4-r1-3', (12, 2), (19, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
