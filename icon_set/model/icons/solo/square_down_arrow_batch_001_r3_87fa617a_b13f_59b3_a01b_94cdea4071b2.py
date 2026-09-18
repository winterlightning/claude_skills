"""A square button with a downward chevron: expand, next, or move down.

Plan: one rounded-square frame owns a chevron mirrored about the vertical axis
x=24; one arm length drives both arms.
Keyshape: SQUARE, centerline box (6,6)-(42,42).
Reduction: the reference's slightly softened corners become radius-4 corners.
Construction reference: Lucide `square-chevron-down`.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_001_r3_shapes import rounded_rect

SOURCE_ICON_ID = "87fa617a-b13f-59b3-a01b-94cdea4071b2"
SOURCE_PATH = "/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/arrows/arrow rectangle left svg270_87fa617a-b13f-59b3-a01b-94cdea4071b2.svg"
EXPORTED_REFERENCE_PATH = "work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/arrow rectangle left svg270_87fa617a-b13f-59b3-a01b-94cdea4071b2.svg"
AUTHOR = "claude-opus-5"


class SquareDownArrowBatch001R3(Solo48):
    icon_id = "square-down-arrow-batch-001-r3"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "arrows"
    aliases = ("square-chevron-down",)
    keywords = ("arrow", "down", "chevron", "expand", "button", "square")

    def build(self) -> None:
        rounded_rect(self, "button", 6, 6, 42, 42, radius=4)
        axis_x, arm = 24, 9
        vertex_y = 29  # optical centre: the open side reads lighter
        self.add_polyline(
            "chevron",
            (axis_x - arm, vertex_y - arm), (axis_x, vertex_y), (axis_x + arm, vertex_y - arm),
        )
