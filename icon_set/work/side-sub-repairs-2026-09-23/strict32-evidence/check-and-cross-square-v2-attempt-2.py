"""Rounded square containing a check, diagonal divider, and cross."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import rounded_rect

SOURCE_ICON_ID = "7dbf66c8-b270-487e-b0d5-155420bf9983"
SOURCE_PATH = "pictographic-primitives/other/rectangle remove and check_7dbf66c8-b270-487e-b0d5-155420bf9983.svg"
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('rounded square', 'check', 'diagonal divider', 'cross')
REPAIR_PLAN = {'concept': 'check and cross square', 'core_parts': ('rounded square', 'check', 'diagonal divider', 'cross'), 'flexible_parts': 'Only minor curves and spacing may be simplified for 32px clearance', 'ladder': 'Rebalance and redraw on the strict SUB32 canvas'}



class DrawingVariant2(Sub32):
    icon_id = "check-and-cross-square-v2"
    variant_of = "check-and-cross-square"
    variant_label = "Strict 32x32 repair draft"
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/state"
    aliases = ("accept-reject",)
    keywords = ("check", "cross", "yes", "no", "choice")

    def build(self):
        rounded_rect(self, "frame", 2, 2, 30, 30, 4)
        self.add_polyline("check", (8, 12), (10, 15), (13, 9))
        self.add_line("divider", (14, 24), (18, 8))
        self.add_line("cross-a", (20, 19), (24, 23))
        self.add_line("cross-b", (20, 23), (24, 19))
        self.relate("connect", "cross-a", "cross-b")
