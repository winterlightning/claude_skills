"""Rounded battery case, separate right terminal, and central charging bolt."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import rounded_rect

SOURCE_ICON_ID = "638f0a9f-914c-4078-b32c-13c8ec4aacf6"
SOURCE_PATH = "pictographic-primitives/other/battery 1_638f0a9f-914c-4078-b32c-13c8ec4aacf6.svg"
AUTHOR = "gpt-5"


class Drawing(Sub32):
    icon_id = "charging-battery-symbol"
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/state"
    aliases = ("battery-charging",)
    keywords = ("battery", "charge", "power", "bolt")

    def build(self):
        rounded_rect(self, "battery", 2, 4, 26, 28, 4)
        self.add_line("terminal", (30, 12), (30, 20))
        self.add_polyline("bolt", (18, 9), (11, 18), (17, 17), (13, 24))
