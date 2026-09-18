"""Independent 32px profile of text-number-three-digit-daa2822c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'daa2822c-e67f-46c5-b0c3-95e9fef6b6e4'
SOURCE_PATH = 'icon_set/dist/text32/text-number-three-digit-daa2822c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('daa2822c-e67f-46c5-b0c3-95e9fef6b6e4', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/3_daa2822c-e67f-46c5-b0c3-95e9fef6b6e4.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-three-digit-daa2822c',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-3',)
REFERENCE_EXPORT_SHA256 = '6058c24e14cab72ab13c42ef220f46874da8ba5da3ecf8d7ea54e36716882c9e'

class Drawing(TextSub32):
    icon_id = 'text-number-three-digit-daa2822c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 22
    text_ink_bounds = (0.0, 0.0, 22.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (13, 2))
        self.add_bezier('p1-r1-2', (13, 2), ((17, 2), (20, 5), (20, 9)))
        self.add_bezier('p1-r1-3', (20, 9), ((20, 13), (17, 16), (13, 16)))
        self.add_line('p1-r1-4', (13, 16), (9, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (10, 16), (13, 16))
        self.add_bezier('p2-r1-2', (13, 16), ((17, 16), (20, 19), (20, 23)))
        self.add_bezier('p2-r1-3', (20, 23), ((20, 27), (17, 30), (13, 30)))
        self.add_line('p2-r1-4', (13, 30), (2, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
