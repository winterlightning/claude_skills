"""Independent 32px profile of text-underlined-rutherfordium-symbol-8242da2c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '8242da2c-63f3-4dca-b0e7-542ae0f60a4f'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-rutherfordium-symbol-8242da2c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8242da2c-63f3-4dca-b0e7-542ae0f60a4f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/rf (text u)_8242da2c-63f3-4dca-b0e7-542ae0f60a4f.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-rutherfordium-symbol-8242da2c',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-r-uppercase', 'letter-f')
REFERENCE_EXPORT_SHA256 = '180614b5a4b094c71a377ff820b0185d195a9ed53b930d7e656fb0c6ef90b404'

class Drawing(TextSub32):
    icon_id = 'text-underlined-rutherfordium-symbol-8242da2c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 31
    text_ink_bounds = (0.0, 0.0, 31.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (29, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (25, 21), (25, 7))
        self.add_bezier('p2-r1-2', (25, 7), ((25, 5), (27, 3), (29, 3)))
        self.add_line('p2-r1-3', (29, 3), (29, 3))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (22, 8), (27, 8))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 21), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (9, 2))
        self.add_bezier('p4-r1-3', (9, 2), ((13, 2), (15, 5), (15, 7)))
        self.add_bezier('p4-r1-4', (15, 7), ((15, 10), (13, 12), (9, 12)))
        self.add_line('p4-r1-5', (9, 12), (2, 12))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (9, 12), (16, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p4-r1-4', 'p5-r1-1')
        self.relate('connect', 'p4-r1-5', 'p5-r1-1')
