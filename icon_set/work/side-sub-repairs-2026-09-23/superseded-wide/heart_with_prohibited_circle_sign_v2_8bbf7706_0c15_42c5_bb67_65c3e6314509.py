"""Heart inside a prohibition circle with the source's two exposed slash ends."""
from ._tall_base import SourceFaithfulSideSub
from ...keyshapes import Keyshape
from ._compact_reference_helpers import circle
SOURCE_ICON_ID = '8bbf7706-0c15-42c5-bb67-65c3e6314509'
SOURCE_PATH = 'pictographic-primitives/other/slash heart_8bbf7706-0c15-42c5-bb67-65c3e6314509.svg'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('interrupted enclosing circle', 'two short diagonal marks', 'heart')

class DrawingVariant2(SourceFaithfulSideSub):
    canvas_width = 60
    canvas_height = 60
    icon_id = 'heart-with-prohibited-circle-sign-v2'
    variant_of = 'heart-with-prohibited-circle-sign'
    variant_label = 'Complete source on a proportionate canvas'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'state'
    category = 'primitives/state'
    aliases = ('no-heart', 'heart-prohibited')
    keywords = ('heart', 'prohibited', 'ban', 'slash', 'no')

    def build(self):
        self.add_bezier('ring-upper-left', (6, 14), ((11, 6), (20, 2), (30, 2)))
        self.add_bezier('ring-upper-right', (30, 2), ((46, 2), (58, 14), (58, 30)))
        self.add_bezier('ring-right', (58, 30), ((58, 35), (57, 39), (54, 42)))
        self.add_contour('frame-upper', 'ring-upper-left', 'ring-upper-right', 'ring-right', closed=False)
        self.add_bezier('ring-bottom-right', (52, 48), ((45, 55), (38, 58), (30, 58)))
        self.add_bezier('ring-bottom-left', (30, 58), ((14, 58), (2, 46), (2, 30)))
        self.add_bezier('ring-left', (2, 30), ((2, 27), (3, 24), (6, 22)))
        self.add_contour('frame-lower', 'ring-bottom-right', 'ring-bottom-left', 'ring-left', closed=False)
        self.add_line('slash-upper', (6, 14), (9, 15))
        self.add_line('slash-lower', (54, 42), (50, 40))
        self.relate('connect', 'frame-upper', 'slash-upper')
        self.relate('connect', 'frame-upper', 'slash-lower')
        self.add_bezier('heart', (30, 46), ((16, 34), (14, 28), (14, 22)), ((14, 14), (24, 12), (30, 20)), ((36, 12), (46, 14), (46, 22)), ((46, 30), (40, 36), (30, 46)))
        self.add_contour('heart-shape', 'heart', closed=True)
