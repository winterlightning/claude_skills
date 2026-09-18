"""Independent 32px profile of text-underlined-ru-text-faf37a6a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'faf37a6a-7393-40f3-8b50-95ee4633df4c'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-ru-text-faf37a6a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('faf37a6a-7393-40f3-8b50-95ee4633df4c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/ru (text u)_faf37a6a-7393-40f3-8b50-95ee4633df4c.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-ru-text-faf37a6a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-r-uppercase', 'letter-u')
REFERENCE_EXPORT_SHA256 = '0da52351b22960d0df8f070223bce5bc7d1290b95bd92eab45f4c2aa81052e4e'

class Drawing(TextSub32):
    icon_id = 'text-underlined-ru-text-faf37a6a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 35
    text_ink_bounds = (0.0, 0.0, 35.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (33, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (22, 8), (22, 16))
        self.add_bezier('p2-r1-2', (22, 16), ((22, 19), (25, 21), (28, 21)))
        self.add_bezier('p2-r1-3', (28, 21), ((31, 21), (33, 19), (33, 16)))
        self.add_line('p2-r1-4', (33, 16), (33, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 21), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (9, 2))
        self.add_bezier('p3-r1-3', (9, 2), ((13, 2), (15, 5), (15, 7)))
        self.add_bezier('p3-r1-4', (15, 7), ((15, 10), (13, 12), (9, 12)))
        self.add_line('p3-r1-5', (9, 12), (2, 12))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (9, 12), (16, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p3-r1-4', 'p4-r1-1')
        self.relate('connect', 'p3-r1-5', 'p4-r1-1')
