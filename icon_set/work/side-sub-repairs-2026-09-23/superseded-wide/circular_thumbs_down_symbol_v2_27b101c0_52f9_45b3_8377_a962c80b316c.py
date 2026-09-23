"""Downward thumb gesture enclosed by the source's circular frame."""
from ._tall_base import SourceFaithfulSideSub
from ...keyshapes import Keyshape
from ._compact_reference_helpers import circle
SOURCE_ICON_ID = '27b101c0-52f9-45b3-8377-a962c80b316c'
SOURCE_PATH = 'pictographic-primitives/state/circle thumbs down_27b101c0-52f9-45b3-8377-a962c80b316c.svg'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('enclosing circle', 'cuff', 'downward thumb hand')

class DrawingVariant2(SourceFaithfulSideSub):
    canvas_width = 60
    canvas_height = 60
    icon_id = 'circular-thumbs-down-symbol-v2'
    variant_of = 'circular-thumbs-down-symbol'
    variant_label = 'Complete source on a proportionate canvas'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'state'
    category = 'primitives/state'
    aliases = ('dislike-circle', 'thumbs-down-circle')
    keywords = ('thumb', 'down', 'dislike', 'negative')

    def build(self):
        circle(self, 'frame', 30, 30, 28)
        self.add_line('cuff', (16, 20), (16, 38))
        self.add_bezier('hand', (16, 22), ((24, 22), (24, 18), (32, 18)), ((38, 18), (40, 20), (42, 26)), ((44, 32), (48, 38), (42, 38)), ((36, 38), (34, 38), (34, 38)), ((36, 44), (34, 50), (30, 50)), ((26, 50), (24, 40), (18, 38)), ((16, 38), (16, 34), (16, 22)))
        self.add_contour('thumb', 'hand', closed=True)
