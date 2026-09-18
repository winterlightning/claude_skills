"""Independent 32px profile of text-krone-currency-symbol-642219cf.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '642219cf-80b0-47d2-9e4e-d483908bbe52'
SOURCE_PATH = 'icon_set/dist/text32/text-krone-currency-symbol-642219cf.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('642219cf-80b0-47d2-9e4e-d483908bbe52', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/kr (text u)_642219cf-80b0-47d2-9e4e-d483908bbe52.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-krone-currency-symbol-642219cf',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-k-uppercase', 'letter-r')
REFERENCE_EXPORT_SHA256 = 'bd8398af5b825f5f1837207dfbda3adc0658b98eab39cd683efd8a0f4940b007'

class Drawing(TextSub32):
    icon_id = 'text-krone-currency-symbol-642219cf-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 29
    text_ink_bounds = (0.0, 0.0, 29.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (27, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (22, 8), (22, 12))
        self.add_line('p2-r1-2', (22, 12), (22, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (22, 12), ((22, 10), (24, 8), (26, 8)))
        self.add_line('p3-r1-2', (26, 8), (27, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 2), (2, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (15, 2), (2, 12))
        self.add_line('p5-r1-2', (2, 12), (15, 21))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
