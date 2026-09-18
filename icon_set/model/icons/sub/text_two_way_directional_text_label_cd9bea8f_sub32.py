"""Independent 32px profile of text-two-way-directional-text-label-cd9bea8f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'cd9bea8f-8517-461f-8200-f3e2227f3c22'
SOURCE_PATH = 'icon_set/dist/text32/text-two-way-directional-text-label-cd9bea8f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cd9bea8f-8517-461f-8200-f3e2227f3c22', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/2 way (text)_cd9bea8f-8517-461f-8200-f3e2227f3c22.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-two-way-directional-text-label-cd9bea8f',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-2', 'letter-w-uppercase', 'letter-a-uppercase', 'letter-y-uppercase')
REFERENCE_EXPORT_SHA256 = '1b32427d164de0fe19e3b95a1a12dc8c5054f4aa86475a5ecbbf4272e098e659'

class Drawing(TextSub32):
    icon_id = 'text-two-way-directional-text-label-cd9bea8f-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 130
    text_ink_bounds = (0.0, 0.0, 130.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (106, 2), (117, 17))
        self.add_line('p1-r1-2', (117, 17), (128, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (117, 17), (117, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (77, 30), (87, 3))
        self.add_bezier('p3-r1-2', (87, 3), ((87, 2.3333333333333335), (87.33333333333333, 2), (88, 2)))
        self.add_bezier('p3-r1-3', (88, 2), ((88, 2), (88.33333333333333, 2.3333333333333335), (89, 3)))
        self.add_line('p3-r1-4', (89, 3), (98, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (82, 18), (94, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (40, 2), (46, 28))
        self.add_bezier('p5-r1-2', (46, 28), ((46.666666666666664, 29.333333333333332), (47, 30), (47, 30)))
        self.add_bezier('p5-r1-3', (47, 30), ((47, 30), (47.333333333333336, 29.333333333333332), (48, 28)))
        self.add_line('p5-r1-4', (48, 28), (54, 4))
        self.add_bezier('p5-r1-5', (54, 4), ((54, 3.3333333333333335), (54.333333333333336, 3), (55, 3)))
        self.add_bezier('p5-r1-6', (55, 3), ((55, 3), (55.333333333333336, 3.3333333333333335), (56, 4)))
        self.add_line('p5-r1-7', (56, 4), (62, 28))
        self.add_bezier('p5-r1-8', (62, 28), ((62, 29.333333333333332), (62.333333333333336, 30), (63, 30)))
        self.add_bezier('p5-r1-9', (63, 30), ((63, 30), (63, 29.333333333333332), (63, 28)))
        self.add_line('p5-r1-10', (63, 28), (70, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', 'p5-r1-6', 'p5-r1-7', 'p5-r1-8', 'p5-r1-9', 'p5-r1-10', closed=False)
        self.add_line('p6-r1-1', (2, 2), (16, 2))
        self.add_bezier('p6-r1-2', (16, 2), ((19, 2), (21, 5), (21, 8)))
        self.add_bezier('p6-r1-3', (21, 8), ((21, 9), (21, 11), (19, 12)))
        self.add_line('p6-r1-4', (19, 12), (6, 21))
        self.add_bezier('p6-r1-5', (6, 21), ((3, 23), (2, 25), (2, 28)))
        self.add_line('p6-r1-6', (2, 28), (2, 29))
        self.add_bezier('p6-r1-7', (2, 29), ((2, 29), (3, 30), (3, 30)))
        self.add_line('p6-r1-8', (3, 30), (22, 30))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', 'p6-r1-5', 'p6-r1-6', 'p6-r1-7', 'p6-r1-8', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
