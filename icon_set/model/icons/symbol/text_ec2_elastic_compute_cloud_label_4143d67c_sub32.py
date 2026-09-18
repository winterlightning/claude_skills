"""Independent 32px profile of text-ec2-elastic-compute-cloud-label-4143d67c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '4143d67c-2e84-4f9e-8095-87e86e008f75'
SOURCE_PATH = 'icon_set/dist/text32/text-ec2-elastic-compute-cloud-label-4143d67c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4143d67c-2e84-4f9e-8095-87e86e008f75', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/ec2 (text)_4143d67c-2e84-4f9e-8095-87e86e008f75.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-ec2-elastic-compute-cloud-label-4143d67c',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-e-uppercase', 'letter-c-uppercase', 'digit-2')
REFERENCE_EXPORT_SHA256 = 'f8cac4af48808433e039c9eac76b7068ed96582bd939f4c5dd5606fd0c2c4bc1'

class Drawing(TextSub32):
    icon_id = 'text-ec2-elastic-compute-cloud-label-4143d67c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 74
    text_ink_bounds = (0.0, 0.0, 74.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (52, 2), (66, 2))
        self.add_bezier('p1-r1-2', (66, 2), ((69, 2), (72, 5), (72, 8)))
        self.add_bezier('p1-r1-3', (72, 8), ((72, 9), (71, 11), (69, 12)))
        self.add_line('p1-r1-4', (69, 12), (56, 21))
        self.add_bezier('p1-r1-5', (56, 21), ((53, 23), (52, 25), (52, 28)))
        self.add_line('p1-r1-6', (52, 28), (52, 29))
        self.add_bezier('p1-r1-7', (52, 29), ((52, 29), (53, 30), (53, 30)))
        self.add_line('p1-r1-8', (53, 30), (72, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_arc('p2-r1-1', (44, 6), (44, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (19, 2), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (2, 30))
        self.add_line('p3-r1-3', (2, 30), (19, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 16), (16, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
