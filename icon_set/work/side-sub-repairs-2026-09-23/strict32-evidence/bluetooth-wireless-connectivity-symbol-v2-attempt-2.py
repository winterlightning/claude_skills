"""Bluetooth rune enclosed by the source's complete circular frame."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import circle

SOURCE_ICON_ID = "809bf53d-f979-4aa8-bf75-748eb9b9dacd"
SOURCE_PATH = "pictographic-primitives/other/circle bluetooth_809bf53d-f979-4aa8-bf75-748eb9b9dacd.svg"
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('enclosing circle', 'Bluetooth spine and paired lobes', 'two left branches')
REPAIR_PLAN = {'concept': 'bluetooth wireless connectivity symbol', 'core_parts': ('enclosing circle', 'Bluetooth spine and paired lobes', 'two left branches'), 'flexible_parts': 'Only minor curves and spacing may be simplified for 32px clearance', 'ladder': 'Rebalance and redraw on the strict SUB32 canvas'}



class DrawingVariant2(Sub32):
    icon_id = "bluetooth-wireless-connectivity-symbol-v2"
    variant_of = "bluetooth-wireless-connectivity-symbol"
    variant_label = "Strict 32x32 repair draft"
    keyshape = Keyshape.CIRCLE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/symbol"
    aliases = ("bluetooth",)
    keywords = ("wireless", "connectivity", "radio")

    def build(self):
        circle(self, "frame", 16, 16, 14)
        self.add_polyline("bluetooth", (10, 12), (16, 16), (23, 12), (16, 8), (16, 24), (23, 20), (16, 16), (10, 20))
