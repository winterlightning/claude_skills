"""Independent 32px profile of text-underlined-capital-letter-b-5597f318.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '5597f318-b426-459a-89c5-29372f14b28f'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-capital-letter-b-5597f318.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5597f318-b426-459a-89c5-29372f14b28f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/b (text u)_5597f318-b426-459a-89c5-29372f14b28f.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-capital-letter-b-5597f318',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-b-uppercase',)
REFERENCE_EXPORT_SHA256 = '8644c134f90cd49212b8a709212c4fae2895b5c2c7e367c3f023874c77ee7cdb'

class Drawing(TextSub32):
    icon_id = 'text-underlined-capital-letter-b-5597f318-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 17
    text_ink_bounds = (0.0, 0.0, 17.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (15, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 21), (2, 2))
        self.add_line('p2-r1-2', (2, 2), (8, 2))
        self.add_bezier('p2-r1-3', (8, 2), ((12, 2), (14, 4), (14, 7)))
        self.add_bezier('p2-r1-4', (14, 7), ((14, 9), (12, 12), (8, 12)))
        self.add_line('p2-r1-5', (8, 12), (2, 12))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_bezier('p3-r1-1', (8, 12), ((13, 12), (15, 14), (15, 16)))
        self.add_bezier('p3-r1-2', (15, 16), ((15, 19), (13, 21), (8, 21)))
        self.add_line('p3-r1-3', (8, 21), (2, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-3')
        self.relate("connect", 'p2-r1-4', 'p3-r1-1')
        self.relate("connect", 'p2-r1-5', 'p3-r1-1')
