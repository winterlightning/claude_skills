"""Rounded square containing a check, diagonal divider, and cross."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import rounded_rect

SOURCE_ICON_ID = "7dbf66c8-b270-487e-b0d5-155420bf9983"
SOURCE_PATH = "pictographic-primitives/other/rectangle remove and check_7dbf66c8-b270-487e-b0d5-155420bf9983.svg"
AUTHOR = "gpt-5"


class Drawing(Sub32):
    icon_id = "check-and-cross-square"
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/state"
    aliases = ("accept-reject",)
    keywords = ("check", "cross", "yes", "no", "choice")

    def build(self):
        rounded_rect(self, "frame", 2, 2, 30, 30, 4)
        self.add_polyline("check", (7, 11), (10, 15), (15, 7))
        self.add_line("divider", (14, 25), (21, 5))
        self.add_line("cross-a", (22, 20), (27, 25))
        self.add_line("cross-b", (22, 25), (27, 20))
        self.relate("connect", "cross-a", "cross-b")
