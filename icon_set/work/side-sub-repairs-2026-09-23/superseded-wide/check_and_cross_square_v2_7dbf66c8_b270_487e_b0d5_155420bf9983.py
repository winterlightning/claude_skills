"""Rounded square containing a check, diagonal divider, and cross."""
from ._tall_base import SourceFaithfulSideSub
from ...keyshapes import Keyshape
from ._compact_reference_helpers import rounded_rect
SOURCE_ICON_ID = '7dbf66c8-b270-487e-b0d5-155420bf9983'
SOURCE_PATH = 'pictographic-primitives/other/rectangle remove and check_7dbf66c8-b270-487e-b0d5-155420bf9983.svg'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('rounded square', 'check', 'diagonal divider', 'cross')

class DrawingVariant2(SourceFaithfulSideSub):
    canvas_width = 60
    canvas_height = 60
    icon_id = 'check-and-cross-square-v2'
    variant_of = 'check-and-cross-square'
    variant_label = 'Complete source on a proportionate canvas'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/state'
    aliases = ('accept-reject',)
    keywords = ('check', 'cross', 'yes', 'no', 'choice')

    def build(self):
        rounded_rect(self, 'frame', 2, 2, 58, 58, 8)
        self.add_polyline('check', (12, 20), (18, 28), (28, 12))
        self.add_line('divider', (26, 48), (40, 10))
        self.add_line('cross-a', (42, 38), (50, 48))
        self.add_line('cross-b', (42, 48), (50, 38))
        self.relate('connect', 'cross-a', 'cross-b')
