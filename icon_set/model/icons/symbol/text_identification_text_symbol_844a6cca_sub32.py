"""Independent 32px profile of text-identification-text-symbol-844a6cca.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '844a6cca-9183-43b4-8e32-4dbb2c81a21f'
SOURCE_PATH = 'icon_set/dist/text32/text-identification-text-symbol-844a6cca.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('844a6cca-9183-43b4-8e32-4dbb2c81a21f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/Id_844a6cca-9183-43b4-8e32-4dbb2c81a21f.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-identification-text-symbol-844a6cca',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-i-uppercase', 'letter-d')
REFERENCE_EXPORT_SHA256 = 'cfced66bd2704364a79bf449bf604c7bed02b8eb24875ab435ab96e395d4b01c'

class Drawing(TextSub32):
    icon_id = 'text-identification-text-symbol-844a6cca-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 39
    text_ink_bounds = (0.0, 0.0, 39.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (37, 25), ((36, 28), (32, 30), (29, 30)))
        self.add_bezier('p1-r1-2', (29, 30), ((24, 30), (19, 26), (19, 20)))
        self.add_bezier('p1-r1-3', (19, 20), ((19, 15), (24, 11), (29, 11)))
        self.add_bezier('p1-r1-4', (29, 11), ((32, 11), (35, 12), (37, 15)))
        self.add_bezier('p1-r1-5', (37, 15), ((37, 15), (37, 16), (37, 16)))
        self.add_line('p1-r1-6', (37, 16), (37, 25))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (37, 16), (37, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 2), (11, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (7, 2), (7, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 30), (11, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
