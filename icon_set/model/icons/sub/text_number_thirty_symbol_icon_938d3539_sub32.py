"""Independent 32px profile of text-number-thirty-symbol-icon-938d3539.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '938d3539-4c60-42ce-a3e5-41e92e309fc2'
SOURCE_PATH = 'icon_set/dist/text32/text-number-thirty-symbol-icon-938d3539.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('938d3539-4c60-42ce-a3e5-41e92e309fc2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/30_938d3539-4c60-42ce-a3e5-41e92e309fc2.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-thirty-symbol-icon-938d3539',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-3', 'digit-0')
REFERENCE_EXPORT_SHA256 = 'dd962ee50c56cd2a1659b4ca29e6341d9d2dde9c9e016387ca7e5a545ef655a6'

class Drawing(TextSub32):
    icon_id = 'text-number-thirty-symbol-icon-938d3539-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 50
    text_ink_bounds = (0.0, 0.0, 50.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (28, 10), (48, 10), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (48, 10), (48, 22))
        self.add_arc('p1-r1-3', (48, 22), (28, 22), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (28, 22), (28, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
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
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-2')
        self.relate("connect", 'p2-r1-4', 'p3-r1-1')
        self.relate("connect", 'p2-r1-4', 'p3-r1-2')
