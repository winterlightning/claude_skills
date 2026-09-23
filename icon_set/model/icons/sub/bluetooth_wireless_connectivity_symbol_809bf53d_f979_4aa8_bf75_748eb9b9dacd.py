"""Bluetooth rune enclosed by the source's complete circular frame."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import circle

SOURCE_ICON_ID = "809bf53d-f979-4aa8-bf75-748eb9b9dacd"
SOURCE_PATH = "pictographic-primitives/other/circle bluetooth_809bf53d-f979-4aa8-bf75-748eb9b9dacd.svg"
AUTHOR = "gpt-5"


class Drawing(Sub32):
    icon_id = "bluetooth-wireless-connectivity-symbol"
    keyshape = Keyshape.CIRCLE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/symbol"
    aliases = ("bluetooth",)
    keywords = ("wireless", "connectivity", "radio")

    def build(self):
        circle(self, "frame", 16, 16, 14)
        self.add_polyline("bluetooth", (7, 10), (16, 16), (25, 10), (16, 6), (16, 26), (25, 22), (16, 16), (7, 22))
