"""Independent 32px profile of text-number-thirty-two-1caf07ae.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '1caf07ae-b765-4e87-8322-6a4c81ec96e2'
SOURCE_PATH = 'icon_set/dist/text32/text-number-thirty-two-1caf07ae.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1caf07ae-b765-4e87-8322-6a4c81ec96e2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/32 (text)_1caf07ae-b765-4e87-8322-6a4c81ec96e2.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-thirty-two-1caf07ae',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-3', 'digit-2')
REFERENCE_EXPORT_SHA256 = 'a0dd0eb87beea6a1c33d8e1926f1c0a8a5410b9c6df80e855870f618f66c6ec7'

class Drawing(TextSub32):
    icon_id = 'text-number-thirty-two-1caf07ae-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 50
    text_ink_bounds = (0.0, 0.0, 50.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (28, 2), (42, 2))
        self.add_bezier('p1-r1-2', (42, 2), ((45, 2), (48, 5), (48, 8)))
        self.add_bezier('p1-r1-3', (48, 8), ((48, 9), (47, 11), (45, 12)))
        self.add_line('p1-r1-4', (45, 12), (32, 21))
        self.add_bezier('p1-r1-5', (32, 21), ((29, 23), (28, 25), (28, 28)))
        self.add_line('p1-r1-6', (28, 28), (28, 29))
        self.add_bezier('p1-r1-7', (28, 29), ((28, 29), (29, 30), (29, 30)))
        self.add_line('p1-r1-8', (29, 30), (48, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (2, 2), (13, 2))
        self.add_bezier('p2-r1-2', (13, 2), ((17, 2), (20, 5), (20, 9)))
        self.add_bezier('p2-r1-3', (20, 9), ((20, 13), (17, 16), (13, 16)))
        self.add_line('p2-r1-4', (13, 16), (9, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (10, 16), (13, 16))
        self.add_bezier('p3-r1-2', (13, 16), ((17, 16), (20, 19), (20, 23)))
        self.add_bezier('p3-r1-3', (20, 23), ((20, 27), (17, 30), (13, 30)))
        self.add_line('p3-r1-4', (13, 30), (2, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-2')
        self.relate('connect', 'p2-r1-4', 'p3-r1-1')
        self.relate('connect', 'p2-r1-4', 'p3-r1-2')
