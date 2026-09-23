"""Rounded battery case, separate right terminal, and central charging bolt."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import rounded_rect

SOURCE_ICON_ID = "638f0a9f-914c-4078-b32c-13c8ec4aacf6"
SOURCE_PATH = "pictographic-primitives/other/battery 1_638f0a9f-914c-4078-b32c-13c8ec4aacf6.svg"
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('rounded battery case', 'right terminal', 'lightning bolt')
REPAIR_PLAN = {'concept': 'charging battery symbol', 'core_parts': ('rounded battery case', 'right terminal', 'lightning bolt'), 'flexible_parts': 'Only minor curves and spacing may be simplified for 32px clearance', 'ladder': 'Rebalance and redraw on the strict SUB32 canvas'}



class DrawingVariant2(Sub32):
    icon_id = "charging-battery-symbol-v2"
    variant_of = "charging-battery-symbol"
    variant_label = "Strict 32x32 repair draft"
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/state"
    aliases = ("battery-charging",)
    keywords = ("battery", "charge", "power", "bolt")

    def build(self):
        rounded_rect(self, "battery", 2, 4, 22, 28, 4)
        self.add_line("terminal", (30, 12), (30, 20))
        self.add_polyline("bolt", (15, 11), (9, 16), (16, 18), (10, 21))
