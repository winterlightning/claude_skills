"""Independent 32px profile of text-underlined-letters-c-and-f-f3cd7ed4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'f3cd7ed4-5031-4ad9-81d5-6b22299bc142'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letters-c-and-f-f3cd7ed4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f3cd7ed4-5031-4ad9-81d5-6b22299bc142', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/cf (text u)_f3cd7ed4-5031-4ad9-81d5-6b22299bc142.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letters-c-and-f-f3cd7ed4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-f')
REFERENCE_EXPORT_SHA256 = '901ef0bfd1ae1090b97030b470b9dead16682eb4263130ed3674ca1887f69afb'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letters-c-and-f-f3cd7ed4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 29
    text_ink_bounds = (0.0, 0.0, 29.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (27, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (23, 21), (23, 7))
        self.add_bezier('p2-r1-2', (23, 7), ((23, 5), (25, 3), (27, 3)))
        self.add_line('p2-r1-3', (27, 3), (27, 3))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (20, 8), (25, 8))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (14, 5), ((12, 3), (11, 2), (9, 2)))
        self.add_bezier('p4-r1-2', (9, 2), ((6, 2), (2, 6), (2, 12)))
        self.add_bezier('p4-r1-3', (2, 12), ((2, 17), (6, 21), (9, 21)))
        self.add_bezier('p4-r1-4', (9, 21), ((11, 21), (12, 20), (14, 18)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
