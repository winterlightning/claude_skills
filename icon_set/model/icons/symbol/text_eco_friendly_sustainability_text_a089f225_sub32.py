"""Independent 32px profile of text-eco-friendly-sustainability-text-a089f225.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'a089f225-71e3-44d9-b16d-3c57fb7884fb'
SOURCE_PATH = 'icon_set/dist/text32/text-eco-friendly-sustainability-text-a089f225.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a089f225-71e3-44d9-b16d-3c57fb7884fb', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/eco (text)_a089f225-71e3-44d9-b16d-3c57fb7884fb.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-eco-friendly-sustainability-text-a089f225',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-e-uppercase', 'letter-c-uppercase', 'letter-o-uppercase')
REFERENCE_EXPORT_SHA256 = '18a00a7d02338b9d7d693af735b5376778bf95f80dbc70fcb61c6bb27029d1f3'

class Drawing(TextSub32):
    icon_id = 'text-eco-friendly-sustainability-text-a089f225-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 74
    text_ink_bounds = (0.0, 0.0, 74.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (52, 16), (72, 16), radius_x=10, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('p1-r1-2', (72, 16), (52, 16), radius_x=10, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (44, 6), (44, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (19, 2), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (2, 30))
        self.add_line('p3-r1-3', (2, 30), (19, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 16), (16, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
