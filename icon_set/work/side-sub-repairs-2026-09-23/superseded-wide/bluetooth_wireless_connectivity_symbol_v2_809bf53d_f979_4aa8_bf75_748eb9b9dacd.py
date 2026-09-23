"""Bluetooth rune enclosed by the source's complete circular frame."""
from ._tall_base import SourceFaithfulSideSub
from ...keyshapes import Keyshape
from ._compact_reference_helpers import circle
SOURCE_ICON_ID = '809bf53d-f979-4aa8-bf75-748eb9b9dacd'
SOURCE_PATH = 'pictographic-primitives/other/circle bluetooth_809bf53d-f979-4aa8-bf75-748eb9b9dacd.svg'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('enclosing circle', 'Bluetooth spine and paired lobes', 'two left branches')

class DrawingVariant2(SourceFaithfulSideSub):
    canvas_width = 60
    canvas_height = 60
    icon_id = 'bluetooth-wireless-connectivity-symbol-v2'
    variant_of = 'bluetooth-wireless-connectivity-symbol'
    variant_label = 'Complete source on a proportionate canvas'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/symbol'
    aliases = ('bluetooth',)
    keywords = ('wireless', 'connectivity', 'radio')

    def build(self):
        circle(self, 'frame', 30, 30, 28)
        self.add_polyline('bluetooth', (12, 18), (30, 30), (48, 18), (30, 10), (30, 50), (48, 42), (30, 30), (12, 42))
