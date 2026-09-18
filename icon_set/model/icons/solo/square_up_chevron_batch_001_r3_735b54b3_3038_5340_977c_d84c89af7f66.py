"""A square button with an upward chevron: collapse, previous, or move up.

Plan: one rounded-square frame owns a chevron mirrored about the vertical axis
x=24; one arm length drives both arms.
Keyshape: SQUARE, centerline box (6,6)-(42,42).
Reduction: the reference's slightly softened corners become radius-4 corners.
Construction reference: Lucide `square-chevron-up`.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_001_r3_shapes import rounded_rect

SOURCE_ICON_ID = "735b54b3-3038-5340-977c-d84c89af7f66"
SOURCE_PATH = "/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/arrows/arrow rectangle left svg90_735b54b3-3038-5340-977c-d84c89af7f66.svg"
EXPORTED_REFERENCE_PATH = "work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/arrow rectangle left svg90_735b54b3-3038-5340-977c-d84c89af7f66.svg"
AUTHOR = "claude-opus-5"


class SquareUpChevronBatch001R3(Solo48):
    icon_id = "square-up-chevron-batch-001-r3"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "arrows"
    aliases = ("square-chevron-up",)
    keywords = ("arrow", "up", "chevron", "collapse", "button", "square")

    def build(self) -> None:
        rounded_rect(self, "button", 6, 6, 42, 42, radius=4)
        axis_x, arm = 24, 9
        vertex_y = 19  # optical centre: the open side reads lighter
        self.add_polyline(
            "chevron",
            (axis_x - arm, vertex_y + arm), (axis_x, vertex_y), (axis_x + arm, vertex_y + arm),
        )
