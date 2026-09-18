"""Independent 32px profile of text-underline-text-c11d8345.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'c11d8345-5e6e-493f-985d-ee6acb6e9b09'
SOURCE_PATH = 'icon_set/dist/text32/text-underline-text-c11d8345.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c11d8345-5e6e-493f-985d-ee6acb6e9b09', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/te (text u)_c11d8345-5e6e-493f-985d-ee6acb6e9b09.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underline-text-c11d8345',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-t-uppercase', 'letter-e')
REFERENCE_EXPORT_SHA256 = 'a1cdcadb344aec4d53d7bf252f92142df8e569eaa64187a6b3c19d76e828a0a7'

class Drawing(TextSub32):
    icon_id = 'text-underline-text-c11d8345-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 39
    text_ink_bounds = (0.0, 0.0, 39.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (37, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (37, 15), ((37, 11), (34, 8), (30, 8)))
        self.add_bezier('p2-r1-2', (30, 8), ((27, 8), (24, 11), (24, 15)))
        self.add_bezier('p2-r1-3', (24, 15), ((24, 18), (27, 21), (30, 21)))
        self.add_bezier('p2-r1-4', (30, 21), ((33, 21), (35, 20), (36, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (24, 15), (37, 15))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 2), (17, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (9, 2), (9, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
