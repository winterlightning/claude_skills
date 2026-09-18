"""Independent 32px profile of text-alphabet-letters-s-and-m-4948e3d9.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '4948e3d9-c691-4600-b65b-84b1ea7abd1c'
SOURCE_PATH = 'icon_set/dist/text32/text-alphabet-letters-s-and-m-4948e3d9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4948e3d9-c691-4600-b65b-84b1ea7abd1c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/sm_4948e3d9-c691-4600-b65b-84b1ea7abd1c.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-alphabet-letters-s-and-m-4948e3d9',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-m-uppercase')
REFERENCE_EXPORT_SHA256 = '6122f51980d2bc90c693c49090d8e24c4f0cd3dd08c266d01e1c841b448d31b8'

class Drawing(TextSub32):
    icon_id = 'text-alphabet-letters-s-and-m-4948e3d9-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 57
    text_ink_bounds = (0.0, 0.0, 57.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (28, 30), (28, 2))
        self.add_line('p1-r1-2', (28, 2), (41, 20))
        self.add_line('p1-r1-3', (41, 20), (55, 2))
        self.add_line('p1-r1-4', (55, 2), (55, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (20, 6), ((19, 3), (15, 2), (12, 2)))
        self.add_bezier('p2-r1-2', (12, 2), ((8, 2), (4, 4), (3, 9)))
        self.add_bezier('p2-r1-3', (3, 9), ((3, 9), (3, 9), (3, 10)))
        self.add_bezier('p2-r1-4', (3, 10), ((3, 17), (20, 13), (20, 22)))
        self.add_bezier('p2-r1-5', (20, 22), ((20, 22), (20, 22), (20, 23)))
        self.add_bezier('p2-r1-6', (20, 23), ((20, 28), (16, 30), (11, 30)))
        self.add_bezier('p2-r1-7', (11, 30), ((7, 30), (4, 29), (2, 26)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
