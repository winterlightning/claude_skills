"""Independent 32px profile of text-number-thirty-one-0fd4fb2a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '0fd4fb2a-cc60-433e-bbae-f44be8a2c0be'
SOURCE_PATH = 'icon_set/dist/text32/text-number-thirty-one-0fd4fb2a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0fd4fb2a-cc60-433e-bbae-f44be8a2c0be', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/31 (text)_0fd4fb2a-cc60-433e-bbae-f44be8a2c0be.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-thirty-one-0fd4fb2a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-3', 'digit-1')
REFERENCE_EXPORT_SHA256 = '7cc6dd89bcaefeaaaa6fae2477a185d165f7061b6f66acaee1b0af40e21d0af7'

class Drawing(TextSub32):
    icon_id = 'text-number-thirty-one-0fd4fb2a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 43
    text_ink_bounds = (0.0, 0.0, 43.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (35, 30), (35, 3))
        self.add_bezier('p1-r1-2', (35, 3), ((35, 2), (34, 2), (34, 2)))
        self.add_line('p1-r1-3', (34, 2), (28, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (28, 30), (41, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 2), (13, 2))
        self.add_bezier('p3-r1-2', (13, 2), ((17, 2), (20, 5), (20, 9)))
        self.add_bezier('p3-r1-3', (20, 9), ((20, 13), (17, 16), (13, 16)))
        self.add_line('p3-r1-4', (13, 16), (9, 16))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (10, 16), (13, 16))
        self.add_bezier('p4-r1-2', (13, 16), ((17, 16), (20, 19), (20, 23)))
        self.add_bezier('p4-r1-3', (20, 23), ((20, 27), (17, 30), (13, 30)))
        self.add_line('p4-r1-4', (13, 30), (2, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.relate("connect", 'p3-r1-3', 'p4-r1-1')
        self.relate("connect", 'p3-r1-3', 'p4-r1-2')
        self.relate("connect", 'p3-r1-4', 'p4-r1-1')
        self.relate("connect", 'p3-r1-4', 'p4-r1-2')
